#Crea una funcion que sume 2 matrices

def adding_matrices(matrix_01,matrix_02):
    #Comprobation 01
    if len(user_matrix_01) != len(user_matrix_02):
        return "Error. Matrices de diferente tamaño 01"
    
    #Comprobation 02
    for m_01,m_02 in zip(matrix_01,matrix_02):
        if len(m_01) != len(m_02):
            return "Error. Matrices de diferente tamaño 02"
        
    #Sumar matricez
    matrix_to_return = matrix_02

    for number_01,date_01 in enumerate(matrix_01):
        for number_02,date_02 in enumerate(date_01):
            print(number_01,number_02)

    # print(matrix_to_return)}
    #Necesitare algo mas basico 
        
    

user_matrix_01 =   [[1,2],
                    [3,5],
                    [4,7],]

user_matrix_02 =   [[9,8],
                    [4,5],
                    [6,7]]

print(adding_matrices(user_matrix_01,user_matrix_02))