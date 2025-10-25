# Define la clase Book.
# Define la clase Library.
# Crea dos o tres instancias de Book (ej. book1, book2).
# Crea una instancia de Library (ej. my_library).
# Usa el método add_book para añadir tus libros a la biblioteca (ej. my_library.add_book(book1)).
# Llama al método list_books para ver si se imprimen los detalles de los libros que añadiste.
# (Si hiciste el reto) Imprime la longitud de tu biblioteca: print(len(my_library)).

class Book:
    def __init__(self, name, autor, pages):
        self.name = name
        self.autor = autor
        self.pages = pages

class Library():
    def __init__(self, name):
        self.name = name
        self.books = []

    def __len__(self):
        return len(self.books)
    
    def add_book(self, book):
        if isinstance(book,Book):
            self.books.append(book)

    def list_books(self):
        for book in self.books:
            print("--------------------")
            print(f"Nombre  : {book.name}")
            print(f"Autor   : {book.autor}")
            print(f"Paginas : {book.pages}")

# Creamos libros
lolita  = Book("Lolita","Vladimir Nabokov",400)
comedia = Book("Divina Comedia","Dante alighieri",700)
quijote = Book("Don Quijote de la Mancha", "Miguel de Cervantes", 1345)

# Creamos una libreria 
library_of_alexandria = Library("Library of Alexandria")

# Añadimos los libros a la libreria
library_of_alexandria.add_book(lolita)
library_of_alexandria.add_book(comedia)
library_of_alexandria.add_book(quijote)

# Mostramos la cantidad de libros 
print(f"-- La libreria tiene: {len(library_of_alexandria)} libro/s --")

# Mostramos todos los libros de la libreria
library_of_alexandria.list_books()

# 34 minutos