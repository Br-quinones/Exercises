# Crea una función que multiple a cada celda de la matriz por un numero indicado por el usuario.

def multiplier_number_to_matrix(matrix,multiplier):
    # Comprobacion 01
    if type(matrix) != list or type(multiplier) != int:
        raise ValueError("Tipo de datos incorrecto en los argumentos")
    
    # Creamos la matriz
    matrix_to_return = [[number for number in line] for line in matrix]

    # Multiplicamos valor por valor
    for position_01,row in enumerate(matrix_to_return):
        for position_02,number in enumerate(row):
            matrix_to_return[position_01][position_02] = number * multiplier
    
    # Retornamos la matriz
    return matrix_to_return

matrix_01 = [[5,3],
            [4,3],
            [0,2]]

matrix_02 = [[4,344],
            [99,-42],
            [42,-23]]

matrix_multiplied_01 = multiplier_number_to_matrix(matrix_01,3)
matrix_multiplied_02 = multiplier_number_to_matrix(matrix_02,9)

print(*matrix_multiplied_01 ,sep="\n")
print("----------")
print(*matrix_multiplied_02 ,sep="\n")

#66 minutos