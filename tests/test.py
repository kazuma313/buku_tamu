import unittest
import module as module

class TestStringMethods(unittest.TestCase):
    
    def setUp(self):    # this method will run before starting all the other test methods
        print("Starting a method/test: ")
    
    def test_noTeleponTest1(self):
        test_param = 10
        result = module.input_noTelepon(test_param)
        self.assertFalse(isinstance(result, AssertionError))
        
    def test_noTeleponTest2(self):
        test_param = "082222222222"
        result = module.input_noTelepon(test_param)
        self.assertEqual(result, test_param)
        
    def test_noTeleponTest3(self):
        test_param = "083222222222"
        result = module.input_noTelepon(test_param)
        self.assertEqual(result, test_param)
        
    def test_noTeleponTest4(self):
        test_param = "083"
        result = module.input_noTelepon(test_param)
        self.assertFalse(isinstance(result, AssertionError))
        
    def test_nama1(self):
        test_param = ""
        result = module.input_nama(test_param)
        self.assertFalse(isinstance(result, AssertionError))
        
    def test_nama2(self):
        test_param = 13
        result = module.input_nama(test_param)
        self.assertEqual(result, "13")
        
if __name__ == '__main__':
    print("test")
    unittest.main()