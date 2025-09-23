#Repara el ejercicio 31.

    #Crea un programa que comprueba si los paréntesis, llaves y corchetes
    #de una expresión están equilibrados.
    #- Equilibrado significa que estos delimitadores se abren y cieran
    #  en orden y de forma correcta.
    #- Paréntesis, llaves y corchetes son igual de prioritarios.
    #  No hay uno más importante que otro.
    #- Expresión balanceada: { [ a * ( c + d ) ] - 5 }
    #- Expresión no balanceada: { a * ( c + d ) ] - 5 }


def delimiter_checker(formula):
    delimiter_dictionaries = {"]": "[", "}": "{", ")": "("}

    delimiters_list = []
    for element in formula:
        if element in ["(",")","[","]","{","}"]:
            delimiters_list.append(element)

    empty_list = []
    for delimiter in delimiters_list:
        if delimiter in ["[","{","("]:
            empty_list.append(delimiter)
        elif delimiter in ["]","}",")"] and len(empty_list) > 0:
            if delimiter_dictionaries[delimiter] == empty_list[-1]:
                empty_list.pop()
            else: 
                return "Formula invalida"
        else:
            return "Formula invalida"

    if empty_list == []:
        return "Formula valida"
    else:
        return "Formula invalida"

formula_01 = "{ [ a * ( c + d ) ] - 5 }" 
formula_02 = "{ a * ( c + d ) ] - 5 }"   
formula_03 = "a * c + d - 5"

print(f"Una formula equilibrada da como resultado: {delimiter_checker(formula_01)}")
print(f"Una formula no equilibrada como resultado: {delimiter_checker(formula_02)}")
print(f"Una formula vacia da como resultado: {delimiter_checker(formula_03)}")

#13:56 minutos