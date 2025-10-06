#
# Evaluate Python
#
# Notes  :
# 1) To run from command line type "Python src/main.py"
# 2) Debug in VS Code using the launch.json configuration "Python: Current File"
# 3) PEP 8 is the defacto style guide for Python (https://www.python.org/dev/peps/pep-0008/)
# 4) The Python standard library is an extensive set of Python modules e.g. sys, math, strings etc (https://docs.python.org/3/library/)
# 5) The Python Package Index (PyPi) is the official third-party software repository for Python (https://pypi.org/)
# 6) Ensure PyLint package is installed to run code analysis
# 7) Use PIP package manager to install additional Python packages e.g. camelcase
# 8) In Python each file is a module, the folder of a Python program is a package of modules
#

#
# Import
#

# Standard Library
import sys                              # System-specific parameters and functions
import math                             # Mathmatical functions
import string                           # Common string operations
import re                               # Regular expressions
import json                             # Functions to encode and decode json data
import os                               # Access to operating system functionality
import logging                          # Logging module
import pickle                           # Serialaize/Deserialize Python objects to files
import platform                         # Platform information
import uuid                             # Create UUID objects according to RFC 4122

# collections imports
from collections import Counter         # Count occurences of values
from collections import deque           # Double-ended queue
from collections import OrderedDict     # Ordered dictionary

# datetime imports
from datetime import datetime           # A combination of a date and a time.
from datetime import timedelta          # A duration expressing the difference between two date, time, or datetime instances

# threading Imports
from threading import Thread            # Thread

# PyPI Packages
import numpy as np                      # Advanced array operations

# Custom Libraries
import algorithm                          # My own code module

#
# Setup
#
def fSetup():
    # Create temp folder if it does not exist
    folder_path = "temp"
    os.makedirs(folder_path, exist_ok=True)

#
# 1. Output using print()
#


def fOutput():
    # Simple output using f-string formatting
    print(f'Hello World on {datetime.now().strftime("%c")}')
    print(f'Platorm: {sys.platform}')
    print(f'Python Version: {sys.version}')
    print(f'Pi: {math.pi}')
    print(f'Square Root of 85 to 3dp is {math.sqrt(85):.3f}.')
    print(f'Python Implementation: {platform.python_implementation()}')

    # Supress eol on print to show output on same line
    print('2 to the power 6: ', end='')
    print(2 ** 6)

    # Print a word multiple times
    firstWord = 'Spam!'
    print(firstWord * 8)

    # Print array values
    L = [123, 'spam', 1.23]
    print("Length of list:", len(L))
    print(L[0], L[1], L[2])

#
# 2. Variables and Scope
#

# A variable is created the moment you first assign a value to it.
# A variable name must start with a letter or the underscore character.
# A variable name cannot start with a number.
# Variables that are created outside of a function are known as global variables, else they are local variables.
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# String variables can be declared either by using single or double quotes.


def fVariables():
    v1 = 5
    v2 = "John"
    print(v1)
    print(v2)

    v3, v4, v5 = "Grapefruit", "Banana", "Cherry"
    print(v3, v4, v5)

    husband = 'Tony Gyles'
    wife = "Paula Gyles"
    print(f"husband and wife = {husband} and {wife}")

#
# 3. Data Types
#

# Python has the following data types built-in by default, in these categories:
#
# String Type:      str
# Numeric Types:    int, float, complex
# Sequence Types:   list, tuple, range
# Mapping Type:     dict
# Set Types:        set, frozenset
# Boolean Type:     bool
# Binary Types:     bytes, bytearray, memoryview
# Miscellaneous:    none


