import pyautogui
import time
import keyboard
import win32api, win32con

while 1:
	if keyboard.is_pressed("P"):
		break

	if pyautogui.locateOnScreen('C:/Users/attil/Documents/FallGuys-AutoLaunch/FallGuys-AutoLaunch/image/jouer.png', confidence=0.9):
		keyboard.press_and_release('space')
		print ("Lancement d'une partie")
		time.sleep(1)

	#if pyautogui.locateOnScreen('C:/Users/attil/Documents/FallGuys-AutoLaunch/FallGuys-AutoLaunch/image/ok rouge.png', confidence=0.9):
		keyboard.press_and_release('esc')
		time.sleep(1)

	if pyautogui.locateOnScreen('C:/Users/attil/Documents/FallGuys-AutoLaunch/FallGuys-AutoLaunch/image/retour.png', confidence=0.9):
		keyboard.press_and_release('esc')
		time.sleep(1) 

	if pyautogui.locateOnScreen('C:/Users/attil/Documents/FallGuys-AutoLaunch/FallGuys-AutoLaunch/image/ok bleu.png', confidence=0.9):
		keyboard.press_and_release('space')
		print ("C'est fini!")
		time.sleep(1)

	if pyautogui.locateOnScreen('C:/Users/attil/Documents/FallGuys-AutoLaunch/FallGuys-AutoLaunch/image/ok recompense.png', confidence=0.9):
		keyboard.press_and_release('space')
		print ("Récompense récupéré!")
		time.sleep(1)     

	if pyautogui.locateOnScreen('C:/Users/attil/Documents/FallGuys-AutoLaunch/FallGuys-AutoLaunch/image/confirmer.png', confidence=0.9):
		keyboard.press_and_release('space')
		print ("Retour à l'acceuil")
		time.sleep(1)  

	if pyautogui.locateOnScreen('C:/Users/attil/Documents/FallGuys-AutoLaunch/FallGuys-AutoLaunch/image/quitter.png', confidence=0.9):
		keyboard.press_and_release('esc')
		time.sleep(1)  

	if pyautogui.locateOnScreen('C:/Users/attil/Documents/FallGuys-AutoLaunch/FallGuys-AutoLaunch/image/rester quitter.png', confidence=0.9):
		keyboard.press_and_release('esc')
		time.sleep(1)   