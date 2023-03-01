import unittest
from learn_circle_ci.modules.hello_world import print_hello_world

class HelloWorldTest(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(print_hello_world("PJ"), "From PJ, Hello World!")
if __name__ == "__main__":
    unittest.main()