def fDataTypes():

    s1 = "Hello World"                              # str
    s2 = str(7689)                                  # str, being set explicitly
    # str, convert from number to string value in hex
    s3 = hex(99)
    # str, binary string prefixed with '0b'
    s4 = bin(99)

    i1 = 20                                         # int
    i2 = int(400)                                   # int, being set explicitly

    f1 = 20.5                                       # float
    # float, being set explicitly
    f2 = float(877)

    c1 = 1j                                         # complex
    c2 = complex(i1)                                # complex

    l1 = ["apple", "banana", "cherry"]              # list
    t1 = ("apple", "banana", "cherry")              # tuple
    r1 = range(5)                                   # range
    d1 = {"name": "John", "age": 36}              # dict
    s1 = {"apple", "banana", "cherry"}              # set
    # frozenset. This is an immutable set and values cannot be changed.
    s2 = frozenset({"apple", "banana", "cherry"})

    b1 = True                                       # bool
    b2 = False                                      # bool
    b3 = bool(1)                                    # bool

    bin1 = b"Hello"                                 # bytes
    bin2 = bytearray(5)                             # bytearray
    bin3 = memoryview(bytes(5))                     # memoryview

    # NoneType. This is the Python equivalent to NULL in other languages
    n1 = None

    # Get type
    x = ("apple", "banana", "cherry")
    # Use isinstance() instead as it takes subclasses into account
    print('Type= ', type(x))

    # Multiline string using 3 double quotes (or three single quotes)
    n = """To be or
    not to be"""

#
# 4. Operators
#


def fOperators():
    # Arithemtic Operators
    ao1, ao2, ao3 = 2, 7, 26

    aoresult1 = ao1 + ao2
    aoresult2 = ao1 - ao2
    aoresult3 = ao1 * ao2
    aoresult4 = ao3 / ao2
    aoresult5 = 9 % ao2           # Modulus i.e. remainder
    aoresult6 = ao2 ** 3            # Exponentiation
    # Floor division, divide and drop fractional part. Expected result = 3
    aoresult7 = 22 // 7

    # Assignment Operators
    z = 15
    z += 3
    z -= 4
    z *= 7
    z /= 7
    z %= 6

    # Comparison Operators (==, !=, >, >=, < , <=)
    x, y, z = 0, 99, 35

    if x != 45:
        print("x not equal to 45")

    if y == 99:
        print("x equal to 99")

    if 0 < z < 100:
        print("logical and example")

    # Identity Operators (is, is not)
    list1 = ["carp", "pipe", "barbel", "perch"]
    list2 = ["carp", "pipe", "barbel", "perch"]
    list3 = list1

    if list1 is not list2:
        print("List1 and List2 are different objects")

    if list1 is list3:
        print("List1 and List3 are the same object")

    # id() - Check identity of objects i.e. memory address
    print("Identity 1,2,3 : ", id(list1), id(list2), id(list3))

    # Membership Operators (in, not in)
    fruits = {"apple", "banana", "cherry"}
    if "lemon" in fruits:
        print("lemon found")
    else:
        print("missing fruit")

    if "grape" not in fruits:
        print("Where are my grapes?")

    # Logical operators (and, or, not)
    lo1 = 16
    lo2 = 19

    if (lo1 == 16) and (lo2 == 19):
        print("logical and example")

    if (lo1 > 4) or (lo1 < -20):
        print("logical or example")

    if not 40 < lo1 < 200:
        print("logical not example")

    # Bitwise operators
    bit1 = int('00100001', 2)
    bit2 = int('10100011', 2)

    bitres = bit1 & bit2  # bitwise and
    print(bin(bitres))

    bitres = bit1 | bit2  # bitwise or
    print(bin(bitres))

    bitres = bit1 ^ bit2  # bitwise xor, Sets each bit to 1 if only one of two bits is 1
    print(bin(bitres))

#
# 5. Collections
#    * List[]       is a collection which is ordered and changeable.            Allows duplicate members.
#    * Tuple()      is a collection which is ordered and unchangeable.          Allows duplicate members.
#    * Set{}        is a collection which is unordered and unindexed.           No duplicate members.
#    * Dictionary{} is a collection which is unordered, changeable and indexed. No duplicate members.


