import math, logging
from MandelbrotSet_2.Utility import Utility

class Color3f():
    """ """
    
    def __init__(self, red:int = 0, green:int = 0, blue:int = 0):
        
        # Class variables
        self.red = red
        self.green = green
        self.blue = blue 

        self.rgb = (self.red, self.green, self.blue)

    def __eq__(self, color02):
        
        if  Utility.float_equality(self.red, color02.red) and \
            Utility.float_equality(self.green, color02.green) and \
            Utility.float_equality(self.blue, color02.blue):
            return True
        else: 
            return False

    def __ne__(self, color02):
        if self == color02:
            return False
        else: 
            return True

    def __add__(self, color02): 
        
        output_color = Color3f()

        output_color.red = self.red + color02.red
        output_color.green = self.green + color02.green
        output_color.blue = self.blue + color02.blue

        return output_color

    def __sub__(self, color02): 
        
        output_color = Color3f()

        output_color.red = self.red - color02.red
        output_color.green = self.green - color02.green
        output_color.blue = self.blue - color02.blue

        return output_color

    def __mul__(self, scaler:float):
        output_color = Color3f()

        output_color.red = self.red * scaler
        output_color.green = self.green * scaler
        output_color.blue = self.blue * scaler

        return output_color

    def __mul__(self, input02):
        output_color = Color3f()

        if type(input02) == float or type(input02) == int:
            output_color.red = self.red * input02
            output_color.green = self.green * input02
            output_color.blue = self.blue * input02
        elif type(input02) == Color3f:
            output_color.red = self.red * input02.red
            output_color.green = self.green * input02.green
            output_color.blue = self.blue * input02.blue
        else:
            logging.error("Color3f::__mul__->Type Error")
            TypeError
        return output_color

    def __str__(self):
        return "({0}, {1}, {2})".format(self.red, self.green, self.blue)

    def convert_to_int(self): 
        self.red = math.floor(self.red)
        self.green = math.floor(self.green)
        self.blue = math.floor(self.blue)