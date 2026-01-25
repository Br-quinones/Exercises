#### ---- Ejercicio: Rota una matriz cuadrada en 90 grad0s horarios ---- ####

def rotate_matrix_clockwise(matrix : list[list]) -> list[list[int]]:
    # Verificacion 1
    if len(matrix) == 0:
        raise TypeError("Invalid: Empty matrix")
    
    # Verificacion 2
    if not isinstance(matrix, list):
        raise TypeError("Only matrixs")
    
    # Verificacion 3
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("Only matrixs")
        
        if len(matrix) != len(row):
            raise TypeError("Invalid: Only square matrixs")
    
    # The logic
    matrix_to_return = []

    # Transponer: Convertir filas en columnas
    for row in list(zip(*matrix)):
        matrix_to_return.append(list(reversed(list(row))))

    return matrix_to_return

user_matrix_01 = [
    [1,2],
    [3,4],
]

user_matrix_02 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

for line in rotate_matrix_clockwise(user_matrix_01):
    print(line)

print("------------------")

for line in rotate_matrix_clockwise(user_matrix_02):
    print(line)