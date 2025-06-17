import unittest
import temp_conversion_tool



class TestCuboid(unittest.TestCase):
    def test_temp_converter(self):
        self.assertAlmostEqual(convert_to_celsius(104),40)
        self.assertAlmostEqual(convert_to_celsius(55),12.78)
        self.assertAlmostEqual(convert_to_celsius(89),31.67)
    
C/Users/ROB/Desktop/yaw\'s\ only/WORK/alx repo/alx_be_python/