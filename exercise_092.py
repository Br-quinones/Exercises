# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada
# tipo de pizza aparecen a continuación.
# • Ingredientes vegetarianos: Pimiento y tofu.
# • Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta
# le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además
# de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla la pizza elegida 

pizza_order = input("Quiere una pizza vegetariana (y/n): ")

if pizza_order == "y":
    menu = ["Pimiento", "Tofu"]
else:
    menu = ["Peperoni", "Jamon", "Salmon"]

print("--- Ingrediente ---")
for position, ingredient in enumerate(menu):
    print(f"[{position}]. {ingredient}.")

user_ingredient = int(input("Ingrese el numero del ingrediente a agregar: "))

print(f"--- Pizza elegida ---")
print(f"- Tomate")
print(f"- Mozzarella")
print(f"- {menu[user_ingredient]}")
    

    

    
    
