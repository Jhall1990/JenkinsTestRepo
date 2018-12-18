import sys
import unittest
import xmlrunner


class PythonTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, 1)

    def test_2(self):
        self.assertEqual(2, 2)

    def test_3(self):
        self.assertEqual(3, 3)

    def test_4(self):
        self.assertEqual(4, 4)

    def test_5(self):
        self.assertEqual(5, 5)


def main():
    report_dir = sys.argv[1:][0]
    print report_dir
    del sys.argv[1:]
    test_runner = xmlrunner.XMLTestRunner(output=report_dir)
    unittest.main(testRunner=test_runner)
    # unittest.main()


if __name__ == '__main__':
    main()
