
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
    """두 수를 나눕니다. 0으로 나누는 경우 에러 메시지를 반환합니다."""
    if y == 0:
        return "오류: 0으로 나눌 수 없습니다."
    return x / y

if __name__ == "__main__":
    try:
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))

        print(f"\n--- 계산 결과 ---")
        print(f"{num1} + {num2} = {add(num1, num2)}")
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
        
        division_result = divide(num1, num2)
        print(f"{num1} / {num2} = {division_result}")

    except ValueError:
        print("오류: 유효한 숫자를 입력해주세요.")
    except Exception as e:
        print(f"예상치 못한 오류가 발생했습니다: {e}")
