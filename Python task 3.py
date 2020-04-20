import random

print("Hi! This is a guessing game, are you ready?")

def guessing_game():
    play = True
    while play:

        easy = random.randint(1,10)
        medium = random.randint(1,20)
        hard = random.randint(1,50)

        print("""
        Would you like to play on easy, medium or hard?
        Type 'e' for easy, 'm' for medium or 'h' for hard!""") 
         
        choose_level = True
        while choose_level:
            level = input()
            if level == "e":
                print("You choose easy level!")
                choose_level = not True
                break
            if level == "m":
                print("You choose medium level!")
                choose_level = not True
                break
            if level == "h":
                print("You choose hard level!")
                choose_level = not True
                break
            else:
                print("Invalid input! Please choose either e, m, or h.")
        
        if level == 'e':
            print("You selected easy, you have 6 guesses. Guess between 1-10.")
            guesses_limit = 6
            while guesses_limit != 0:
                guess = int(input("Enter you number: "))
                if guess == easy:
                    print("You got it right! " + str(easy))
                    break
                elif guess < easy:
                    print("You got it wrong!")
                elif guess > easy:
                    print("You got it wrong!")
                guesses_limit -= 1
                print('You now have ' + str(guesses_limit) + 'guesses left!')

                if guesses_limit == 5: 
                    print('you now have ' + str(guesses_limit) + 'guesses left!')
                if guesses_limit == 4: 
                    print('you now have ' + str(guesses_limit) + 'guesses left!')
                if guesses_limit == 3: 
                    print('you now have ' + str(guesses_limit) + 'guesses left!')
                if guesses_limit == 2: 
                    print('you now have ' + str(guesses_limit) + 'guesses left!')
                if guesses_limit == 1: 
                    print('you now have ' + str(guesses_limit) + 'guesses left!')
                if guesses_limit == 0: 
                    print('Game Over')

        if level == 'm':
            print("You selected medium, you have 4 guesses. Guess between 1-20.")
            guesses_limit = 4
            while guesses_limit != 0:
                guess = int(input("Enter you number: "))
                if guess == medium:
                    print("You got it right! " + str(medium))
                    break
                elif guess < medium:
                    print("You got it wrong!")
                elif guess > medium:
                    print("You got it wrong!")

                guesses_limit -= 1
                print('You now have ' + str(guesses_limit) + 'guesses left!')

                if guesses_limit == 4: 
                    print('you now have ' + str(guesses_limit) + 'guesses left!')
                if guesses_limit == 3: 
                    print('you now have ' + str(guesses_limit) + 'guesses left!')
                if guesses_limit == 2: 
                    print('you now have ' + str(guesses_limit) + 'guesses left!')
                if guesses_limit == 1: 
                    print('you now have ' + str(guesses_limit) + 'guesses left!')
                if guesses_limit == 0: 
                    print('Game Over')

        if level == 'h':
            print("You selected hard, you have 3 guesses. Guess between 1-50.")
            guesses_limit = 3
            while guesses_limit != 0:
                guess = int(input("Enter you number: "))
                if guess == hard:
                    print("You got it right! " + str(hard))
                    break
                elif guess < hard:
                    print("You got it wrong!")
                elif guess > hard:
                    print("You got it wrong!")

                guesses_limit -= 1
                print('You now have ' + str(guesses_limit) + 'guesses left!')

                if guesses_limit == 3: 
                    print('you now have ' + str(guesses_limit) + 'guesses left!')
                if guesses_limit == 2: 
                    print('you now have ' + str(guesses_limit) + 'guesses left!')
                if guesses_limit == 1: 
                    print('you now have ' + str(guesses_limit) + 'guesses left!')
                if guesses_limit == 0: 
                    print('Game Over')
                   
guessing_game()  