def fCollections():
    #
    # List []
    #

    # First element = 0 Last element  = -1
    # Changeable
    # Duplicates
    fruitsList = ["apple", "banana", "cherry", "lemon", "orange"]
    print(fruitsList)
    fruitsList.append("grapefruit")
    print(fruitsList)
    print("First item           = " + fruitsList[0])
    print("Second item          = " + fruitsList[1])
    print("Third item           = " + fruitsList[2])
    print("Second to last item  = " + fruitsList[-2])
    print("Last  item           = " + fruitsList[-1])
    fruitsList[0] = "blackberries"                 # Change element
    fruitsother = fruitsList[1:3]                  # Get items 1 to 2
    fruitsother = fruitsList[:4]                   # Get items 0 to 3
    print(fruitsList)

    # Enumerate list
    for i, value in enumerate(fruitsList):
        print(f'Fruit[{i}] = {value}')

    # Sort list
    unsortedAnimals = ["tiger", "zebra", "badger",
                       "owl", "lion", "bear", "gazelle", "termite"]
    sortedAnimals = sorted(unsortedAnimals)

    # Remove duplicates from a list
    duplist = ["a", "b", "a", "c", "c"]
    deduplist = list(dict.fromkeys(duplist))
    print(deduplist)

    # Add lists
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]
    list3 = list1 + list2
    print(list3)

    # slice() object
    list4 = ["pencil", "pen", "clipboard", "rubber"]
    slice0to2 = slice(0, 2, 1)
    listfromsplice = list4[slice0to2]   # Expect ["pencil", "pen"]
    print(listfromsplice)

    # Create list from range()
    mylist = list(range(20))

    # Create list using list comprehension
    squares = [x**2 for x in range(11)]
    cubes = [x**3 for x in range(15)]

    #
    # Tuples()
    #

    # First element = 0 Last element  = -1
    # Immutable
    # Duplicates
    fruitsTuple = ("starfruit", "persimmon", "feijoa", "jackfruit", "papaya")
    print(fruitsTuple[1])         # 2nd item
    print(fruitsTuple[-1])        # last item

    for x in fruitsTuple:
        print(x)

    # concatenate tuples (cannot concat string only)
    exoticFruitsTuple = ("Rambutan", "Durian")
    allfruits = fruitsTuple + exoticFruitsTuple

    # slice() object
    alphabet = ("a", "b", "c", "d", "e", "f", "g", "h")
    slice3to5 = slice(3, 5, 1)
    print(alphabet[slice3to5])  # Expect ("d", "e")

    # unpack a tuple
    fruit1, fruit2, fruit3, fruit4, fruit5 = fruitsTuple

    #
    # Sets  {}
    #

    # Cannot access elements by a number! But can add or remove
    # No duplicates
    carsSet = {"Mustang", "Panda", "Capri", "Jaguar"}
    morecarsSet = {"X5", "Q7", "Panda"}
    carsSet.add("Touareg")
    # Update set with contents of another set, but remove duplicates
    carsSet.update(morecarsSet)
    print(carsSet)
    # Remove an element from a set if it is a member
    carsSet.discard("Porsche")

    #
    # Dictionary {}
    #

    # Create empty dictionarty
    emptyDict = {}

    # Create a dictionary with items of key/value pairs
    carDict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "colour": "light blue",
        "engine": 3000,
        "interior": "walnut"
    }

    # Print a value for a key
    print(carDict["model"])

    # Add a new item
    carDict["topspeed"] = 120
    print("Dictionary length = " + str(len(carDict)))

    # Remove an item
    carDict.pop("interior")

    # Update existing item
    carDict["colour"] = "dark blue"

    # Get lowest and highest keys (only works if all keys of same type)
    lowest = min(carDict)   # Expect "brand"
    highest = max(carDict)   # Expect "year"

    # Check if key in dictionary
    checkKey = "color"
    if checkKey in carDict:
        print("Key Found: ", checkKey)

    # Enumerate dictionary
    for k, v in carDict.items():
        print("Key=", k, "Value=", v)

    # Create a dictionary with multiple values per key.
    def group_by_owners(pfiles):
        # create empty dictionary
        dictResult = {}

        # k, v mapping to v, k
        for key, value in pfiles.items():
            newKey = value
            newValue = key
            dictResult.setdefault(newKey, []).append(newValue)

        return dictResult

    # For given dictionary input, create new dictionary output with multiple values for keys
    files = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
    expected = {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}

    print(group_by_owners(files))

