import logging, math

from MandelbrotSet_2.Utility import Utility
from MandelbrotSet_2.Color3f import Color3f
from MandelbrotSet_2.CanvasImage import CanvasImage

class MandelbrotSet():
    """ """ 
    
    def __init__(self, canvas_width = 350, canvas_height = 200, max_iteration = 1000):

        # Class Variables
        # ---------------
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        # viewspace
        self.x_view_max =  1.0 
        self.x_view_min = -2.5
        self.y_view_max =  1.0
        self.y_view_min = -1.0

        self.max_iteration = max_iteration

        self.trans_x = 0  
        self.trans_y = 0
        self.scaler = 1.0 

        # color bands
        self.low_color  = Color3f(1.0, 0.0, 0.0)
        self.mid_color  = Color3f(0.0, 1.0, 0.0)
        self.high_color = Color3f(0.0, 0.0, 1.0)

        self.color_band_thresholds = (0.33, 0.66)

        # Create Image
        self.canvas = CanvasImage(self.canvas_width, self.canvas_height)
    

    def set_viewspace(self):
        """Set the viewing area for within mandelbrot set""" 

        # Defines 'c' value. Sets the normalization scale. Use this to control field of view for image.
        # X scale must be between (-2.5, 1.0)
        self.x_view_max = (1.0 * self.scaler) + self.trans_x
        self.x_view_min = (-2.5 * self.scaler) + self.trans_x
        # Y scale must be between(-1.0, 1.0)
        self.y_view_max = (1.0 * self.scaler) + self.trans_y
        self.y_view_min = (-1.0 * self.scaler) + self.trans_y    

    def translate_viewspace(self, trans_x = 0.0, trans_y = 0.0):
        """Translate the image to view different areas of mandelbrot set""" 

        self.trans_x = trans_x 
        self.trans_y = trans_y

    def zoom_viewspace(self, scaler = 0.5): 
        """Zoom in and out of mandelbrot set""" 

        self.scaler = scaler 

    def get_iteration_value_at_pixel(self, x_pos, y_pos):
        """Determines the iteration count at a given pixel(x,y)"""
        
        # Constant variables (Do NOT Change)
        iteration = 0
        x = 0
        y = 0

        # Main logic loop for function. Determines if 'c' value (x0,y0) maintain stability. i.e. does NOT go to infinity
        while (x*x + y*y <= 2*2 and iteration < self.max_iteration): 
            x_temp = x*x - y*y + x_pos
            y = 2*x*y + y_pos
            x = x_temp
            iteration += 1 # increment

        return iteration

    def rgb_colormode(self, color, iteration_value, thresholds:(float,float), \
                            low_color:Color3f, mid_color:Color3f, high_color:Color3f): 
        """Renders image in rgb colormode""" 

        if iteration_value < (self.max_iteration * thresholds[0]):
            color = low_color * color
        elif (self.max_iteration * thresholds[0]) <= iteration_value and iteration_value < (self.max_iteration * thresholds[1]):
            color = mid_color * color
        elif (self.max_iteration * thresholds[1]) <= iteration_value :
            color = high_color * color
            
        color.convert_to_int()
        return color

    def grayscale_colormode(self, color, multiple = 1.0): 
        """Renders image in grayscale colormode""" 

        color.red = math.floor(color.red * multiple) 
        color.green = math.floor(color.green * multiple)
        color.blue = math.floor(color.blue * multiple)

        return color

    def draw(self, colormode = "rgb", colorspace="linear"): 
        """Draws the mandelbrot set""" 

        for Py in range(0, self.canvas_height):
            for Px in range(0, self.canvas_width):

                x0 = Utility.normalize_data(Px+1, self.canvas_width, 0,  self.x_view_max,  self.x_view_min)
                y0 = Utility.normalize_data(Py+1, self.canvas_height, 0, self.y_view_max,  self.y_view_min)

                iteration_value = self.get_iteration_value_at_pixel(x0, y0)
                color = self.canvas.pixel_color(iteration_value, self.max_iteration, colorspace)

                # color mode
                if colormode == 'rgb':
                    color = self.rgb_colormode(color, iteration_value, self.color_band_thresholds, \
                                                    self.low_color, self.mid_color,self.high_color )
                elif colormode == 'grayscale':
                    color = self.grayscale_colormode(color)
                else:
                    logging.error("MandelbrotSet::draw->ERROR: colormode not speficied correctly.(\"rgb\" or \"grayscale\")")
                    NotImplementedError

                logging.debug("MandelbrotSet::draw->Pixel Pos(%d, %d): rgb(%d,%d,%d)" % (Px+1, Py+1, color.red, color.green, color.blue))
                self.canvas.draw_point((Px,Py), (color.red, color.green, color.blue)) # plot point

        logging.info('MandelbrotSet::draw->Done drawing!')
