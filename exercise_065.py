# Create a function that receives text and returns the vowel that is repeated most often.
# - Be careful with some special cases.
# - If there are no vowels, it can return empty.

def the_most_repeated_vowel(text):
    vowel_and_amount = {
        "a" : 0,
        "e" : 0,
        "i" : 0,
        "o" : 0,
        "u" : 0,
    }
    
    for letter in text:
        if letter in list(vowel_and_amount):
            vowel_and_amount[letter] += 1

    most_repeated_vowel_letter = ""
    most_repeated_vowel_number = 0

    for vowel in vowel_and_amount:
        if vowel_and_amount[vowel] > most_repeated_vowel_number:
            most_repeated_vowel_letter = vowel
            most_repeated_vowel_number = vowel_and_amount[vowel]

        elif vowel_and_amount[vowel] == most_repeated_vowel_number and most_repeated_vowel_number != 0:
            most_repeated_vowel_letter = most_repeated_vowel_letter + vowel

    return most_repeated_vowel_letter
        
text_01 = "I would rather kill my people than see them become undead. Anyone who opposes me will be considered a traitor."

print(the_most_repeated_vowel(text_01))

#38 minutes