#
# 6. Conditional Statements
#


def fConditional():
    # Python Indentation
    # Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
    # Python uses indentation to indicate a block of code.
    # Recommended indentation = 4 spaces.
    # In the if statement  below, if print... was not idnented it would generate a run-time error

    # If Statement
    conNumber = 23
    if conNumber < 10:
        print("Number is less than 10")
    elif 10 < conNumber <= 50:
        print("Number is between 10 and 50")
    else:
        print("Number is greater than 50 ")

    # While Loop
    i = 1
    while i < 6:
        print(i)
        i += 1
    else:
        print("i is no longer less than 6")

    # For Loop
    numbersum = 0
    numsequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 99, 102, 210]
    for n in numsequence:
        if n == 99:
            break
        elif n % 2 != 0:
            continue
        else:
            numbersum += n
    print(f"Sum of even numbers up to finding 99: {numbersum}")

    numbersum2 = 0
    for l in range(5):
        numbersum2 += l
    print(f"Sum of range(5):{numbersum2}")

#
# 7. Functions
#

# Simple function


def double_number(param1):
    return param1 + param1

# Using a default parameter (param2)


def add_two(param1, param2=0):
    return param1 + param2

# Generator function that uses the yield keyword instead of return


def square_generator():
    sq = 1
    # An Infinite loop to generate squares
    while True:
        yield sq*sq  # function will return from this line and ...
        sq += 1    # on next call will resume from here

# Function with a variable number of arguments


def weather_report(intro, *args):
    report = intro
    for arg in args:
        report += " " + arg
    return report.rstrip()

# Function with a variable number of key word arguments


def person_report(**kwargs):
    person = {}
    for key, value in kwargs.items():
        person[key] = value
    return person


def fFunctions():
    # map() function returns a map object(which is an iterator) of the results after applying the given function to each item
    numbers = [1, 2, 3, 4]
    result1 = map(double_number, numbers)
    # Using lambda as alternative to function name
    result2 = map(lambda x: x * x, numbers)
    print("Result1:", list(result1))
    print("Result2:", tuple(result2))

    # Call function with a default parameter
    z1 = add_two(23, 25)
    z2 = add_two(47)
    print("add_two with 2 params=", z1, "add_two with 1 param", z2)

    # Call generator function
    for num in square_generator():
        if num > 100:
            print()
            break
        print(num, end=' ')

    # Call function with a variable number of arguments
    todays_weather = weather_report(
        "Today the weather is", "sunny", "cloudy", "light rain")
    print(todays_weather)

    # Call function with a variable number of key word arguments
    aPerson = person_report(
        firstName='Tony', surName='Gyles', age=56, city='Basingstoke')

    # Call Lambda Functions
    def add10(a): return a + 10
    print(add10(5))

    def multiplytwo(x, y): return x * y
    print(multiplytwo(6, 9))

#
# 8. Classes
#

# The self parameter is a reference to the current instance of the class
# It does not have to be named self , you can call it whatever you like,
# but it has to be the first parameter of any function in the class:


