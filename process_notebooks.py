import json
import os
import re

def find_python_blocks_with_slides(qmd_content):
    # Split content into lines for processing
    lines = qmd_content.split('\n')
    
    blocks = []
    current_slide = 0
    current_block = []
    in_python_block = False
    
    for line in lines:
        # Check for slide markers (##)
        if line.strip().startswith('##'):
            current_slide += 1
            continue
            
        # Check for Python code block start
        if line.strip().startswith('```{python}') or line.strip() == '```python':
            in_python_block = True
            current_block = []
            continue
            
        # Check for code block end
        if line.strip() == '```' and in_python_block:
            if current_block:  # Only add non-empty blocks
                blocks.append({
                    'slide_number': current_slide,
                    'code': '\n'.join(current_block)
                })
            in_python_block = False
            continue
            
        # Collect Python code
        if in_python_block:
            current_block.append(line)
    
    return blocks

def create_notebook(blocks):
    notebook = {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.8"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    
    for block in blocks:
        # Add markdown cell with slide number
        header_cell = {
            "cell_type": "markdown",
            "metadata": {
                "slideshow": {"slide_type": "slide"}
            },
            "source": [f"# Slide {block['slide_number']}\n"]
        }
        notebook["cells"].append(header_cell)
        
        # Add code cell
        code_cell = {
            "cell_type": "code",
            "metadata": {
                "slideshow": {"slide_type": "fragment"}
            },
            "source": block['code'].splitlines(True),
            "outputs": [],
            "execution_count": None
        }
        notebook["cells"].append(code_cell)
    
    return notebook

def process_lecture(lecture_number):
    qmd_path = f"/home/kmcalist/QTM447/Spring2025/Lectures/Lecture{lecture_number}/Lecture{lecture_number}.qmd"
    ipynb_path = f"lectures/slideipynb/Lecture{lecture_number}.ipynb"
    
    try:
        # Read QMD file
        with open(qmd_path, 'r', encoding='utf-8') as f:
            qmd_content = f.read()
        
        # Extract Python blocks with their slide numbers
        blocks = find_python_blocks_with_slides(qmd_content)
        
        if not blocks:
            print(f"Warning: No Python blocks found in Lecture {lecture_number}")
            return
        
        # Create notebook
        notebook = create_notebook(blocks)
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(ipynb_path), exist_ok=True)
        
        # Write notebook
        with open(ipynb_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=2, ensure_ascii=False)
            
        print(f"Successfully processed Lecture {lecture_number} with {len(blocks)} Python blocks")
        
    except Exception as e:
        print(f"Error processing Lecture {lecture_number}: {e}")

# Process all lectures
for i in range(1, 29):
    print(f"\nProcessing Lecture {i}")
    process_lecture(i) 