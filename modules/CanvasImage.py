import os, logging
from PIL import Image, ImageDraw

from modules.Utility import Utility
from modules.Color3f import Color3f

class CanvasImage():
    def __init__(self, canvas_width, canvas_height, background_color = 'black'):

        # Class Variables
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        self.image = Image.new('RGBA', (self.canvas_width, self.canvas_height), background_color)
        self.draw = ImageDraw.Draw(self.image)
        logging.info("CanvasImage::__init__->Canvas Created: %s x %s" % (self.canvas_width, self.canvas_height))

    def pixel_color(self, iteration_value:int, max_iteration:int, colorspace:str, rgb_weights:Color3f = Color3f(1.0,1.0,1.0)): 
        """Determines pixel's color value"""

        # colorspace adjustment
        if colorspace == "linear": 
            rgb_value = int(Utility.normalize_data(iteration_value,0,max_iteration,0,255))
        elif colorspace == "log": 
            rgb_value = int(Utility.log_conversion(iteration_value)) # interprets data on a logarithmic scale
        else: 
            logging.error("CanvasImage::pixel_color->ERROR: colorspace not speficied correctly.(\"Log\" or \"linear\")")
            NotImplementedError

        output_color = Color3f()

        output_color.red = rgb_value
        output_color.green = rgb_value
        output_color.blue = rgb_value

        return output_color
    
    def draw_point(self, pixel_position, color_rgb):
        logging.debug("MandelImage::draw_point->pixel_position: " + str(pixel_position) + " color_rgb: " + str(color_rgb))
        self.draw.point(pixel_position, color_rgb)

    def save_image(self, dir, name = "madelbrotSet", file_extension = ".png", \
                    version_number = 0, version_padding = 3, \
                    enable_frames = False, frame_number = 0, frame_padding = 3):
        """saves final image"""
        
        # define output
        version_number = "v%s" % (str(version_number).zfill(version_padding))
        resolution = str(self.canvas_width) + "x" + str(self.canvas_height)
        file_name = "%s_%s_%s" % (name, resolution, version_number) # ex. "madelbrotSet_3500x2000_v006.png"

        # add frame number if enabled        
        if enable_frames == True: 
            frame = str(frame_number).zfill(frame_padding)
            file_name = file_name + "_" + frame

        # add file extension
        file_name = file_name + file_extension
        
        # Create final output path
        image_path = os.path.join(dir, file_name)

        # Save Image
        self.image.save(image_path) 
        logging.info('CanvasImage::save_image->SUCESS:Image Saved->%s' % (image_path))

        return (True, image_path)