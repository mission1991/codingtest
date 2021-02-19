''' 별파티!!
---------- 1
*
**
***
****
*****
******
---------- 2
******
*****
****
***
**
*
---------- 3
     *
    **
   ***
  ****
 *****
******
---------- 4
   *
  ***
 *****
*******
---------- 5
   *
  ***
 *****
*******
 *****
  ***
   *
'''
n = int(input())

for i in range(1, n):
    print(i * '*')


for i in range(n, 0, -1):
    print(i * '*')


for i in range(1, n):
    for j in range(n - i):  # n수 부터 줄어듦
        print(' ', end='')
    for j in range(i):  # n수 부터 늘어남
        print('*', end='')
    print()


for i in range(1, n):
    for j in range(n - i):
        print(' ', end='')
    for j in range(2 * i -1):
        print('*', end='')
    print()

y = int(input("마름모 홀수로 입력 : "))
x = int(y / 2) + 1
print(x)
for i in range(1, 2 * x):
    if i <= x:
        for j in range(x - i):
            print(' ', end='')
        for j in range(2 * i - 1):
            print('*', end='')
        print()
    else:
        for j in range(i - x):
            print(' ', end='')
        for j in range((2 * x - i) * 2 - 1):
            print('*', end='')
        print()