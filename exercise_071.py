# Crea una funcion que retorne la palabra mas frecuente en un texto

def most_frequent_word_detector(text):
    # Quitamos mayusculas y simbolos
    text_without_simbols = ""
    for letter in text:
        if letter not in ["¡", "!", "¿", "?", ".", ",", ":", ";"]:
            text_without_simbols += str(letter).lower()
            

    # Quitamos las tildes
    plain_text = ""
    for letter in text_without_simbols:
        if letter == "á":
            plain_text += "a"
        elif letter == "é":
            plain_text += "a"
        elif letter == "é":
            plain_text += "i"
        elif letter == "ó":
            plain_text += "o"
        elif letter == "ú":
            plain_text += "u"
        else:
            plain_text += letter

    # Creamos una lista de las palabras
    list_words = [] ; word = ""
    for letter in plain_text:
        word += letter

        if letter == " ":
            list_words.append(word)
            word = ""

    # Lo colocamos en un diccionario 
    dict_words = dict()

    for word in list_words:
        dict_words[word] = 0

    for word in list_words:
        dict_words[word] += 1

    return max(dict_words, key=dict_words.get)


user_text = "¡No pienses sobre sentimientos reales! ¿Finges no darte cuenta? De la absoluta realidad y tu corazón Así es como disminuye tu refugio Vendiendo tus heridas poco a poco Gritando frágilmente, qué acto vergonzoso ¡Te recomiendo algo! El escape final ¿Serás salvado de la dulce trampa en la que caíste? En este mundo donde la cordura ya no es suficiente ¿Tal vez la mejor solución son la ignorancia y el rendirse? ¿Un ramo de flores adornado con palabras también puede robar corazones?"
print(most_frequent_word_detector(user_text))


