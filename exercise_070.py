
def most_frequent_word_detector(text):
    #### 
    text_without_signes = []
    for letter in text:
        if letter not in ["¡", "!", "¿", "?", ".", ",", ";", ":"]:
            text_without_signes.append(letter)

    #####
    text_without_signes.append(" ")
    text = "".join(text_without_signes)

    ####
    words_in_the_text = [] ; word = ""
    for letter in text:
        if letter == " ":
            words_in_the_text.append(word)
            word = ""
        
        word += letter
    
    ####
    all_words = dict()

    for word in words_in_the_text:
        all_words[word] = 0

    for word in words_in_the_text:
        all_words[word] += 1

    dinero = max(all_words)

    print(dinero)


user_text = "¡No pienses sobre sentimientos reales! ¿Finges no darte cuenta? De la absoluta realidad y tu corazón Así es como disminuye tu refugio Vendiendo tus heridas poco a poco Gritando frágilmente, qué acto vergonzoso ¡Te recomiendo algo! El escape final ¿Serás salvado de la dulce trampa en la que caíste? En este mundo donde la cordura ya no es suficiente ¿Tal vez la mejor solución son la ignorancia y el rendirse? ¿Un ramo de flores adornado con palabras también puede robar corazones?"

print(most_frequent_word_detector(user_text))

# 27 minutos