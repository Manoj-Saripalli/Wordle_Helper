# Wordle_Helper
Personal project to help me review the fundamentals of git commands and python scripting while also helping me solve the daily wordle with much less stress and tedious work. 
Original plan was to have the user provide their latest guess with the color category of each word (green, yellow, or grey) and have the program spit out all possible words that match. Unfortunately my initial implementation was not effecient enough to be practical, as when there were guesses that didn't have too many green words the possible permutations were too great and it would take far to long for my program to process everything and provide possible words. It's been since shifted to take multiple guesses from the user where the user just provides fixed characters (assuming the user selects these characters based on the green/yellow words from their guess) and the program then spits out all the possible words from there. An example workflow can be seen below:

User Guesses "CRANE"
No words are green, "C", "A", and "N" are yellow, "R" and "E" are grey
User starts program, enter "r" and "e" as grey characters, and then for the guess enters the yellow letters in an order where they are in different spots in the word.
User guesses "nac**" as an example and the output provides one possible answer, "nacho"
User enters "nacho" into Wordle and finds the "A" is green and the "N" and "C" are still yellow.
User adds in the new grey letters and gusses again, this time with "*anc*" to keep a where it is and change the position of the yellow characters
Only word provided by the output is "fancy"
Congrats, fancy was the wordle for the day!

Upcoming changes:
Fix bug where guessing a full 5 letter word puts program into an infinite loop instead of letting it progress naturally
Have all single letter inputs be translated to lowercase before being added to internal lists
Eventually get the program to take a single guess and provide all the possible words in a time and resource efficient manner
