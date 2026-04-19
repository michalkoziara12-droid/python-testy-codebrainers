# zły kod
import pytest

moja_kolekcja = [1, 3, 2]





def test_1():  # Added missing function definition
    assert moja_kolekcja == [1, 2, 3]

def test_2():
    moja_kolekcja.sort()
    assert moja_kolekcja == [1, 2, 3]

def test_3():
    assert moja_kolekcja == [1, 3, 2]
def test_4():    moja_kolekcja.sort()
    assert moja_kolekcja == [1, 2, 3]

def test_5():
    assert moja_kolekcja == [1, 3, 2]