import pyautogui
import os
from pathlib import Path
import time
import keyboard
import win32api, win32con

main_path = Path(__file__).parent

while 1:
	if keyboard.is_pressed("P"):
		break

	if pyautogui.locateOnScreen(f'{main_path}\image\-Go.png', confidence=0.9):
		keyboard.press_and_release('space')
		print ("Démarrage du jeu!")
		time.sleep(1)

	if pyautogui.locateOnScreen(f'{main_path}\image\-Jouer.png', confidence=0.9):
		keyboard.press_and_release('space')
		print ("Lancement d'une partie")
		time.sleep(1)

	if pyautogui.locateOnScreen(f'{main_path}\image\-Retour.png', confidence=0.9):
		keyboard.press_and_release('esc')
		time.sleep(1) 

	if pyautogui.locateOnScreen(f'{main_path}\image\-Ok bleu.png', confidence=0.9):
		keyboard.press_and_release('space')
		print ("C'est fini!")
		time.sleep(1)

	if pyautogui.locateOnScreen(f'{main_path}\image\-Ok recompense.png', confidence=0.9):
		keyboard.press_and_release('space')
		print ("Récompense récupéré!")
		time.sleep(1)     

	if pyautogui.locateOnScreen(f'{main_path}\image\-Confirmer.png', confidence=0.9):
		keyboard.press_and_release('space')
		print ("Retour à l'acceuil")
		time.sleep(1)  

	if pyautogui.locateOnScreen(f'{main_path}\image\-Quitter.png', confidence=0.9):
		keyboard.press_and_release('esc')
		time.sleep(1)  

	if pyautogui.locateOnScreen(f'{main_path}\image\-Rester quitter.png', confidence=0.9):
		keyboard.press_and_release('esc')
		time.sleep(1)   

	#if pyautogui.locateOnScreen(f'{main_path}\image\-Ok rouge.png', confidence=0.9):
		keyboard.press_and_release('esc')    
		time.sleep(1)
