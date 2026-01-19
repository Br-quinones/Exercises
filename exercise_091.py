# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta
# formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo
# B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo 

def append_to_group(name: str, sex : str) -> str:
    """
    0) Verificacion incial
    """
    if len(name) == 0 or len(sex) == 0:
        return "None"
    
    """
    1) Creamos variables
    """
    first_letter = name[0].lower()
    sex = sex.lower()

    """
    2) Verificacion de introduccion de argumentos
    """
    if sex not in ["f","m"]:
        return "None"
    
    if first_letter not in [chr(letter) for letter in range(97,123)]:
        return "None"

    """
    3) La seleccion de grupos
    """
    if first_letter in [chr(letter) for letter in range(97,109)]: # Desde 'a' hasta 'm'
        if sex == "f": # Verificamos si es mujer 
            return "A" 
    
    if first_letter in [chr(letter) for letter in range(111,123)]: # Desde 'n' hasta 'z'
        if sex == "m": # Verificamos si es hombre 
            return "A" 
    
    # Si no se cumple nignuno de las anteriores
    return "B"

user_name = input("Insert your name: ")
user_sex  = input("Insert your sex(F/M): ")

print(f"Your group is: {append_to_group(user_name, user_sex)}")