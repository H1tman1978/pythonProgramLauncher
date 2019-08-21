# Python Program Launcher V 0.0.1
#### By Tony Rolfe

Python Program Launcher is a Python script for creating a desktop program launcher in the Windows environment.

## Installation

Copy the script to any folder. Future versions will include an automated installation process.


## Usage

Open your command line interface to the installation folder and type the following command:
```bash
python programlauncher.py
```

## Instructions to Modify Script
```html
1. Double check program constants' path to ensure paths are correct. This is especially true 
in the Windows environment. You WILL need to change the user name, etc.
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
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[GPL3.0](https://choosealicense.com/licenses/gpl-3.0/)
