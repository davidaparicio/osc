import unittest
import main

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(main.test_requests(), 200)

if __name__ == '__main__':
    unittest.main()