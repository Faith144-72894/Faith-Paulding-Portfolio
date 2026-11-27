import pytest
from app import *

def test_case_1():
    assert evaluate({'ev':80,'pv':100,'ac':100,'bac':200})['eac']==250

def test_case_2():
    assert evaluate({'ev':0,'pv':0,'ac':0,'bac':200})['eac'] is None

def test_case_3():
    with pytest.raises(ValueError):
        evaluate({'ev':-1,'pv':100,'ac':100,'bac':200})

