import os, logging
from modules.MandelbrotSet import MandelbrotSet
from modules.Color3f import Color3f

#Sets up logging
logging.basicConfig(level=logging.DEBUG, format='\t%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
#logging.disable(logging.ERROR) # uncomment to block debug logging.debug messages
#logging.disable(logging.DEBUG) # uncomment to block debug logging.debug messages
#logging.disable(logging.INFO) # uncomment to block debug logging.info messages and below

class Main():
    """ Top Level Class. (Call only once)"""
    def __init__(self):
        pass 

    @staticmethod
    def main():
        
        # Generate mandelbrot set
        mandelbrot = MandelbrotSet(700, 400, max_iteration = 1000)
        mandelbrot.translate_viewspace(-0.81, -0.185)
        mandelbrot.zoom_viewspace(0.006)
        mandelbrot.set_viewspace()
        mandelbrot.high_color = Color3f(0.0,1.0,1.0)
        mandelbrot.draw(colormode = "rgb", colorspace = "linear")
        
        # Save Path
        relative_dir = os.path.dirname(__file__)
        output_dir = os.path.join(relative_dir, "__render__\\")

        # save image
        mandelbrot.canvas.save_image(output_dir, version_number=12)

# Entry Point
if __name__ == "__main__":
    Main.main()
