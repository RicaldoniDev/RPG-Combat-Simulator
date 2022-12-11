import PySimpleGUI as sg

radio_tag = ["Next", "PREV"]

sg.theme("DarkBlue3")
sg.set_options(font=("Courier New", 11))

cols = [
    [[sg.Text("Next element is sg.Input", size=(28, 1)), sg.Input()]],
    [[sg.Input(), sg.Text("Previous element is sg.Input", size=(28, 1))]],
]

layout =[
    [sg.Radio(text, "position", default=(i==0), enable_events=True, key=text)
        for i, text in enumerate(radio_tag)],
    [sg.Column(cols[i], visible=(i==0), key=f'COL {i}') for i in range(2)],
]

window = sg.Window("Title", layout, finalize=True)

while True:

    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event in radio_tag:
        for i in range(2):
            window[f'COL {i}'].update(visible=values[radio_tag[i]])

window.close()