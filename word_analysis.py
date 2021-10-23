def word_analysis(word):
    number_of_vowels = 0
    number_of_cons = 0
    number_of_numbers = 0
    number_of_spaces = 0
    number_of_other = 0
    the_vowels = ["a", "e", "i", "o", "u"]
    the_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    the_cons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    for letter in word.lower():
        if letter in the_vowels:
            number_of_vowels += 1
        elif letter in the_numbers:
            number_of_numbers += 1
        elif letter in the_cons:
            number_of_cons += 1
        elif letter == " ":
            number_of_spaces += 1
        else:
            number_of_other += 1

    return f"\n" + "\n" + "Number of Vowels:...... " + str(number_of_vowels) + "\n" + "Number of Consonants:.. " + str(
        number_of_cons) + "\n" + "Number of Spaces:...... " + str(
        number_of_spaces) + "\n" + "Number of Digits:...... " + str(
        number_of_numbers) + "\n" + "Number of Other Chars:. " + str(number_of_other) + "\n"


a = str(input("\n" + "\n" + "Enter a word: "))
print(word_analysis(a))
