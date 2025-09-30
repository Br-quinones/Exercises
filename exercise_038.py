#  Crea un programa que determine si dos vectores son ortogonales.
#  - Los dos array deben tener la misma longitud.
#  - Cada vector se podría representar como un array. Ejemplo: [1, -2]

def are_orthogonal(vector_01,vector_02):
    vw_01 = vector_01[0] * vector_02[0]
    vw_02 = vector_01[1] * vector_02[1]
    
    product = vw_01 + vw_02

    return product == 0

true_vector_01 = [1,-2]
true_vector_02 = [4,2]

false_vector_01 = [4,3]
false_vector_02 = [5,-4]

print(f"los vectores {true_vector_01} y {true_vector_02} dan a la prueba de ortogonal como: {are_orthogonal(true_vector_01,true_vector_02)}")
print(f"los vectores {false_vector_01} y {false_vector_02} dan a la prueba de ortogonal como: {are_orthogonal(false_vector_01,false_vector_02)}")

#22:04 minutes