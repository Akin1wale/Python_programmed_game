name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end, and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input(
        "You have come to a river. You can walk around it or swim across. Type 'walk' to walk around or 'swim' to swim across: ").lower()

    if answer == "swim":
        print("You swam across the river and were eaten by an alligator. You lose.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water, and lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input(
        "You come to a bridge. It looks wobbly. Do you want to cross it or head back? Type 'cross' to cross or 'back' to go back: ").lower()

    if answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them? Type 'yes' to talk or 'no' to ignore: ").lower()

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win!")
        elif answer == "no":
            print("You ignore the stranger and they are offended. You lose.")
        else:
            print("Not a valid option. You lose.")
    elif answer == "back":
        print("You go back and lose.")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")
