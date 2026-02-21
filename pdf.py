import os
import sys
import math

def format_bytes(bytes):
    """Converte bytes para formato legível"""
    if bytes == 0:
        return "0 Bytes"
    
    k = 1024
    sizes = ["Bytes", "KB", "MB", "GB"]
    i = int(math.floor(math.log(bytes) / math.log(k)))
    
    return f"{round(bytes / pow(k, i), 1)} {sizes[i]}"

def format_name(filename):
    """Converte nome do arquivo para display"""
    name = filename.replace('.pdf', '').replace('-', ' ').replace('_', ' ')
    return ' '.join(word.capitalize() for word in name.split()) + '.pdf'

def generate_pdf_js(folder_path='pdfs'):
    """Gera código JavaScript dos PDFs na pasta"""
    
    if not os.path.exists(folder_path):
        print(f"Erro: Pasta '{folder_path}' não encontrada!")
        return
    
    # Coleta PDFs
    pdfs = []
    for filename in sorted(os.listdir(folder_path)):
        if filename.lower().endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            size = format_bytes(os.path.getsize(file_path))
            
            pdfs.append({
                'name': format_name(filename),
                'filename': filename,
                'size': size
            })
    
    if not pdfs:
        print(f"Nenhum PDF encontrado em '{folder_path}'")
        return
    
    # Gera JavaScript
    print("const pdfList = [")
    for i, pdf in enumerate(pdfs):
        comma = "," if i < len(pdfs) - 1 else ""
        print(f'    {{')
        print(f'        name: "{pdf["name"]}",')
        print(f'        filename: "{pdf["filename"]}",')
        print(f'        size: "{pdf["size"]}"')
        print(f'    }}{comma}')
    print("];")
    
    print(f"\n// {len(pdfs)} PDFs encontrados")

if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else 'pdfs'
    generate_pdf_js(folder)