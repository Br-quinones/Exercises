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
    more_large_word = ""
    test_large_word = ""

    for letter in word:
        if letter != " ":
            test_large_word += letter
        else:
            if len(test_large_word) > len(more_large_word):
                more_large_word = test_large_word
                test_large_word = ""
            else:
                test_large_word = ""

    cover = (f"**{"*"*len(more_large_word)}**")

    #######

    the_word_list = []
    word_to_apped = ""

    for letter in word:
        if letter != " ":
            word_to_apped += letter
        else:
            the_word_list.append(word_to_apped)
            word_to_apped = ""
    
    ########

    print(cover)
    for word in the_word_list:
        espaces = len(more_large_word) - len(word)
        print("* " + word  + " "*espaces + " *")
    print(cover)

asterisk_frame("En un lugar de la mancha de cuyo nombre no quisiera recordar no ha mucho tiempo")

#45:25 minutos