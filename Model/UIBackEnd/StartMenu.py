def startMenu():

    while (True):
        print("Welcome to Sorare fantasy stats")
        print("Press 1 to see available statistics")
        print("Press 2 to go back")
        print("Press 3 to quit")

        userInput = str(input("Please pick an option"))
        if userInput not in ['1','2','3']:
            print('Please enter one of the valid options')
        else:
            if userInput == "1":
                return 1
            elif userInput == "2":
                return 2
            else:
                print("quitting...")
                return 3






