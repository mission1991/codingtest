# 첫 번째 인자를 기준으로 두 번째 인자의 중복 된 값 제거

def sol(first, second):
	first_set =  set(first.split(','))
	second_set = set(second.split(','))
	comma = first_set & second_set
	return ','.join(sorted(comma))


print(sol("one,two,three,four,five,five,one,six", "one,two,five,the,six"))