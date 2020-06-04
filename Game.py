word = list("apple")
hidden = []
for character in word:
    hidden.append("_")

attempts = 0
max_attempts = 4 

isGameOver = False
while not isGameOver:

    print(f'You have {max_attempts - attempts} attempts remaining')
        
    #hiddenString = " ".join(hidden)
    print(f"the current word is: {' '.join(hidden)}")

    print("     -------------")
    print("         |    |")
    print("         |    " + ("0" if attempts > 0 else ""))
    print("         |    " + ("/\\" if attempts > 1 else ""))
    print("         |    " + ("|" if attempts > 2 else ""))
    print("         |    " + ("/\\" if attempts > 3 else ""))
    print("    -----------")


    letterGuessed = input("Guess a letter: ")

    print('\n\n\n')

    if letterGuessed in word:

        print("You guessed the letter correctly!")
        for i in range(len(word)):
            character = word[i]
            if character == letterGuessed:
                hidden[i] = word[i]
                word[i] = "_"
    else:
        
        print("You guessed the wrong letter!")
        attempts += 1

    if all("_" == char for char in word):
        print('congrats !! You won the game :)')
        isGameOver = True
                

    if attempts >= max_attempts:
        print('You Lost the game :( Try again :)')
        isGameOver = True
                
