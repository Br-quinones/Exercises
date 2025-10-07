#  Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
#  y retorne lo siguiente:
#  - "X" si han ganado las "X"
#  - "O" si han ganado los "O"
#  - "Empate" si ha habido un empate
#  Nota: La matriz puede no estar totalmente cubierta.
#  Se podría representar con un vacío "", por ejemplo.

def analizar_matriz(matrix):
    #Encontar en fila
    for position,_ in enumerate(matrix):
        if len(set(matrix[position])) == 1:
            return matrix_01[position][0] 
    
    #Encontar en columna
    for position,_ in enumerate(matrix):
        if matrix[0][position] == matrix[1][position] == matrix[2][position]:
            return matrix[1][position]
        
    #Encontar en Cruz
    if matrix[0][0] == matrix[1][1] == matrix[2][2]:
        return matrix[1][1] 
    if matrix[2][0] == matrix[1][1] == matrix[0][2]:
        return matrix [1][1]
    
    #Si no se cumple todas las victorias entonces
    return "Empate"

matrix_01 =[["X","O","O"],
            ["O","X","O"],
            ["X","O","X"]]

print(analizar_matriz(matrix_01))

#01:18:41
