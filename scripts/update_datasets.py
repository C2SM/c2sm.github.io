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
    return json.loads(response.text)

def read_markdown(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_markdown(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)

def generate_markdown_default(json_data, dataset, entry):
    """
    Generates markdown content for climate datasets.

    This function iterates over variables in the provided JSON data, processing each
    to generate a markdown string that lists variables and their details for a given dataset.

    Parameters:
    - json_data (dict): The JSON data containing variables and their resolutions.
    - dataset (str): The name of the dataset being processed.

    Returns:
    - str: A markdown-formatted string listing variables and their details.
    """
    if entry == ENTRY_VARIABLES:
        markdown_content = f"{entry} \n"
    else: 
        markdown_content = f"{entry} "
    
    first_iteration = True
    for variable, resolutions in json_data['data'].items():
        if dataset == 'cmip6-ng':
            # Logic for CMIP6-ng datasets
            if entry == ENTRY_VARIABLES:
                markdown_content += generate_variable_info_cmip6ng(variable, resolutions, first_iteration)
        else:
            # Original logic for datasets with an additional scenario level
            if entry == ENTRY_VARIABLES:
                markdown_content += generate_variable_info_default(variable, resolutions, first_iteration)
        first_iteration = False

    return markdown_content

def generate_markdown_cordex(json_data, entry):
    """
    Generates markdown content for CORDEX(-ReKLiEs) datasets.

    This function compiles details about variables across scenarios and temporal resolutions
    from the provided JSON data. It then processes this information to generate a markdown
    string that lists variables, scenarios, and their temporal resolutions.

    Parameters:
    - json_data (dict): The JSON data containing scenarios, temporal resolutions, and variables.

    Returns:
    - str: A markdown-formatted string listing variables along with their scenarios and temporal resolutions.
    """
    markdown_content = "- Variables: \n"
    
    variable_details = {}
    for scenario, temporal_resolutions in json_data['data'].items():
        for temporal_resolution, variables in temporal_resolutions.items():
            for variable, details in variables.items():
                if variable not in variable_details:
                    variable_details[variable] = {}
                if scenario not in variable_details[variable]:
                    variable_details[variable][scenario] = set()
                # Add resolution to the set of resolutions for this scenario
                variable_details[variable][scenario].add(temporal_resolution)
    
    first_iteration = True
    for variable, scenarios_resolutions in variable_details.items():
        markdown_content += generate_variable_info_cordex(variable, scenarios_resolutions, first_iteration)
        first_iteration = False

    return markdown_content
    
def generate_variable_info_cordex(variable, scenarios_resolutions, first_iteration):
    """
    Processes CORDEX data to generate markdown information for a single variable.

    This function creates a markdown string for a given variable, detailing the scenarios
    and temporal resolutions available for that variable.

    Parameters:
    - variable (str): The variable being processed.
    - scenarios_resolutions (dict): A dictionary mapping scenarios to sets of temporal resolutions.
    - first_iteration (bool): Indicates if this is the first variable being processed (affects formatting).

    Returns:
    - str: A markdown-formatted string for the variable, including scenario and resolution details.
    """
    variable_info = ""
    tooltip_content = " — ".join(
        f"{scenario}: {', '.join(sorted(resolutions))}" 
        for scenario, resolutions in scenarios_resolutions.items()
    )
    if first_iteration:
        variable_info += f"  `{variable}`{{ title=\"{tooltip_content}\" }}"
        first_iteration = False
    else:
        variable_info += f",\n  `{variable}`{{ title=\"{tooltip_content}\" }}"

    return variable_info

def generate_variable_info_cmip6ng(variable, resolutions, first_iteration):
    """
    Processes cmip6-ng data to generate markdown information for a single variable.

    This function creates a markdown string for a given variable, detailing the resolutions
    and, depending on the dataset, additional details like grid type and date range.

    Parameters:
    - variable (str): The variable being processed.
    - resolutions (dict): A dictionary mapping resolutions to their details.
    - first_iteration (bool): Indicates if this is the first variable being processed (affects formatting).

    Returns:
    - str: A markdown-formatted string for the variable, including resolution and grid type.
    """
    variable_info = ""
    if first_iteration:
        variable_info += f"  `{variable}`{{ title=\""
    else:
        variable_info += f",\n  `{variable}`{{ title=\""
    first_iteration_info = True
    for resolution, grid in resolutions.items():
        for grid_type, grid_values in grid.items():
            if first_iteration_info:
                variable_info += f"{resolution} ({grid_type})"
                first_iteration_info = False
            else:
                variable_info += f", {resolution} ({grid_type})"

    variable_info += "\" }"
    return variable_info

def generate_variable_info_default(variable, resolutions, first_iteration):
    """
    Processes climate data to generate markdown information for a single variable.

    This function creates a markdown string for a given variable, detailing the resolutions
    and, depending on the dataset, additional details like grid type and date range.

    Parameters:
    - variable (str): The variable being processed.
    - resolutions (dict): A dictionary mapping resolutions to their details.
    - first_iteration (bool): Indicates if this is the first variable being processed (affects formatting).
    - dataset (str): The name of the dataset, which determines the detail level in the markdown.

    Returns:
    - str: A markdown-formatted string for the variable, including resolution and possibly other details.
    """
    variable_info = ""
    if first_iteration:
        variable_info += f"  `{variable}`{{ title=\""
    else:
        variable_info += f",\n  `{variable}`{{ title=\""
    first_iteration_info = True
    for resolution, grid in resolutions.items():
        for grid_type, grid_values in grid.items():
            date_range = grid_values.get('date_range', 'N/A')
            if first_iteration_info:
                variable_info += f"{resolution} ({grid_type}): {date_range}"
                first_iteration_info = False
            else:
                variable_info += f", {resolution} ({grid_type}): {date_range}"

    variable_info += "\" }"
    return variable_info
    
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
        dataset_json = download_json(f'https://zephyr-c2sm.s3.eu-central-1.amazonaws.com/file_tree_{dataset}_noindent.json')
        heading_dataset = datasets[dataset]
        print(heading_dataset)
        if dataset.startswith('cordex'):
            markdown_variables = generate_markdown_cordex(dataset_json, ENTRY_VARIABLES)
            markdown_size = generate_markdown_cordex(dataset_json, ENTRY_SIZE)
            markdown_number = generate_markdown_cordex(dataset_json, ENTRY_NUMBER)
        else:
            markdown_variables = generate_markdown_default(dataset_json, dataset, ENTRY_VARIABLES)
            markdown_size = generate_markdown_default(dataset_json, dataset, ENTRY_SIZE)
            markdown_number = generate_markdown_default(dataset_json, dataset, ENTRY_NUMBER)

        # Attempt to update each markdown file until the correct one is found and updated
        updated_variables = False
        updated_size = False
        updated_number = False

        for markdown_file_path in markdown_files:
            if check_heading_exists(markdown_file_path, heading_dataset):
                updated_variables = replace_entry(markdown_file_path, heading_dataset, markdown_variables, ENTRY_VARIABLES)
                updated_size = replace_entry(markdown_file_path, heading_dataset, markdown_size, ENTRY_SIZE)
                updated_number = replace_entry(markdown_file_path, heading_dataset, markdown_number, ENTRY_NUMBER)
                break  # Stop searching once the correct file is updated
        
        if not updated_variables:
            print(f"Could not find '{ENTRY_VARIABLES}' list entry for heading {heading_dataset} in any markdown files. No changes applied.")
        if not updated_size:
            print(f"Could not find '{ENTRY_SIZE}' list entry for heading {heading_dataset} in any markdown files. No changes applied.")
        if not updated_number:
            print(f"Could not find '{ENTRY_NUMBER}' list entry for heading {heading_dataset} in any markdown files. No changes applied.")

if __name__ == "__main__":
    main()