name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk around and swim to swim accross: ")

    if answer == "swim":
        print("You swim accross and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("Not a valid option. You loose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks dangerous, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back to the main road and lose")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a strenger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You talk to the stranger and he gave you the treasure. You WIN! ")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print("Not a valid option. You loose.")
    else:
        print("Not a valid option. You loose.")

else:
    print("Not a valid option. You loose.")

print("Thank you for trying", name)