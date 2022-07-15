name = input("Enter your name: ")
print('')

print("Hi", name,"!, I'm counselor bot! I heard you're stressed?")
print("...")
response = input("is this true? Y or N?  ")
print('')
if response == "Y":
    print('')
    Q2 = input("I'm sorry to hear that, Do you want me to listen (L) or offer advice (A) ?")
    if Q2 == "L":
        print('')
        problem = input("what's going on?")
        if problem != '' or "A":
            print('')
            print('Thanks for sharing, hope that made you feel better...')
            print("I know that I can't exactly say that I know how you feel, after all I'm just a bot...")
            lAdvice = input("But I could offer some practical advice on your stress..? Y or N?")
            if lAdvice == 'Y':
                print('')
                stressor=input("So can you do something about what is stressing you? Y or N?")
                if stressor == 'Y':
                    print('')
                    print("Than my best advice is to write down all the things you CAN do,and DO it!")
                    print("You'll feel a lot better once you get the ball rolling")
                elif stressor == 'N':
                    print('')
                    print("You can't do anything about this problem, looks like it's out of your control")
                    print("Try destressing or seeking help: you never know who is willing to lend a hand.")
                    print("Also remember that life is just ups and downs, so know that for the dark time you're in, there will be better days.")
                else:
                    print('')
                    print("please enter Y or N")
            if lAdvice == 'N':
                print('')
                print("No worries, always here to listen! Take it easy now")
            else:
                print('')
                print("please enter Y or N")
    if Q2 == "A":
        problemas = input("what's going on?")
        if problemas != '':
            print('')
            print('Thanks for sharing, hope that made you feel better...')
            print("I know that I can't exactly say that I know how you feel, after all I'm just a bot...")
            Q3 = input('Can you do something about this said problem? Y or N? ')
            if Q3 == 'Y':
                print("")
                print("Than my best advice is to write down all the things you CAN do,and DO it!")
                print("You'll feel a lot better once you get the ball rolling")
                print("Goodluck")
            elif Q3 == 'N':
                print("")
                print("You can't do anything about this problem, looks like it's out of your control")
                print("Try destressing or seeking help: you never know who is willing to lend a hand.")
                print("Also remember that life is just ups and downs, so know that for the dark time you're in, there will be better days.")
            else:
                print('')
                print("please enter Y or N")
else:
    print('')
    print("Looks like you've got things under control, you have a good one!")
