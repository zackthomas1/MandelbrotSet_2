import unittest,os, sys, logging

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from modules.Color3f import Color3f

#Sets up logging
logging.basicConfig(level=logging.DEBUG, format='\t%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
#logging.disable(logging.ERROR) # uncomment to block debug logging.debug messages
logging.disable(logging.DEBUG) # uncomment to block debug logging.debug messages
#logging.disable(logging.INFO) # uncomment to block debug logging.info messages and below

class Test_Color3f(unittest.TestCase):
    def test_initialize_color(self):

        test_color = Color3f(0.5, 0.75, 0.25)

        self.assertAlmostEqual(test_color.red, 0.5)
        self.assertAlmostEqual(test_color.green, 0.75)
        self.assertAlmostEqual(test_color.blue, 0.25)

        self.assertAlmostEqual(test_color.rgb, (0.5,0.75,0.25))

    def test_two_colors_equal(self): 
        color_01 = Color3f(0.5,0.5,0.5)
        color_02 = Color3f(0.5, 0.5, 0.5)

        self.assertTrue(color_01 == color_02)

    def test_two_colors_Notequal(self):
        color_01 = Color3f(0.5,0.5,0.5)
        color_02 = Color3f(0.60, 0.5, 0.5)

        self.assertTrue(color_01 != color_02)

    def test_add_two_colors(self): 

        color_01 = Color3f(0.5,0.5,0.5)
        color_02 = Color3f(0.25, 0.25, 0.25)

        result_color = color_01 + color_02
        answer = Color3f(0.75, 0.75, 0.75)

        self.assertEqual(result_color, answer)

    def test_subtract_two_colors(self): 

        color_01 = Color3f(0.5,0.5,0.5)
        color_02 = Color3f(0.25, 0.25, 0.25)

        result_color = color_01 - color_02
        answer = Color3f(0.25, 0.25, 0.25)
    
        self.assertEqual(result_color, answer)

    def test_multiple_color_by_scaler(self): 
        color_01 = Color3f(1.0, 1.0, 1.0)
        scaler = 0.5; 

        result = color_01 * scaler
        answer = Color3f(0.5,0.5,0.5)

        self.assertEqual(result, answer)

    def test_multiple_color_by_color(self):
        color01 = Color3f(1.0,1.0,1.0)
        color02 = Color3f(0.35,0.45,0.5)

        result = color01 * color02
        answer = Color3f(0.35, 0.45, 0.5)

        self.assertEqual(result, answer)

    def test_convert_to_int(self):
        color = Color3f(2.1, 10.9, 200.5)
        color.convert_to_int()
        answer = Color3f(2, 10, 200)

        self.assertTrue(color == answer)

if __name__ == "__main__": 
    unittest.main()
