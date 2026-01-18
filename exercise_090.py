# Crea una función que sea capaz de transformar Ingles al lenguaje básico del universo Star Wars: el "Aurebesh".
# - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".

def convert_to_aurebesh(text: str) -> str:
    english_to_aurebesh = {
    "a"  : "aurek",
    "b"  : "besh ",
    "c"  : "cresh",
    "d"  : "dorn",
    "e"  : "esk",
    "f"  : "forn",
    "g"  : "grek",
    "h"  : "herf",
    "i"  : "isk",
    "j"  : "jenth",
    "k"  : "krill",
    "l"  : "lenth",
    "m"  : "mern",
    "n"  : "nern",
    "o"  : "osk",
    "p"  : "peth",
    "q"  : "qek",
    "r"  : "resh",
    "s"  : "senth",
    "t"  : "trill",
    "u"  : "usk",
    "v"  : "vev",
    "w"  : "wesk",
    "x"  : "xesh",
    "y"  : "yirt",
    "z"  : "zerek",
    "ch" : "cherek",
    "ae" : "enth",
    "eo" : "onith",
    "kh" : "krenth",
    "ng" : "nen",
    "oo" : "orenth",
    "sh" : "shen",
    "th" : "thesh",
    }
    character_list = [letter for letter in text.lower()]
    
    text_to_return = "" ; skip_cycle = False
    for position, character in enumerate(character_list):
        # Verificamos si saltamos de ciclo
        if skip_cycle:
            skip_cycle = False 
            continue

        # Agregamos caracter si no esta en diccionario
        if character not in english_to_aurebesh.keys():
            text_to_return += character
            continue

        # Agregamos caracter si es el ultimo caracter de lista
        if position == len(character_list) - 1:
            text_to_return += english_to_aurebesh[character]
            continue
            
        # Agregamos caracter de 2 letras
        if str(character) + str(character_list[position+1]) in english_to_aurebesh.keys():
            text_to_return += english_to_aurebesh[str(character) + str(character_list[position+1])]
            skip_cycle = True
        else:
            text_to_return += english_to_aurebesh[character]

    return text_to_return

user_text_01 = "Now, I call out to the spirits of this place. I will give anything, or pay any price, if only you will help me save my people."
user_text_02 = "shisa"

print(convert_to_aurebesh(user_text_01))
print(convert_to_aurebesh(user_text_02))
