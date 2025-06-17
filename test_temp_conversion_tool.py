#testing of the temp_conversion_tool given in assignments, unit test is usually done in a different script from the original to be tested
from fns_and_dsa.temp_conversion_tool import convert_to_celsius, convert_to_fahrenheit #import the module and the function.
import unittest #import init test



#define a class. by anyname. with (unittest.TestCase) as the argument
class TestTempConverter(unittest.TestCase):
    def test_to_celsius(self):
        self.assertAlmostEqual(convert_to_celsius(104),40) #use the self.assertalmostequal method to test to see if your code is yielding the answers you expect
        self.assertAlmostEqual(convert_to_celsius(55),12.78, places=2) #the method takes a minimum of 2 arguments to see if both are almost equal
        self.assertAlmostEqual(convert_to_celsius(89),31.6664, places=3) #the places indicate by what decimal place the accuaracy should be checked

    def test_to_fahrenheit(self):
        self.assertAlmostEqual(convert_to_fahrenheit(40),104)
        self.assertAlmostEqual(convert_to_fahrenheit(12.78),55, delta=0.01) #the delta argument indicates the difference between the 2 numbers , if true will pass
        self.assertAlmostEqual(convert_to_fahrenheit(31.67),89, places=1)
    
if __name__ == "__main__": #this statement means to only run the code in this block if the file is being run directly not if --
    unittest.main(verbosity=2) # -- being imported as a module in another file.