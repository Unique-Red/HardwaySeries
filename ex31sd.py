print("""You asked to pick between two  coloured balls.
You have colour #red and #blue.
Do you pick red or blue""")

ball = input("> ")

if ball == "red":
    print("You have chosen a time bomb.")
    print("What will you do?")
    print("1. Diffuse it.")
    print("2. Throw it away and run.")

    bomb = input("> ")

    if bomb == "1":
        print("You've chosen danger. Good luck!")
    elif bomb == "2":
        print("You've chosen safety. Nice!")
    else:
        print(f"Well, doing {bomb} is probably better.")
    
elif ball == "blue":
    print("You have to choose between money and time")
    print("which will you choose?")