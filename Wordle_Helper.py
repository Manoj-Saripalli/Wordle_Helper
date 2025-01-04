# Imported Libraries
import re

# Importing the dictionary file and creating a list of all the words in the dictionary
file = open("american-english", "r")
words = file.read().split()
file.close()
    
def is_word(word):
    return word.lower() in words

# All Initial Variables
g_list = [None]*5
alphabet_list = list(map(chr, range(ord('a'), ord('z')+1)))
b_list, remaining_green_indeces, gen_index_list, all_words_list = ([] for i in range(4))
final_loop = True

# Take a list of letters that have been confirmed greyed out
while True:
    grey_letter = input("Please enter letters that have been greyed out below. enter \'done\' when you are finished: \n")
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
    alphabet_list.remove(i)
print("Alphabet List after letter removal: \n", str(alphabet_list))

# Loop to keep taking guesses and provide possible words
while final_loop:
    # Initial loop to take Wordle guess and make sure it is valid
    while True:
        guess = input('Please enter your 5 letter Wordle Guess in the following form:\nLetters for fixed characters and symbols or numbers for characters to be filled in\n')
        if len(guess)==5:
            break
        print('Guess must be 5 letters long Try Again')
    # Takes user input to determine the colors of all the letters in the guess
    for index, item in enumerate(guess):
        if item.isalpha():
            g_list[index] = item.lower()

    # Go through green letter list to determine what characters need to be filled in
    for index, item in enumerate(g_list):
        if item == None:
            remaining_green_indeces.append(index)
            gen_index_list.append(0)
            
    # Generate a big list based on green letters
    loop = True
    while loop:
        temp_word = g_list.copy()
        #print(temp_word)
        for i in range(len(remaining_green_indeces)):
            #print(f"remaining_green_indeces:\n{remaining_green_indeces}\ngen_index_list\n{gen_index_list}")
            temp_word[remaining_green_indeces[i]]= alphabet_list[gen_index_list[i]]
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

    print("All remaining words: ")
    for i in all_words_list:
        word = ''.join(i)
        print(word)
    while True:
        final = input("Would you like to continue guessing? (yes or no)\n")
        if final == 'yes':
            final_loop = True
            g_list = [None]*5
            remaining_green_indeces, gen_index_list, all_words_list = ([] for i in range(3))
            break
        elif final == 'no':
            final_loop = False
            break
        else:
            print("Please enter either yes or no")
