import random

def make_matrix_random(n: int) -> list[list[int]]:
    matrix = [[random.randint(1,101) for j in range(n)] for i in range(n)]

    return matrix

user_matrix = make_matrix_random(5)

# Maldito Vsc 3 dias sin funcionar