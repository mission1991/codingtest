'''
디지털 시계에 하루동안(00:00~23:59) 3이 표시되는 시간을 초로 환산하면 총 몇 초(second) 일까요?
디지털 시계는 하루동안 다음과 같이 시:분(00:00~23:59)으로 표시됩니다.
00:00 (60초간 표시됨)
00:01
00:02
...
23:59
'''


hour = 24
min = 60
second = 0

for h in range(hour):
    for m in range(min):
        if "3" in str(h) or "3" in str(m):
            second += 60

print(second)