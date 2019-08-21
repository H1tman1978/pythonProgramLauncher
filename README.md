# pythonProgramLauncher
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
