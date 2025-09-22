#   Crea una función que reciba dos cadenas como parámetro (str1, str2)
#   e imprima otras dos cadenas como salida (out1, out2).
#   - out1 contendrá todos los caracteres presentes en la str1 pero NO
#     estén presentes en str2.
#   - out2 contendrá todos los caracteres presentes en la str2 pero NO
#     estén presentes en str1.

def letter_comparison(str1,str2):
    #1° comparation
    letters_only_in_str1 = ""
    for letter_01 in str1:
        if letter_01 not in str2:
            letters_only_in_str1 += letter_01
    print(letters_only_in_str1)

    #2 comparation 
    letters_only_in_str2 = ""
    for letter_02 in str2:
        if letter_02 not in str1:
            letters_only_in_str2 += letter_02
    print(letters_only_in_str2)

word_01 = "abcde"
word_02 = "abcxy"

letter_comparison(word_01,word_02)

#11:42 minutos 