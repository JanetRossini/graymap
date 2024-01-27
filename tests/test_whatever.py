import pytest


class TestMore:
    def test_hookup(self):
        assert 3 + 1 == 4

    def test_another_thing(self):
        assert 2*2 == 4


def test_free_hookup():
    assert 4*5 == 20
