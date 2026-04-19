import pytest


@pytest.fixture
def moja_kolekcja():
    return [1, 3, 2]


def test_1(moja_kolekcja):
    assert moja_kolekcja == [1, 3, 2]

def test_2(moja_kolekcja):
    moja_kolekcja.sort()
    assert moja_kolekcja == [1, 2, 3]

def test_3(moja_kolekcja):
    assert moja_kolekcja == [1, 3, 2]