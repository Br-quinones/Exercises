# Crea una funcion que multiple dos matrises.
			
    # # Primera fila 
    # valor_01 = matrix_multiplying[0][0] * matrix_multiplier[0][0]
    # valor_02 = matrix_multiplying[0][1] * matrix_multiplier[1][0]
    # valor_03 = matrix_multiplying[0][2] * matrix_multiplier[2][0]
    # valor_04 = matrix_multiplying[0][3] * matrix_multiplier[3][0]

    # matrix_product[0][0] = sum([valor_01,valor_02,valor_03,valor_04])
    
    # valor_01 = matrix_multiplying[0][0] * matrix_multiplier[0][1]
    # valor_02 = matrix_multiplying[0][1] * matrix_multiplier[1][1]
    # valor_03 = matrix_multiplying[0][2] * matrix_multiplier[2][1]
    # valor_04 = matrix_multiplying[0][3] * matrix_multiplier[3][1]

    # matrix_product[0][1] = sum([valor_01,valor_02,valor_03,valor_04])

    # valor_01 = matrix_multiplying[0][0] * matrix_multiplier[0][2]
    # valor_02 = matrix_multiplying[0][1] * matrix_multiplier[1][2]
    # valor_03 = matrix_multiplying[0][2] * matrix_multiplier[2][2]
    # valor_04 = matrix_multiplying[0][3] * matrix_multiplier[3][2]

    # matrix_product[0][2] = sum([valor_01,valor_02,valor_03,valor_04])

    # # Segunda fila
    # valor_01 = matrix_multiplying[1][0] * matrix_multiplier[0][0]
    # valor_02 = matrix_multiplying[1][1] * matrix_multiplier[1][0]
    # valor_03 = matrix_multiplying[1][2] * matrix_multiplier[2][0]
    # valor_04 = matrix_multiplying[1][3] * matrix_multiplier[3][0]

    # matrix_product[1][0] = sum([valor_01,valor_02,valor_03,valor_04])
    
    # valor_01 = matrix_multiplying[1][0] * matrix_multiplier[0][1]
    # valor_02 = matrix_multiplying[1][1] * matrix_multiplier[1][1]
    # valor_03 = matrix_multiplying[1][2] * matrix_multiplier[2][1]
    # valor_04 = matrix_multiplying[1][3] * matrix_multiplier[3][1]

    # matrix_product[1][1] = sum([valor_01,valor_02,valor_03,valor_04])

    # valor_01 = matrix_multiplying[1][0] * matrix_multiplier[0][2]
    # valor_02 = matrix_multiplying[1][1] * matrix_multiplier[1][2]
    # valor_03 = matrix_multiplying[1][2] * matrix_multiplier[2][2]
    # valor_04 = matrix_multiplying[1][3] * matrix_multiplier[3][2]

    # matrix_product[1][2] = sum([valor_01,valor_02,valor_03,valor_04])

def multiply_matrix(matrix_multiplying,matrix_multiplier):
    matrix_to_return = [[None for j in matrix_multiplier[0]] for i in matrix_multiplying]

    list_to_sum = []
    for position_01 in range(len(matrix_multiplying)):
        for position_02 in range(len(matrix_multiplier[0])):
            for position_03 in range(len(matrix_multiplier)):
                list_to_sum.append(matrix_multiplying[position_01][position_03] * matrix_multiplier[position_03][position_02])
            matrix_to_return[position_01][position_02] = sum(list_to_sum)
            list_to_sum = []

    return matrix_to_return
    
matrix_01 = [
    [5,3,-4,-2],
    [8,-1,0,-3],
]
matrix_02 = [
    [1,4,0],
    [-5,3,7],
    [0,-9,5],
    [5,1,4],
]

print(multiply_matrix(matrix_01,matrix_02))

#142 minutos