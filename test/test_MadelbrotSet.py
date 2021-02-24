import unittest,os, sys

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from modules.MandelbrotSet import MandelbrotSet

class Test_MadelbrotSet(unittest.TestCase): 

    def test_init(self):
        pass

    def test_set_viewspace(self):
        pass

    def test_translate_viewspace(self): 
        pass

    def test_zoom_viewspace(self):
        pass

    def test_get_iteration_value_at_pixel(self):
        pass

    def test_rgbcolor_colormode(self):
        pass

    def test_grayscale_colormode(self):
        pass

    def test_draw(self):
        pass

if __name__ == "__main__": 
    unittest.main()