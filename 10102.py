V = int(input())
vote = input()
A = vote.count('A')
B = vote.count('B')
if A == B:
    print('Tie')
elif A > B:
    print('A')
else:
    print('B')