fizzbuzz = [input().strip() for _ in range(3)]

# 마지막 숫자 찾기 (Fizz, Buzz, FizzBuzz는 숫자가 아님)
last_number = None
for i in reversed(fizzbuzz):
    if i.isdigit():
        last_number = int(i)
        break

# 만약 숫자가 있었다면 그 숫자의 다음 값 사용
if last_number is not None:
    next_number = last_number + 1
else:
    # 숫자가 없었다면, 가장 마지막 값이 Fizz, Buzz, FizzBuzz 중 하나일 것
    first_number = None
    for i in fizzbuzz:
        if i.isdigit():
            first_number = int(i)
            break

    next_number = first_number + fizzbuzz.index("FizzBuzz") + 1

# FizzBuzz 규칙 적용
if next_number % 3 == 0 and next_number % 5 == 0:
    print("FizzBuzz")
elif next_number % 3 == 0:
    print("Fizz")
elif next_number % 5 == 0:
    print("Buzz")
else:
    print(next_number)
