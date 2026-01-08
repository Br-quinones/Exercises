# Exercise of the A.I for I learn polymorphism

class Library():
    def __init__(self):
        self.items : list[Book | Magazine] = []

    def add_item(self, item):
        self.items.append(item)

    def show_catalog(self):
        if len(self.items) == 0:
            print("The library is empaty")
        else:
            for item in self.items:
                print(item.get_description())

class Media():
    def __init__(self, title, autor):
        self.title = title
        self.autor = autor

    def get_description(self):
        return f"{self.title} by {self.autor}"

class Book(Media):
    def __init__(self, title, autor, page_count):
        super().__init__(title, autor)
        self.page_count = page_count

    def get_description(self):
        basic_information = super().get_description()
        return f"{basic_information} with {self.page_count} pages."

class Magazine(Media):
    def __init__(self, title, autor, issue_number):
        super().__init__(title, autor)
        self.issue_number = issue_number

    def get_description(self):
        basic_information = super().get_description()
        return f"{basic_information} with {self.issue_number} issure"

#### Test of A.I ###
if __name__ == "__main__":
    my_library = Library()
    
    # Creating objects
    book_01 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
    mag_01  = Magazine("National Geographic", "Various", 142)
    
    # Adding to library
    my_library.add_item(book_01)
    my_library.add_item(mag_01)
    
    # Showing results
    my_library.show_catalog()

# 61 minutes