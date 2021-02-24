import unittest,os, sys

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from modules.CanvasImage import CanvasImage

class Test_CanvasImage(unittest.TestCase): 

    def test_init(self):
        canvas = CanvasImage(700, 400)

        self.assertEqual(canvas.canvas_width, 700)
        self.assertEqual(canvas.canvas_height, 400)

    def test_pixel_color(self): 
        pass
        
    def test_draw_point(self): 
        pass

    def test_save_image(self): 

        canvas = CanvasImage(700, 400)

        parent_dir = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
        output_dir = os.path.join(parent_dir, "..\\__render__\\")

        # save image
        result = canvas.save_image(output_dir, version_number=6)
        
        self.assertTrue(result[0])


if __name__ == "__main__": 
    unittest.main()
