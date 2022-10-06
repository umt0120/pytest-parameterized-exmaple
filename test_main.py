from main import func
import pytest

def test_func() -> None:
    assert func(3) == 4


@pytest.mark.parametrize("input,expected", [(3, 4), (5, 6), (-1, 0)])
def test_func_parametrize(input: int, expected: int) -> None:
    assert func(input) == expected

@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input: str, expected: int):
    assert eval(test_input) == expected