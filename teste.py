import PySimpleGUI as sg


def tela():
    window = sg.Window('titulo', layout=[
        [sg.Text('Texo aleatorio', k='lixo')],
        [sg.Button('valores'), sg.Button('redirect')]
    ])

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        elif event == 'valores':
            print(window['lixo'].get())
        elif event == 'redirect':
            meu_pau()
        
        window.close()
    
def meu_pau():
    win2 = sg.Window('tits', layout=[
        [sg.Text('Textasso pika das galaxia', k='buceta')],
        [sg.Button('mostra')]
    ])
    while True:
        evento, valores = win2.read()

        if evento == sg.WIN_CLOSED:
            break
        
        elif evento == 'mostra':
            print(valores, evento)

tela()