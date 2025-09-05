"""
Refactoriza el codigo del ejercicio dia 12.
"""

import msvcrt

inventory_01 = [
    {"product": "Manzanas", "price": 2.5, "cantidad": 100},
    {"product": "Leche", "price": 1.5, "cantidad": 50},
    {"product": "Pan", "price": 1.0, "cantidad": 200},
    {"product": "Huevos", "price": 3.0, "cantidad": 0}, 
    {"product": "Azucar", "price": 4.0, "cantidad": 200},
]

#### Funcion para calcular el valor total
def calculate_inventory_value(current_inventory):
    for products in range(len(current_inventory)):
        current_inventory[products]["valor total"] = float(current_inventory[products]["price"] * current_inventory[products]["cantidad"])

    return current_inventory

### Se llama a la funcion para acutalizar la lista
updated_inventory = calculate_inventory_value(inventory_01)

###Se imprime los valores en un codigo ordenado
print("--- Valor del Inventario ---")
for products in range(len(updated_inventory)):
    print(f"Producto: {updated_inventory[products]["product"]}")
    print(f"Precio: $/{updated_inventory[products]["price"]}")
    print(f"Cantidad: {updated_inventory[products]["cantidad"]}")
    print(f"Valor Total: $/{updated_inventory[products]["valor total"]}")
    print("------------------------------")

###Parte final para salir del programa
print("Presione cualquier tecla para salir.")
msvcrt.getch()

#15:20 minutos