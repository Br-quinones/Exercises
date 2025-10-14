# -Crea una función que retorne una matriz del tamaño deseado y 
# -Que sea rellenado con el numero que el usuario coloque en uno de los argumentos.
	# def make_matrix(row,column,number)

def make_matrix(row,column,number):
    # Hunt bugs in the arguments
    if type(row) != int or type(column) != int or type(number) != int:
        raise ValueError("Error. Solo se admiten enteros")
    if row <= 0 or column <= 0:
        raise ValueError("Error. Fila o columa en Zero.")

    # Make matrix to return
    matrix_to_return = []
    
    # Make row and column in the matrix
    for i,position in enumerate(range(row)):
        matrix_to_return.append([])
        for j in range(column):
            matrix_to_return[position].append(number)

    # Retorn the matrix
    return matrix_to_return

matrix_01 = make_matrix(row=20,column=20,number=1)
for fila in matrix_01:
    print(fila)

# 24 minutos