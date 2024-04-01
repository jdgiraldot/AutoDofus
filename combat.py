import pyautogui
import time

def find_positions():

    screenshot = pyautogui.screenshot()
    pixels = screenshot.load()

    enemy = (0, 0, 255)  # Enemigo
    ally = (255, 0, 0)  # Aliado

    start_x, start_y = (330, 25)
    end_x, end_y = (1590, 915)

    ally_found = False
    enemy_found = False

    for x in range(start_x, end_x):
        for y in range(start_y, end_y):
            if pixels[x, y] == enemy and enemy_found==False:
                enemy_coords = (x, y)
                enemy_found = True
            elif pixels[x, y] == ally and ally_found==False:
                ally_coords = (x, y)
                ally_found = True

            if ally_found and enemy_found:
                break
        if ally_found and enemy_found:
            break

    return enemy_coords, ally_coords

def validate_movement(move_ally_x, move_ally_y, movement):
    move_ally_x += movement[0]
    move_ally_y += movement[1]
    pyautogui.moveTo(move_ally_x, move_ally_y)
    if pyautogui.pixelMatchesColor(int(move_ally_x), int(move_ally_y), (0, 102, 0)): # Sí la posición final es válida
        return True
    elif pyautogui.pixelMatchesColor(int(move_ally_x), int(move_ally_y), (255, 255, 255)): # Si la ubicación es válida
        return True
    elif pyautogui.pixelMatchesColor(int(move_ally_x), int(move_ally_y), (0, 0, 255)): # Si la ubicación es el enemigo
        return True
    else:
        return False


def calculate_displacement(enemy_coords, ally_coords):
    
    # Extraer las coordenadas x e y del enemigo y el aliado
    enemy_x, enemy_y = enemy_coords
    ally_x, ally_y = ally_coords

    # Calcular las distancias en X y Y
    distance_x = enemy_x - ally_x
    distance_y = enemy_y - ally_y

    # Definir los movimientos
    move_up = (-43.50, -21.75)
    move_down = (43.50, 21.75)
    move_left = (-43.50, 21.75)
    move_right = (43.50, -21.75)

    # Inicializar las coordenadas del aliado
    new_ally_x, new_ally_y = ally_x, ally_y

    # Número máximo de movimientos
    max_moves = 6

    # Contador de movimientos
    moves_count = 0

    # Calcular los movimientos necesarios
    while (moves_count < max_moves) and (((abs(distance_x) < 66) and (abs(distance_y) < 35)) == False):
        
        if (distance_x >= 0) and (distance_y >= 0): # Aliado en cuadrante superior izquierdo respecto al enemigo
            if validate_movement(new_ally_x, new_ally_y, move_down):
                new_ally_x += move_down[0]
                new_ally_y += move_down[1]
                distance_x = enemy_x - new_ally_x
                distance_y = enemy_y - new_ally_y
            else:
                new_ally_x += move_right[0]
                new_ally_y += move_right[1]
                distance_x = enemy_x - new_ally_x
                distance_y = enemy_y - new_ally_y
        elif (distance_x <= 0) and (distance_y > 0): # Aliado en cuadrante superior derecho respecto al enemigo
            if validate_movement(new_ally_x, new_ally_y, move_left):
                new_ally_x += move_left[0]
                new_ally_y += move_left[1]
                distance_x = enemy_x - new_ally_x
                distance_y = enemy_y - new_ally_y
            else:
                new_ally_x += move_down[0]
                new_ally_y += move_down[1]
                distance_x = enemy_x - new_ally_x
                distance_y = enemy_y - new_ally_y
        elif (distance_x > 0) and (distance_y <= 0): # Aliado en cuadrante inferior izquierdo respecto al enemigo
            if validate_movement(new_ally_x, new_ally_y, move_right):
                new_ally_x += move_right[0]
                new_ally_y += move_right[1]
                distance_x = enemy_x - new_ally_x
                distance_y = enemy_y - new_ally_y
            else:
                new_ally_x += move_up[0]
                new_ally_y += move_up[1]
                distance_x = enemy_x - new_ally_x
                distance_y = enemy_y - new_ally_y
        elif (distance_x < 0) and (distance_y < 0): # Aliado en cuadrante inferior derecho respecto al enemigo
            if validate_movement(new_ally_x, new_ally_y, move_up):
                new_ally_x += move_up[0]
                new_ally_y += move_up[1]
                distance_x = enemy_x - new_ally_x
                distance_y = enemy_y - new_ally_y
            else:
                new_ally_x += move_left[0]
                new_ally_y += move_left[1]
                distance_x = enemy_x - new_ally_x
                distance_y = enemy_y - new_ally_y

        moves_count += 1

    isCAC = False
    if ((abs(distance_x) < 66) and (abs(distance_y) < 35)):
        isCAC = True

    new_ally_coords = (int(new_ally_x), int(new_ally_y))
    return new_ally_coords, isCAC

def move_and_attack(new_ally_coords, enemy_coords, character, isCAC):

    pyautogui.moveTo(new_ally_coords[0] + 20, new_ally_coords[1])
    pyautogui.click()
    time.sleep(2)

    if character == "Aksheny":
        pyautogui.moveTo(enemy_coords[0] + 20, enemy_coords[1])
        pyautogui.press('3')
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.press('3')
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.press('2')
        pyautogui.click()
        time.sleep(0.5)

    elif character == "Turxton":
        if isCAC:
            pyautogui.moveTo(enemy_coords[0] + 20, enemy_coords[1])
            pyautogui.press('6')
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.press('1')
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.press('3')
            pyautogui.click()
            time.sleep(0.5)
        else:
            pyautogui.press('3')
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.press('9')
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.press('0')
            pyautogui.click()
            time.sleep(0.5)

    else:
        print("Personaje no encontrado")
    
    pyautogui.moveTo(190, 80)
    pyautogui.click()
    pyautogui.press('f1')
    time.sleep(5)

    return