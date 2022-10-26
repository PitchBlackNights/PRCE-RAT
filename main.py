import PySimpleGUI as sg
import os

layout = [  [sg.Text('Thank you for installing PRCE-RAT')],
            [sg.Text('Please enter the address and port of your PRCE-RAT control server:')],
            [sg.Text('ADDRESS:'), sg.InputText()],
            [sg.Text('PORT:'), sg.InputText()],
            [sg.Button('Finish'), sg.Button('Cancel')] ]
window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()  # type: ignore
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Finish':
        address = values[0]
        port = values[1]
        print("Address:",address)
        print("Port:",port)

window.close()