import re
import os

# File paths (adjust these paths as necessary)
selector_file_path = r"../lib/selectors/selectorPlaceholders.scss"
scss_directory = r"../src/"

# List of files to ignore
ignore_files = {
    r"..\ClearVision-v6\src\defaultSettings.scss",
    r"..\ClearVision-v6\src\defaultSettings.scss",
    r"..\ClearVision-v6\src\fixespt2.scss",
    r"..\ClearVision-v6\src\functions.scss",
    r"..\ClearVision-v6\src\keyframes.scss",
    r"..\ClearVision-v6\src\mixins.scss",
    r"..\ClearVision-v6\src\variables.scss"
}

# Step 1: Extract all placeholders from selectorPlaceholders.scss
valid_placeholders = set()
with open(selector_file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    placeholder_pattern = re.compile(r"(%[\w-]+)")
    valid_placeholders.update(placeholder_pattern.findall(content))

# Define a function to remove invalid placeholders
def remove_invalid_placeholders(content, valid_placeholders):
    placeholder_pattern = re.compile(r"(%[\w-]+)")
    
    def placeholder_replacement(match):
        placeholder = match.group(1)
        # Only keep placeholders that exist in the valid list
        return placeholder if placeholder in valid_placeholders else ""
    
    return placeholder_pattern.sub(placeholder_replacement, content)

# Track changed files
changed_files = []

# Step 2: Recursively read all .scss files in the specified directory
for root, dirs, files in os.walk(scss_directory):
    for file_name in files:
        if file_name.endswith('.scss'):
            file_path = os.path.join(root, file_name)
            
            # Skip ignored files
            if file_path.replace("\\", "/") in ignore_files:
                continue
            
            with open(file_path, 'r', encoding='utf-8') as file:
                original_content = file.read()
            
            # Remove invalid placeholders and check if the file has changed
            cleaned_content = remove_invalid_placeholders(original_content, valid_placeholders)
            if cleaned_content != original_content:
                changed_files.append(file_path)
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(cleaned_content)

# Step 3: Output results
if changed_files:
    print("Clean-up complete! Files Changed:")
    for changed_file in changed_files:
        print(changed_file)
else:
    print("No changes made.")
