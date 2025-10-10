#
# Test Script: algorithm_test.py
#
# Purpose:
#   Pytest-based tests for the functions in the algorithm module.
#
# Usage:
#   Run with pytest from the project root directory.
#
# Notes  :
#
# 1) PyTest is currently the most popular test framework for Python
# 2) Online documentation https://docs.pytest.org/en/stable
# 3) PyTest can be run from command line or from within Visual Studio Code
# 4) Each unit test name must start with "test" to be recognised by test runner
# 5) Test Explorer in Visual Studio can be used as a test runner
# 6) All unit tests must be written in the unit test pattern AAA (Arrange, Act and Assert)
#

# Standard Library
import pytest
from parameterized import parameterized

# Application Specific
import src.algorithm as algorithm


def test_multiple2numbers():

    expected = 35
    actual = algorithm.multiply_two(7, 5)
    assert expected == actual

def test_greeting():

    expected = "Hello, Sam"
    actual = algorithm.greeting("Sam")
    assert expected == actual

def test_filehash():

    expected = "844b2ee10a35e1c29be679b7e9746c790aeb4dc8"
    actual = algorithm.calculate_file_hash(".pylintrc")
    assert expected == actual

def test_square_root():

    expected = 7.0000
    ret_value = algorithm.square_root(49)
    compare_value = round(ret_value, 4)

    assert expected == pytest.approx(compare_value)

def test_find_prime_numbers_opt():

    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    actual = algorithm.find_prime_numbers_opt(100)
    assert expected == actual

def test_find_prime_numbers_opt_large():

    # Largest prime number under 20,000
    expected = 19997

    primes = algorithm.find_prime_numbers_opt(20000)
    last_prime = primes[-1]
    assert expected == last_prime

def test_find_prime_numbers():

    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    actual = algorithm.find_prime_numbers(100)
    assert expected == actual

def test_find_prime_numbers_large():

    # Largest prime number under 20,000
    expected = 19997

    primes = algorithm.find_prime_numbers(20000)
    last_prime = primes[-1]
    assert expected == last_prime

def test_is_valid_permutation_invalid_1():

    # Permutation with missing value
    a = [5,2,1,4]

    expected = 0
    actual = algorithm.is_valid_permutation(a)

    assert expected == actual

def test_is_valid_permutation_invalid_2():

    # Permutation with duplicate value
    a = [5,2,1,4,3,2]

    expected = 0
    actual = algorithm.is_valid_permutation(a)

    assert expected == actual

def test_is_valid_permutation_valid_1():

    # Valid permutation
    a = [19,2,4,16,1,5,18,17,3,10,9,6,14,7,8,11,12,15,13]

    expected = 1
    actual = algorithm.is_valid_permutation(a)

    assert expected == actual

def test_is_valid_permutation_valid_2():

    # Valid permutation
    a = [1]

    expected = 1
    actual = algorithm.is_valid_permutation(a)

    assert expected == actual

@parameterized.expand([
    ("P64", 64, 654),
    ("P268", 268, 5268),
    ("P940", 940, 9540),
    ("N268", -268, -2568),
    ("N123", -123, -1235),
    ("N916", -916, -5916),
    ])
def test_Add5ToGiveMaxNumber(name, value, expected):

    actual = algorithm.Add5ToGiveMaxNumber(value)

    assert expected == actual

def createBinaryTree():
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

def test_BinaryTreeTraversal_TopToBottom_1():

    expected = [[3], [9,20], [15,7]]

    binaryTree = createBinaryTree()

    actual = algorithm.BinaryTreeTraversal_TopToBottom(binaryTree)

    assert expected == actual

def test_BinaryTreeTraversal_BottomToTop_1():

    expected = [[15,7], [9,20], [3]]

    binaryTree = createBinaryTree()

    actual = algorithm.BinaryTreeTraversal_BottomToTop(binaryTree)

    assert expected == actual

# This will not be recognized as a test as the method is not prefixed with "test"
# If it was a valid test it would fail
def notatest():

    pytest.fail("This test should not be run!")

def test_Factorial():

    expected = 5040

    actual = algorithm.Factorial(7)

    assert expected == actual
