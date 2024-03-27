from common import *
from combat import *
from gathering import *

import pyautogui
import time

windows = pyautogui.getWindowsWithTitle("Turxton - Dofus 2.71.0.1") # Obtiene la lista de ventanas según el titulo
status = None
route = "Salvia"  # Rutas: Mijo, Salvia.

if windows:
    window = windows[0] # Activa la primera ventana
    window.activate()
    time.sleep(1)

    status = initial_status(status)

    while status != "Fin":

        while status == "Combat":
            window.activate()
            enemy_coords, ally_coords = find_positions()                                # Encontra la posición del enemigo y el aliado
            new_ally_coords, isCAC = calculate_displacement(enemy_coords, ally_coords)  # Calcula el desplazamiento para quedar CAC
            move_and_attack(new_ally_coords, enemy_coords, isCAC)                       # Realiza el desplazamiento y ataque CAC
            status = validate_combat_status(status)                                     # Valida sí el combate finalizó
            
        while status == "Gathering":
            window.activate()
            map = identify_map(route)
            if map < 0:
                status = "Fin"
                break
            resources = identify_resources(route,map)
            gather(resources)
            next_map(map)
            status = validate_gathering_status(status)

else:
    print("No se encontró ninguna ventana con el título especificado")