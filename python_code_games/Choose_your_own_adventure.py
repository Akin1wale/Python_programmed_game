name = imput("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right, pick wisely").lower()

If answer == "left":
    answer = input("You have come to a river, you can walk around it or swim across")

    if answer == "swim":
        print()
    elif answer == "walk":
        print()
    else:
        print("Not a valid option. You lose")
    
elif answer == "right"
