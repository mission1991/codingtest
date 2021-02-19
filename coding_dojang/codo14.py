'''
사다리 게임

input:
a b c d e f
| | | | | |
|-| | |-| |
| | |-| | |
| |-| | |-|
| | |-| | |
|-| | |-| |
| | | | | |
1 2 3 4 5 6

output:
a - 5
b - 2
c - 3
d - 6
e - 1
f - 4
'''

data = '''a b c d e f
| | | | | |
|-| | |-| |
| | |-| | |
| |-| | |-|
| | |-| | |
|-| | |-| |
| | | | | |
1 2 3 4 5 6'''
a = data.split('\n')
b = a[0].split()
c = a[-1].split()

for i in a[1:-1]:
    for j, k in enumerate(i.split('|')):
        if k == '-':
            c[j - 1], c[j] = c[j], c[j - 1]
for d1, d2 in zip(b, c):
    print(d1, '-', d2)
