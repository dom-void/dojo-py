# The script merges all markdown files inside a folder into one file with file names in headers

import os

# path to a folder to merge:
folder_to_merge = ""

def merge_md_files(folder_path: str):
    files = [f for f in os.listdir(folder_path) if f.endswith('.md')]
    files.sort()

    merged_content = ""

    for file_name in files:
        with open(os.path.join(folder_path, file_name), 'r', encoding='utf-8') as file:
            content = file.read()
            merged_content += f"# {file_name[:-3]}\n\n"  # Adds a header with a file name
            merged_content += content + "\n\n"

    with open(os.path.join(folder_path, 'merged_file.md'), 'w', encoding='utf-8') as merged_file:
        merged_file.write(merged_content)

merge_md_files(folder_to_merge)