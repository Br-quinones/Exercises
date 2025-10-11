# Crea una funcion reciba tanta matricez como sean dadas.
# Que se pueda sumar y restar.
# Se prohibe librerias o funciones que lo hagan directamente.

def add_subtract_matrix(*tuple_matrixs):
    #Comprobacion de tamaño (Verificar si son iguales las matricez)
    amount_of_rows    = []
    amount_of_columns = []

    for matrixs in tuple_matrixs:
        amount_of_rows.append(len(matrixs))
        for rows in matrixs:
            amount_of_columns.append(len(rows))

    if len(set(amount_of_columns)) != 1:
        raise "Error. Matricez de diferente tamaño el columnas"
    if len(set(amount_of_rows)) != 1:
        raise "Error. Matricez de diferente tamaño en filas"

    #Crear numero de filas en matris a retornar
    matrix_to_return = []

    for number in range(amount_of_rows[0]):
        matrix_to_return.append([])

    #Restar o Sumar matricez
    for matrix in tuple_matrixs:
        for position_01,row in enumerate(matrix):
            for position_02,number in enumerate(matrix):
                matrix_to_return[position_01] += number

    print(matrix_to_return)

        
######################
user_matrix_01 = [[3,5,4],
                [-4,3,5],]

user_matrix_02 = [[3,9,-5],
                [0,-4,-11]]

user_matrix_03 = [[1,-1,4],
                [9,-6,-10]]

add_subtract_matrix(user_matrix_01,user_matrix_02,user_matrix_03)

#01:07:50

#Se continuara mañana