# 로또 번호 선택
import random

count = int(input("몇장을 구매하시겠습니까? : "))

for _ in range(count):
    lotto = sorted(random.sample(range(1, 46), 6))
    print(lotto)

# 줄 바꿔 출력하기
for i in range(1, 31):
    print(i, end='\t')
    if i % 10 == 0:
        print()

# 별 찍기
for _ in range(5):
    print("*" * 5)