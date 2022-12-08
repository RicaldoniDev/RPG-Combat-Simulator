import os, re, json

def personagem():
    arquivo_personagem = [char.name for char in os.scandir('Chars') if char.is_file()]

    nome_pers = [re.sub('.json$', '', nome) for nome in arquivo_personagem]

    for char in arquivo_personagem:
        with open(f'Chars/{char}', 'r') as f:
            info = json.load(f)
        
        for key, value in info.items():
            yield f'{key}: {value}'

print("Files and Directories in Chars':")

chars = personagem()

for x in chars:
    print(x)


