from datetime import datetime

import pyautogui
import time

def initial_status(status):
    if pyautogui.pixelMatchesColor(1350, 960, (207, 240, 0)): # Identifica sí el botón de combate está activo:
        status = "Combat"
        if pyautogui.pixelMatchesColor(1355, 1007, (173, 173, 173)): # Activa modo criaturas
            pyautogui.hotkey('shift', '%')
            time.sleep(0.5)
        if pyautogui.pixelMatchesColor(47, 355, (88, 88, 88)): # Activar reto aleatorio
            pyautogui.moveTo(47, 355)
            pyautogui.click()
            time.sleep(0.5)
        pyautogui.press('f1')
        print(datetime.now().strftime("[%H:%M:%S]"), status, " (initial status)")
        time.sleep(6)
    else:
        status = "Gathering"
        print(datetime.now().strftime("[%H:%M:%S]"), status, " (initial status)")
        time.sleep(0.5)
    
    return status

def validate_combat_status(status):
    if pyautogui.pixelMatchesColor(1220, 1000, (39, 39, 30)): # Letreto de Victoria , (910, 720, (244, 226, 47)
        status = "Gathering"
        pyautogui.press('esc')
        print(datetime.now().strftime("[%H:%M:%S]"), status)
    else:
        enemyTurn = True
        while enemyTurn:
            if pyautogui.pixelMatchesColor(1350, 960, (207, 240, 0)): # Botón de combate activo:
                enemyTurn = False
            time.sleep(0.1)
    time.sleep(6)
    return status

def validate_gathering_status(status):
    if pyautogui.pixelMatchesColor(1350, 960, (207, 240, 0)): # Identifica sí el botón de combate está activo:
        status = "Combat"
        if pyautogui.pixelMatchesColor(1355, 1007, (173, 173, 173)): # Activa modo criaturas
            pyautogui.hotkey('shift', '%')
            time.sleep(0.5)
        if pyautogui.pixelMatchesColor(47, 355, (88, 88, 88)): # Activar reto aleatorio
            pyautogui.moveTo(47, 355)
            pyautogui.click()
            time.sleep(0.5)
        pyautogui.press('f1')
        print(datetime.now().strftime("[%H:%M:%S]"), status)
        time.sleep(6)
    
    time.sleep(0.5)
    return status

def whatsapp_notification(windows):
    window = windows[1]
    window.activate()
    time.sleep(0.5)
    pyautogui.write("AutoDofus: Aviso de excepcion", interval=0.05)
    pyautogui.press('enter')
    time.sleep(0.5)
    window = windows[0]
    window.activate()
    time.sleep(0.5)
    return