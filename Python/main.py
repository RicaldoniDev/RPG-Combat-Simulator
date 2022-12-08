import PySimpleGUI as sg
from char_creator import principal

def main():
    sg.theme('DarkAmber')

    janela = sg.Window('DnD Combat Sim', layout=[[
        [sg.Text()],
        [sg.Text('Bem vindo, escolha o que deseja fazer')],
        [sg.Text()],
        [sg.Button('Lutar'), sg.Button('Criar Personagem'), sg.Button('Ver todos personagens'), sg.Button('Sair')]
    ]])

    while True:
        event, values = janela.read()

        if event == 'Sair' or event == sg.WIN_CLOSED:
            break
        
        elif event == 'Criar Personagem':
            principal()
            janela.close()

if __name__ == '__main__':
    main()