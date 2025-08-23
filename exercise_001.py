"""
Has un programa en Python que primero le pregunte a una persona cuánto fue el total de su cuenta en un restaurante. Después, el programa debe preguntar qué porcentaje de propina quiere dejar (por ejemplo: 15, 18, 20).
Con esos dos datos, el programa debe calcular cuánto dinero es la propina y cuál es el nuevo total a pagar (la cuenta original más la propina). Al final, debe mostrar esos dos resultados.
"""

bill = float(input("Cual fue el total de su cuenta: "))
tip = float(input("Cuanta propina desea dejar(15, 18, 20...): ")) 

total_tip = (tip * 1/100) * bill
total_bill = total_tip + bill

print(f"propina es: {total_tip:.2f}")
print(f"total a pagar es: {total_bill:.2f}")

#20 minutos