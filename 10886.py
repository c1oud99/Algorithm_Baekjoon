N = int(input())
votes = [int(input()) for _ in range(N)]
cute = votes.count(1)
not_cute = N - cute

if cute > not_cute:
    print('Junhee is cute!')
elif cute < not_cute:
    print('Junhee is not cute!')
