AB = input()
if AB == "1010":
    A, B = 10, 10
elif AB[:2] == '10':
    A, B = 10, int(AB[2])
elif AB[-2:] == '10':
    A, B = int(AB[0]), 10
else:
    A, B = int(AB[0]),int(AB[1])
print(A+B)
