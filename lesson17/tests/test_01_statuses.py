import pytest
import random
import time


def test_success():
    """this test succeeds"""
    time.sleep(random.randint(0, 3))
    assert True


def test_failure():
    """this test fails"""
    time.sleep(1)
    assert False


def test_skip():
    time.sleep(2)
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    time.sleep(3)
    raise Exception('bye-bye')


def test_outdated():
    with open('not_found') as f:
        f.readline()


@pytest.mark.flaky(reruns=2)
def test_flaky():
    """this test is flaky"""
    import random
    assert random.choice([True, False])
