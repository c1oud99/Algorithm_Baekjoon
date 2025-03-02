fizzbuzz = [input().strip() for _ in range(3)]

last_number = None
for i in reversed(fizzbuzz):
    if i.isdigit():
        last_number = int(i)
        break

if last_number is not None:
    next_number = last_number + 1
else:
    first_number = None
    for i in fizzbuzz:
        if i.isdigit():
            first_number = int(i)
            break

    next_number = first_number + fizzbuzz.index("FizzBuzz") + 1

if next_number % 3 == 0 and next_number % 5 == 0:
    print("FizzBuzz")
elif next_number % 3 == 0:
    print("Fizz")
elif next_number % 5 == 0:
    print("Buzz")
else:
    print(next_number)
