def main(guess):
    current_guess = 500
    print(current_guess)
    current_max = 1000
    current_min = 1
    no = 1
    i = 0
    while no < 10:
        if guess[i] == 'lower':
            current_max = current_guess
            current_guess = ((current_min + current_max) // 2)
            print(current_guess)
            no += 1
        elif guess[i] == 'higher':
            current_min = current_guess
            current_guess = ((current_min + current_max) // 2)
            print(current_guess)
            no += 1
        elif guess[i] == 'correct':
            print('I Knew it!')
            break
        i += 1
guess_sample = ['lower', 'higher', 'lower', 'correct']
main(guess_sample)