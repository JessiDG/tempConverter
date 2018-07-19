class Converter:
    """
    A single object of class converter contains no instance variables and can
    convert an inputted int or float to the Celcius or Fahrenheit conversion of it.
    """
    @staticmethod
    def convertToCelcius(num):
        """ Converts the user input to Celcius after checking if it is valid
        """
        try:
            num = ((5/9) * (float(num) - 32))
            return "{0:.2f}".format(num)
        except ValueError:
            return "Please enter a number."

    @staticmethod
    def convertToFahrenheit(num):
        """ Converts the user input to Fahrenheit after checking if it is valid
        """
        try:
            num = (9/5)*(float(num)) + 32
            return "{0:.2f}".format(num)
        except ValueError:
            return "Please enter a number."