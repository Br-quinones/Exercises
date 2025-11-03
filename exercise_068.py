#  Crea un generador de números pseudoaleatorios entre 0 y 100.
#  - No puedes usar ninguna función "random" (o semejante) del
#    lenguaje de programación seleccionado.
# 
#  Es más complicado de lo que parece...

from datetime import datetime

def generation_random_number_zero_to_hundred():
    real_time = str(datetime.now())
    last_two_numbers = str(real_time)[-1:-3:-1]

    if int(real_time[-5]) > 5:
        return int(last_two_numbers) + 1
    if int(real_time[-5]) <= 5:
        return int(last_two_numbers) + 0

random_number_between_0_and_100 = generation_random_number_zero_to_hundred()
print(random_number_between_0_and_100)

# 18 minutos