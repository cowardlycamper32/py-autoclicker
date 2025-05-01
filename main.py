import keyboard as kb
import mouse as ms
from time import sleep as wait
from os import system
from sys import platform
from sys import exit as ext
import windows_toasts as wts

version = "1.0.0"

if platform == "win32" or platform == "win64":
    clearCMD = "cls"
    toasts = True
    toaster = wts.WindowsToaster("AutoClicker V" + version)
    toast = wts.Toast()
    toast.text_fields = ["Hello World!"]
    icon = wts.ToastDisplayImage.fromPath("icon.ico")
    showFor = wts.ToastDuration.Short
    toast.images = [icon]
    toast.duration = showFor
else:
    clearCMD = "clear"

exit = False
button='right'
buttonType = True # MOUSE BUTTONS False for KEYBOARD BUTTONS
delay=0.01
toggle = kb.add_hotkey('alt+shift+f6', lambda: clickerToggle())
dblToggle = kb.add_hotkey('ctrl+shift+f6', lambda: dblToggle())
dbl = False # single
dblStat = "single"
typeToggle = kb.add_hotkey('ctrl+alt+z', lambda: typeTog())
if toasts:
    toast.text_fields = ['Opening Autoclicker V' + version, '\'ctrl+F1\' - EXIT\n\'alt+shift+f6\' - toggle activation\n\'ctrl+alt+z\' - toggle keyboard or mouse\n\'ctrl+shift+f6\' - toggle double click']
    toaster.show_toast(toast)

def dblToggle():
    global dbl
    dbl = not dbl
    if dbl:
        dblStat = "double"
    else:
        dblStat = "single"
    if toasts:
        toast.text_fields = ['toggled click mode', 'key: ' + str(button) + '\n mode: ' + dblStat]
        toaster.show_toast(toast)

def typeTog():
    global buttonType
    global button
    if buttonType == True: # MOUSE
        button = 'shift'
        if toasts:
            toast.text_fields = ['changed to keyboard mode', 'key: ' + str(button) + '\n mode: ' + dblStat]
            toaster.show_toast(toast)
        buttonType = False # set to keyboard
    else:
        button = 'right'
        if toasts:
            toast.text_fields = ['changed to mouse mode', 'button: ' + str(button) + '\n mode: ' + dblStat]
            toaster.show_toast(toast)

        buttonType = True  # set to mouse

kb.add_hotkey('ctrl+f1', lambda: Exit())
ClickerStatus = False
msgOnOff = "off"
def Exit():
    system(clearCMD)
    print('emergency exit')
    if toasts:
        toast.text_fields = ['EXITING!']
        toaster.show_toast(toast)
    global exit
    exit = True

def clickerToggle():
    global ClickerStatus
    global msgOnOff
    if ClickerStatus:
        msgOnOff = "off"
        if toasts:
            toast.text_fields = ['clicker ' + msgOnOff + '!', 'key: ' + str(button) + '\n mode: ' + dblStat]
            toaster.show_toast(toast)
        ClickerStatus = False
    else:
        msgOnOff = "on"
        if toasts:
            toast.text_fields = ['clicker ' + msgOnOff + '!', 'key: ' + str(button) + '\n mode: ' + dblStat]
            toaster.show_toast(toast)
        ClickerStatus = True
    return ClickerStatus

def clicker():
    if buttonType == True:
        if dbl:
            ms.double_click(button)
        else:
            ms.click(button=button)
        wait(delay)
    else:
        if dbl:
            kb.press(button)
            wait(delay/4)
            kb.release(button)
            wait(delay/4)
            kb.press(button)
            wait(delay/4)
            kb.release(button)
            wait(delay/4)
        else:
            kb.press(button)
            wait(delay/2)
            kb.release(button)




while not exit:


    print(msgOnOff + " | " + str(button))
    if kb.is_pressed('alt+left'):
        if toasts:
            toast.text_fields = ['key changed', 'new key: ' + str(button) + '\n mode: ' + dblStat]
            toaster.show_toast(toast)
        button = 'left'
    elif kb.is_pressed('alt+right'):
        if toasts:
            toast.text_fields = ['key changed', 'new key: ' + str(button) + '\n mode: ' + dblStat]
            toaster.show_toast(toast)
        button = 'right'
    if ClickerStatus == True:
        clicker()
    if not exit:
        system(clearCMD)
