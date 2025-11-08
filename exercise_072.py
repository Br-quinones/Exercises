# Crea una funcion con argumento int(n), donde el si retoner si es feliz.

def is_number_happy(number):
    used_number = []
    while True:
        result = list(str(number))

        check = []
        for unit in result:
            check.append(int(unit)**2)

        used_number.append(number)
        number = sum(check)

        if number == 1:
            return True
        if number in used_number:
            return False
        
    
print(is_number_happy(7))

# 45 minutos