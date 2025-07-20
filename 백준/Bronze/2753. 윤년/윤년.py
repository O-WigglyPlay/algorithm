# 윤년 계산하는 방법
# 4로 나누어 떨어지면 윤년 하지만 100으로 나누어떨어지면 평년, 400으로 나누어 떨어지면 다시 윤년이 된다.

year = int(input())

if ((year%4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
  print("1")
else:
  print("0")