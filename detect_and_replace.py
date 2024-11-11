# This script is to aid in finding references that can be shorthands, defined in the variables.scss file
# This script was designed for use with Clearvision variables and needs heavy modification for indivual use. 

import re
import os

# Function to perform the replacements
def replace_shorthands_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        original_content = file.read()

    # Copy the original content
    content = original_content

    # Define the replacements as patterns
    replacements = {
        r"var\(--main-color\)": "$main-color",            # Detect var(--main-color)
        r"var\(--hover-color\)": "$hover-color",          # Detect var(--hover-color)
        r"var\(--text-normal\)": "$text-normal",          # Detect var(--text-normal)
        r"var\(--background-shading\)": "$bg-shading",    # Detect var(--background-shading)
        r"cv\('colors\.main'\)": "$main-color",           # Detect cv('colors.main')
        r"cv\('colors\.hover'\)": "$hover-color",         # Detect cv('colors.hover')
        r"cv\('bg\.app\.shading'\)": "$bg-shading",       # Detect cv('bg.app.shading')
        r"#\{\$(main-color|hover-color|bg-shading|text-normal)\}": r"$\1"  # Detect #{$variable}
    }

    # Apply all replacements
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)

    # Only write back if there are changes
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Replaced shorthand variables in {file_path}")
    else:
        print(f"No changes needed for {file_path}")

# Define the directory to scan for SCSS files
def replace_in_directory(directory):
    # List of specific files to ignore
    ignored_files = {
        os.path.normpath('src/defaultSettings.scss'),
        os.path.normpath('src/variables.scss'),
    }

    # Recursively walk through the directory to find .scss and .css files
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Process only .scss and .css files
            if file.endswith(".scss") or file.endswith(".css"):
                file_path = os.path.normpath(os.path.join(root, file))

                # Skip ignored files
                if file_path in ignored_files:
                    print(f"Skipping file {file_path}")
                    continue

                replace_shorthands_in_file(file_path)

# Specify the 'src' directory for scanning
replace_in_directory('./src')
