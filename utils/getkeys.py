# Citation: Box Of Hats (https://github.com/Box-Of-Hats )

import win32api as wapi
import time
import yaml
from pathlib import Path

main_path = Path(__file__).parent.parent
# Load Config
config_path = f"{main_path}\\utils\\config.yaml"
with open(config_path) as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
dummmy_direction = config['dummmy_direction']





keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'APS$/\\&(%":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)

       

    if 'H' in keys:
        return 'H'
    elif 'B' in keys:
        return 'B'
    elif 'A' in keys:
        return 'A'
    elif 'D' in keys:
        return 'D'
    elif '&' in keys:
        return 'UP_KEY'
    elif '\'' in keys:
        return 'RIGHT_KEY'
    elif '(' in keys:
        return 'DOWN_KEY'
    elif '%' in keys:

        return 'LEFT_KEY'    
    elif ' ' in keys:
        return ' '
    else:
        return dummmy_direction
