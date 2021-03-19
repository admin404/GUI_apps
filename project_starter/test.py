import pyautogui
import os

class mouse_position():
    def __init__(self):
    	self.get_position()

    def get_position(self):
    	position = pyautogui.position()
    	while 1:
    		if (pyautogui.position() != position):
    			print(pyautogui.position())   
    			self.clear() 			

    def clear(self): 
	    # for windows 
	    if os.name == 'nt': 
	        _ = os.system('cls') 
	  
	    # for mac and linux(here, os.name is 'posix') 
	    else: 
	        _ = os.system('clear')

mouse_position()