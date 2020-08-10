import pytest
import random
import string
import session4
import os
import decimal
from decimal import Decimal
import cmath
import inspect
import re
import math

README_CONTENT_CHECK_FOR = [
        '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__'
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 300, "Make your README.md file interesting! Add atleast 300 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_add_100_times():
    tot_sum = Decimal('0')
    q = Decimal(str(session4.Qualean(1)))
    for _ in range(100):
        tot_sum += q
    assert tot_sum == 100 * q, "q + q + ... 100 times is not equal to 100 * q"

def test_sqrt_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        q = session4.Qualean(val)
        assert (q.__sqrt__()) == cmath.sqrt(q), f"sqrt is not working"

def test_decimalsqrt_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        q = session4.Qualean(val)
        sqrt_complex_num = q.__sqrt__()
        sqrt_fun = round(Decimal(sqrt_complex_num.real),10)
        if(sqrt_complex_num.real>0):
            decimal_sqrt = round(q.__decimal__().sqrt(),10)
            assert (sqrt_fun) == decimal_sqrt, f"sqrt decimal precision not matching!"

def test_sum_million():
    result = 0
    # f_num = random.randint(1, 10)
    # g_num = random.randint(1, 20)
    for i in range(1000000):
        val = random.choice([1,0,-1])
        q = session4.Qualean(val)
        result += q.im_num
    assert math.isclose(result, 0, abs_tol=1000), 'q+q+q... is not equal to n*q'


def test_and_short_circuit():
    q1 = session4.Qualean(0)
    result = q1 and q2
    assert not result, 'Expected to result in False when q1 is false and q2 undefined'

def test_or_short_circuit():
    q1 = session4.Qualean(1)
    result = q1 or q2
    assert result, 'Expected to result in True when q1 is true and q2 undefined'

def test_or_short_circuit():
    for i in range(50):
        value = random.choice([-1,0,1])
        q1 = session4.Qualean(value)
        q2 = session4.Qualean(value)
        if bool(q1) == True:
            assert (q1.__or__(q2)) == True, f"Your program returned wrong or"
            assert (q1.__or__()) == True, f"Your program returned wrong or"
            assert (q1.__and__()) == False, f"Q2 not defined"
        else:
            assert (q1.__or__()) == False, f"Q2 not defined"
            assert (q1.__and__(q2)) == False, f"Your program returned wrong and"
            assert (q1.__and__()) == False, f"Your program returned wrong and"


def test_bool_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        q = session4.Qualean(val)
        assert (q.__bool__()) == bool(q), f"Your program returned wrong bool"

def test_float_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        q = session4.Qualean(val)
        assert (type(q.__float__())) == float, f"Your program returned wrong float conversion"

def test_mul_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        q1 = session4.Qualean(val)
        q2 = session4.Qualean(val)
        assert (q1.__mul__(q2)) == q1*q2, f"Your program returned wrong multiplication"

def test_lt_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        q1 = session4.Qualean(val)
        q2 = session4.Qualean(val)
        assert (q1.__lt__(q2)) == (q1<q2), f"Your program returned wrong < comparison"

def test_lte_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        q1 = session4.Qualean(val)
        q2 = session4.Qualean(val)
        assert (q1.__le__(q2)) == (q1<=q2), f"Your program returned wrong <= comparison"

def test_gt_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        q1 = session4.Qualean(val)
        q2 = session4.Qualean(val)
        assert (q1.__gt__(q2)) == (q1>q2), f"Your program returned wrong > comparison"

def test_gte_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        q1 = session4.Qualean(val)
        q2 = session4.Qualean(val)
        assert (q1.__ge__(q2)) == (q1>=q2), f"Your program returned wrong >= comparison"

def test_eq_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        q1 = session4.Qualean(val)
        q2 = session4.Qualean(val)
        assert (q1.__eq__(q2)) == (q1==q2), f"Your program returned wrong == comparison"

def test_invert_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        q = session4.Qualean(val)
        assert (q.__invertsign__()) == -q.im_num, f"wrong inverst sign"

def test_class_methods():
    val = random.choice([1,0,-1])
    q = session4.Qualean(val)
    for i in README_CONTENT_CHECK_FOR:
        assert i in dir(q), 'All defined functions not used!'

def test_class_repr():
    q = session4.Qualean(1)
    assert 'object at' not in q.__repr__()

def test_class_str():
    q = session4.Qualean(1)
    assert 'object at' not in q.__str__()

def test_invalid_input_value():
    with pytest.raises(ValueError):
        session4.Qualean(-10)
    with pytest.raises(ValueError):
        session4.Qualean(Decimal(1.5))
    with pytest.raises(ValueError):
        session4.Qualean(0.1)



