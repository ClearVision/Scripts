import re
import os

# Directory containing the .scss files
scss_directory = r"../src"

# File path for the selectors file
selector_file_path = r"../lib/selectors/selectorPlaceholders.scss"

# Files and folders to ignore
ignored_files = {
    r"..\src\fixespt2.scss",
    r"..\src\functions.scss",
    r"..\src\keyframes.scss",
    r"..\src\mixins.scss",
    r"..\src\variables.scss",
}
ignored_folder = r"..\src\injectors"

# Normalize the ignored file paths once, outside the loop
ignored_files_absolute = {os.path.abspath(f) for f in ignored_files}
ignored_folder_absolute = os.path.abspath(ignored_folder)

# Step 1: Extract the mappings from selectorPlaceholders.scss
mappings = {}
with open(selector_file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    placeholder_pattern = re.compile(r"\.(\w+_\w+)\s*\{\s*@extend\s*(%[\w-]+)")
    for match in placeholder_pattern.finditer(content):
        class_name, variable = match.groups()
        mappings[class_name] = variable

# Step 2: Scan all .scss files and replace classes
new_placeholders = set()
changed_files = []

def replace_classes(content, mappings):
    changes_made_local = False
    class_pattern = re.compile(r"\.(\w+_\w+)(?![\w-])")

    def class_replacement(match):
        nonlocal changes_made_local
        class_name = match.group(1)
        if class_name not in mappings:
            new_placeholders.add(class_name)  # Add the full class name
            changes_made_local = True
            return f"%{class_name.split('_')[0]}"  # Replace with the base class for @extend
        changes_made_local = True
        return mappings.get(class_name, f".{class_name}")

    updated_content = class_pattern.sub(class_replacement, content)
    return updated_content, changes_made_local

# Iterate over all .scss files in the specified directory
for root, dirs, files in os.walk(scss_directory):
    # Skip ignored folder
    if os.path.commonpath([os.path.abspath(root), ignored_folder_absolute]) == ignored_folder_absolute:
        continue

    for file_name in files:
        file_path = os.path.join(root, file_name)
        # Skip ignored files
        if os.path.abspath(file_path) in ignored_files_absolute:
            continue

        if file_name.endswith(".scss"):
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()

            updated_content, file_changed = replace_classes(file_content, mappings)

            # Save the updated content back to the file if changes were made
            if file_changed:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(updated_content)
                changed_files.append(file_path)

# Step 3: Append new placeholders to the selector file if there are any
if new_placeholders:
    with open(selector_file_path, 'a', encoding='utf-8') as file:
        for placeholder in sorted(new_placeholders):
            base_placeholder = placeholder.split('_')[0]  # Extract the base name (before underscore)
            # Write the full class name with the suffix for the class, but the base name for @extend
            file.write(f".{placeholder} {{ \n@extend %{base_placeholder} !optional;\n }}\n")

    changed_files.append(selector_file_path)

# Step 4: Print the results
if not changed_files:
    print("No changes required.")
else:
    print("Update complete! Files changed:")
    for file_path in changed_files:
        print(f"- {os.path.basename(file_path)}")
    
    if new_placeholders:
        print("\nAdded new placeholders:")
        for placeholder in sorted(new_placeholders):
            print(f"%{placeholder.split('_')[0]}")  # Display base name for new placeholder
    else:
        print("No new placeholders were added.")
