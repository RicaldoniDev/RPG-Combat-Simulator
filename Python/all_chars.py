import os, re , PySimpleGUI as sg


def main():

    arquivo_personagem = [char.name for char in os.scandir('Chars') if char.is_file()]

    nome_pers = [re.sub('.json$', '', nome) for nome in arquivo_personagem]

    sg.theme('DarkAmber')

    window = sg.Window('Personagens', layout=[
        *[[sg.Text(f'{char}'), ] for char in nome_pers],
        [sg.Button('Sair')]])

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Sair':
            break


if __name__ == '__main__':
    main()