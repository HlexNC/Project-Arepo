import os
import json
import fnmatch
import re

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            # If the file is not a Python file, remove unnecessary whitespaces
            if not file_path.endswith('.py'):
                # Remove leading/trailing whitespace, multiple spaces, tabs, newlines, etc.
                content = re.sub(r'\s+', ' ', content).strip()

            return content
    except UnicodeDecodeError:
        return None

def parse_gitignore(gitignore_path):
    ignore_patterns = []
    try:
        with open(gitignore_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    ignore_patterns.append(line)
    except FileNotFoundError:
        pass
    return ignore_patterns

def is_ignored(file_path, ignore_patterns):
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(file_path, pattern):
            return True
    return False

def dir_structure(directory):
    structure = {}
    for root, dirs, files in os.walk(directory):
        # Skip 'node_modules' directories and 'output.json'
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        
        # Exclude the output.json itself
        if 'output.json' in files:
            files.remove('output.json')

        relative_path = os.path.relpath(root, directory)
        if relative_path == ".":
            relative_path = ""
        
        sub_structure = structure
        if relative_path:
            for part in relative_path.split(os.sep):
                sub_structure = sub_structure.setdefault(part, {})
        
        for file in files:
            sub_structure[file] = None  # Store presence of file without content

    return structure

def dir_to_json(directory):
    result = {}
    ignore_patterns = []

    # Files that should never be included in the output
    excluded_files = {'.env', '.gitignore', 'package.json', 'package-lock.json', 'output.json'}

    for root, dirs, files in os.walk(directory):
        # Skip 'node_modules' directories
        if 'node_modules' in dirs:
            dirs.remove('node_modules')

        # Check if there's a .gitignore file in the current directory
        gitignore_path = os.path.join(root, '.gitignore')
        ignore_patterns.extend(parse_gitignore(gitignore_path))

        relative_path = os.path.relpath(root, directory)
        if relative_path == ".":
            relative_path = ""
        
        sub_result = result
        if relative_path:
            for part in relative_path.split(os.sep):
                sub_result = sub_result.setdefault(part, {})

        for file in files:
            file_path = os.path.join(root, file)
            relative_file_path = os.path.relpath(file_path, directory)

            # Skip files listed in excluded_files
            if file in excluded_files:
                print(f"Skipping excluded file: {file_path}")
                continue

            # Check for long paths
            if len(file_path) >= 260:  # Windows MAX_PATH limit
                print(f"Skipping file due to long path: {file_path}")
                continue

            # Skip files that match ignore patterns
            if is_ignored(relative_file_path, ignore_patterns):
                continue

            # Skip the output.json file itself
            if file == 'output.json':
                continue

            # Read file content
            file_content = read_file(file_path)
            if file_content is not None:
                sub_result[file] = file_content

    return result

def main():
    directory = r'.'
    
    # Initialize the result object to hold both file contents and structure
    final_output = {}

    # First, add the directory structure to the output
    final_output["structure"] = dir_structure(directory)

    # Then, add the file contents (excluding excluded files)
    final_output["files"] = dir_to_json(directory)

    json_output = os.path.join(directory, 'output.json')

    # Always rewrite the output file, no appending
    with open(json_output, 'w', encoding='utf-8') as json_file:
        # Use 1 space for indentation
        json.dump(final_output, json_file, ensure_ascii=False, indent=1)

    print(f"JSON data has been written to {json_output}")

if __name__ == "__main__":
    main()