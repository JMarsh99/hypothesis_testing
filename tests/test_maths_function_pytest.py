import pytest
from project.complicated_maths_functions import (
    run_complicated_maths_function_1,
    run_complicated_maths_function_2,
    run_complicated_maths_function_3,
    run_complicated_maths_function_4
)


@pytest.mark.parametrize(
    'numbers',
    [
        [1, 82.67, 1000, 10000],
        [123.123, -12, -18.2, -193],
        [0, 1000000000000000000, 9999999.99999, 10101010]
    ]
)
def test_run_complicated_maths_function_1(numbers):
    a, b, c, d = numbers
    run_complicated_maths_function_1(a, b, c, d)


@pytest.mark.parametrize(
    'numbers',
    [
        [1, 82.67, 1000, 10000],
        [123.123, -12, -18.2, -193],
        [0, 1000000000000000000, 9999999.99999, 10101010]
    ]
)
def test_run_complicated_maths_function_2(numbers):
    a, b, c, d = numbers
    run_complicated_maths_function_2(a, b, c, d)


@pytest.mark.parametrize(
    'numbers',
    [
        [1, 82.67, 1000, 10000],
        [123.123, -12, -18.2, -193],
        [0, 1000000000000000000, 9999999.99999, 10101010]
    ]
)
def test_run_complicated_maths_function_3(numbers):
    a, b, c, d = numbers
    run_complicated_maths_function_3(a, b, c, d)


@pytest.mark.parametrize(
    'numbers',
    [
        [1, 82.67, 1000, 10000],
        [123.123, -12, -18.2, -193],
        [0, 1000000000000000000, 9999999.99999, 10101010]
    ]
)
def test_run_complicated_maths_function_4(numbers):
    a, b, c, d = numbers
    run_complicated_maths_function_4(a, b, c, d)
