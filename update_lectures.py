#!/usr/bin/env python3

import os
import re
import glob

def update_lecture_file(lecture_number):
    """Update lecture file to include summary with Python block"""
    lecture_file = f"/home/kmcalist/ClassSites/QTM447/lectures/lecture{lecture_number}.qmd"
    
    # Check if the file exists
    if not os.path.exists(lecture_file):
        print(f"File {lecture_file} doesn't exist, skipping...")
        return False
    
    with open(lecture_file, 'r') as file:
        content = file.read()
    
    # Check if file already has our Python block
    if '#| echo: false' in content and 'import re' in content:
        print(f"Lecture {lecture_number} already updated, skipping...")
        return False
        
    # Pattern to find the end of material boxes before we insert our code
    material_boxes_pattern = r'<div class="material-type"[^>]*>.*?</div>\s*</div>\s*:::(?!\s*</div>\s*:::)'
    match = re.search(material_boxes_pattern, content, re.DOTALL)
    
    if match:
        # Build our Python block
        python_block = f'''

```{{python}}
#| echo: false
#| output: asis

import re
with open("summaries/Lecture{lecture_number}Summary.qmd", "r") as f:
    content = f.read()
    
# Remove YAML front matter
if content.startswith("---"):
    parts = content.split("---", 2)
    if len(parts) >= 3:
        content = parts[2]
    
print(content)
```

:::'''
        
        # Replace existing content after material boxes with our Python block
        new_content = re.sub(
            r'(:::(?!\s*</div>\s*:::))\s*(?:## Lecture Summary)?(?:.*?)(?=:::$|\Z)', 
            r'\1' + python_block, 
            content, 
            flags=re.DOTALL
        )
        
        with open(lecture_file, 'w') as file:
            file.write(new_content)
        print(f"Updated lecture{lecture_number}.qmd successfully")
        return True
    else:
        print(f"Could not find material boxes in lecture{lecture_number}.qmd")
        return False

def update_summary_file(lecture_number):
    """Update summary file to replace \[ \] with $$"""
    summary_file = f"/home/kmcalist/ClassSites/QTM447/lectures/summaries/Lecture{lecture_number}Summary.qmd"
    
    # Check if the file exists
    if not os.path.exists(summary_file):
        print(f"File {summary_file} doesn't exist, skipping...")
        return False
    
    with open(summary_file, 'r') as file:
        content = file.read()
    
    # Replace \[ with $$ and \] with $$
    updated_content = content.replace('\\[', '$$').replace('\\]', '$$')
    
    with open(summary_file, 'w') as file:
        file.write(updated_content)
    
    print(f"Updated Lecture{lecture_number}Summary.qmd successfully")
    return True

def main():
    """Main function to update all lectures"""
    for lecture_number in range(3, 12):  # For lectures 3 through 11
        print(f"\nProcessing Lecture {lecture_number}...")
        update_summary_file(lecture_number)
        update_lecture_file(lecture_number)

if __name__ == "__main__":
    main()
