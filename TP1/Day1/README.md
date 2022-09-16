# 팔로워🏃‍♂️

팀원: 나연 강, 자현 구, 지현 김, 상우 박, 혜민 박, 이선오
팀장: 권태윤

### 각자 오늘 배운 내용을 정리해볼까요? (**T**oday **I** **L**earned)

| 강나연 | 반복문과 딕셔너리, 집합, 리스트 활용하여 간단한 메뉴결정, 이상형 알아보기 프로그램 개발 |
| --- | --- |
| 박혜민 | 파이썬 기본 개념(ch2-list와 dictionary, 반복, 집합, if문) |
| 박상우 | for문 while문, 딕셔너리, 리스트, 집합 등 간단한 파이썬 기초 문법을 사용하여 “오늘은 뭐 드실?” 이라는 미니 프로덕트를 완성하였다. |
| 이선오 | IF문, while True를 활용한 반복문, break, list, set 등의 파이썬 문법을 배웠고 문법을 활용해 간단한 프로덕트를 구현했습니다.  |
| 구자현 | 딕셔너리, 리스트, 집합 자료형 각각의 특징과 차이점을 알았고 이를 이용하여 동일한 기능을 여러 자료형을 이용하여 구현했다. |
| 권태윤 |  |
| 김지현 | 리스트, 딕셔너리, 집합 등 파이썬 언어의 기본적인 형태와 반복문(for,while), if문, input 구문을 활용해 값을 삭제하고 추가하는 법을 배웠습니다. |

### 프로젝트 결과물을 보여주세요.

- 메뉴 자판기

```python
import random
import time

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]

while True:
    print(lunch)
    item = input("음식을 추가 해주세요 : (완료 : q)")
    if(item == "q"):
        break
    else:
        lunch.append(item)
print(lunch)

set_lunch = set(lunch)
while True:
    print(set_lunch)
    item = input("음식을 삭제해주세요 : (완료 : q)")
    if(item == "q"):
        break
    else:
        set_lunch = set_lunch - set([item])

print(set_lunch, "중에서 선택합니다.")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print(random.choice(list(set_lunch)))
```

- 익명 질문 게시판

```python
total_list = []

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_list.append({"질문" : question, "답변" : ""})

for i in total_list:
    print(i["질문"])
    answer = input("답변을 입력해주세요 : ")
    i["답변"] = answer
print(total_list)
```

### 오늘 배운 내용에 대해서 조금 더 알고 싶은데, 참고할 만한 자료는 뭐가 있을까요?

나연: 프로그래머스에서 이 문제 풀어보심 좋을듯 해요~ 추천추천

[https://school.programmers.co.kr/learn/courses/30/lessons/12928](https://school.programmers.co.kr/learn/courses/30/lessons/12928)

### 오늘 배운 내용을 앞으로 어디에 어떻게 적용할 수 있을까요?

나연: 여행사에서 마케팅 일환으로 여행지 추천 프로그램을 만들 수 있을거 같습니다.

선오 : 파이썬 문법을 이용해 다른 프로덕트를 만들어볼 수 있을 것 같습니다. 

상우: 친구들하고 밥먹기 수월해질 것 같다.

지현: 프로젝트 할 때 기본 파이썬 구문을 어렵지 않게 구현할 수 있을 것 같습니다.

자현 : random 모듈을 이용해 확률 게임을 만들어 볼 수 있을 것 같다.

혜민: 게임에서 보유한 재화로 구매할 수 있는 아이템 추천?