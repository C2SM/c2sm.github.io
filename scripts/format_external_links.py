import os
import re
import argparse

def modify_link(line):
    pattern = r'\[([^\]]+)\]\((http[s]?://[^\s\)]+)\)'
    replacement = r'[\1 :material-open-in-new:](\2){:target="_blank"}'
    modified_line, num_subs = re.subn(pattern, replacement, line)
    # Check if the line was already modified or doesn't need modification
    if ':material-open-in-new:' in line and '{:target="_blank"}' in line:
        return line, False
    return modified_line, num_subs > 0

def process_markdown_file(file_path):
    with open(file_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        modified = False
        for i, line in enumerate(lines):
            new_line, changed = modify_link(line)
            if changed:
                modified = True
                lines[i] = new_line
        if modified:
            file.seek(0)
            file.writelines(lines)
            file.truncate()
            print(f"Modified: {file_path}")

def main(start_path):
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file.endswith('.md'):
                process_markdown_file(os.path.join(root, file))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check markdown links in files.')
    parser.add_argument('-p', '--path', default=os.getcwd(), help='Base path to search for markdown files. Defaults to current working directory.')
    args = parser.parse_args()

    main(args.path)