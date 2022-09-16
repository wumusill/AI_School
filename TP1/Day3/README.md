# 팔로워🏃‍♂️ (오전)

팀원: 나연 강, 자현 구, 지현 김, 상우 박, 혜민 박, 이선오
팀장: 권태윤

### 각자 오늘 배운 내용을 정리해볼까요? (**T**oday **I** **L**earned)

| 박혜민 | 크롤링 방법(실시간 검색어 크롤링하고, 보기 좋게 출력하고, 저장하는 방법까지) |
| --- | --- |
| 박상우 | bs4의 BeautifulSoup를 통해 웹 크롤링을 진행하였으며, 실시간 검색어를 추출하여 파일화 하였습니다. |
| 이선오 | 파이썬을 활용한 웹 크롤링의 개념부터 실습까지 학습했고 세 가지 모드로 저장하는 방법을 배웠습니다. |
| 구자현 | 모듈 requests를 이용하여 서버 컴퓨터로부터 어떻게 정보를 받아오는지 알고, 받아온 정보를 모듈 bs4를 이용하여 가공하였다.  |
| 권태윤 | 크롤링의 개념 이해 및 크롤링 하는 방법:
1) request함수 이용하는 법
2) Beautiful soup이용하여 불필요한 데이터 정리하는 법
3) 웹사이트에서 특정 데이터 및 검색한 당일 날짜 입력하는 법
3) 크롤링한 데이터 중 특정 공통점 찾아 원하는 데이터만 추출하는 법
4) 크롤링 막아놓은 웹사이트 대상 크롤링 요청하는 법 |
| 김지현 | 크롤링 코드를 한개씩 뜯어보면서 각각의 함수와 모듈이 어떤 의미를 가지는지 배우고 보기 좋게 표현하는 법을 알게 되었습니다. |

### 프로젝트 결과물을 보여주세요.

- 실시간 검색어 확인하기
    
    ```python
    from bs4 import BeautifulSoup
    import requests
    from datetime import datetime
    
    url = "http://www.daum.net/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rank = 1
    
    results = soup.findAll('a','link_favorsch')
    
    print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))
    
    for result in results:
        print(rank,"위 : ",result.get_text(),"\n")
        rank += 1
    ```
    
- YTN 인기 뉴스
    
    ```python
    from bs4 import BeautifulSoup
    import requests
    from datetime import datetime
    
    url = "https://media.naver.com/press/052/ranking?type=popular"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rank = 1
    
    results = soup.findAll('strong','list_title')
    
    # print(response.text)
    
    search_rank_file = open("rankresult.txt","a")
    
    print(datetime.today().strftime("%Y년 %m월 %d일의 YTN 뉴스 순위입니다.\n"))
    
    for result in results:
        search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
        print(rank,"위 : ",result.get_text(),"\n")
        rank += 1
    ```
    
- 네이버 데이터랩 20대 검색어
    
    ```python
    from bs4 import BeautifulSoup
    import requests
    from datetime import datetime
    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    url = "https://datalab.naver.com/keyword/realtimeList.naver?age=20s"
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    rank = 1
    # span - item_title
    results = soup.findAll('span','item_title')
    
    print(response.text)
    
    search_rank_file = open("rankresult.txt","a")
    
    print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))
    
    for result in results:
        search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
        print(rank,"위 : ",result.get_text(),"\n")
        rank += 1
    ```
    

### 오늘 배운 내용에 대해서 조금 더 알고 싶은데, 참고할 만한 자료는 뭐가 있을까요?

