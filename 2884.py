h, m=map(int, input().split())

time = h * 60 + m - 45
if time < 0:
  print(23, 60+time)
else:
  print(time//60, time%60)
