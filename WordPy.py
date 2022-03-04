import random

words = open("availableWords.txt").read().splitlines() 
word = list(random.choice(words)) 

realWords = open("allWords.txt").read().splitlines() 

print("Welcome to WordPy!\nYou have six attempts to guess a 5 letter word.\n'!' means that that letter is in the right place.\n'*' means that that letter is in the word, but not in that place.")

for x in range(6): 
    
    result = list('-----') 

    guessedWord = input() 
    guess = list(guessedWord) 
    wordCopy = list(word) 
    
    while len(guess) != 5 or (guessedWord in realWords) == False: 
        result = list('-----')  
        print("Your guess must be a real 5 letter word! Try again: ") # 
        guessedWord = input()
        guess = list(guessedWord)
    
    if guess == word:
        print("!!!!!")
        if x+1 == 1:
            print("Congratulations! You guessed the word in 1 guess. The word was '" + "".join(word) + "'.")
            break
        else:
            print("Congratulations! You guessed the word in " + str(x+1) + " guesses. The word was '" + "".join(word) + "'.")
            break
    
    for i in range(5): # check user's guess for correctly placed letters
        if guess[i] == wordCopy[i]:
            result[i] = '!'
            wordCopy[i] = ''

    for i in range(5): # check user's guess for incorrectly placed letters
        for x in range(5): 
            if guess[i] == wordCopy[x]:
                wordCopy[x] = ''
                result[i] = '*'

    print("".join(result))

if guess != word:
    print("You did not guess the word in 6 guesses. The word was '" + "".join(word) + "'.")

input("Press ENTER to exit.")
