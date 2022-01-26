# Initialising necessary variables
program_start = True
pig_latin_word = None
VOWELS = "aeiou"

# Put program in loop to end when user enters quit
while program_start:
    user_word = input("Enter a word: ").lower()

    # Restart program
    if user_word == "quit":
        program_start = False
        break
    else:
        program_start = True

    # Actual Logic
    # Finds the position of all the vowels in the entered word therefore the first index which is position[0] is the
    # position of the first vowel in the word
    position = [i for i, ch in enumerate(user_word) if ch in VOWELS]

    # if the index of position is equal to 0, then it means that the first letter of the entered word is a vowel
    # so add "way" to the word
    if position[0] == 0:
        pig_latin_word = user_word + "way"

    # else it means that it starts with a consonant
    else:
        # so I used 'slicing' to isolate from the first letter to the letter before the first vowel
        sub_word = user_word[0:position[0]]
        # then I used 'slicing' again to find the remaining letters after the first vowel
        rem_word = user_word[position[0]: len(user_word)]

        # then I arranged the strings and added "ay" to it
        pig_latin_word = rem_word + sub_word + "ay"

    # I printed the final word
    print(pig_latin_word)


