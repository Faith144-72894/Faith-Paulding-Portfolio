import pytest
from app import *

def test_case_1():
    assert evaluate({'tasks':{'A':{'days':3,'deps':[]},'B':{'days':5,'deps':['A']}}})['critical_path']==['A','B']

def test_case_2():
    with pytest.raises(ValueError):
        evaluate({'tasks':{'A':{'days':1,'deps':['A']}}})

def test_case_3():
    with pytest.raises(ValueError):
        evaluate({'tasks':{'A':{'days':1,'deps':['B']}}})

