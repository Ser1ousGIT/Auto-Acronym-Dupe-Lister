from docx import Document
from collections import defaultdict

def extr_acro(filepath):
    doc = Document(filepath)
    acro_map = defaultdict(list)

    for para in doc.paragraphs:
        line = para.text.strip()
        if not line:
            continue
        if '\t' in line:
            parts = line.split('\t')
        else:
            parts = line.split('  ')
        parts = [p.strip() for p in parts if p.strip()]
        if len(parts) >= 2:
            acronym, expansion = parts[0], ' '.join(parts[1:])
            acro_map[acronym].append(expansion)

    return acro_map

def find_dupes(acro_map):
    dupes = {}
    for acronym, full_form in acro_map.items():
        if len(full_form) > 1:
            unique_full_form = list(set(full_form))
            dupes[acronym] = {
                "count": len(full_form),
                "full_form": unique_full_form
            }
    return dupes

def print_dupes(dupes):
    print(f"{'Acronym':<10} | {'Count':<5} | Full Form")
    for acronym, data in sorted(dupes.items()):
        full_form = "; ".join(data['full_form'])
        print(f"{acronym:<10} | {data['count']:<5} | {full_form}")

if __name__ == "__main__":
    file_path = "acronyms.docx" 
    acro_map = extr_acro(file_path)
    dupes = find_dupes(acro_map)
    print_dupes(dupes)
