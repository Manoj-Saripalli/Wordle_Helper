# Imported Libraries
import re
# Importing the dictionary file and creating a list of all the words in the dictionary
file = open("american-english", "r")
words = file.read().split()
file.close()
# All Initial Variables
f_list = [None]*5
alphabet_list = list(map(chr, range(ord('a'), ord('z')+1)))
b_list, remaining_fixed_indeces, gen_index_list, all_words_list = ([] for i in range(4))
final_loop = True
# Loop to keep taking guesses and provide possible words
while final_loop:
    # Take a list of letters that have been confirmed greyed out
    while True:
        grey_letter = input("Please enter letters that have been greyed out below (or additional letters if this isn't your first guess). \nEnter \'done\' when you are finished: \n")
        if grey_letter == 'done':
            break
        elif grey_letter.isalpha() and len(grey_letter)==1:
            b_list.append(grey_letter)
        else:
            print("Please make sure you are only entering a single letter character.")
    # Delete confirmed grey letters from alphabet list
    print("Alphabet List before letter removal: \n", str(alphabet_list))
    b_list = list(set(b_list))
    print('b_list: \n', b_list)
    for i in b_list:
        if i in alphabet_list:
            alphabet_list.remove(i)
    print("Alphabet List after letter removal: \n", str(alphabet_list))
    # Initial loop to take Wordle guess and make sure it is valid
    while True:
        guess = input('Please enter your 5 letter Wordle Guess in the following form:\nLetters for fixed characters and symbols or numbers for characters to be filled in\nEx. a**er to provide 5 letter words that start with \"a\" and end with \"er\"\n')
        if len(guess)==5:
            break
        print('Guess must be 5 letters long Try Again')
    # Takes user input to determine which are fixed alphabet characters and which are to be filled in
    for index, item in enumerate(guess):
        if item.isalpha():
            f_list[index] = item.lower()
    # Go through fixed letter list to determine the indexes of the characters that need to be filled in
    for index, item in enumerate(f_list):
        if item == None:
            remaining_fixed_indeces.append(index)
            gen_index_list.append(0)
    # Generate a big list based on fixed letters
    loop = True
    while loop:
        temp_word = f_list.copy()
        for i in range(len(remaining_fixed_indeces)):
            temp_word[remaining_fixed_indeces[i]]= alphabet_list[gen_index_list[i]]
        for i in range(len(gen_index_list)):
            if gen_index_list[i] == (len(alphabet_list)-1):
                loop = False
                gen_index_list[i] = 0
                continue
            else:
                loop = True
                gen_index_list[i]+=1
                break
        if "".join(temp_word) in words:
            all_words_list.append(temp_word)
    # Print all possible words
    print("All remaining words: ")
    for i in all_words_list:
        word = ''.join(i)
        print(word)
    # Ask user if they would like to continue guessing
    while True:
        final = input("Would you like to continue guessing? (yes or no)\n")
        if final == 'yes':
            final_loop = True
            f_list = [None]*5
            remaining_fixed_indeces, gen_index_list, all_words_list = ([] for i in range(3))
            break
        elif final == 'no':
            final_loop = False
            break
        else:
            print("Please enter either yes or no")
