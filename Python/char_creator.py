import json, re, random, PySimpleGUI as sg

def remove_white_space(text):
    return re.sub('\s', '-', text)


def principal():
    sg.theme('DarkAmber')   # Dar um pouco de cor ao programa

    # Carregar os arquivos necessários
    with open('Info/armor.json', 'r') as arm:
        ARMOR = json.load(arm)
    with open('Info/weapons.json', 'r') as wpn:
        WEAPONS = json.load(wpn)
    # ----------------------------------------------
    
    # Salvar as chaves dos dicionários em listas
    armor_list = list(ARMOR.keys())
    weapon_list = list(WEAPONS.keys())
    
    # Criar a janela principal
    window = sg.Window(title='Criador de personagem', layout=[
        [sg.Text('Nome do personagem:', size=(16,1)), sg.InputText(key='-NAME-')],
        [sg.Text('Arma:', size=(16,1)), sg.InputCombo((weapon_list), key='-WPN-', readonly=True)],
        [sg.Text('Armadura:', size=(16,1)), sg.InputCombo((armor_list), key='-ARM-', readonly=True)],
        [sg.Text('O personagem tem escudo? ', size=(21,1)), sg.Radio('Sim', 'shield', key='-SIM-'), sg.Radio('Não', 'shield', key='-NAO-')],
        [sg.Button('Criar personagem'), sg.Button('Fechar')]], modal=True)
    # ----------------------------------------------
    
    # Loop que ouve constantemente por eventos na janela
    while True:
        event, values = window.read()

        # Se clicar no 'X' ou em 'Sair' sai do loop e fecha a janela
        if event == sg.WIN_CLOSED or event == 'Fechar':
            break
        # ------------------------------------------

        if event == 'Criar personagem':
            # Checar se o personagem tem um escudo
            if values['-SIM-']:

                # Se a arma dele tiver a propriedade 2-hand, ele não será capaz de usar um escudo
                if '2-hand' in WEAPONS[values['-WPN-']]['props']:
                    sg.popup('Erro!', 'Você não pode usar um escudo com uma arma de 2 mãos')
                    continue
                else:
                    shield = True
                # -------------------------------
            else:
                shield = False
            atributos(values['-NAME-'],values['-WPN-'],values['-ARM-'], shield)
        window.close()


def atributos(name:str, wpn:str, arm:str, shield:bool):
    sg.theme('Dark Amber')


    # Essa tela está dividida em colunas, para melhor organização
    janela = sg.Window('Escolha seus atributos', layout=[
        [sg.Column([
            [sg.Text('Pontos restantes:', size=(15, 1))],
            [sg.Text('Força:', k='-STR-', size=(15, 1))],
            [sg.Text('Destreza:', k='-DEX-', size=(15, 1))],
            [sg.Text('Constituição:', k='-HP-', size=(15, 1))]]), sg.VSeparator(),
        sg.Column([
            [sg.Text('30',size=(8, 1), k='-NUM-')],
            [sg.Text('0', k='-STR_PT-', size=(15, 1))],
            [sg.Text('0', k='-DEX_PT-', size=(15, 1))],
            [sg.Text('0', k='-HP_PT-', size=(15, 1))]]), sg.VSeparator(),
        sg.Column([
            [sg.Text()],
            [sg.Button('+', k='-ADD_STR-', size=(1,1))],
            [sg.Button('+', k='-ADD_DEX-',size=(1,1))],
            [sg.Button('+', k='-ADD_HP-',size=(1,1))],
            ]),
        sg.Column([
            [sg.Text()],
            [sg.Button('-', k='-SUB_STR-', size=(1,1))],
            [sg.Button('-', k='-SUB_DEX-',size=(1,1))],
            [sg.Button('-', k='-SUB_HP-',size=(1,1))],
            ])],
        [sg.Button('Confirmar'), sg.Button('Cancelar')]], modal=True)

    while True:
        event, _ = janela.read()

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

        # Para evitar o uso de 3 ifs e elifs o programa procura dentre esta lista,
        # e ela pode ser expandida para mais atributos, desde que seja seguido o padrão de nomenclatura das chaves
        elif event in ['-ADD_STR-', '-ADD_DEX-', '-ADD_HP-']:

            # Pega apenas os caracters depois do '-ADD_' e para no penúltimo,
            # e então transorma na chave dos pontos
            atr = event[5 : len(event)-1]
            change = f'-{atr}_PT-'

            # Apenas pega os textos de números e transorma-os em int
            current_num = int(janela[change].get())
            max_num = int(janela['-NUM-'].get())


            # Enquanto o número máximo de pontos for acima de 0, ele vai continuar alterando os números
            if max_num > 0:
                janela[change].update(current_num + 1)
                janela['-NUM-'].update(max_num - 1)
            
        elif event in ['-SUB_STR-', '-SUB_DEX-', '-SUB_HP-']:

            # Pega apenas os caracters depois do '-ADD_' e para no penúltimo,
            # e então transorma na chave dos pontos
            atr = event[5 : len(event)-1]
            change = f'-{atr}_PT-'

            # Apenas pega os textos de números e transorma-os em int
            current_num = int(janela[change].get())
            try:
                max_num = int(janela['-NUM-'].get())
            except ValueError:
                sg.popup('Erro!', 'Role o dado antes de adicionar o bonus!')
                continue

            # Enquanto o número máximo de pontos for abaixo de 0, ele vai continuar alterando os números
            if max_num < 30:
                janela[change].update(current_num - 1)
                janela['-NUM-'].update(max_num + 1)
        
        elif event == 'Confirmar':
            dados = {
                'name' : name,
                'weapon' : wpn,
                'armor' : arm,
                'shield' : shield,
                'strength': int(janela['-STR_PT-'].get()),
                'dexterity': int(janela['-DEX_PT-'].get()),
                'HP' : 30 + int(janela['-HP_PT-'].get()),
            }
            
            try:
                with open(f'Chars/{name}.json', 'x') as f:
                   json.dump(dados, f)
                   break
            except FileExistsError:
                sg.popup('Erro!', 'Esse personagem já existe')
            janela.close()




def main():
    principal()

if __name__ == '__main__':
    main()
