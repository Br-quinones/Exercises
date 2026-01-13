# Crea un programa que analice texto y obtenga:
# - Número total de palabras.
# - Longitud media de las palabras.
# - Número de oraciones del texto (cada vez que aparecen un punto).
# - Encuentre la palabra más larga.
#
# Todo esto utilizando un único bucle.

def text_analize(text):
    # number_of_words
    actual_word = ""
    list_words = []

    # average_word_length
    sum_all_the_length = 0

    # number_of_orations
    number_of_orations = 0

    # word_most_large
    word_most_large = ""

    for letter in text+" ":
        if letter in [",",":",";"]:
            pass
        elif letter == ".":
            number_of_orations += 1
        elif letter != " " and letter :
            actual_word = actual_word + letter
            sum_all_the_length += 1
        else:
            if len(word_most_large) < len(actual_word):
                word_most_large = actual_word
            list_words.append(actual_word)
            actual_word = ""

    if len(text) == 0:
        numbero_of_words = 0
    else:
        numbero_of_words = len(list_words)
    
    return {"number_of_words"      : numbero_of_words,
            "average_word_length"  : sum_all_the_length/len(list_words),
            "number_of_orations"   : number_of_orations,
            "list_word_most_large" : word_most_large}

user_text = "Now, I call out to the spirits of this place. I will give anything, or pay any price, if only you will help me save my people."
print(text_analize(""))

