name = input('What is your name? ')

while True:
    x = input(name + ', enter an integer between 1 and 100 >> ')
    x = int(x)

    if 1 <= x <= 100:
        # If the integer entered is odd and less than 60, print the number entered and “Odd and less than 60.”
        if x % 2 != 0 and x < 60:
            print('Odd and less than 60')
        # If the integer entered is even and in the inclusive range of 2 to 24, print “Even and less than 25.”
        elif x % 2 == 0 and 2 <= x <= 24:
            print('Even and less than 25')
        # If the integer entered is even and in the inclusive range of 26 to 60, print “Even and between 26 and 60 inclusive.”
        elif x % 2 == 0 and 26 <= x <= 60:
            print('Even and between 26 and 60 inclusive')
        # If the integer entered is even and greater than 60, print the number entered and “Even and greater than 60.”
        elif x % 2 == 0 and x > 60:
            print('Even and greater than 60')
        # If the integer entered is odd and greater than 60, print the number entered and “Odd and greater than 60.”
        elif x % 2 != 0 and x > 60:
            print('Odd and greater than 60')
    else:
        print('Invalid number, try again')

    keep_going = input(name + ', would you like to continue? y/n >> ')

    if keep_going != "y":
        break
