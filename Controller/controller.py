from Model.UIBackEnd.StartMenu import startMenu
from Model.UIBackEnd.StatisticsMenu import statisticsMenu

class Controller():

    #The Controller will call the different back end services based on what the UI tells it to do.
    #so as of now we need a pull data function, we need a average away from the mean also.
    # user must be asked for input for pull data, this should be supplied from the UI side,
    # the controller funtion should take it as input
    #must also map a start and quit

    def __init__(self, UI):
        self.status = 0
        self.UI = UI

    def callStartMenu(self):
        self.status = startMenu()
        return self.decisionInterpreter(self.status)

    def callStatisticsMenu(self):
        self.status = statisticsMenu()
        return self.decisionInterpreter(self.status)

    def decisionInterpreter(self, status):
        if status == 0:
            self.callStartMenu()
        elif status == 1:
            self.callStatisticsMenu()
        elif status == 2:
           self.decisionInterpreter(self.returnToMainMenu(status))
        else:
            status = 99

    def statisticsInterpreter(self, status):
        return status

    #goes back to the main menu
    def returnToMainMenu(self, status):
        self.status = 0
        return self.status

    def runner(self, status):
        self.status = status
        return self.decisionInterpreter(status)

