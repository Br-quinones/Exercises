#Crea una funcion que reste tantas matrices como sean dadas.
	
def matrix_subtraction(*tuple_matrixs):
    # Comprobation 01 (verificar si son matricez)
    for matrix in tuple_matrixs:
        if type(matrix) != list:
            raise ValueError("Solo se aceptan matrices")
    
    # Comprobation 02 (Comprobar tamaño de las matricez)
    number_of_row    = [] 
    number_of_column = []
    
    for matrix in tuple_matrixs:
        number_of_row.append(len(matrix))
        for row in matrix:
            number_of_column.append(len(row))

    if len(set(number_of_row)) != 1 or len(set(number_of_column)) != 1:
        raise ValueError("Numero de filas o columnas desiguales")
        
    # Creamos una copia de la primera matriz para restar
    matrix_to_return = [[column for column in row] for row in tuple_matrixs[0]]

    # Restamos las demas matricez a la primera
    for matrix in tuple_matrixs[1:]:
        for position_01,cell in enumerate(matrix):
            for position_02,number in enumerate(cell):
                matrix_to_return[position_01][position_02] -= number

    # Devolvemos el resultado
    return matrix_to_return

matrix_01 = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
matrix_02 = [
    [13, 54, 29],
    [13, 17, 21],
    [25, 29, 33]
]
matrix_03 = [
    [10, -5, -44],
    [-2, 48, -44],
    [-6, 14, -94]
]

subtracted_matrix = matrix_subtraction(matrix_01,matrix_02,matrix_03)
print(*subtracted_matrix, sep="\n")

#68 minutos