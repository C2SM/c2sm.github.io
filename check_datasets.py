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

def update_markdown(markdown, json_data):
    for variable, resolutions in json_data['data'].items():
        for resolution, details in resolutions.items():
            for detail_type, detail_values in details.items():
                date_range = detail_values.get('date_range', '')
                missing = detail_values.get('missing', [])
                # Assuming there's a specific way you want to format this in the markdown
                # For example, using placeholders like {{variable_day_date_range}}
                date_range_placeholder = f'{{{{{variable}_{resolution}_date_range}}}}'
                missing_placeholder = f'{{{{{variable}_{resolution}_missing}}}}'
                markdown = markdown.replace(date_range_placeholder, date_range)
                if missing:
                    missing_text = ', '.join(missing)
                else:
                    missing_text = 'None'
                markdown = markdown.replace(missing_placeholder, missing_text)
    return markdown

def generate_markdown_with_tooltips(json_data, heading_dataset):
    markdown_content = f"## {heading_dataset}\n\n"
    markdown_content += "- Variables: \n"
    datasets_with_scenario = ['cmip5', 'cmip6', 'cmip6-ng', 'cordex', 'cordex-reklies']
    
    first_iteration = True
    if heading_dataset.lower() in datasets_with_scenario:
        # New logic for datasets with an additional scenario level
        for scenario, scenario_data in json_data['data'].items():
            for variable, resolutions in scenario_data.items():
                markdown_content += append_variable_info(variable, resolutions, first_iteration, include_scenario=True, scenario=scenario)
                first_iteration = False
    else:
        # Original logic for datasets without an additional scenario level
        for variable, resolutions in json_data['data'].items():
            markdown_content += append_variable_info(variable, resolutions, first_iteration)
            first_iteration = False

    markdown_content += "\n\n"
    return markdown_content

def append_variable_info(variable, resolutions, first_iteration, include_scenario=False, scenario=None):
    variable_info = ""
    if first_iteration:
        variable_info += f"  `{variable}`{{ title=\""
    else:
        variable_info += f",\n  `{variable}`{{ title=\""
    for resolution, details in resolutions.items():
        first_iteration_info = True
        for detail_type, detail_values in details.items():
            date_range = detail_values.get('date_range', 'N/A')
            if first_iteration_info:
                if include_scenario:
                    variable_info += f"{scenario}, {resolution} ({detail_type}): {date_range}"
                else:
                    variable_info += f"{resolution} ({detail_type}): {date_range}"
                first_iteration_info = False
            else:
                if include_scenario:
                    variable_info += f", {scenario}, {resolution} ({detail_type}): {date_range}"
                else:
                    variable_info += f", {resolution} ({detail_type}): {date_range}"
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
        dataset_markdown = generate_markdown_with_tooltips(dataset_json, heading_dataset)
        write_markdown(markdown_file_path, dataset_markdown)

if __name__ == "__main__":
    main()