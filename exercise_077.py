# Crea una función que reciba dos cadenas de texto casi iguales,
# a excepción de uno o varios caracteres.
# La función debe encontrarlos y retornarlos en formato lista/array.
# - Ambas cadenas de texto deben ser iguales en longitud.
# - Las cadenas de texto son iguales elemento a elemento.
# - No se pueden utilizar operaciones propias del lenguaje
#   que lo resuelvan directamente.

def search_for_repeated_strings(string_01,string_02):
    return [str_02 for str_01,str_02 in zip(string_01,string_02) if str_01 != str_02]

user_text_01 = "Me llamo.Brais Moure"
user_text_02 = "Me llamo brais moure"

print(search_for_repeated_strings(user_text_01,user_text_02))

# 21 minutos