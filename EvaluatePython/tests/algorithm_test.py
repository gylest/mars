#
# Program: Unit Test Script for Compute Module
#
# Notes  :
# 1) The Python unit testing framework, sometimes referred to as “PyUnit,” is a Python language version of JUnit
# 2) Online documentation (https://docs.python.org/3/library/unittest.html)
# 3) A testcase is created by subclassing unittest.TestCase.
# 4) Each unit test name must start with "test" to be recognised by test runner
# 5) Test Explorer in Visual Studio can be used as a test runner
# 6) All unit tests must be written in the unit test pattern AAA (Arrange, Act and Assert)
#

# Standard Library
import unittest
from parameterized import parameterized
import src.algorithm as algorithm

class TestHarness(unittest.TestCase):

    def test_multiple2numbers(self):

        expected = 35
        actual = algorithm.multiply_two(7, 5)
        self.assertEqual(expected, actual)

    def test_greeting(self):

        expected = "Hello, Sam"
        actual = algorithm.greeting("Sam")
        self.assertEqual(expected, actual)

    def test_filehash(self):

        expected = "844b2ee10a35e1c29be679b7e9746c790aeb4dc8"
        actual = algorithm.calculate_file_hash(".pylintrc")
        self.assertEqual(expected, actual)

    def test_square_root(self):

        expected = 7.0000
        ret_value = algorithm.square_root(49)
        compare_value = round(ret_value, 4)
        self.assertAlmostEqual(expected, compare_value)

    def test_find_prime_numbers_opt(self):

        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

        actual = algorithm.find_prime_numbers_opt(100)
        self.assertEqual(expected, actual)

    def test_find_prime_numbers_opt_large(self):

        # Largest prime number under 20,000
        expected = 19997

        primes = algorithm.find_prime_numbers_opt(20000)
        last_prime = primes[-1]
        self.assertEqual(expected, last_prime)

    def test_find_prime_numbers(self):

        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

        actual = algorithm.find_prime_numbers(100)
        self.assertEqual(expected, actual)

    def test_find_prime_numbers_large(self):

        # Largest prime number under 20,000
        expected = 19997

        primes = algorithm.find_prime_numbers(20000)
        last_prime = primes[-1]
        self.assertEqual(expected, last_prime)

    def test_is_valid_permutation_invalid_1(self):

        # Permutation with missing value
        a = [5,2,1,4]

        expected = 0
        actual = algorithm.is_valid_permutation(a)

        self.assertEqual(expected,actual)

    def test_is_valid_permutation_invalid_2(self):

        # Permutation with duplicate value
        a = [5,2,1,4,3,2]

        expected = 0
        actual = algorithm.is_valid_permutation(a)

        self.assertEqual(expected,actual)

    def test_is_valid_permutation_valid_1(self):

        # Valid permutation
        a = [19,2,4,16,1,5,18,17,3,10,9,6,14,7,8,11,12,15,13]

        expected = 1
        actual = algorithm.is_valid_permutation(a)

        self.assertEqual(expected,actual)

    def test_is_valid_permutation_valid_2(self):

        # Valid permutation
        a = [1]

        expected = 1
        actual = algorithm.is_valid_permutation(a)

        self.assertEqual(expected,actual)

    @parameterized.expand([
       ("P64", 64, 654),
       ("P268", 268, 5268),
       ("P940", 940, 9540),
       ("N268", -268, -2568),
       ("N123", -123, -1235),
       ("N916", -916, -5916),
    ])
    def test_Add5ToGiveMaxNumber(self, name, value, expected):

        actual = algorithm.Add5ToGiveMaxNumber(value)

        self.assertEqual(expected,actual)

    def createBinaryTree(self):
        #---------------------------------------------------------------------------------------------------------------------
        # Create Binary Tree
        # Nodes can be either a) Root Node, b) Leaf Node (node with no children), c) Intermediate Node (node with children)
        # Node Levels: Start at top with level 0, then level 1 etc
        # Element Numbers: Root = 1, Next Level first element to left = 2, element to tight = 3 etc
        #---------------------------------------------------------------------------------------------------------------------
        leafNodeL2E4 = algorithm.TreeNode(15)
        leafNodeL2E5 = algorithm.TreeNode(7)
        leafNodeL1E2 = algorithm.TreeNode(9)
        intNodeL1E3  = algorithm.TreeNode(20,leafNodeL2E4,leafNodeL2E5)
        rootNodeL0E1 = algorithm.TreeNode(3,leafNodeL1E2,intNodeL1E3)

        return rootNodeL0E1

    def test_BinaryTreeTraversal_TopToBottom_1(self):

        expected = [[3], [9,20], [15,7]]

        binaryTree = self.createBinaryTree()

        actual = algorithm.BinaryTreeTraversal_TopToBottom(binaryTree)

        self.assertEqual(expected,actual)

    def test_BinaryTreeTraversal_BottomToTop_1(self):

        expected = [[15,7], [9,20], [3]]

        binaryTree = self.createBinaryTree()

        actual = algorithm.BinaryTreeTraversal_BottomToTop(binaryTree)

        self.assertEqual(expected,actual)

    # This will not be recognized as a test as the method is not prefixed with "test"
    # If it was a valid test it would fail
    def notatest(self):

        self.fail("This test should not be run!")

    def test_Factorial(self):

        expected = 5040

        actual = algorithm.Factorial(7)

        self.assertEqual(expected,actual)


#
# If this run as startup file, the if statement is true and the main() is called.
# This will run all tests within class and print report at the end.
#
if __name__ == '__main__':
    unittest.main()
