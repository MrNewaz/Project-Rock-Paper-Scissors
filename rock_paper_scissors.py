import random

while True:
    my_answer = input('Choose: rock, paper or scissors: ')
    my_answer = my_answer.lower()

    if my_answer.lower() == 'quit':
        break

    if my_answer != 'rock' and my_answer != 'paper' and my_answer != 'scissors':
        print("Plese choose a valid answer")
        continue

    computer_answer = random.choice(['rock', 'paper', 'scissors'])
    print(f"The computer chose: {computer_answer}")

    if my_answer == computer_answer:
        print("You Tied")
        continue
    elif(my_answer == 'paper' and computer_answer == 'rock'):
        print("You win!")
        break
    elif(my_answer == 'rock' and computer_answer == 'scissors'):
        print("You win!")
        break
    elif(my_answer == 'scissors' and computer_answer == 'paper'):
        print("You win!")
        break
    else:
        print("You lose! Try again")
