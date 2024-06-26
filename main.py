from common import *
from combat import *
from gathering import *

import pyautogui
import time


status = None
route = "Mijo"  # Rutas: Mijo, Salvia.
character = "Aksheny" # Personaje: Turxton, Aksheny
map = 0

windows = pyautogui.getWindowsWithTitle(character) # Obtiene la lista de ventanas según el titulo
# windows += pyautogui.getWindowsWithTitle("WhatsApp")

if windows:
    window = windows[0] # Activa la primera ventana
    window.activate()
    time.sleep(0.5)

    status = initial_status(status)

    while status != "Fin":

        try:
            while status == "Combat":
                enemy_coords, ally_coords = find_positions()                                # Encontra la posición del enemigo y el aliado
                new_ally_coords, isCAC = calculate_displacement(enemy_coords, ally_coords)  # Calcula el desplazamiento para quedar CAC
                move_and_attack(new_ally_coords, enemy_coords, character, isCAC)            # Realiza el desplazamiento y ataque CAC
                status = validate_combat_status(status)                                     # Valida sí el combate finalizó
        except:
            # whatsapp_notification(windows)
            status = initial_status(status)
            continue
        
        try:
            while status == "Gathering":
                map = identify_map(route, map)
                # if map < 0:
                #     status = "Fin"
                #     break
                resources = identify_resources(route,map)
                gather(resources)
                next_map(map)
                status = validate_gathering_status(status)
        except:
            # whatsapp_notification(windows)
            status = initial_status(status)
            continue
            
else:
    print("No se encontró ninguna ventana con el título especificado")