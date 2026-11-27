import pytest
from app import *

def test_case_1():
    assert evaluate({'classification':'restricted','approved':True})['route']=='deny'

def test_case_2():
    assert evaluate({'classification':'unknown','approved':True})['route']=='deny'

def test_case_3():
    assert evaluate({'classification':'public','approved':'yes'})['route']=='deny'

def test_case_4():
    assert evaluate({'classification':'internal','approved':True})['route']=='approved endpoint'

