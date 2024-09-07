print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
go = input("Where would you like to go: left or right?")
if go == "left":
    left = input("You wanna swim or wait?")
    if left == "wait":
        door = input("Which door: red, yellow, blue")
        if door == "yellow":
            print("you won")
        else:
            print("You lost")
    else:
        print("You lost")

else:
    print("you lost")
