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
    markdown_content += f"- Variables: \n"
    first_iteration = True
    for variable, resolutions in json_data['data'].items():
        if first_iteration:
            markdown_content += f"  `{variable}`{{ title=\""
            first_iteration = False
        else:
            markdown_content += f",\n  `{variable}`{{ title=\"" 
        first_iteration_info = True
        for resolution, details in resolutions.items():
            # Iterate over all keys in details
            for detail_type, detail_values in details.items():
                date_range = detail_values.get('date_range', 'N/A')
                if first_iteration_info:
                    markdown_content += f"{resolution} ({detail_type}): {date_range}"    
                    first_iteration_info = False
                else:
                    markdown_content += f", {resolution} ({detail_type}): {date_range}"    
        markdown_content += f"\" }}"

    markdown_content += "\n\n"
    return markdown_content

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