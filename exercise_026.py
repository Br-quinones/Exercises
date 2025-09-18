# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.

def find_the_area_of_a_polygon(figure,*sides):
    #Comprobation for bugs#
    if figure not in ["triangle","square","rectangle"]:
        return "Invalid figure."
    if figure == "triangle" and len(sides) != 3:
        return "For the triangle need 3 arguments"
    if figure == "square" and len(sides) != 1:
        return "For the square need 1 argumets"
    if figure == "rectangle" and len(sides) != 2:
        return "For the rectangle need 2 argumets"

    #find the area#
    if figure == "triangle":
        l1,l2,l3= sides
        s = (l1+l2+l3)/2 # s = semiperimeter
        area = (s*(s-l1)*(s-l2)*(s-l3))** 0.5
    elif figure == "square":
        l = sides[0]
        area = l*l
    elif figure == "rectangle":
        l1,l2 = sides
        area = l1*l2
    
    return area

print(f"El área del triángulo es: {find_the_area_of_a_polygon("triangle",4,3,3)}cm²")
print(f"El área del cuadrado es: {find_the_area_of_a_polygon("square",5)}cm²")
print(f"El área del rectángulo es: {find_the_area_of_a_polygon("rectangle",4,6)}cm²")

#51:42 minutos