from day6 import lets_light

def test_1():
    assert lets_light(["turn on 0,0 through 999,999"]) == 1000000


def test_2():
    assert lets_light(["turn off 499,499 through 500,500"]) == 0


def test_3():
    assert lets_light(["turn on 498,499 through 500,500","turn off 499,499 through 500,500"]) == 2