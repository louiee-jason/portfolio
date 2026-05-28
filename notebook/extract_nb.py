import json
import sys

def extract(nb_path):
    with open(nb_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    code = []
    markdown = []
    
    for i, cell in enumerate(data.get('cells', [])):
        if cell['cell_type'] == 'code':
            code.append(f"# --- Code Cell {i} ---")
            code.append(''.join(cell.get('source', [])))
            code.append('\n')
        elif cell['cell_type'] == 'markdown':
            markdown.append(f"<!-- Markdown Cell {i} -->")
            markdown.append(''.join(cell.get('source', [])))
            markdown.append('\n')
            
    with open('nb_extracted.py', 'w', encoding='utf-8') as f:
        f.write('\n'.join(code))
        
    with open('nb_extracted.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(markdown))
        
    print(f"Extracted {len(code)} code lines and {len(markdown)} markdown lines")

if __name__ == '__main__':
    extract(sys.argv[1])
