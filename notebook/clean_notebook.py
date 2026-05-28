import json
import re

def clean_notebook(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    cleaned_cells = []
    
    for cell in nb.get('cells', []):
        source = cell.get('source', [])
        if not source:
            continue # skip empty cells
            
        if cell['cell_type'] == 'markdown':
            new_source = []
            for line in source:
                # Add bullet point to conclusions if missing
                if line.startswith("- Conclusion Question"):
                    line = line.replace("- Conclusion Question", "**Conclusion** - Question")
                new_source.append(line)
            cell['source'] = new_source
            cleaned_cells.append(cell)
        
        elif cell['cell_type'] == 'code':
            # keep if it has actual code
            if any(line.strip() for line in source):
                cleaned_cells.append(cell)
                
    nb['cells'] = cleaned_cells
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=2)

if __name__ == '__main__':
    clean_notebook('Proyek_Analisis_Data_Louie (1).ipynb', 'ECommerce_Analysis.ipynb')
    print("Notebook cleaned and saved as ECommerce_Analysis.ipynb")
