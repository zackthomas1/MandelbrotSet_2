import math, logging

#Sets up logging
logging.basicConfig(level=logging.DEBUG, format='\t%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
#logging.disable(logging.ERROR) # uncomment to block debug logging.debug messages
logging.disable(logging.DEBUG) # uncomment to block debug logging.debug messages
#logging.disable(logging.INFO) # uncomment to block debug logging.info messages and below

class Utility():
    def __init__(self):
        pass 

    @staticmethod
    def normalize_data(input_value, input_max, input_min, output_max=1.0, nMin=0.0):
        """Normalize data linearly"""

        Pn = ((input_value - input_min)/(input_max-input_min)) * (output_max - nMin)+ nMin
        return Pn

    @staticmethod
    def log_conversion(value, gamma = 2.2):
        """Convert incoming values into logarithm with 255(max RGB value) as limit. 
        This will help sperate values in the mid and lower range range"""

        gamma_correction = math.pow(value, gamma)
        logging.debug("Utility::log_conversion->For x=%s: fn=%s" %(value,gamma_correction))

        return gamma_correction

    @staticmethod 
    def float_equality(float_value_a, float_value_b, delta = 0.0001):
        """ Determines if two float values are equal"""

        if abs(float_value_a - float_value_b) < delta:
            return True
        else: 
            return False