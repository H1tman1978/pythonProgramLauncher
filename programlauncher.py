"""
programlauncher
by Tony Rolfe

Script to create a desktop program launcher for several programs.
Currently supports FireFox, IBM Notes, Slack and PyCharm installed in default locations.
Script can be readily adjusted to other users' locations if the user has a beginner to intermediate knowledge of Python.
----------------------------------------------

Instructions:

1. Double check program constants' path to ensure paths are correct. This is especially true in the Windows environment.
You WILL need to change the user name, etc.
    eg. TonyRolfe to your username

2. If you would like to add new ones:
    A. Add a new constant with the program's path
        eg CHROME = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    B. Add a new button to the list of buttons on Layout constant
        eg PsG.Button('Chrome'),
    C. Add a corresponding event listener to the list of elif statements.
        eg     elif event == 'Chrome':
                    sp = subprocess.Popen([CHROME, values['_URL_']], shell=True, stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
"""

import subprocess
import PySimpleGUI as PsG

# Constants that point to specific program's path. Change to suit your needs/specifications
FIREFOX = r"C:\Program Files\Mozilla Firefox\firefox.exe"
IBM_NOTES = r"C:\Notes\notes.exe"
SLACK = r"C:\Users\TonyRolfe\AppData\Local\slack\slack.exe"
PYCHARM = r"C:\Program Files\JetBrains\PyCharm 2019.2\bin\pycharm64.exe"

# Layout constant for the window
LAYOUT = [
    [PsG.Text('Text area', key='_TEXT_')],
    [PsG.Input(do_not_clear=True, key='_URL_')],
    [PsG.Button('FireFox'), PsG.Button('IBM Notes'), PsG.Button('Slack'), PsG.Button('PyCharm'), PsG.Button('Exit')]
]
TITLE = 'Desktop Program Launcher'

window = PsG.Window(TITLE, LAYOUT)

# Event Listener
while True:
    event, values = window.Read()
    print(event, values)
    if event is None or event == 'Exit':
        break
    elif event == 'FireFox':
        sp = subprocess.Popen([FIREFOX, values['_URL_']], shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
    elif event == 'IBM Notes':
        sp = subprocess.Popen([IBM_NOTES, values['_URL_']], shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
    elif event == 'Slack':
        sp = subprocess.Popen([SLACK, values['_URL_']], shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
    elif event == 'PyCharm':
        sp = subprocess.Popen([PYCHARM, values['_URL_']], shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)

# Close the window
window.Close()