- 크롤링
    
    [크롤링(crawling) 이해 및 기본](https://www.fun-coding.org/crawl_basic2.html)
    
- header 값, 나의 user-agent 조회
    
    [what is my user agent](https://www.whatismybrowser.com/detect/what-is-my-user-agent/)
    
- BeautifulSoup
    
    [뷰티플수프 문서 - 뷰티플수프 4.0.0 문서](https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/)
    
- requests
    
    [Developer Interface - Requests 2.28.1 documentation](https://requests.readthedocs.io/en/latest/api/#requests.Response)
    

### 오늘 배운 내용을 앞으로 어디에 어떻게 적용할 수 있을까요?

크롤링을 통해 자동으로 데이터를 수집할 수 있다.

게임 전투력 랭킹 크롤링

프로젝트를 할 때 SNS 관련 최신 정보나 기존에 없던 데이터를 직접 실시간으로 수집 가능


<br>
<br>
<br>

# 팔로워🏃‍♂️ (오후)

### 각자 오늘 배운 내용을 정리해볼까요? (**T**oday **I** **L**earned)

| 박혜민 | 날씨 정보 가져오기, 번역, 이메일 보내기(오류 너무 많이 나서 실습을 하나도 못했어요. 다시 해봐야겠습니다) |
| --- | --- |
| 박상우 | api를 이용하여 날씨 가져오기, 이메일 전송하기, 번역하는 함수를 만들고 학습하였습니다. |
| 이선오 | API 개념, 사용방법
API key, API doc
API 링크를 통해 요청 보내기
요청을 보낼 때 필요한 정보 링크에 포함시키는 방법
json을 이용한 파이썬 문자열의 타입 변경
lang 파라미터 추가로 언어를 변경하는 방법
googletrans 라이브러리 import
translate 함수 : translate(text, dect, src)
SMTP : 간단하게 이메일을 보내기 위한 약속
SMTP 서버 연결을 위한 재료 : Address, Port
smtplib : SMTP에 쉽게 접근할 수 있는 라이브러리
MIME : 메일 표준. SMTP에 이 형태로만 메일 요청 가능
email.message 모듈의 EmailMessage 기능 활용
Header : MIME 형태 중 하나로 Subject, From, To
메일에 사진 첨부하는 함수 add_attachment
add_attachment 재료 : image, maintype(첨부한 파일의 유형), subtype(확장자)
binary : 컴퓨터가 읽고 이해하기 가장 편한 문자
imghdr : 확장자를 파악해주는 파이썬 내장 모듈 |
| 구자현 | Package(email, googletrans) 사용 방법을 실습을 통해 알아봤다.
API를 이용하여 외부 서버에서 데이터를 가져올 수 있다.
정규식을 이용해 사용자 입력값 제한을 코드 한 줄로 할 수 있다.
json.loads() 함수는 dictionary 자료형을 return 한다. |
| 권태윤 | 날씨 정보 받아오기:
api에 대한 개념 이해
f를 이용해 텍스트에 변수 넣기
requests.get() 이용한 api데이터 가져오기
json을 이용한 데이터 str->딕셔너리 형태 저장
json 내부 특정 데이터 추출
api 파라미터 추가 이용해 데이터 형식 바꾸기
번역기:
Translator() 사용하는 법
translate함수 사용법
언어 감지하는 법 및 번역하는 법
파이썬으로 메일 보내기:
SMTP작동 원리
SMTP서버 연결하는 법
MIME개념 이해& 변환 방법
smtp.send_message()함수 사용법
read, write, append기능 공부
이미지 파일 바이너리 형식 전환
정규 표현식 통한 메일 유효성 검증
bool 함수 사용 방법 |
| 김지현 | 1. API
application programming interface
응용 프로그래밍 인터페이스
프로그램과 프로그램을 이어주는 인터페이스!
ex) api 사용하여 날씨 정보 출력하는 프로그램

크롤링은 한정적이고, 사이트에 표기된 것만 긁어올 수 있는 반면
api는 누군가 만들어둔 프로그램을 통해서 api key로 데이터를 가져와 쓸 수 있다

api doc: 사용방법 설명서
https://openweathermap.org/current
1) 링크를 만든다
공통 url+?+재료(파라미터)
2) 서버에 링크로 요청한다
requests 모듈
3) 예쁘게 만들어 텍스트 파일로 저장
json: 데이터를 주고받을 때 사용하는 포맷
4) 형태에서 언어, 값 단위 등도 바꿀 수 있음

2. 번역하기 (언어 감지/번역 라이브러리)
library: 모듈을 큰 기능 단위로 묶어놓은 것
라이브러리 > 모듈 > 기능 > 함수

Translator() : 번역기 기능
detect(text) : 언어 감지
translate(text, dest, src) : 번역할 문장, 목적 언어, 텍스트 언어(생략 가능)

3. 파이썬으로 메일 보내기
SMTP : 간단하게 메일을 보내기 위한 약속
SMTP 서버에는 주소와 포트번호(어떤 문을 열고 들어갈까?)가 존재

