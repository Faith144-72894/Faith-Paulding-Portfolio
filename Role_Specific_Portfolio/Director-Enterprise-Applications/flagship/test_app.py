import pytest
from app import *

def test_case_1():
    assert evaluate({'id':'X','amount':10000})['state']=='review'

def test_case_2():
    assert evaluate({'id':'X','amount':9999})['state']=='approved'

def test_case_3():
    assert evaluate({'id':'X','amount':'bad'})['status']==400

def test_case_4():
    assert evaluate({'amount':1})['status']==400

