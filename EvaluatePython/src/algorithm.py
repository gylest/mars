#
# Import
#

# Standard Library
import hashlib

#
# Constants
#
PRIME_MINISTER = {
    "name": "Boris Johnson",
    "age": 55,
    "country": "United Kingdom",
    "address": "10 Downing Street"
}

#
# Classes
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, value, left_node=None, right_node=None):
        self.val = value
        self.left = left_node
        self.right = right_node


#
# Functions
#

#
# Form greeting string
#
def greeting(name):
    return "Hello, " + name

#
# Calculate Hash Value for a file
#
def calculate_file_hash(filename):
    block_size = 65536
    hasher = hashlib.sha1()
    with open(filename, 'rb') as afile:
        buf = afile.read(block_size)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(block_size)
    return hasher.hexdigest()

#
# Multiply 2 Numbers
#
def multiply_two(number_one, number_two):
    return_value = number_one * number_two
    return return_value

#
# Calculate Square Root using Newton-Raphson method
#
def square_root(number):
    x = number
    y = 1.000000  # iteration initialzation.
    e = 0.000001  # accuracy after decimal place.
    while x-y > e:
        x = (x+y)/2
        y = number/x
    return x

#
# Find list of prime numbers up to parameter value
# Optimized function
#
def find_prime_numbers_opt(n):
    primes = []
    count = 2

    if n > 1:
        while count <= n:
            divisors = list(range(2, count, 1))
            divcount = 0
            for i in divisors:
                rem = count % i
                if rem == 0:
                    divcount += 1
                    break
                # Optimization. Once divisor past half way point then exit as primes will not exist
                if i * 2 > count:
                    break
            if divcount == 0:
                primes.append(count)
            count += 1
    return primes

#
# Find list of prime numbers up to parameter value
#
def find_prime_numbers(n):
    primes = []
    count = 2

    if n > 1:
        while count <= n:
            divisors = list(range(2, count, 1))
            divcount = 0
            for i in divisors:
                rem = count % i
                if rem == 0:
                    divcount += 1
            if divcount == 0:
                primes.append(count)
            count += 1
    return primes

#
# Check if list if valid permutation 1 ... N
# 0 = Invalid
# 1 = Valid
#
def is_valid_permutation(a:any):
    return_value = 0

    sorted_a = sorted(a)
    dedup = list(dict.fromkeys(sorted_a))

    if len(sorted_a) != len(dedup):
        return return_value

    max_value = sorted_a[-1]
    b = list(range(1, max_value+1))
    diff = list(set(b)-set(sorted_a))

    if len(diff) == 0:
        return_value = 1

    return return_value

# Fizz Buzz Test:
# Write a program that prints the numbers from 1 to n.
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.
def fizzbuzz(n):

    for i in range(1, n+1, 1):
        rem3 = i % 3
        rem5 = i % 5

        if rem3 == 0 and rem5 == 0:
            print("FizzBuzz")
        elif rem3 == 0:
            print("Fizz")
        elif rem5 == 0:
            print("Buzz")
        else:
            print(i)

# Fibonacci Sequence Test
# The next number is found by adding up the two numbers before it.
# Write a program that prints n numbers from  fibonacci sequence
def fibonacci_sequence(n):
    a, b = 0, 1
    # use underscore(_) character in for expression to indicate not interested in the index
    for _ in range(n):
        print(a)
        a, b = b, a + b

#
# Add 5 to a number in such a way to make number the biggest possible value
# e.g. 268 => 5268, 940 = 9540
#
def add5_to_give_max_number(n):
    result = 0
    resultstr = ""
    digit = 5

    positive = n >= 0
    done = False

    string_number = str(abs(n))

    for ch in string_number:
        thisdigit = int(ch)
        if (digit >= thisdigit) and positive and (not done):
            resultstr += str(digit) + str(thisdigit)
            done = True
        elif (digit <= thisdigit) and (not positive) and (not done):
            resultstr += str(digit) + str(thisdigit)
            done = True
        else:
            resultstr += str(thisdigit)

    if not done:
        resultstr += str(digit)
        done = True

    result = int(resultstr)

    if not positive:
        result *= (-1)

    return result

#
# Binary Tree Traversal: Bottom to top from left to right
#
def binary_tree_traversal_bottom_to_top(root):
    if root is None:
        return []
    # In the first stage, we store hte nodes (not their value).
    result = []
    next_layer = [root]
    while len(next_layer) != 0:
        result.append(next_layer)
        # Gather the nodes in the next deeper layer.
        next_layer = []
        for father in result[-1]:
            if father.left is not None:
                next_layer.append(father.left)
            if father.right is not None:
                next_layer.append(father.right)
    # In the second stage, we convert the nodes into their values.
    result = [[node.val for node in layer] for layer in result]
    return result[::-1]

#
# Binary Tree Traversal: Top to Bottom from left to right
#
def binary_tree_traversal_top_to_bottom(root):
    if root is None:
        return []
    # In the first stage, we store hte nodes (not their value).
    result = []
    next_layer = [root]
    while len(next_layer) != 0:
        result.append(next_layer)
        # Gather the nodes in the next deeper layer.
        next_layer = []
        for father in result[-1]:
            if father.left is not None:
                next_layer.append(father.left)
            if father.right is not None:
                next_layer.append(father.right)
    # In the second stage, we convert the nodes into their values.
    result = [[node.val for node in layer] for layer in result]
    return result

#
# Calculate factorial for a number (n)
#
def factorial(num):
    factorial_return = 0

    # check if the number is negative, positive or zero
    if num > 0:
        factorial_return = 1
        for i in range(1, num + 1):
            factorial_return = factorial_return*i

    return factorial_return
