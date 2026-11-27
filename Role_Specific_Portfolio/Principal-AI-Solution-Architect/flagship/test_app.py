import pytest
from app import *

def test_case_1():
    assert evaluate({'query':'leave'})['source']=='P01'

def test_case_2():
    assert evaluate({'query':'unknown'})['source'] is None

def test_case_3():
    assert evaluate({'query':'leave expenses'})['source'] is None

def test_case_4():
    with pytest.raises(ValueError):
        evaluate({'query':' '})

