from day5 import naughty_or_nice

def test_1():
    assert naughty_or_nice(["qjhvhtzxzqqjkmpb"]) == 1


def test_2():
    assert naughty_or_nice(["uurcxstgmygtbstg"]) == 0


def test_3():
    assert naughty_or_nice(["ieodomkazucvgmuy"]) == 0

def test_4():
    assert naughty_or_nice(["ykriratovsvxxasf"]) == 0

def test_5():
    assert naughty_or_nice(["aaavrv"]) == 0

def test_6():
    assert naughty_or_nice(["uurcxstgmygtbstg", "ieodomkazucvgmuy", "zgsnvdmlfuplrubt"]) == 0


def test_7():
    assert naughty_or_nice(["urrvucyrzzzooxhx"]) == 0