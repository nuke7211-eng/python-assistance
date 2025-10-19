
import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    """덧셈 함수 테스트"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
    assert add(0, 0) == 0

def test_subtract():
    """뺄셈 함수 테스트"""
    assert subtract(10, 5) == 5
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0
    assert subtract(5, 10) == -5

def test_multiply():
    """곱셈 함수 테스트"""
    assert multiply(3, 4) == 12
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1
    assert multiply(10, 0) == 0

def test_divide():
    """나눗셈 함수 테스트"""
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5
    assert divide(5, 2) == 2.5
    # 0으로 나누는 경우 테스트
    assert divide(10, 0) == "오류: 0으로 나눌 수 없습니다."
