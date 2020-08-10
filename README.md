# Session 4 - Numeric Types
# EPAi session4 assignment

#### Numeric Type - II

Integers, Constructors, Bases, Rational Numbers, Floats, rounding, Coercing to Integers and equality

#### Objective of Assignment:

Write a Qualean class that is inspired by Boolean+Quantum concepts. We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state. The moment you assign it a real number, it immediately finds an imaginary number random.uniform(-1, 1) and multiplies with it and stores that number internally after using Bankers rounding to 10th decimal place. 

Implement the below functions:

    #'__and__' - performs and operation between the given values
    #'__or__', - performs or operation between the given values
    #'__repr__', - returns the string represent of the input Qualean value
    #'__str__', - returns the string represent of the input Qualean value
    #'__add__', - adds the 2 numbers and returns the sum
    #'__eq__', -  check if 2 numbers are equal 
    #'__float__', - returns the float representation of the Qualean value
    #'__ge__',  - returns if the value is greater than equal to the value being compared with
    #'__gt__', - returns if the value is greater than the value being compared with
    #'__invertsign__', - returns the value with the opposite sign(if +ve then it returns -ve of the value and vice versa) 
    #'__le__', - returns if the value is less than equal to the value being compared with
    #'__lt__', - returns if the value is less than the value being compared with
    #'__mul__', - returns the product of the 2 values
    #'__sqrt__', - returns the square root of the value
    #'__bool__'  - checks if the value is not zero


Written a test file, that tests all of the functions mentioned above + the other basic ones we have seen in the previous tests till now. Your unit test file must contain at least 25 tests, and they must not be repetitive. Some of the tests it must implement are:
1. q + q + q ... 100 times = 100 * q
2. q.__sqrt__() = Decimal(q).sqrt
3. sum of 1 million different qs is very close to zero (use isclose)
4. q1 and q2 returns False when q2 is not defined as well and q1 is False
5. q1 or q2 returns True when q2 is not defined as well and q1 is not false