import pytest


class TestMore:
    def test_hookup(self):
        assert 2 + 1 == 4

    def test_another_thing(self):
        assert 2*3 == 4


def test_free_hookup():
    assert 2*5 == 20
