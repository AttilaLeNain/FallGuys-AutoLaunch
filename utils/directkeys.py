# direct inputs
# source to this solution and code:
# http://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

import ctypes
import time
from typing import List

SendInput = ctypes.windll.user32.SendInput
'''
List of keycodes:
` = 0x29 #on ANSI keyboards (ISO key is overridden in CRDKeyboard) 
^ = 0x29 # on ISO keyboards 
1 = 0x02
2 = 0x03
3 = 0x04
4 = 0x05
5 = 0x06
6 = 0x07
7 = 0x08
8 = 0x09
9 = 0x0A
0 = 0x0B
- = 0x0C
= = 0x0D
Tab = 0x0F
Q = 0x10
W = 0x11
E = 0x12
R = 0x13
T = 0x14
Y = 0x15
U = 0x16
I = 0x17
O = 0x18
P = 0x19
[ = 0x1A
] = 0x1B
A = 0x1E
S = 0x1F
D = 0x20
F = 0x21
G = 0x22
H = 0x23
J = 0x24
K = 0x25
L = 0x26
; = 0x27
' = 0x28
\ = 0x2B
Z = 0x2C
X = 0x2D
C = 0x2E
V = 0x2F
B = 0x30
N = 0x31
M = 0x32
, = 0x33
. = 0x34
/ = 0x35


# Non-printing keys.

# F-keys
f1 = 0x3b	
f2 = 0x3c	
f3 = 0x3d	
f4 = 0x3e	
f5 = 0x3f	
f6 = 0x40	
f7 = 0x41	
f8 = 0x42	
f9 = 0x43	
f10 = 0x44	
f11 = 0x57	
f12 = 0x58	
Scroll lock (f15) = 0x46	

# Print Screen and Pause/Break is hardcoded in CRDKeyboard

# Misc keys
esc = 0x01
return = 0x1c
enter = 0x1c
space = 0x39

# Right group
insert = 0xd2
delete = 0xd3
backspace = 0x0e
left arrow = 0xcb
right arrow = 0xcd
up arrow = 0xc8
down arrow = 0xd0
home = 0xc7
end = 0xcf
page up = 0xc9
page down = 0xd1

# Numpad
Numlock toggle, using 'clear' button = 0x45
Numeric =, just use normal equals = 0xd	
Numeric / = 0xb5
Numeric * = 0x37
Numeric - = 0x4a
Numeric + = 0x4e
Numeric . = 0x53
Numeric 0 = 0x52
Numeric 1 = 0x4f
Numeric 2 = 0x50
Numeric 3 = 0x51
Numeric 4 = 0x4b
Numeric 5 = 0x4c
Numeric 6 = 0x4d
Numeric 7 = 0x47
Numeric 8 = 0x48
Numeric 9 = 0x49
Numeric enter = 0x9c

'''



W = 0x11
A = 0x1E
S = 0x1F
D = 0x20
M = 0x32
K = 0x25
L = 0x26
R = 0x27
F = 0x21
J = 0x24


LEFT_ARROW = 0xcb
RIGHT_ARROW = 0xcd
UP_ARROW = 0xc8
DOWN_ARROW = 0xd0


SPACE = 0x57

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

if __name__ == '__main__':
    PressKey(0x11)
    time.sleep(1)
    ReleaseKey(0x11)
    time.sleep(1)