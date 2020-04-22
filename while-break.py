while True:  #while loop will run until Break statement fires
    guess = input('Guess a number between 1 and 10: ')
    if int(guess) == 8: #must type cast guess variable because it is stored as string
        print('You won!')
        break
    print(f'{guess} was not the right number, try again.')