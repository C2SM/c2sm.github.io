import requests
import json
import yaml

# Globally define the list entry strings for the data to be replaced
ENTRY_VARIABLES = "- Variables:"
ENTRY_SIZE = "- Size:"
ENTRY_NUMBER = "- Number of files:"

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def download_json(url):
    response = requests.get(url)
    response.raise_for_status()
    return json.loads(response.text)

def read_markdown(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_markdown(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)

def walk(node, depth, path=()):
    """Yields every (path, node) pair of the file tree at the given depth."""
    if len(path) == depth:
        yield path, node
    elif isinstance(node, dict):
        for key, child in node.items():
            if key != 'date_range':
                yield from walk(child, depth, path + (key,))

def generate_variables(json_data):
    """
    Generates the markdown variable list of a dataset from its file tree.

    The tree levels are identified by the 'labels' of the file index. Archives organized
    by scenario list the scenarios and temporal resolutions of each variable; all other
    archives list the temporal resolutions and grids, including the date range if available.

    Parameters:
    - json_data (dict): The file index containing 'labels' and the file tree 'data'.

    Returns:
    - str: A markdown-formatted list of variables with their details as tooltips.
    """
    labels = [label.replace(' ', '_') for label in json_data['labels']]
    var, res = labels.index('variable'), labels.index('temporal_resolution')
    details = {}
    if 'scenario' in labels[:var]:
        scen = labels.index('scenario')
        for path, _ in walk(json_data['data'], max(var, res, scen) + 1):
            details.setdefault(path[var], {}).setdefault(path[scen], set()).add(path[res])
        tooltips = {v: '; '.join(f"{s}: {', '.join(sorted(r))}" for s, r in sorted(d.items())) for v, d in details.items()}
    else:
        grid = labels.index('grid')
        for path, node in walk(json_data['data'], max(var, res, grid) + 1):
            date_range = f": {node['date_range']}" if 'date_range' in node else ''
            details.setdefault(path[var], {})[f"{path[res]} ({path[grid]}){date_range}"] = None
        tooltips = {v: ', '.join(d) for v, d in details.items()}
    entries = {v: f"`{v}`{{ title=\"{t}\" }}" for v, t in tooltips.items()}
    if labels[0] != 'institution':
        return f"{ENTRY_VARIABLES}\n" + ",\n".join(f"  {e}" for e in entries.values())
    # Archives organized by institution group the variables by the institutions providing them
    providers = {}
    for path, _ in walk(json_data['data'], var + 1):
        providers.setdefault(path[var], set()).add(path[0])
    institutions = set().union(*providers.values())
    groups = {}
    for v, e in entries.items():
        groups.setdefault(frozenset(providers[v]), []).append(e)
    lines = [ENTRY_VARIABLES]
    for insts, group in sorted(groups.items(), key=lambda g: -len(g[0])):
        label = 'All institutions' if insts == institutions else f"Only {', '.join(sorted(insts))}"
        lines.append(f"    - {label}:\n" + ",\n".join(f"      {e}" for e in group))
    return '\n'.join(lines)

def generate_summary(json_data, entry):
    """Generates the markdown size or number of files entry of a dataset."""
    value = json_data['total_size'] if entry == ENTRY_SIZE else f"{json_data['file_count']:,}"
    return f"{entry} {value} :material-information-outline:{{ title=\"last updated: {json_data['last_updated']}\" }}"


def replace_entry(file_path, heading_dataset, new_variables_content, entry):
    """
    Replaces a specified list entry for a specified dataset within a markdown file.

    This function searches for a specific dataset heading within a markdown file and replaces
    the content of the specified entry that follows this heading with new content. It handles
    skipping unrelated sections and ensures that the replacement is done at the correct indentation level.

    Parameters:
    - file_path (str): The path to the markdown file to be modified.
    - heading_dataset (str): The heading of the dataset section where variables need to be replaced.
                             This should match the markdown heading format, e.g., "### DatasetName".
    - new_variables_content (str): The new content to replace the existing list entry with.
                                   This content should be a string formatted according to markdown syntax.

    Note:
    - The function assumes that the variables section starts with a line `entry` at the same
      indentation level as the dataset heading.
    - It also assumes that a new section starts with a heading at the same indentation level as the
      `entry` line or with a higher-level heading (e.g., "##").
    """
    with open(file_path, 'r') as file:
        content = file.readlines()
    
    heading_found = False
    skip_section = False  # Flag to indicate if the current section should be skipped
    start_index = end_index = None
    for i, line in enumerate(content):
        # Check for the "## Raw Archives" heading to skip this section
        if line.strip() == "## Raw Archives":
            skip_section = True
        # If we're skipping a section and encounter another "##" heading, stop skipping
        if skip_section and line.strip().startswith("## ") and not line.strip() == "## Raw Archives":
            skip_section = False
        # Check for an exact match with the heading, considering markdown syntax
        if not skip_section and line.strip() == f"### {heading_dataset}":
            heading_found = True
            continue
        # Stop at the next heading so entries of other datasets are never modified
        if heading_found and line.lstrip().startswith("#"):
            break
        if heading_found and line.strip().startswith(entry):
            start_index = i
            break
    
    if start_index is not None:
        # Determine the indentation level of the "- Variables:" line
        variables_indentation = len(content[start_index]) - len(content[start_index].lstrip())
        
        for i in range(start_index + 1, len(content)):
            # Check if the line is at the same indentation level and starts with "- "
            line_indentation = len(content[i]) - len(content[i].lstrip())
            if content[i].strip().startswith("- ") and line_indentation == variables_indentation:
                end_index = i
                break
        if end_index is None:
            end_index = len(content)
        
        content = content[:start_index] + [new_variables_content + '\n'] + content[end_index:]
        
        with open(file_path, 'w') as file:
            file.writelines(content)

        print(f"Updated '{entry}' entry in {heading_dataset} section in file {file_path}")
        return True
    else:
        return False

def check_heading_exists(file_path, heading_dataset):
    """
    Checks if a specified heading exists within a markdown file.

    This function opens a markdown file and iterates through its lines to find a match for a specified heading.
    The heading is expected to be at the level of an H3 markdown heading (### HeadingName).

    Parameters:
    - file_path (str): The path to the markdown file to be searched.
    - heading_dataset (str): The exact text of the heading to search for, not including the markdown heading syntax (e.g., "DatasetName" for "### DatasetName").

    Returns:
    - bool: True if the heading is found, False otherwise.
    """
    formatted_heading = f"### {heading_dataset}"
    
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() == formatted_heading:
                return True
    return False

def main():
    markdown_files = [
        './docs/datasets/climate_model_data.md',
        './docs/datasets/obs_reanalysis_data.md'
    ]

    # Read the datasets file
    datasets = read_yaml('datasets.yaml')

    # Process data for each dataset and append markdown file
    for dataset in datasets.keys():
        # Load the JSON data for the dataset from https://data.iac.ethz.ch/zephyr/file_index/ and merge with metadata
        try:
            dataset_json = download_json(f'https://data.iac.ethz.ch/zephyr/file_index/file_tree_{dataset}_noindent.json')
            dataset_json_meta = download_json(f'https://data.iac.ethz.ch/zephyr/file_index/meta_{dataset}.json')
        except requests.HTTPError as error:
            print(f"Skipping {dataset}: file index not available ({error})")
            continue
        dataset_json = {**dataset_json, **dataset_json_meta}
        heading_dataset = datasets[dataset]

        print(heading_dataset)

        # Generate the markdown content for the dataset
        markdown_variables = generate_variables(dataset_json)
        markdown_size = generate_summary(dataset_json, ENTRY_SIZE)
        markdown_number = generate_summary(dataset_json, ENTRY_NUMBER)

        # Initialize flags to track if the variables, size, and number of files entries were updated
        updated_variables = False
        updated_size = False
        updated_number = False

        # Attempt to update each markdown file until the correct one is found and updated
        for markdown_file_path in markdown_files:
            if check_heading_exists(markdown_file_path, heading_dataset):
                updated_variables = replace_entry(markdown_file_path, heading_dataset, markdown_variables, ENTRY_VARIABLES)
                updated_size = replace_entry(markdown_file_path, heading_dataset, markdown_size, ENTRY_SIZE)
                updated_number = replace_entry(markdown_file_path, heading_dataset, markdown_number, ENTRY_NUMBER)
                break  # Stop searching once the correct file is updated
        
        # Print a message if no updates were made for the dataset
        if not updated_variables:
            print(f"Could not find '{ENTRY_VARIABLES}' list entry for heading {heading_dataset} in any markdown files. No changes applied.")
        if not updated_size:
            print(f"Could not find '{ENTRY_SIZE}' list entry for heading {heading_dataset} in any markdown files. No changes applied.")
        if not updated_number:
            print(f"Could not find '{ENTRY_NUMBER}' list entry for heading {heading_dataset} in any markdown files. No changes applied.")

if __name__ == "__main__":
    main()