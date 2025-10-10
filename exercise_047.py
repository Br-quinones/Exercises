#Soluciona el ejercicio 46
#Crea una funcion que sume 2 matrices

def adding_matrices(matrix_01,matrix_02):
    #Comprobation 01
    if len(matrix_01) != len(matrix_02):
        return "Error. Matrices de diferente tamaño"
    
    #Comprobation 02
    for m_01,m_02 in zip(matrix_01,matrix_02):
        if len(m_01) != len(m_02):
            return "Error. Matrices de diferente tamaño"
        
    #Sumar matricez
    matrix_to_return = matrix_02

    for number_01,date_01 in enumerate(matrix_01):
        for number_02 in range(len(date_01)):
            matrix_to_return[number_01][number_02] = matrix_01[number_01][number_02] + matrix_02[number_01][number_02]
        
    return matrix_to_return
    
user_matrix_01 =   [[-1,2,4],
                    [3,5,99],
                    [4,7,87],
                    [-1,3,-3]]

user_matrix_02 =   [[-9,8,3],
                    [4,-5,-3],
                    [6,7,-44],
                    [-3,9,41]]

sum_matrix = adding_matrices(user_matrix_01,user_matrix_02)
print(sum_matrix)

#34:04 minutos