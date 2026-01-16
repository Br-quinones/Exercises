# Dada una URL con parámetros, crea una función que obtenga sus valores.
# No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.

# Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
# los parámetros serían ["2023", "0"]

def get_parameters(url: str) -> list:
    # Checking 1
    if "?" not in url:
        return []

    # Get all after of '?'
    keys_parameter_and = url.split("?")[1]

    # Get list with key : value
    keys_parameter = keys_parameter_and.split("&") 
    
    print(keys_parameter)

    # Get only the parameter    
    list_parameter = []
    for i in keys_parameter:
        if "=" in i:
            list_parameter.append(i.split("=")[1])
        else:
            list_parameter.append("")

    return list_parameter

print(get_parameters("https://retosdeprogramacion.com?year=2023&challenge=0"))
print(get_parameters("https://google.com"))
print(get_parameters("https://retosdeprogramacion.com?year=&challenge="))
print(get_parameters("https://example.com?admin&user=guest"))
print(get_parameters("https://example.com?signature=abc=123"))