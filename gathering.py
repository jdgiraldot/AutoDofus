import pyautogui
import time
import random

def identify_map(route):
    if route == "Mijo":
        maps = [(0, 0, (0, 0, 0)), (0, 0, (0, 0, 0)), (0, 0, (0, 0, 0)), (0, 0, (0, 0, 0))]
    elif route == "Salvia":
        maps = [(1260, 210, (94, 62, 12)),  # 01
                (800, 205, (240, 203, 63)), # 02
                (1020, 200, (36, 25, 19)),  # 03
                (370, 440, (255, 208, 25))] # 04
    else:
        print("Ruta no reconocida")
        time.sleep(1)
        return -1

    for i in range(len(maps)):
        if pyautogui.pixelMatchesColor(*maps[i]):
            return i
    
    print("Mapa no encontrado")
    time.sleep(1)
    return -1

def identify_resources(route, map):

    if route == "Salvia":
        if map == 0:
            resources = [(1070, 820, (150, 47, 91)),    # Salvia 1
                         (807, 166, (87, 37, 61)),      # Salvia 2
                         (492, 273, (34, 165, 23)),     # Menta
                         (1328, 290, (221, 232, 193))]  # Ortiga
        elif map == 1:
            resources = [(547, 256, (169, 95, 139)),    # Salvia
                         (922, 141, (225, 232, 188)),   # Ortiga
                         (755, 151, (189, 193, 126)),   # Gobio 1
                         (890, 305, (143, 163, 108)),   # Gobio 2
                         (925, 620, (212, 234, 49))]    # Fresno
        elif map == 2:
            resources = [(1463, 190, (172, 95, 142)),   # Salvia 1
                         (590, 755, (120, 40, 89))]     # Salvia 2
        elif map == 3:
            resources = [(1200, 60, (177, 66, 112)),    # Salvia
                         (1372, 521, (228, 234, 183))]  # Ortiga
        else:
            print("Mapa de recursos no encontrado")
    else:
        print("Ruta no reconocida")

    return resources

def gather(resources):

    gathering = False
    rx = random.randint(-2, 2)
    ry = random.randint(-2, 2)
    pyautogui.keyDown('shift')

    for resource in resources:
        if pyautogui.pixelMatchesColor(resource[0], resource[1], resource[2]):
            gathering = True
            pyautogui.moveTo(resource[0] + rx, resource[1] + ry)
            pyautogui.click()
            time.sleep(5)

    pyautogui.keyUp('shift')

    if gathering == False:
        time.sleep(random.randint(2, 3))
    
    return

def next_map(current_map):

    # Cambio de mapa centrado
    # right = (1600 + random.randint(-10, 10), 500 + random.randint(-100, 100))
    # down = (960 + random.randint(-100, 100), 905 + random.randint(-5, 5))
    # left = (320 + random.randint(-10, 10), 500 + random.randint(-100, 100))
    # up = (960 + random.randint(-100, 100), 30 + random.randint(-5, 5))

    # Cambio de mapa optimizado esquinas
    right = (1590 + random.randint(-10, 10), 750 + random.randint(-100, 100))
    down = (450 + random.randint(-80, 80), 905 + random.randint(-5, 5))
    left = (320 + random.randint(-10, 10), 200 + random.randint(-100, 100))
    up = (1450 + random.randint(-80, 80), 30 + random.randint(-5, 5))
    
    pyautogui.keyDown('shift')

    if current_map == 0:
        pyautogui.moveTo(right[0], right[1])
        pyautogui.click()
    elif current_map == 1:
        pyautogui.moveTo(down[0], down[1])
        pyautogui.click()
    elif current_map == 2:
        pyautogui.moveTo(left[0], left[1])
        pyautogui.click()
    elif current_map == 3:
        pyautogui.moveTo(up[0], up[1])
        pyautogui.click()
    else:
        print("Mapa actual no encontrado")
    
    pyautogui.keyUp('shift')

    next_map = False
    while next_map == False:
        if pyautogui.pixelMatchesColor(5, 30, (0, 0, 0)):
            next_map = True
        time.sleep(0.1)
    time.sleep(1)

    return