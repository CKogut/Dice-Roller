import random

# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.

play = 'y'
while play == 'y':
    num_of_dice = 0
    while True:
        dice_input = input('Choose how many dice to roll. Enter a number 1 through 6: ')
        if dice_input.strip() in ('1', '2', '3', '4', '5', '6'):
            num_of_dice = int(dice_input)
            break
        else:
            print("Invalid input.")

    print(f"Rolling {num_of_dice} dice")

    for x in range(1, num_of_dice + 1):
        print(f"Die {x} is a {random.randint(1,6)}")

    play_again = input("Roll again?")

