def statisticsMenu():
    while (True):
        print("Available stats include")
        print("Press 1 to go back")
        print("Press 2 to quit")
        #maybe define a matrix for this. We receive the filters from the user. We should be able to compare stats to
        #each other i.e pts to min etc. This is where the matrix could be good
        print('Press 3 to see consistency data')
        print('press 4 to see player data')

        userInput = str(input("Please pick an option"""))
        if userInput not in ['1','2','3','4']:
            print('Please enter one of the valid options')
        else:
            if userInput == "1":
                return 2
            elif userInput == "2":
                print("quiting...")
                return 3
            elif userInput == "3":
                print('consistency data')
                return 4
            elif userInput == '4':
                print('player data')





