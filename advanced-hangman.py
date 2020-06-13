import random
def hangman():

    word = random.choice(["BeYourself" , "BeHappy" , "motivate" , "conquer" , "Smiling" , "awesome" , "fanatbulous" , "DoNotGiveUp" , "TheBestYou" , "UniqueYou" ])
    validLetters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    turn = 10
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("Congratulations! You guessed the right words! You won!")
            break

        print("Guess the words:" , main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Please enter a valid character")
            guess = input()

        if guess not in word:
            turn = turn - 1
            if turn == 9:
                print("9 turns left")
                print("  ---------  ")
            if turn == 8:
                print("8 turns left")
                print("  ---------  ")
                print("   |         ")
                print("   |         ")
                print("   |         ")
                print("   |         ")
                print("   |         ")
            if turn == 7:
                print("7 turns left")
                print("  --------  ")
                print("   |        ")
                print("   |        ")
                print("   |        ")
                print("   |        ")
                print("   |        ")
                print("  --------- ")
            if turn == 6:
                print("6 turns left")
                print("  --------  ")
                print("   |   |    ")
                print("   |        ")
                print("   |        ")
                print("   |        ")
                print("   |        ")
                print("  --------- ")
            if turn == 5:
                print("5 turns left")
                print("  --------  ")
                print("   |   |    ")
                print("   |   O    ")
                print("   |        ")
                print("   |        ")
                print("   |        ")
                print("  --------- ")
            if turn == 4:
                print("4 turns left")
                print("  --------  ")
                print("   |   |    ")
                print("   |   O    ")
                print("   |   |    ")
                print("   |        ")
                print("   |        ")
                print("  --------- ")
            if turn == 3:
                print("3 turns left")
                print("  --------  ")
                print("   |   |    ")
                print("   |   O    ")
                print("   |   |\   ")
                print("   |        ")
                print("   |        ")
                print("  --------- ")
            if turn == 2:
                print("2 turns left")
                print("  --------  ")
                print("   |   |    ")
                print("   |   O    ")
                print("   |  /|\   ")
                print("   |        ")
                print("   |        ")
                print("  --------- ")
            if turn == 1:
                print("1 turns left")
                print("Last chance left !")
                print("  --------  ")
                print("   |   |    ")
                print("   |   O    ")
                print("   |  /|\   ")
                print("   |  /     ")
                print("   |        ")
                print("  --------- ")
            if turn == 0:
                print("You guessed the wrong word! You lost the game :( Try again :)")
                print("  --------  ")
                print("   |   |    ")
                print("   |   O    ")
                print("   |  /|\   ")
                print("   |  / \   ")
                print("   |        ")
                print("  --------- ")
                break


name = input("Please Enter your name: ")
print("Welcome" , name )
print ("Here we go !")
print("------------------- --------------------------------------------------------------------------------")
print("Try to guess the word in less than 10 attempts ! All the very Best !!")
hangman()
print()