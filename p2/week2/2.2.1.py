import datetime

dateparams = [int(i) for i in input().split()]
days = int(input())

d = datetime.date(*dateparams)
delta = datetime.timedelta(days)
ans = d + delta
print(ans.year, ans.month, ans.day)