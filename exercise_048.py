# Crea una funcion reciba tanta matricez como sean dadas.
# Que se pueda sumar y restar.
# Se prohibe librerias o funciones que lo hagan directamente.

def add_subtract_matrix(sign,*tuple_matrixs):
    #Comprobacion de signo (Verificar si es negativo o positivo)
    if sign != "+" and sign != "-":
        raise ValueError("Signo no valido")
    
    #Comprobacion de tamaño (Verificar si son iguales las matricez)
    amount_of_rows    = []
    amount_of_columns = []

    for matrixs in tuple_matrixs:
        amount_of_rows.append(len(matrixs))
        for rows in matrixs:
            amount_of_columns.append(len(rows))

    if len(set(amount_of_columns)) != 1:
        raise ValueError("Error. Matricez de diferente tamaño el columnas")
    if len(set(amount_of_rows)) != 1:
        raise ValueError("Error. Matricez de diferente tamaño en filas")

    # Crear matris a retornar
    matrix_to_return = []
    
    # Agregar filas y columnas
    for position,_ in enumerate(range(amount_of_rows[0])):
        matrix_to_return.append([])
        for _ in range(amount_of_columns[0]):
            matrix_to_return[position].append(0)

    for matrix in tuple_matrixs:
        for position_01,row in enumerate(matrix):
            for position_02,number in enumerate(row):
                if sign == "+":
                    matrix_to_return[position_01][position_02] += number
                if sign == "-":
                    matrix_to_return[position_01][position_02] -= number
            
    return matrix_to_return

######################
user_matrix_01 = [[3,5,4],
                [-4,3,5],]

user_matrix_02 = [[3,9,-5],
                [0,-4,-11]]

user_matrix_03 = [[1,-1,4],
                [9,-6,-10]]

print("-------- Matrices --------")
print(user_matrix_01)
print(user_matrix_02)
print(user_matrix_03)
print("--------------------------")
print("--- Suma de 3 matrices ---")
print(add_subtract_matrix("+",user_matrix_01,user_matrix_02,user_matrix_03))
print("--- Resta de 3 matrices ---")
print(add_subtract_matrix("-",user_matrix_01,user_matrix_02,user_matrix_03))
print("--------------------------")

# 93 minutos

#Dios mio mi señor jesucristo me ha abandonado. Me duele todo mi cuerpo y tengos mareos a mas no poder. Esase esta la razón de hacer con tanta lentitud los ejercicios de matricez.