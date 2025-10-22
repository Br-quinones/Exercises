# Crea un generador de mapas procedural en ASCII

import random

def generate_matrix_map():
    """
    1) Generamos una matrix aletroia con un rango para el tamaño.
    """
    # Creamos los rango en que se pueden generar los mapas
    range_y = random.randint(15,30) # Modificar el rango de las i
    range_x = random.randint(15,60) # Modificar el rango de las j

    # Genereramos un mapa de puros puntos
    map_to_return = [[1 for j in range(range_x)] for i in range(range_y)]

    """
    2) Colocamos pared en los bordes.
    """
    # Cambiamos las primeras y ultimas i por "#"
    for i in range(len(map_to_return)):
        map_to_return[i][0] = 2
        map_to_return[i][-1] = 2

    # Cambiamos las primeras y ultimas j por "#"
    for j in range(len(map_to_return[0])):
        map_to_return[0][j] = 2
        map_to_return[-1][j] = 2

    """
    3) Generamos los suelos
    """
    # 4 celulas muerta
    map_to_return[+1][-2] = 3
    map_to_return[-2][+1] = 3
    map_to_return[-2][-2] = 3
    map_to_return[+1][+1] = 3

    # Generamos 1 celula madre
    daughter_cell_y, daughter_cell_x = int(len(map_to_return)/2) , int(len(map_to_return[0])/2)

    # Empezamos a mover la celula madre para crear celulas hijas
    while True:
        random_movement = random.choice(["w","s","a","d"])

        if random_movement == "w":
            daughter_cell_y -= 1
        if random_movement == "s":
            daughter_cell_y += 1
        if random_movement == "a":
            daughter_cell_x -= 1
        if random_movement == "d":
            daughter_cell_x += 1

        if map_to_return[daughter_cell_y][daughter_cell_x] == 3:
            break
        
        if map_to_return[daughter_cell_y][daughter_cell_x] != 2:
            map_to_return[daughter_cell_y][daughter_cell_x] = 0
        else:
            if random_movement == "w":
                daughter_cell_y += 1
            if random_movement == "s":
                daughter_cell_y -= 1
            if random_movement == "a":
                daughter_cell_x += 1
            if random_movement == "d":
                daughter_cell_x -= 1

    """
    4) Convertimos los int() a str()
    """
    for y_coordinate, line in enumerate(map_to_return):
        for x_coordinate, cell in enumerate(line):
            if map_to_return[y_coordinate][x_coordinate] == 0: 
                map_to_return[y_coordinate][x_coordinate] = "."
            else:
                map_to_return[y_coordinate][x_coordinate] = "#"

    return map_to_return


# 150 minutos