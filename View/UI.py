from Controller.controller import Controller

class UI():

    def __init__(self):
        self.status = 0
        self.controller = Controller(UI)

    def start(self, status):
        return self.controller.runner(status)

    def setStatus(self, status):
        self.status = status

    def run(self):
        status = self.start(self.status)

