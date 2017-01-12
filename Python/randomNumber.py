#The user can guess an inifinite number of times in this program
number = 6 #sets the variable number
while True:
    print("Guess my number")
    userGuess = input()
    guess = int(userGuess) #converts user string to int

    if guess > number:
        print("Your guess is too high")
    if guess < number:
        print("Your guess is too low!")
    if guess == number:
        print("You got it right!")
        break
