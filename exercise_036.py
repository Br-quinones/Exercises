#  Crea una función que reciba días, horas, minutos y segundos (como enteros)
#  y retorne su resultado en milisegundos.

def convert_time_in_miliseconds(days=0,hours=0,minutes=0,seconds=0):
    miliseconds_to_return = 0
    
    miliseconds_to_return += int(days) * 86400000
    miliseconds_to_return += int(hours) * 3600000
    miliseconds_to_return += int(minutes) * 60000
    miliseconds_to_return += int(seconds) * 1000

    return miliseconds_to_return

print(f"En 01:12:40:30 a milisegundos es: {convert_time_in_miliseconds(days=1,hours=12,minutes=40,seconds=30)} milisegundos.")

#44:02 minutos