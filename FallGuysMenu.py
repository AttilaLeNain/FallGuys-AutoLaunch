from pyautogui import *
import pyautogui
import time
from utils.getkeys import key_check
import keyboard
import win32api, win32con

while 1:  
	if pyautogui.locateOnScreen('C:/Users/attil/Desktop/Script Python/FallGuys Menu/image/jouer.png', confidence=0.9) !=None:
		keyboard.press_and_release('space')
		print ("Lancement d'une partie")
		time.sleep(1)

	#if pyautogui.locateOnScreen('C:/Users/attil/Desktop/Script Python/FallGuys Menu/image/ok rouge.png', confidence=0.9) !=None:
		keyboard.press_and_release('esc')
		time.sleep(1)

	if pyautogui.locateOnScreen('C:/Users/attil/Desktop/Script Python/FallGuys Menu/image/retour.png', confidence=0.9) !=None:
		keyboard.press_and_release('esc')
		time.sleep(1) 

	if pyautogui.locateOnScreen('C:/Users/attil/Desktop/Script Python/FallGuys Menu/image/ok bleu.png', confidence=0.9) !=None:
		keyboard.press_and_release('space')
		print ("C'est fini!")
		time.sleep(1)

	if pyautogui.locateOnScreen('C:/Users/attil/Desktop/Script Python/FallGuys Menu/image/ok recompense.png', confidence=0.9) !=None:
		keyboard.press_and_release('space')
		print ("Récompense récupéré!")
		time.sleep(1)     

	if pyautogui.locateOnScreen('C:/Users/attil/Desktop/Script Python/FallGuys Menu/image/confirmer.png', confidence=0.9) !=None:
		keyboard.press_and_release('space')
		print ("Retour à l'acceuil")
		time.sleep(1)  

	if pyautogui.locateOnScreen('C:/Users/attil/Desktop/Script Python/FallGuys Menu/image/quitter.png', confidence=0.9) !=None:
		keyboard.press_and_release('esc')
		time.sleep(1)  

	if pyautogui.locateOnScreen('C:/Users/attil/Desktop/Script Python/FallGuys Menu/image/rester quitter.png', confidence=0.9) !=None:
		keyboard.press_and_release('esc')
		time.sleep(1)  

	# Arrêter le script avec la touche H
	keys = key_check()
	if keys == "H":
		break