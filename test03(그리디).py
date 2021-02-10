'''
당신은 음식점의 계산을 도와주는 점원입니다.  카운터에는 거스름돈으로
사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정합니다.
손님에게 거슬러 주어야 할 돈이 N원일 때 거슬러 주어야 할 최소 개수를 구하세요.
단, 거슬러 줘야 할 돈 N은 항상 10의 배수입니다.
'''

N = int(input())
count = 0

# 큰 단위의 화폐부터  차례대로 확인하기
coins = [500, 100, 50, 10]

for coin in coins:
    count += N // coin # 해당 화폐로 거슬루 줄 수 있는 동전의 개수 세기
    N %= coin
print(count)


