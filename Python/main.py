# ----------------------------------------------
# Coding: utf-8
# Project: RPG Combat Simulator
# File: main.py
# Author: RicaldoniDev
# Created on 10/12/2022 - it's dd/mm/yyyy
# ----------------------------------------------

import json, re, os, PySimpleGUI as sg
from char_creator import principal

def main():
    sg.theme('DarkAmber')

    janela = sg.Window('DnD Combat Sim', layout=[[
        [sg.Text()],
        [sg.Text('Bem vindo, escolha o que deseja fazer')],
        [sg.Text()],
        [sg.Button('Lutar'), sg.Button('Criar Personagem'), sg.Button('Sair')]
    ]])

    while True:
        event, _ = janela.read()

        if event == 'Sair' or event == sg.WIN_CLOSED:
            break
        
        elif event == 'Criar Personagem':
            principal()

        elif event == 'Lutar':
            selecione_seu_personagem()


def abrir_json_personagem(char_name:str):
    with open(f'Chars/{char_name}.json', 'r') as f:
        return json.load(f)

def selecione_seu_personagem():

    arquivo_personagem = [char.name for char in os.scandir('Chars') if char.is_file()]

    if len(arquivo_personagem) < 2:
        sg.popup('Não há personagens suficiente para batalha', title='Erro!')
        return

    nome_pers = [re.sub('.json$', '', nome) for nome in arquivo_personagem]

    sg.theme('DarkAmber')

    window = sg.Window('Personagens', layout=[
        *[[[sg.Text(f'{char}', k='-NOME-'), ],
        [sg.Text('Arma:'), sg.Text(abrir_json_personagem(char)['weapon'])],
        [sg.Text('Armadura:'), sg.Text(abrir_json_personagem(char)['armor'])],
        [sg.Text('Escudo:'), sg.Text(abrir_json_personagem(char)['shield'])],
        [sg.Text('Força:'), sg.Text(abrir_json_personagem(char)['strength'])],
        [sg.Text('Destreza:'), sg.Text(abrir_json_personagem(char)['dexterity'])],
        [sg.Text('HP:'), sg.Text(abrir_json_personagem(char)['HP'])],
        [sg.Button(f'Choose {char}')], sg.HSep()] for char in nome_pers], # I've got the screen displaying all characters, but I need to display their info too, and for that I'd need to acess each char file
        [sg.Button('Sair')]], modal=True)
  
    while True:
        event, _ = window.read()

        if event == sg.WIN_CLOSED or event == 'Sair':
            window.close()
            break
        
        if event in [f'Choose {char}' for char in nome_pers]:
            print(window['-NOME-'].get())

    


if __name__ == '__main__':
    main()