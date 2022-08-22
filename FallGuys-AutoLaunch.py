import pyautogui
import os
from pathlib import Path
import time
import keyboard
import win32api, win32con

main_path = Path(__file__).parent

while 1:
	t = time.localtime()
	current_time = time.strftime("%H:%M:%S", t)
	if keyboard.is_pressed("P"):
		break

	if pyautogui.locateOnScreen(f'{main_path}\image\-Go.png', confidence=0.9):
		keyboard.press_and_release('space')
		print (current_time,"Démarrage du jeu!")
		time.sleep(0.5)

	if pyautogui.locateOnScreen(f'{main_path}\image\-Deco.png', confidence=0.9):
		keyboard.press_and_release('space')
		print (current_time,"Reconnexion!")
		time.sleep(0.5)

	if pyautogui.locateOnScreen(f'{main_path}\image\-Jouer.png', confidence=0.9):
		keyboard.press_and_release('space')
		print (current_time,"Lancement d'une partie")
		time.sleep(0.5)

	if pyautogui.locateOnScreen(f'{main_path}\image\-Retour.png', confidence=0.9):
		keyboard.press_and_release('esc')
		time.sleep(0.5) 

	if pyautogui.locateOnScreen(f'{main_path}\image\-Ok bleu.png', confidence=0.9):
		keyboard.press_and_release('space')
		print (current_time,"C'est fini!")
		time.sleep(0.5)

	if pyautogui.locateOnScreen(f'{main_path}\image\-Ok recompense.png', confidence=0.9):
		keyboard.press_and_release('space')
		print (current_time,"Récompense récupéré!")
		time.sleep(0.5)     

	if pyautogui.locateOnScreen(f'{main_path}\image\-Confirmer.png', confidence=0.9):
		keyboard.press_and_release('space')
		print (current_time,"Retour à l'acceuil")
		time.sleep(0.5)  

	if pyautogui.locateOnScreen(f'{main_path}\image\-Quitter.png', confidence=0.9):
		keyboard.press_and_release('esc')
		time.sleep(0.5)  

	if pyautogui.locateOnScreen(f'{main_path}\image\-Rester quitter.png', confidence=0.9):
		keyboard.press_and_release('esc')
		time.sleep(0.5)   

	#if pyautogui.locateOnScreen(f'{main_path}\image\-Ok rouge.png', confidence=0.9):
		keyboard.press_and_release('esc')    
		time.sleep(0.5)