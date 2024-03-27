import pyautogui
import time

def initial_status(status):
    if pyautogui.pixelMatchesColor(1350, 960, (207, 240, 0)): # Identifica sí el botón de combate está activo:
        status = "Combat"
        pyautogui.press('f1')
        time.sleep(0.5)
        if pyautogui.pixelMatchesColor(260, 420, (191, 231, 0)): # Seleccionar reto
            pyautogui.press('f1')
        print("Initial status: ", status)
    else:
        status = "Gathering"
        print("Initial status: ", status)
    
    time.sleep(0.5)
    return status

def validate_combat_status(status):
    if pyautogui.pixelMatchesColor(910, 720, (244, 226, 47)): # Letreto de Victoria (910, 720, (244, 226, 47)) o (930, 720, (243, 224, 44))
        status = "Gathering"
        pyautogui.press('esc')
        print("New status: ", status)
    elif pyautogui.pixelMatchesColor(910,730, (201, 137, 107)): # Letreto de Derrota 
        status = "Fin"  # Para un futuro desarrollo este estado será: "En Camino"
        pyautogui.press('esc')
        print("New status: ", status)
    # else:
    #     print("Continua en status: ", status)

    time.sleep(0.5)
    return status

def validate_gathering_status(status):
    if pyautogui.pixelMatchesColor(1350, 960, (207, 240, 0)): # Identifica sí el botón de combate está activo:
        status = "Combat"
        pyautogui.press('f1')
        time.sleep(0.1)
        if pyautogui.pixelMatchesColor(260, 420, (191, 231, 0)): # Seleccionar reto
            pyautogui.press('f1')
        print("New status: ", status)
    
    time.sleep(0.5)
    return status
