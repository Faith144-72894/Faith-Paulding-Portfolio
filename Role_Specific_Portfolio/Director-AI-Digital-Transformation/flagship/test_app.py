import pytest
from app import *

def test_case_1():
    assert evaluate({'hours':100,'rate':10,'adoption':.5,'cost':1000})['roi']==-.5

def test_case_2():
    with pytest.raises(ValueError):
        evaluate({'hours':100,'rate':10,'adoption':2,'cost':1000})

def test_case_3():
    with pytest.raises(ValueError):
        evaluate({'hours':100,'rate':10,'adoption':.5,'cost':0})