class Person:
    cancerrisk = 1.2   # Class variable, shared by all instances

    def __init__(self, fname, lname, age):   # Class constructor
        self.firstname = fname
        self.lastname = lname
        self.age = age

    def printname(self):
        print(self.firstname, self.lastname)

    def chanceofcancer(self):
        return(self.age*self.cancerrisk)

    # Class method can change class variables or even instantiate and return an object
    @classmethod
    def cancerrisk_set(cls, risk):
        cls.cancerrisk = risk

    @staticmethod     # Static method using independent data and code
    def check_tall_enough(heightMetres):
        if heightMetres > 1.5:
            return True
        else:
            return False

# class definitions cannot be empty, but if you have not completed it yet use the pass keyword


class Address:
    pass


def fClasses():
    # Create object from class definition
    p1 = Person("John", "Doe", 35)
    p1.printname()
    print("First Name:", p1.firstname, "Last Name:", p1.lastname,
          "Age:", p1.age, "Chance of cancer:", p1.chanceofcancer())

    # Using class method to change class variable
    p2 = Person("Tony", "Gyles", 50)
    p2.cancerrisk_set(2.3)
    print("First Name:", p2.firstname, "Last Name:", p2.lastname,
          "Age:", p2.age, "Chance of cancer:", p2.chanceofcancer())

    # Using static method
    tallEnough = Person.check_tall_enough(1.6)

#
# 9. Inheritance
#

# The super() function that will make the child class inherit all the methods and properties from its parent
# If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.


class Student(Person):
    def __init__(self, fname, lname, age, year):
        super().__init__(fname, lname, age)
        self.graduationyear = year

    def welcome(self):
        print("Welcome ", self.firstname, self.lastname,
              " to the class of ", self.graduationyear)


def fInheritance():
    # Create object from class definition
    s1 = Student("James", "Gyles", 24, 2019)

    # Use properties and methods from parent class
    s1.printname()
    print(s1.firstname)
    print(s1.lastname)
    print(s1.age)

    # Use properties and methods from derived class
    s1.welcome()
    print(s1.graduationyear)

#
# 10. Iterators
#
# Iterable Class
# Must implement methods __iter()__ and __next()__
# StopIteration halts the iteration


class MyNumbers:
    def __init__(self, max_value=0):
        self.max_value = max_value
        self.n = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max_value:
            result = self.n
            self.n += 1
            return result
        else:
            raise StopIteration


def fIterators():
    # An iterator is an object that contains a countable number of values
    # Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__()
    nuts = ("brazil", "hazelnut", "peanut", "walnut")
    nutsIter = iter(nuts)

    print(next(nutsIter))
    print(next(nutsIter))

    print("Instead of next() can use for loop")
    for x in nuts:
        print(x)

    print("A string is iterable")
    for x in "London":
        print(x)

    numbers = MyNumbers(12)
    numbersIter = iter(numbers)

    for x in numbersIter:
        print(x, end=' ')
    print()

#
# 11. Modules
#
# You can choose to import only parts from a module, by using the from keyword e.g. from compute import primeminister


def fModules():
    # Using my own custom module
    print(algorithm.greeting("April"))

    address = algorithm.PRIME_MINISTER["address"]
    print("Prime Minister address = " + address)

#
# 12. Dates (Standard Library)
#


def fDates():
    # A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
    now = datetime.now()
    print(now)
    print(now.year)

    # Format Code List for strftime(). Only sample shown!
    # %A    Full weekly day        (e.g. Sunday)
    # %a    Abbreviated weekly day (e.g. Sun)
    # %B    Full month name        (e.g. December)
    # %c    Locale’s appropriate date and time representation
    print(f"Week Day: {now.strftime('%A')}", )
    print(f"Month: {now.strftime('%B')}")
    print(f"Date/Time: {now.strftime('%c')}")

    # Create my birth date
    mybirthdate = datetime(1963, 12, 29)
    print(f"My birth date: {mybirthdate.strftime('%c')}")

    # timedelta
    print(f"timedelta value: {str(timedelta(days=180,hours=20, minutes=35))}")
    print(
        f"In 2 weeks and 3 days it will be: {str(now + timedelta(weeks=2,days=3))}")

