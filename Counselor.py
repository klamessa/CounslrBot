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
        rTip = input("Would you like some relaxation tips? Y or N?").upper()
        if rTip == 'Y':
            relaxation_tips()
        elif rTip == 'N':
            print('\nNo worries, always here to listen! Take it easy now')
        else:
            print('\nPlease enter Y or N')
    else:
        print('\nPlease enter Y or N')


name = input("Enter your name: ")
print('\nHi', name, "!, I'm counselor bot! I heard you're stressed?")
print("...")
response = input("is this true? Y or N?  ").upper()


if response == 'Y':
    Q2 = input("\nI'm sorry to hear that, Do you want me to listen (L) or offer advice (A) ?").upper()
    if Q2 == 'L':
        problem = input("\nWhat's going on?")
        if problem != '':
            print('\nThanks for sharing, hope that made you feel better...')
            print("I know that I can't exactly say that I know how you feel, after all I'm just a bot...")
            lAdvice = input("But I could offer some practical advice on your stress..? Y or N?").upper()
            if lAdvice == 'Y':
                give_advice()
            elif lAdvice == 'N':
                print('\nNo worries, always here to listen! Take it easy now')
            else:
                print('\nPlease enter Y or N')
    elif Q2 == 'A':
        input("What's going on?")
        print('\nThanks for sharing, hope that made you feel better...')
        print("I know that I can't exactly say that I know how you feel, after all I'm just a bot...")
        give_advice()
    else:
        print('\nPlease enter L or A')
else:
    print('\nLooks like you\'ve got things under control, you have a good one!')


def relaxation_tips():
    """Provide relaxation techniques."""
    print("\nHere are some relaxation techniques that may help:")
    print("1. Deep Breathing: Take a deep breath in, hold for 3 seconds, and exhale slowly. Repeat 5 times.")
    print("2. Visualization: Close your eyes and imagine a peaceful place, like a beach or a forest.")
    print("3. Stretching: Stand up, reach for the sky, and then touch your toes. Rotate your wrists and ankles.")
    print("4. Take a Break: Sometimes, just stepping away from a problem for a few minutes can help clear your mind.")
    print("5. Listen to Music: Put on your favorite calming song and take a moment to just listen.")
    print("\nRemember, everyone is different. What works for one person might not work for another. It's all about finding what's best for you.")






