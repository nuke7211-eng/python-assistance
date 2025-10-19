import argparse

def add(x, y):
    """두 수를 더합니다."""
    return x + y

def subtract(x, y):
    """두 수를 뺍니다."""
    return x - y

def multiply(x, y):
    """두 수를 곱합니다."""
    return x * y

def divide(x, y):
    """두 수를 나눕니다."""
    if y == 0:
        return "오류: 0으로 나눌 수 없습니다."
    return x / y

def main():
    """계산기 메인 함수 (명령줄 인수 사용)"""
    parser = argparse.ArgumentParser(description="간단한 계산기 프로그램. 두 숫자와 연산을 지정합니다.")
    parser.add_argument("num1", type=float, help="첫 번째 숫자")
    parser.add_argument("num2", type=float, help="두 번째 숫자")
    parser.add_argument("-o", "--operation", type=str, required=True,
                        choices=['add', 'subtract', 'multiply', 'divide'],
                        help="수행할 연산 (add, subtract, multiply, divide)")

    args = parser.parse_args()

    result = None
    if args.operation == 'add':
        result = add(args.num1, args.num2)
    elif args.operation == 'subtract':
        result = subtract(args.num1, args.num2)
    elif args.operation == 'multiply':
        result = multiply(args.num1, args.num2)
    elif args.operation == 'divide':
        result = divide(args.num1, args.num2)

    print(f"결과: {result}")

if __name__ == "__main__":
    main()
