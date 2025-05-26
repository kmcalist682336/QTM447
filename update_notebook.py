import nbformat
from nbformat.v4 import new_markdown_cell

# Read the notebook
with open('lectures/ipynbs/Lecture11Code.ipynb') as f:
    nb = nbformat.read(f, as_version=4)

# Read our markdown content
with open('lecture11_with_explanations.txt') as f:
    explanations = f.read()

# Split explanations into sections
sections = explanations.split('##')
sections = ['#' + s for s in sections[1:]]  # Add back the # for each section

# Create markdown cells
markdown_cells = [new_markdown_cell(section.strip()) for section in sections]

# Insert markdown cells at appropriate positions
positions = [0, 2, 4, 8, 12, 16, 20, 24]  # Adjust these positions as needed
for pos, cell in zip(positions, markdown_cells):
    nb.cells.insert(pos, cell)

# Write the modified notebook
with open('lectures/ipynbs/Lecture11Code.ipynb', 'w') as f:
    nbformat.write(nb, f)
print('Notebook updated successfully') 