import json
import os

def is_notebook_empty(notebook_path):
    with open(notebook_path, 'r') as f:
        notebook = json.load(f)
        return len(notebook.get('cells', [])) == 0

# Check and delete empty notebooks
for i in range(1, 29):
    notebook_path = f'lectures/slideipynb/Lecture{i}.ipynb'
    if os.path.exists(notebook_path):
        if is_notebook_empty(notebook_path):
            os.remove(notebook_path)
            print(f"Deleted empty notebook: Lecture{i}.ipynb")
        else:
            print(f"Kept notebook with content: Lecture{i}.ipynb") 