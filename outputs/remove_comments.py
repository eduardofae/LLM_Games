import os

THIS_FILE = ".\\remove_comments.py"

def get_files_in_dir(path='.'):
    files = []
    for arquive in os.listdir(path):
        full_path = os.path.join(path, arquive)
        if os.path.isdir(full_path):
            files.extend(get_files_in_dir(full_path))
        elif (full_path != THIS_FILE):
            files.append(full_path)
    print(f"Arquivos de {path} adquiridos com sucesso!")
    return files

def remove_comments(files=[]):
    for file in files:
        f = open(file, 'r')
        text = f.read()
        f.close()
        
        if(text.count('```') > 0):
            text = text.split('```')[1].replace('python\n', '', 1)

        f = open(file, 'w')
        f.write(text)
        f.close()
        print(f"Comentário do arquivo {file} removido com sucesso!")

print("Adquirindo Arquivos")
files = get_files_in_dir(".")
print("Todos os Arquivos foram adquiridos com sucesso!\n")
print("Removendo comentários")
remove_comments(files)
print("Todos os Comentário foram removidos com sucesso!")