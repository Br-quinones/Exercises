# Crea un sistema donde se coloca un mapa generado en ASCII
# Que el sistema lo convierta en matrix
# Que se pueda mover en la matrix con un "@"

from colorama import Fore
from sys import stdout
import msvcrt
import copy

player = Fore.CYAN + "@" + Fore.RESET

# Convertirmos de un diseño de mapa a una matriz
def map_to_matrix(map):
    list_row = []
    matrix = []

    for line in map:
        for string in line:
            for letter in string:
                if letter != " ":
                    list_row.append(letter)
            matrix.append(list_row)
            list_row = []
    
    return matrix

# Graficamos una matrix sin comas ni corchetes
def graph_matrix_map(matrix_map):
    for line in matrix_map:
        for string in line:
            stdout.write(string + " ")
        print("")

# Verificamos si un movimiento es valido (Beta)
def check_movement(key,matrix_map):
    matrix_original = copy.deepcopy(matrix_map)
    
    for position_01,line in enumerate(matrix_map):
        for position_02,string in enumerate(line):
            if string == player:
                coordinate_y,coordinate_x = position_01,position_02

    matrix_map[coordinate_y][coordinate_x] = "."
    
    if key == "w":
        coordinate_y -= 1
    elif key == "s":
        coordinate_y += 1
    elif key == "a":
        coordinate_x -= 1
    elif key == "d":
        coordinate_x += 1

    if matrix_map[coordinate_y][coordinate_x] == "#":
        return matrix_original

    matrix_map[coordinate_y][coordinate_x] = player

    return matrix_map
    
# Limpiamos pantalla de forma extremadamente rapida
def clear_screen():
    print('\033[H\033[J', end='', flush=True)

# Obtenesmos una tecla
def get_key():
    key = msvcrt.getch().decode("latin-1")
    return key

# El primer mapa
map_01 = [
    ["# # # # # # # # # # # # # # #"],
    ["# . . . # . . . # . . . . . #"],
    ["# . . . . . . . . . . . . . #"],
    ["# . . . # . . . # . . . . . #"],
    ["# # # # # # # # # # # # # # #"],
]

# Crear mapa
matrix_map_01 = map_to_matrix(map_01)
matrix_map_01[2][2] = player

# El juego
while True:
    clear_screen() 

    graph_matrix_map(matrix_map_01)

    key = get_key()

    if key in ["w","a","s","d"]:
        matrix_map_01 = check_movement(key,matrix_map_01)

# 90 minutos 

#Me encanto realizar esto, esto se marca para mi nuevo gran proyecto