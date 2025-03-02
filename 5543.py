hamburger = [int(input()) for _ in range(3)]
drink = [int(input()) for _ in range(2)]
print(min(h + d - 50 for h in hamburger for d in drink))