def play_funct(play):
    counter = 0

    while play == "yes":

        q1 = input("How much is 5+5? ")
        #.lower() turns the input into a lower case
        q2 = input("Who won the NBA finals last year? ").lower()
        q3 = input("Will you succeed? ").lower()
        counter += 1

        #q1 will be by default a string but the "int()" turns into an int.
        if int(q1) == 10 and (q2 == "golden state" or q2 == "warriors") and q3 == "yes":
            print("Congrats you have answered all questions correctly! ")
            play = input("Would you like to play again? ")

        else:
            print("You got question(s) wrong :( ")
            play = input("Would you like to play again? ")

    else:
        if play == "no" and counter == 0:
            print("You suck!")
        elif play == "no" and counter != 0:
            print("Aw see you some other time then :(")

        elif play == "yes":
            play_funct(play)

        else:
            play = input("Please enter either \"yes\" or \"no\". ")
            play_funct(play)


print("Welcome to my computer quiz!")
play = input("Would you like to play my quiz game? ").lower()
play_funct(play)