#
# 13. JSON (Standard Library)
#


def fJson():
    #
    # Convert from JSON to Python
    #
    jsonWorker = '{ "name":"John", "age":30, "city":"New York"}'

    # parse json into a dictionary
    dictWorker = json.loads(jsonWorker)

    # the result is a Python dictionary:
    print("Name:", dictWorker["name"])
    print("Age:", dictWorker["age"])
    print("City:", dictWorker["city"])

    #
    # Convert from Python to JSON
    #
    # a Python object (dict):
    dictCityWorker = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    # convert python dict into string with valid JSON
    strCityWorker = json.dumps(dictCityWorker)
    print(strCityWorker)

#
# 14. Regular Expressions (Standard Library)
#


def fRegExp():
    txt = "The rain in Spain"
    listWords = re.findall("ai", txt)
    print("List Words:", listWords)

#
# 15. Try ... Except
#


def fException():
    try:
        numerator = 10
        denominator = 0
        divValue = numerator / denominator
    except ArithmeticError:
        exception_info = sys.exc_info()
        print("Exception during math operation, reported value = ",
              exception_info[1])
    finally:
        print("The 'try except' is finished")

#
# 16. User Input
#


def fUserInput():
    username = input("Enter username:")
    print("Username is: " + username)

#
# 17. Strings
#


def fStrings():
    # Simple string functions
    forename = "Jessica"
    forename_lower = forename.lower()
    forename_upper = forename.upper()
    forename_reverse = forename[::-1]
    forename_replace = forename.replace("ica", "")

    spaced_name = " Freddy the Frog "
    spaced_strip = spaced_name.strip()   # Strip spaces from left and right
    spaced_left_strip = spaced_name.lstrip()  # Strip spaces from left
    spaced_right_strip = spaced_name.rstrip()  # Strip spaces from right

    # Get digits sequence
    digits = string.digits
    print("Digits:", digits)

    # Formatting using a format specification
    quantity = 3
    itemno = 567
    price = 49
    # :.2f = #:(fieldwidth).(precision)fixed point
    myorder = "I want {} pieces of item number {} for £{:.2f}."
    print(myorder.format(quantity, itemno, price))

    # f-strings
    amount = 450
    orderid = 6281718
    orderMessage = f"Hello, Your order {orderid} for the amount {amount} is complete."
    print(orderMessage)

#
# 18. File Handling and OS module
#


def fFiles():
    # setup
    NEW_FILE = "temp/newfile.txt"
    PICKLE_FILE = "temp/emp1.pkl"

    # Create new file/delete if exists
    filename = NEW_FILE
    if os.path.exists(filename):
        os.remove(filename)
    f1 = open(filename, "x", encoding="utf-8")

    # Write string to a text file
    # Open file for writing in text mode (which is default mode)
    f2 = open(filename, "w", encoding="utf-8")
    f2.write("Its the end of the world 2020!")
    f2.close()

    # Write list to text file
    contentList = ["Overwatch 10/10\n", "Gwent 9/10\n", "Borderlands 3 8/10\n"]
    filenameGames = "temp/MyBestGames.txt"
    f4 = open(filenameGames, 'w', encoding="utf-8")
    f4.writelines(contentList)
    f4.close()

    # Read text file into a list
    f4 = open(filenameGames, 'r', encoding="utf-8")
    Lines = f4.readlines()             # Read all lines into a list

    for line in Lines:
        strippedLine = line.strip()
        print(strippedLine)

    # Write dictionary and list to file (Pickling)
    people = ["john doe", "andrew webber", "terry hart"]
    clanguages = {"Python": 3.7, "C#": 8, "Java": 13}
    # Open file for writing in binary mode
    pickle_file = open(PICKLE_FILE, "wb")
    pickle.dump(people, pickle_file)
    pickle.dump(clanguages, pickle_file)
    pickle_file.close()

    # Read dictionary and list from file (Unpickling)
    # Open file for reading in binary mode
    pickle_file = open(PICKLE_FILE, 'rb')
    people_list = pickle.load(pickle_file)
    clanguages_dict = pickle.load(pickle_file)
    print(f"Unpickle list: {people_list}")
    print(f"Unpickle languages: {clanguages_dict}")
    pickle_file.close()

