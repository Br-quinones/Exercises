#Crea un programa que comprueba si los paréntesis, llaves y corchetes
#de una expresión están equilibrados.
#- Equilibrado significa que estos delimitadores se abren y cieran
#  en orden y de forma correcta.
#- Paréntesis, llaves y corchetes son igual de prioritarios.
#  No hay uno más importante que otro.
#- Expresión balanceada: { [ a * ( c + d ) ] - 5 }
#- Expresión no balanceada: { a * ( c + d ) ] - 5 }

def delimiter_checker(formula):
    delimiter_dictionaries_01 = {"[":"]","{":"}","(":")"}
    delimiter_dictionaries_02 = {"]": "[", "}": "{", ")": "("}
    number_of_delimiters = {"{":0, "}":0, "[":0, "]":0, "(":0, ")":0}

    delimiters_list = []
    for element in formula:
        if element in ["{","}","[","]","(",")"]:
            delimiters_list.append(element)

    #1° comprobation
    for delimiter in delimiters_list:
        number_of_delimiters[delimiter] += 1
    if number_of_delimiters["("] != number_of_delimiters[")"] or number_of_delimiters["["] != number_of_delimiters["]"] or number_of_delimiters["{"] != number_of_delimiters["}"]:
        return "unbalanced formula"
    
    #2° comprobation 
    empty_list = []
    for delimiter in delimiters_list:
        if delimiter in ["{","[","("]:
            empty_list.append(delimiter)
        if delimiter in ["}","]",")"]:
            if delimiter_dictionaries_02[delimiter] == empty_list[-1]:
                empty_list.pop()
            else: 
                return "unbalaced formula"

    return "balanced formula"

good_formula = "{ [ a * ( c + d ) ] - 5 }"
bad_formula = "{ a * ( c + d ) ] - 5 }"
empty_formula = "a * c + d - 5"

print(f"Una formula equilibrada da como resultado: {delimiter_checker(good_formula)}")
print(f"Una formula no equilibrada como resultado: {delimiter_checker(bad_formula)}")
print(f"Una formula vacia da como resultado: {delimiter_checker(empty_formula)}")

#01:38:41 minutos