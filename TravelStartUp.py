from TravelController import TravelController


class ProgramStartUp:

    def __init__(self):
        """
         Initialize an instance of TravelController class
        """
        self.controller = TravelController()

    def run(self):
        """
        Run the program
        """
        self.controller.run()

if __name__ == "__main__":
    app = ProgramStartUp()
    app.run()

