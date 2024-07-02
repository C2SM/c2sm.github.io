import requests
import json
import yaml

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

def generate_markdown_with_tooltips(json_data, heading_dataset, dataset):
    markdown_content = "- Variables: \n"
    
    if dataset.startswith('cordex'):
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
            markdown_content += process_cordex_data(variable, scenarios_resolutions, first_iteration)
            first_iteration = False
    else:
        first_iteration = True
        # Original logic for datasets without an additional scenario level
        for variable, resolutions in json_data['data'].items():
            markdown_content += process_obs_reana_data(variable, resolutions, first_iteration, dataset)
            first_iteration = False

    return markdown_content
    
def process_cordex_data(variable, scenarios_resolutions, first_iteration):
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

def process_obs_reana_data(variable, resolutions, first_iteration, dataset):
    variable_info = ""
    if first_iteration:
        variable_info += f"  `{variable}`{{ title=\""
    else:
        variable_info += f",\n  `{variable}`{{ title=\""
    first_iteration_info = True
    if dataset == 'cmip6-ng':
        for resolution, grid in resolutions.items():
            for grid_type, grid_values in grid.items():
                if first_iteration_info:
                    variable_info += f"{resolution} ({grid_type})"
                    first_iteration_info = False
                else:
                    variable_info += f", {resolution} ({grid_type})"
    else:
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

    
def replace_variables_section(file_path, heading_dataset, new_variables_content):
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
        if heading_found and line.strip().startswith("- Variables:"):
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

def check_heading_exists(file_path, heading_dataset):
    """Check if the heading exists in the given file, considering markdown syntax."""
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
        dataset_markdown = generate_markdown_with_tooltips(dataset_json, heading_dataset, dataset)

        # Attempt to update each markdown file until the correct one is found and updated
        updated = False
        for markdown_file_path in markdown_files:
            if check_heading_exists(markdown_file_path, heading_dataset):
                replace_variables_section(markdown_file_path, heading_dataset, dataset_markdown)
                print(f"Updated dataset section in: {markdown_file_path}")
                updated = True
                break  # Stop searching once the correct file is updated
        
        if not updated:
            print(f"Could not find heading in any markdown files for dataset: {dataset}")

if __name__ == "__main__":
    main()