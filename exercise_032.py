#Repara el ejercicio 31.

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