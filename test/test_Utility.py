import unittest,os, sys

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from modules.Utility import Utility


class Test_TestUtility(unittest.TestCase):
    def test_normalize_data_01(self):

        # ARRANGE
        input_value = 50
        input_max = 100
        input_min = 0
        output_max = 1.0
        output_min = 0.0

        # ACT
        result = Utility.normalize_data(input_value, input_max, input_min, output_max, output_min)

        # ASSERT
        self.assertAlmostEqual(result, 0.5)

    def test_normalize_data_02(self):
    
        # ARRANGE
        input_value = 50
        input_max = 100
        input_min = 0
        output_max = 0.0
        output_min = 200.0

        # ACT
        result = Utility.normalize_data(input_value, input_max, input_min, output_max, output_min)

        # ASSERT
        self.assertAlmostEqual(result, 100)

    def test_log_conversion(self):

        # ASSERT 
        self.assertAlmostEqual(Utility.log_conversion(1), 1)
        self.assertAlmostEqual(Utility.log_conversion(0.5),0.2176, delta=0.001)
        self.assertAlmostEqual(Utility.log_conversion(2),4.5947934)

    def test_float_equality(self):

        float_01 = 5.0
        float_02 = 5.0000001

        self.assertTrue(Utility.float_equality(float_01, float_02))

if __name__ == "__main__": 
    unittest.main()
