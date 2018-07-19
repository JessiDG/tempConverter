import tkinter

class MyFrame(tkinter.Frame):
    """
    The class MyFrame is the View for a simple program that exemplifies the Model/View/Controller
    architecture. This View class is a tkinter.Frame that contains three Buttons, a user-entry field,
    and a label and a Label. Two buttons notify the Controller when they are pressed, and the other
    Button quits the app. The label displays the converted value. The text field allows a user
    to input the number they want to convert to Celcius or Fahrenheit, but all conversions are handled
    in the model.
      """
    def __init__(self, controller):
        tkinter.Frame.__init__(self)
        self.pack()
        self.controller = controller    # saves a reference to the controller so that we can call methods
        # on the controller object when the user generates events

        self.userEntryF = tkinter.Entry()
        self.userEntryF.insert(0, "")
        self.userEntryF.pack({"side": "left"})

        self.userEntryC = tkinter.Entry()
        self.userEntryC.insert(0, "")
        self.userEntryC.pack({"side": "left"})

        self.convertToFahrenheitButton = tkinter.Button(self)
        self.convertToFahrenheitButton["text"] = "Convert to Fahrenheit        "
        self.convertToFahrenheitButton["command"] = self.controller.convertToFahrenheitButtonPressed
        self.convertToFahrenheitButton.pack({"side": "left"})

        self.convertToCelciusButton = tkinter.Button(self)
        self.convertToCelciusButton["text"] = "Convert to Celcius              "
        self.convertToCelciusButton["command"] = self.controller.convertToCelciusButtonPressed
        self.convertToCelciusButton.pack({"side": "left"})

        self.labelForOutput = tkinter.Label(self)
        self.labelForOutput["text"] = ""
        self.labelForOutput.pack({"side": "right"})

        self.quitButton = tkinter.Button(self)
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] = self.quit
        self.quitButton.pack({"side": "left"})