https://velog.io/@smearth18/멋쟁이사자처럼-ai-스쿨-220916 |

### 프로젝트 결과물을 보여주세요.

- 날씨정보 받아오기
    
    ```python
    import requests
    import json
    
    city = "Seoul"
    apikey = "################################"
    lang = "kr"
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"
    
    result = requests.get(api)
    
    data = json.loads(result.text)
    
    # 지역 : name
    print(data["name"],"의 날씨입니다.")
    # 자세한 날씨 : weather - description
    print("날씨는 ",data["weather"][0]["description"],"입니다.")
    # 현재 온도 : main - temp
    print("현재 온도는 ",data["main"]["temp"],"입니다.")
    # 체감 온도 : main - feels_like
    print("하지만 체감 온도는 ",data["main"]["feels_like"],"입니다.")
    # 최저 기온 : main - temp_min
    print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
    # 최고 기온 : main - temp_max
    print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
    # 습도 : main - humidity
    print("습도는 ",data["main"]["humidity"],"입니다.")
    # 기압 : main - pressure
    print("기압은 ",data["main"]["pressure"],"입니다.")
    # 풍향 : wind - deg
    print("풍향은 ",data["wind"]["deg"],"입니다.")
    # 풍속 : wind - speed
    print("풍속은 ",data["wind"]["speed"],"입니다.")
    ```
    
- 번역하기
    
    ```python
    from googletrans import Translator
    
    translator = Translator()
    
    sentence = input("번역을 원하는 문장을 입력해주세요 : ")
    dest = input("어떤 언어로 번역을 원하시나요? : ")
    
    result = translator.translate(sentence, dest)
    detected = translator.detect(sentence)
    
    print("============출 력 결 과============")
    print(detected.lang,":",sentence)
    print(result.dest,":",result.text)
    print("=================================")
    ```
    
- 메일 보내기
    
    ```python
    import smtplib
    from email.message import EmailMessage
    import imghdr
    import re
    
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 465
    
    def sendEmail(addr):
        reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
        if bool(re.match(reg,addr)):
            smtp.send_message(message)
            print("정상적으로 메일이 발송되었습니다.")
        else:
            print("유효한 이메일 주소가 아닙니다.")
    
    message = EmailMessage()
    message.set_content("코드라이언 수업중입니다.")
    
    message["Subject"] = "이것은 제목입니다."
    message["From"] = "###@gmail.com"
    message["To"] = "###@gmail.com"
    
    with open("codelion.png","rb") as image:
        image_file = image.read()
    
    image_type = imghdr.what('codelion',image_file)
    message.add_attachment(image_file,maintype='image',subtype=image_type)
    
    smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
    smtp.login("###@gmail.com","######")
    
    # 메일을 보내는 sendEmail 함수를 호출해서 실행해보기
    sendEmail("###@gmail.com")
    smtp.quit()
    ```
    

### 오늘 배운 내용에 대해서 조금 더 알고 싶은데, 참고할 만한 자료는 뭐가 있을까요?

- 이메일에 사진 첨부 응용 자료
    
    [Python 22(이메일에 사진첨부)](https://velog.io/@gcgang0303/Python-22%EC%9D%B4%EB%A9%94%EC%9D%BC%EC%97%90-%EC%82%AC%EC%A7%84%EC%B2%A8%EB%B6%80)
    
- googletrans `AttributeError: 'NoneType' object has no attribute 'group'` 해결 방법
    
    [](https://velog.io/@kir315/googletrans-%EC%98%A4%EB%A5%98-%ED%95%B4%EA%B2%B0)
    
- 정규표현식
    
    [점프 투 파이썬](https://wikidocs.net/4308)
    
- Python 문자열 포맷팅 여러가지 방법들
    
    [[Python] 문자열 포맷팅 방법들 (%, str.format, f-string)](https://brownbears.tistory.com/421)
    

### 오늘 배운 내용을 앞으로 어디에 어떻게 적용할 수 있을까요?

- 프로젝트에 필요한 데이터를 api로 가져와 사용할 수 있다.
- 정규식을 이용하여 사용자 입력값에 대해 제약 조건을 만들 수 있다.