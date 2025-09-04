"""
Datos Iniciales: Empieza con la lista de productos.
Función de Cálculo: Crea una función calculate_inventory_value que reciba la lista completa de productos.
Procesar y Devolver: La función debe recorrer la lista. Para cada producto, debe calcular precio * cantidad y añadirlo al diccionario con la clave "valor_total". Al final, debe return la lista completa y modificada.
Mostrar Resultados: Tu código principal debe llamar a la función una sola vez, recibir la lista actualizada y luego recorrerla para mostrar el nombre, precio, cantidad y el nuevo "valor_total" de cada producto.
"""

import msvcrt

inventory_01 = [
    {"product": "Manzanas", "price": 2.5, "cantidad": 100},
    {"product": "Leche", "price": 1.5, "cantidad": 50},
    {"product": "Pan", "price": 1.0, "cantidad": 200},
    {"product": "Huevos", "price": 3.0, "cantidad": 0}, 
    {"product": "Azucar", "price": 4.0, "cantidad": 200},
]

def calculate_inventory_value(list_number , current_inventory):
    return float(current_inventory[list_number]["price"] * current_inventory[list_number]["cantidad"])

print("--- Valor del Inventario ---")
for products in range(len(inventory_01)):
    inventory_01[products]["valor total"] = calculate_inventory_value(products, inventory_01)

    print(f"Producto: {inventory_01[products]["product"]}")
    print(f"Precio: $/{inventory_01[products]["price"]}")
    print(f"Cantidad: {inventory_01[products]["cantidad"]}")
    print(f"Valor Total: $/{inventory_01[products]["valor total"]}")
    print("------------------------------")

print("Presione cualquier tecla para salir.")
msvcrt.getch()

#25:04 minutos