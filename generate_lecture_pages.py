import os
import re

# Lecture titles from index.qmd
LECTURE_TITLES = {
    1: "Introduction",
    2: "Statistical Machine Learning Basics",
    3: "Generalization: The Predictive Goal",
    4: "Linear Models: The Starting Point",
    5: "Loss Minimization and Optimization",
    6: "Adaptive Minimization Methods",
    7: "Nonlinearities and Universal Approximators",
    8: "Introduction to Neural Networks for Tabular Data",
    9: "Deep Neural Networks: What do they learn? Do they learn things?? Let's find out!",
    10: "Backpropogation: The microwave dinner of optimization algorithms",
    11: "Vanishing Gradients and Generalization for Deep Neural Networks",
    12: "Convolutional Neural Networks for Image Classification",
    13: "CNN Architectures and Transfer Learning",
    14: "Object Detection in Images",
    15: "Semantic Segmentation",
    16: "A Very Fast Lecture on Recurrent Neural Networks and LSTMs",
    17: "Sequence Models and Attention",
    18: "Transformers: RNNs are so last decade",
    19: "Representation Learning and Vision Transformers",
    20: "Intro to Generative Models: Autoregressives and Autoencoders",
    21: "Deterministic Autoencoders (and why they fail for image generation); Intro to Bayesian Machine Learning",
    22: "Bayesian Machine Learning",
    23: "Variational Autoencoders",
    24: "More on Variational Autoencoders and Introduction to Generative Adversarial Networks",
    25: "Generative Adversarial Networks",
    26: "Diffusion Models and Stable Diffusion",
    27: "Interpretable Deep Learning: Post-Hoc Methods and Glass-Box Models",
    28: "Ethics and Fairness in Deep Learning and Modern Artificial Intelligence"
}

def check_file_exists(filepath):
    return os.path.exists(filepath)

def generate_material_box(title, link_path, image_path, is_active):
    if is_active:
        return f"""<a href="{link_path}" class="material-box" target="_blank" rel="noopener noreferrer">
    <div class="material-title">{title}</div>
    <div class="material-image">
        <img src="images/interface/{image_path}" alt="{title}" class="interface-image">
    </div>
</a>"""
    else:
        return f"""<div class="material-box disabled">
    <div class="material-title">{title}</div>
    <div class="material-image">
        <img src="images/interface/{image_path}" alt="{title}" class="interface-image disabled">
    </div>
</div>"""

def generate_lecture_page(lecture_num):
    title = LECTURE_TITLES.get(lecture_num, f"Lecture {lecture_num}")
    
    # Check which files exist
    html_exists = check_file_exists(f"lectures/htmls/Lecture{lecture_num}.html")
    slide_ipynb_exists = check_file_exists(f"lectures/slideipynb/Lecture{lecture_num}.ipynb")
    code_ipynb_exists = check_file_exists(f"lectures/ipynbs/Lecture{lecture_num}Code.ipynb")
    
    content = f"""---
title: "Lecture {lecture_num}: {title}"
format:
  html:
    css: ../styles.css
---

```{{=html}}
<style>
.materials-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
    margin: 60px auto;
    max-width: 1200px;
}}

.material-box {{
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 25px;
    background: #ffffff;
    transition: all 0.3s ease;
    text-decoration: none;
    color: inherit;
    display: flex;
    flex-direction: column;
    aspect-ratio: 1;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}}

.material-box:not(.disabled):hover {{
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    border-color: #3498db;
}}

.material-box.disabled {{
    opacity: 0.5;
    cursor: not-allowed;
    background: #f8f9fa;
}}

.material-title {{
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 20px;
    font-size: 1.3em;
    text-align: center;
}}

.material-image {{
    flex-grow: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
}}

.interface-image {{
    width: 100%;
    height: 100%;
    object-fit: contain;
    transition: transform 0.2s ease;
}}

.material-box:hover .interface-image {{
    transform: scale(1.05);
}}

.interface-image.disabled {{
    opacity: 0.5;
    filter: grayscale(100%);
}}

@media (max-width: 1200px) {{
    .materials-grid {{
        padding: 0 20px;
    }}
}}

@media (max-width: 992px) {{
    .materials-grid {{
        grid-template-columns: repeat(2, 1fr);
    }}
}}

@media (max-width: 768px) {{
    .materials-grid {{
        grid-template-columns: 1fr;
    }}
    
    .material-box {{
        aspect-ratio: auto;
        height: 300px;
    }}
}}
</style>

<div class="materials-grid">
    {generate_material_box(
        "Lecture Slides",
        f"htmls/Lecture{lecture_num}.html",
        "slides.svg",
        html_exists
    )}
    {generate_material_box(
        "Slide Code",
        f"slideipynb/Lecture{lecture_num}.ipynb",
        "code.svg",
        slide_ipynb_exists
    )}
    {generate_material_box(
        "Lecture Code",
        f"ipynbs/Lecture{lecture_num}Code.ipynb",
        "notebook.svg",
        code_ipynb_exists
    )}
</div>
```"""
    
    with open(f"lectures/lecture{lecture_num}.qmd", 'w') as f:
        f.write(content)

# Generate pages for all lectures
for i in range(1, 29):
    generate_lecture_page(i) 