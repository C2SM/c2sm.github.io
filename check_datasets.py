import requests
import json
import re
import boto3

def download_json(url):
    response = requests.get(url)
    return json.loads(response.text)

def read_markdown(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_markdown(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def update_markdown(markdown, json_data):
    # This is a placeholder. You'll need to replace this with the actual logic
    # to update the markdown content based on the JSON data.
    return re.sub(r'(Size: )(\d+ TB)', r'\1' + str(json_data['size']) + ' TB', markdown)

# Main part of the script
json_data1 = download_json('https://zephyr-c2sm.s3.eu-central-1.amazonaws.com/datasets.json')
json_data2 = download_json('https://zephyr-c2sm.s3.eu-central-1.amazonaws.com/file_tree_cordex_noindent.json')

markdown = read_markdown('climate_model_data.md')

updated_markdown = update_markdown(markdown, json_data1)
updated_markdown = update_markdown(updated_markdown, json_data2)

write_markdown('climate_model_data.md', updated_markdown)