#
# 19. Logging
#


def fLogging():
    # Setup
    LOG_FILE = "temp/evaluatepython.log"

    # If you do not set a file then logging will go to console
    # The log level determines what gets output.
    # Log levels are highest to lowest ["CRITICAL","ERROR","WARNING","INFO","DEBUG"]
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO, filemode='w')
    logging.debug('This message will not go to the log file')
    logging.info('This will be logged')
    logging.warning('And this, too')

#
# 20. Threading
#


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None, args=None, kwargs=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, timeout=None):
        Thread.join(self, timeout)
        return self._return


def fThreading():
    # To get return value from function called by Thread , must use this helper class
    inputValue = 2450.0
    thread1 = ThreadWithReturnValue(
        target=algorithm.square_root, args=(inputValue,))
    thread1.start()
    result1 = thread1.join()
    logging.info("Square root of %s = %s", str(
        inputValue), str(round(result1, 4)))

#
# 21. Collections
#


def fAdvancedCollections():
    #
    # Counter - It keeps a count of the number of occurrences of any value in the container (subclass of dictionary)
    #

    # Create counter
    counter = Counter(['a', 'b', 'c', 'a', 'b', 'a'])

    # Create dictionary from counter
    dictCounter = dict(counter)

    # loop counter
    for i in counter.elements():
        print(f"{i}: {counter[i]}")

    # get most common
    common = counter.most_common(2)

    #
    # Deque - Double-ended queue. Can add or remove items from both ends
    #

    # Create and append string to left and right
    deq = deque("Google")
    deq.appendleft("Hello ")
    deq.append("from Tony")
    print(deq)

    #
    # Ordered Dictionary - A dictionary that preserves order of items added to dictionary
    #

    # Create ordered dictionary
    od = OrderedDict()
    od['a'] = 'SAS'
    od['b'] = 'PYTHON'
    od['c'] = 'R'

    for k, v in od.items():
        print(k, ":", v)

#
# 22. Tests
#


def fTests():
    algorithm.fizzbuzz(100)

    algorithm.FibonacciSequence(10)

#
# 23. PIP (Package Manager for Python)
#


def fPip():
    # Install package "numpy" using PIP from PyPI
    a = np.array([20, 30, 40, 50])
    b = np.arange(4)
    c = a-b
    bsquared = b**2

    print("Array Subtraction: ", c)
    print("Array Squared: ", bsquared)
    print("Array Element Compare < 35: ", a < 35)

#
# 24. Decorators
#  A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.
#  Decorators are usually called before the definition of a function you want to decorate.
#


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator
def say_hi():
    return 'hello there'


def fDecorators():
    print("Uppercase Decorator result: ", say_hi())

#
# 25. Internet Protocols and Support (Standard Library)
#


def fInternetProtocols():
    # Create a v4 uuid
    myuuid = uuid.uuid4()

    print('Your UUID is: ' + str(myuuid))


#
# Main Entry Point
#
def main():
    fSetup()
    fOutput()
    fVariables()
    fDataTypes()
    fOperators()
    fCollections()
    fConditional()
    fFunctions()
    fClasses()
    fInheritance()
    fIterators()
    fModules()
    fDates()
    fJson()
    fRegExp()
    fException()
    fUserInput()
    fStrings()
    fFiles()
    fLogging()
    fThreading()
    fAdvancedCollections()
    fTests()
    fPip()
    fDecorators()
    fInternetProtocols()


#
# If this run as startup file, the if statement is true and the main() is called.
#
if __name__ == '__main__':
    main()
