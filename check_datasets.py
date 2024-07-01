import requests
import json
import os
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
    markdown_content = f"## {heading_dataset}\n\n"
    markdown_content += "- Variables: \n"
    
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

    markdown_content += "\n\n"
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

def main():
    markdown_file_path = '../c2sm.github.io-mkdocs/docs/datasets/variables_date_ranges.md'
    # Check if the file exists before attempting to delete it
    if os.path.exists(markdown_file_path):
        os.remove(markdown_file_path)
        print(f"Removed old markdown file: {markdown_file_path}")
    else:
        print(f"No old markdown file to remove: {markdown_file_path}")

    # Read the datasets file
    datasets = read_yaml('datasets.yaml')

    # Process data for each dataset and append markdown file
    for dataset in datasets.keys():
        dataset_json = download_json(f'https://zephyr-c2sm.s3.eu-central-1.amazonaws.com/file_tree_{dataset}_noindent.json')
        heading_dataset = datasets[dataset]
        print(heading_dataset)
        dataset_markdown = generate_markdown_with_tooltips(dataset_json, heading_dataset, dataset)
        write_markdown(markdown_file_path, dataset_markdown)

if __name__ == "__main__":
    main()