#  Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
#  - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
#  - EXTRA: ¿Eres capaz de dibujar más figuras?

def graph_figure(figure,size):
    """
    En algunos casos se coloco un espacio extra.
    Esto es por que la division entre linea y linea es grande, pero la division entre asterisco y asterisco es corta.
    Asi que para compesar se añadio un espacio. Unicamente para la simetria
    """

    if figure == "line":
        print("* " * size)

    elif figure == "square":
        for iterator in range(size):
            print("* " * size)
        
    elif figure == "triangle":
        for iterator in range(size):
            print((size-iterator) * " " + "*" + " *"*iterator)

    elif figure == "rectangle":
        for iterator in range(int(size/2)):
            print("* " * size)

    else: 
        print(f"Error, la figura {figure}, no se reconoce.")

print(" --- Graficar una linea --- ")
graph_figure("line",10)

print(" --- Graficar un Cuadrado --- ")
graph_figure("square",10)

print(" --- Graficar un Triangulo --- ")
graph_figure("triangle",10)

print(" --- Graficar un Rectangulo ---")
graph_figure("rectangle",10)

#20:30 minutes