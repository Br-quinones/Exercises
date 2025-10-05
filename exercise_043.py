# Refactoriza el ejercicio 42 
# Crea una función que reciba un texto y muestre cada palabra en una línea,
# formando un marco rectangular de asteriscos.
# - ¿Qué te parece el reto? Se vería así:
#   **********
#   * ¿Qué   *
#   * te     *
#   * parece *
#   * el     *
#   * reto?  *
#   **********

def asterisk_frame(word):
    word_list = word.split(" ")

    #Primera parte
    word_more_large = ""
    for word in word_list:
        if len(word) > len(word_more_large):
            word_more_large = word 
    
    #Segunda parte
    cover = "**" + "*"*(len(word_more_large)) + "**"

    #Tercer parte
    print(cover)
    for word in word_list:
        print("* " + word + " "*(len(word_more_large) - len(word)) + " *")
    print(cover)

asterisk_frame("En un lugar de la mancha")

#10:14 minuos