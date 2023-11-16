import random

# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.


def get_num_of_die():
    while True:
        dice_input = input('Choose how many dice to roll. Enter a number 1 through 6: ')
        if dice_input.strip() in ('1', '2', '3', '4', '5', '6'):
            return int(dice_input)
        else:
            print("Invalid input.")


def roll_dice(num):
    for x in range(1, num + 1):
        print(f"Die {x} is a {random.randint(1, 6)}")


def play_again():
    while True:
        play_input = input("Roll again? Y or N: ")
        if play_input.strip().lower() == 'y':
            return True
        elif play_input.strip().lower() == 'n':
            print("Goodbye")
            return False
        else:
            print("Invalid input")


play = True
while play:
    num_of_dice = get_num_of_die()

    print(f"Rolling {num_of_dice} dice")

    roll_dice(num_of_dice)

    play = play_again()

