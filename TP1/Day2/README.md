# 팔로워 🏃‍♂️ (오전)

팀원: 나연 강, 자현 구, 지현 김, 상우 박, 혜민 박, 이선오
팀장: 권태윤

### 각자 오늘 배운 내용을 정리해볼까요? (**T**oday **I** **L**earned)

| 이름 | **T**oday **I** **L**earned |
| --- | --- |
| 박혜민 | Ch2. 형변환(int), 리스트(append, insert, del, remove, len, sum, max, min), 딕셔너리/ Ch3. if문(if+list, if+dict) |
| 박상우 | 정수형 자료료 변환하는 int(), 사칙연산자, 리스트와 딕셔너리 내에서의 덧셈, 곱셈, 인덱스로 데이터 변환, 추가, 삭제 하는 법 등을 배워 학습하였습니다. |
| 이선오 | 문자형 데이터를 숫자로 바꾸는 int, 리스트/딕셔너리에 새로운 데이터를 추가/삭제하는 append, insert/del, remove 문법을 배웠습니다. if문을 활용해 조건이 true일 때 값을 반환하는 간단한 모델을 구현했습니다. |
| 구자현 | 자료형에 요소를 추가, 삭제, 요약할 수 있고 상황에 따라 다른 기능을 수행하는 조건문을 여러 자료형을 이용해 구현했습니다.  |
| 권태윤 | 파이썬의 for문, while문, if문을 공부했으며 이외에도 형변화(int), 리스트, 딕셔너리 등의 기능을 공부했습니다. |
| 김지현 | 형태를 변환하는 int(), 연산자(+,-,*,/), 리스트와 딕셔너리에 데이터를 추가하고 삭제하는 방법, sum/max/min, 조건문, 반복문에 대해서 더 자세히 학습했습니다. continue, range를 통해 반복문을 더 자유롭게 쓸 수 있습니다. |

### 프로젝트 결과물을 보여주세요.

- 중국집 메뉴판
    
    ```python
    menu = {"짜장" : 4000, "짬뽕" : 5000, "탕수육" : 9000}
    
    menu["냉면"] = 6000 #냉면 추가
    
    print(menu["짬뽕”]) #짬뽕 가격 출력
    
    menu["탕수육"] = 8500 #탕수육 가격 변경
    
    del menu["짜장”] #짜장 삭제
    
    print(menu)
    ```
    
    ```python
    menu = {"짜장":1000, "짬뽕":2000, "탕수육":3000}
    
    food = input("먹고 싶은 메뉴를 입력해주세요 : ")
    
    if food in menu : 
        print(menu[food], "원 입니다.")
    else :
        print("주문 불가")
    ```
    

### 오늘 배운 내용에 대해서 조금 더 알고 싶은데, 참고할 만한 자료는 뭐가 있을까요?

- Python 내장 함수
    
    [Built-in Functions - Python 3.10.7 documentation](https://docs.python.org/ko/3/library/functions.html)
    
- 딕셔너리 사용법
    
    [점프 투 파이썬](https://wikidocs.net/16)
    

### 오늘 배운 내용을 앞으로 어디에 어떻게 적용할 수 있을까요?

- 딕셔너리를 활용하여 가맹점, 혹은 고객 정보 관리
- 비밀번호 잠금해제

<br>
<br>
<br>


# 팔로워 🏃‍♂️ (오후)

### 각자 오늘 배운 내용을 정리해볼까요? (**T**oday **I** **L**earned)


| 이름 | **T**oday **I** **L**earned |
| --- | --- |
| 박혜민 | 반복문(for문과 range, random 활용) |
| 박상우 | for문과 if문을 통해 별찍기, 출력값 줄 바꾸기, 로또 번호 추출기 등을 만들고 배웠습니다. |
| 이선오 | for문을 활용한 반복 출력과 출력값 줄바꿈 등을 배웠습니다. |
| 구자현 | 조건문을 통해 반복문을 제어함으로써 원하는 값을 얻을 수 있다. |
| 권태윤 | for문을 이용한 조건문에서 반복한 값을 내는 법, random 함수 이용하는 법, 줄 바꿈을 배웠습니다. |
| 김지현 | 예제를 통해 조건문과 반복문을 실습해보면서 체화할 수 있었습니다. |

### 프로젝트 결과물을 보여주세요.

- 별이 빛나는 밤
    
    ```python
    for x in range(5) :
        print("*" * (x + 1))
    ```
    
    ```python
    #1
    for x in range(5) :
        print("*")
    #2-1
    print("*" * 5)
    #2-2
    for x in range(5) :
        print("*", end="")
    #3-1
    for x in range(5) :
        print("*****")
    #3-2
    for x in range(5) :
        print("*" * 5)
    #4
    for x in range(5) :
        print("*" * (x + 1))
    ```
    
- 줄 바꿔 출력하기
    
    ```python
    x = int(input("숫자를 입력하세요 : "))
    for i in range(x) :
        if i % 10 == 0 
            print() 
        print(i+1, end="\t") 
    ```
    
    ```python
    x = int(input("숫자를 입력하세요 : "))
    
    for i in range(x) :
        if i % 10 == 0 :
            print()
        print(i+1, end="\t")
    
    print()
    ```
    
- 로또당첨번호 생성기
    
    ```python
    import random
    
    count = int(input("몇장을 구매하시겠습니까? : "))
    
    for x in range(count):
        lotto = sorted(random.sample(range(1, 46), 6))
        print(lotto)
    ```
    
    ```python
    import random
    
    count = int(input("로또를 몇개 구매하시겠습니까? "))
    
    for i in range(count) :
        lotto = random.sample(range(1, 46), 6)
        lotto.sort()
        print(lotto)
    
    print("로또 종료")
    ```
    

### 오늘 배운 내용에 대해서 조금 더 알고 싶은데, 참고할 만한 자료는 뭐가 있을까요?

- 정렬 두 가지 방법
    
    [[Python] 정렬 문법 sort() sorted() reverse](https://velog.io/@aonee/Python-%EC%A0%95%EB%A0%AC-sort-sorted-reverse)
    
- Comprehension
    
    [파이썬의 Comprehension 소개](https://mingrammer.com/introduce-comprehension-of-python/)
    

### 오늘 배운 내용을 앞으로 어디에 어떻게 적용할 수 있을까요?

- 당첨자 뽑기 프로그램 생성