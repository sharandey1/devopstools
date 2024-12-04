import unittest 
def add_numbers(a,b):
    return a+b
class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(2,3)
        self.assertEqual(result,5)

def deduct_numbers(a,b):
    return a-b
class TestDeductNumbers(unittest.TestCase):
    def test_deduct_numbers(self):
        result = deduct_numbers(2,3)
        self.assertEqual(result,-1)

def multiply_numbers(a,b):
    return a*b
class TestMultiplyNumbers(unittest.TestCase):
    def test_multiply_numbers(self):
        result = multiply_numbers(2,3)
        self.assertEqual(result,6)

def divide_numbers(a,b):
    return a/b
class TestDivideNumbers(unittest.TestCase):
    def test_divide_numbers(self):
        result = divide_numbers(6,3)
        self.assertEqual(result,2)

def add_numbers2(a,b):
    return a+b
class TestAddNumbers(unittest.TestCase):
    def test_add_numbers2(self):
        result = add_numbers2(2,3)
        self.assertEqual(result,5)

if __name__=='__main__':
    unittest.main()

