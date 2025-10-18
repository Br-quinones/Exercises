# Crea una funcion que multiple una matriz con un vector
	
def multiply_matrix_vector(matrix,vector):
    # Creamos una copia de igual tamaño pero sin valores
    matrix_multiplication =  [[None for j in i]for i in matrix] 

    # Reemplazmos por numeros los numeros multiplicados
    for i,line in enumerate(matrix):
        for j,number in enumerate(line):
            matrix_multiplication[i][j] = number * vector[i]
    
    # Sumanos las listas anidadas para tener el total
    matrix_to_return = [sum(total) for total in matrix_multiplication]
    
    #Retornamos matriz 
    return matrix_to_return

matrix_01 = [
    [3,4,5],
    [5,5,3],
]

vector_01 = [4,2,9]

print(multiply_matrix_vector(matrix_01,vector_01))

# 25 minutos
