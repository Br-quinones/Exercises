# Crea un funcion que analice texto y obtenga:

# - Encuentre la palabra más larga.
#
# Todo esto utilizando un único bucle.

def analize_text(text):
    word_dict = {}

    longest_word = ""
    for letter in (text + " "):
        if letter != " ":
            longest_word += letter
        else:
            word_dict[longest_word] = len(longest_word)
            longest_word = ""

    return max(word_dict, key=word_dict.get)

user_text = "En un lugar de la mancha de cuyo nombre no quisiera acordar"
print(analize_text(user_text))

# 12 minutos