import pytest
from app import split_integer


# Test 1
@pytest.mark.parametrize(
    "val, num, result",
    [
        (2, 2, 2),
        (3, 3, 3),
        (4, 2, 4),
        (6, 3, 6),
        (17, 7, 17),
        (31, 11, 31),
        (100, 9, 100),
    ],
)
def test_sum_of_the_parts_should_be_equal_to_value(
    val: int, num: int, result: int
) -> None:
    assert (
        sum(split_integer.split_integer(val, num)) == result
    ), f"Sum of the parts should be equal to {result}, but it isn't"


# Test 2
@pytest.mark.parametrize(
    "val, num, result",
    [
        (2, 2, [1, 1]),
        (3, 3, [1, 1, 1]),
        (4, 2, [2, 2]),
        (6, 3, [2, 2, 2]),
        (8, 4, [2, 2, 2, 2]),
        (9, 3, [3, 3, 3]),
        (10, 5, [2, 2, 2, 2, 2]),
        (12, 6, [2, 2, 2, 2, 2, 2]),
    ],
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    val: int, num: int, result: list
) -> None:
    assert (
        split_integer.split_integer(val, num) == result
    ), f"Function should split {val} into {num} equal parts, but it doesn't"


# Test 3
@pytest.mark.parametrize(
    "val, num, result",
    [
        (5, 1, [5]),
        (11, 1, [11]),
        (17, 1, [17]),
        (31, 1, [31]),
        (100, 1, [100]),
    ],
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
    val: int, num: int, result: list
) -> None:
    assert (
        split_integer.split_integer(val, num) == result
    ), f"Function should return {result} when {val} is split into one part, but it doesn't"


# Test 4
@pytest.mark.parametrize(
    "val, num, result",
    [
        (5, 2, [2, 3]),
        (11, 3, [3, 4, 4]),
        (17, 4, [4, 4, 4, 5]),
        (31, 5, [6, 6, 6, 6, 7]),
        (100, 9, [11, 11, 11, 11, 11, 11, 11, 11, 12]),
    ],
)
def test_parts_should_be_sorted_when_they_are_not_equal(
    val: int, num: int, result: list
) -> None:
    assert (
        split_integer.split_integer(val, num) == result
    ), f"Function should return {result} when {val} is split into {num} parts, but it doesn't"


# Test 5
@pytest.mark.parametrize(
    "val, num, result",
    [
        (1, 3, [0, 0, 1]),
        (2, 5, [0, 0, 0, 1, 1]),
        (5, 10, [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]),
        (7, 12, [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]),
        (10, 15, [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
    ],
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    val: int, num: int, result: list
) -> None:
    assert (
        split_integer.split_integer(val, num) == result
    ), f"Function should return {result} when {val} is split into {num} parts, but it doesn't"
