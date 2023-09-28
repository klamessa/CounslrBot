def give_advice():
    Q3 = input('Can you do something about this said problem? Y or N? ').upper()
    if Q3 == 'Y':
        print("\nThen my best advice is to write down all the things you CAN do,and DO it!")
        print("You'll feel a lot better once you get the ball rolling")
        print("Goodluck")
    elif Q3 == 'N':
        print("\nYou can't do anything about this problem, looks like it's out of your control")
        print("Try destressing or seeking help: you never know who is willing to lend a hand.")
        print("Also remember that life is just ups and downs, so know that for the dark time you're in, there will be better days.")
    else:
        print('\nPlease enter Y or N')


name = input("Enter your name: ")
print('\nHi', name, "!, I'm counselor bot! I heard you're stressed?")
print("...")
response = input("is this true? Y or N?  ").upper()

