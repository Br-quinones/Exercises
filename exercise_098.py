### generador de matriz identidad ####

def generation_matrix(n):
    matrix_to_return = [[0 for j in range(n)] for i in range(n)]

    for position in range(n):
        matrix_to_return[position][position] = 1

    return matrix_to_return

for line in generation_matrix(5):
    print(line)