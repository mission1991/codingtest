'''
파이썬과 같은 몇몇 프로그래밍 언어는 Pothole_case 를 더 선호하는 언어라고 합니다.

Example:
codingDjango --> coding_django
numGoat30 --> num_goat_3_0
위 보기와 같이 CameleCase를 Pothole_case 로 바꾸는 함수를 만들어요!
'''

catxt = 'codingDjango3'
potxt = ''

for i in catxt:
    if i.isupper() or i.isdigit():
        potxt += '_' + i.lower()
    else:
        potxt += i

print(potxt)

