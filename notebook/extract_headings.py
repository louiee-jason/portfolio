import json
import glob

files = ["[Clustering]_Submission_Akhir_BMLP_Louie_Jason (1).ipynb", "[Klasifikasi]_Submission_Akhir_BMLP_Louie_Jason.ipynb"]

for fname in files:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        print(f"=== {fname} ===")
        for cell in nb.get('cells', []):
            if cell['cell_type'] == 'markdown':
                source = cell.get('source', [])
                for line in source:
                    if line.startswith('#'):
                        print(line.strip())
        print("\n")
    except Exception as e:
        print(f"Error reading {fname}: {e}")
