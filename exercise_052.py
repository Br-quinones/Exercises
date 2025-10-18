# En un matriz grafica un personaje que se mueve dentro de ella.

import msvcrt
import sys 
from colorama import Fore

def make_matrix(row,column,number):
    # Make matrix to return
    matrix_to_return = []
    
    # Make row and column in the matrix
    for i,position in enumerate(range(row)):
        matrix_to_return.append([])
        for j in range(column):
            matrix_to_return[position].append(number)

    # Retorn the matrix
    return matrix_to_return

matrix_01 = make_matrix(15,90,".")


coordenada_y = 0
coordenada_x = 0

player_ascci = Fore.CYAN + "@" + Fore.RESET

while True:
    print("\033[2J\033[H]", end="", flush=True)
    
    for line in matrix_01:
        for signo in line:
            sys.stdout.write(signo)
        sys.stdout.write("\n")

    matrix_01[coordenada_y][coordenada_x] = "." 

    key = msvcrt.getch().decode("latin-1")

    if key == "d":
        coordenada_x += 1
    if key == "a":
        coordenada_x -= 1
    if key == "s":
        coordenada_y += 1
    if key == "w":
        coordenada_y -= 1

    matrix_01[coordenada_y][coordenada_x] = player_ascci

# 45 minutos