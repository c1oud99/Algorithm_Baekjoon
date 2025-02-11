N = int(input())
members = []

for i in range(N):
    age, name = input().split()
    age = int(age)
    members.append((age, name, i))

members.sort(key=lambda member: (member[0], member[2]))

for member in members:
        print(member[0], member[1])