import tkinter
import myFrame  # the VIEW
import converter  # the MODEL

class Controller:
    """
    The Controller for an app that follows the Model/View/Controller architecture.
    When the user presses a Button on the View, this Controller calls the appropriate
    methods in the Model. The Controller handles all communication between the Model
    and the View. A single object of this class connects the Model and View, specifically
    connecting the user actions (pressing buttons) with calculations.
    """

    def __init__(self):
        """
        This starts the Tk framework up, instantiates the Model (a Counter object),
        instantiates the View (a MyFrame object), and starts the event loop that waits
        for the user to press a Button on the View.
        """
        root = tkinter.Tk()
        self.model = converter.Converter()
        self.view = myFrame.MyFrame(self)
        self.view.mainloop()
        root.destroy()

    @staticmethod
    def isNumber(num):
        """"
        This static method checks to see if an inputted number in any unicode-covered language
        is actually a number or is a string. Code from: https://www.pythoncentral.io/how-to-check-if-a-string-is-a-number-in-python-including-unicode/
        """
        try:
            float(num)
            return True
        except ValueError:
            pass
        try:
            import unicodedata
            unicodedata.numeric(num)
            return True
        except (TypeError, ValueError):
            pass
        return False

    def convertToCelciusButtonPressed(self):
        """
        Python calls this method when the user presses the convertToCelciusButtonPressed in the View.
        """
        userInput = self.view.userEntryC.get()
        if self.isNumber(userInput):
            convertedNum = self.model.convertToCelcius(userInput)
            self.view.labelForOutput["text"] = "Result: " + str(convertedNum) + " (Celcius)"
        else:
            self.view.labelForOutput["text"] = "#"

    def convertToFahrenheitButtonPressed(self):
        """
        Python calls this method when the user presses the convertToFahrenheitButtonPressed in the View.
        """
        userInput = self.view.userEntryF.get()
        if self.isNumber(userInput):
            convertedNum = self.model.convertToFahrenheit(userInput)
            self.view.labelForOutput["text"] = "Result: " + str(convertedNum) + " (Fahrenheit)"
        else:
            self.view.labelForOutput["text"] = "#"


if __name__ == "__main__":
    c = Controller()