# Aprederemos a usar clases esta semana.
# Crea una clase que guarde libros 

class Book:
    def __init__(self, name,autor,pages):
        self.name = name
        self.autor = autor
        self.pages = pages

lolita = Book("Lolita","Vladimir Nabokov",400)
comedia = Book("Divina Comedia","Dante alighieri",700)

print(f"El peor libro es: {lolita.name}, escrito por {lolita.autor} y con {lolita.pages} paginas.")
print(f"El mejor libro es: {comedia.name}, escrito por {comedia.autor} y con {comedia.pages} paginas.")

#25 minutos