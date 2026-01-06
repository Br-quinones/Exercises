# Se requiere desarrollar una aplicación de consola en Python que permita a un usuario gestionar sus pendientes diarios. El sistema debe estar basado en Programación Orientada a Objetos (POO) y debe ser robusto ante entradas incorrectas del usuario.

class Task():
    def __init__(self, description: str, is_completed: bool, priority: int):
        self.description  = description
        self.is_completed = is_completed
        self.priority     = priority

    def change_description(self):
        self.description = input("Introduzca su descripción: ")

    def mark_completed(self):
        if self.is_completed == False:
            self.is_completed = True

    def change_priority(self):
        while True:
            try:
                self.priority = int(input("Introduzca su prioridad[1-3]: "))
                if 1 <= self.priority <= 3:
                    break
                else:
                    print("Solo se admiten numeros del 1 al 3")
            except:
                print("Solo se admiten numeros")

    def view_tasks(self):
        bool_to_str = {True  : "X", False : "·"}

        print("--------------------------------")
        print(f"Descripción : [{self.description}]")
        print(f"Completado  : [{bool_to_str[self.is_completed]}]")
        print(f"Prioridad   : [{self.priority}]")
        print("--------------------------------")

class TaskManager:
    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self):
        while True:
            try:
                add_description = str(input("Introduzca una descripcion: "))
                add_priority    = int(input("Introduzca una prioridad(1-3): "))

                if 1 <= add_priority <= 3:
                    break
                else:
                    print("Solo se admiten numeros del 1 al 3")
            except:
                print("Coloque lo datos correctamente")

        task_to_add = Task(description=add_description, is_completed=False, priority=add_priority)
        self.tasks.append(task_to_add)

    def show_all_tasks(self):
        if len(self.tasks) == 0:
            print("No existen tareas a mostrar")
        else:
            for item in self.tasks:
                item.view_tasks()

# 179 minutos

# tuve que salvar mi año escolar y hacer recuperacion de fisica y quimica, por eso no pude subir ejercicios a mi git-hub, pero ya volvi a ser libre para hacer lo que me gusta.