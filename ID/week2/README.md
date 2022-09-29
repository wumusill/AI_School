# 🦁 TIL

# ✅ Seaborn 시각화 연습
> * [seaborn 그래프 종류, 공식 문서 보기](https://seaborn.pydata.org/examples/index.html)



<br>

# ✅ requests


### 🔗 Link
> * [Requests 공식 문서](https://requests.readthedocs.io/en/latest/)

* 정은님 추천 `URL about REST API`
> * https://spoqa.github.io/2012/02/27/rest-introduction.html
> * https://meetup.toast.com/posts/92
> * https://blog.naver.com/ydot/222738115724


* 혜은님 추천 `URL about Module of requests`
> * https://me2nuk.com/Python-requests-module-example/#requests-get-post-put--delete-head-options


## 1. requests란 ?

> ***Requests** is an elegant and simple HTTP library for Python, built for human beings.*

- Python에서 특정 웹사이트에 HTTP 요청을 보내는 모듈
- 특정 웹사이트에 HTTP 요청을 보내 HTML 문서를 받아올 수 있는 라이브러리
    - 정확히는 HTML 문서가 아닌 단순한 String 형식의 자료
        - `BeautifulSoup`과 같은 라이브러리를 통해 HTML 문서로 바꿀 수 있다.

<br>


## 2. requests 라이브러리 설치 및 로드

- Requests officially supports Python 3.7+.
    - Python 3.7 이상의 버전에서 지원된다.
* 기본적으로 `pip`를 이용해 설치하며, 이후 import를 통해 호출할 수 있다. 

```python
!pip install requests
```

<br>

## 3. http 통신 방식

### http란?

- 클라이언트가 웹 서버에게 사용자 요청의 목적이나 행동에 대해 알리는 수단.
- 최초의 http에는 GET() 하나만 사용, 이후 다양한 메서드 개발
    
    ### http 메서드의 종류 5가지
    
    ### `GET`
    
    : 필요한 데이터를 Query String 에 담아 전송하며, 리소스를 조회하는데 사용한다. 
    
    ### `POST`
    
    :  요청한 데이터를 처리하며, 데이터를 등록하는 데 주로 사용한다. 
    
    ### `PUT`
    
     :  POST와 유사한 전송 구조를 가지지만 보통 내용을 갱신하는 위주로 사용된다.
    
    ### `PATCH`
    
    : 리소스를 부분적으로 변경한다.
    
    ### `DELETE`
    
    : 웹 리소스를 제거한다.
    
    - 이외의 http 메서드는 [위키피디아](https://ko.wikipedia.org/wiki/HTTP)를 참고하자.
    
    ### http 상태코드
    
    클라이언트가 보낸 요청의 처리 상태를 응답에서 알려주는 기능이며, `100 ~ 500번대`의 넘버를 사용한다.
    
    <aside>
  
    💡 **상태코드 종류**
    
   > **1xx (정보)** : 요청을 받았으며 프로세스를 계속한다. <br>
   > **2xx (성공) :** 요청을 성공적으로 받았으며 인식했고 수용하였다. <br>
   > **3xx (리다이렉션)** : 요청 완료를 위해 추가 작업 조치가 필요하다. <br>
   > **4xx (클라이언트 오류)** : 요청의 문법이 잘못되었거나 요청을 처리할 수 없다. <br>
   > **5xx (서버 오류)** : 서버가 명백히 유효한 요청에 대해 충족을 실패했다.
    
    → 데이터 수집시에는 `200 OK` 가 나오는지 확인 하는 것이 중요!!
    
    </aside>
    
    ```python
    import requests
    
    # 네이버 금융 일별시세 사이트
    url = "https://finance.naver.com/item/sise_day.naver?code=005930&page=10"
    
    response = requests.get(url, headers = {"user-agent":"Mozilla/5.0"})
    response
    
    >>> <Response [200]>
    ```
    
    - 구체적인 http 상태코드는 [위키피디아](https://ko.wikipedia.org/wiki/HTTP_%EC%83%81%ED%83%9C_%EC%BD%94%EB%93%9C)를 참고하자


<br>


## 4. requests 메서드
* 자세한건 [여기](https://me2nuk.com/Python-requests-module-example/#requests-get-post-put--delete-head-options)를 확인!

### `Response()`

### `requests.Response()`

- HTTP 요청에 대한 서버의 응답을 포함한 객체
- 해당 객체에는 HTTP 요청에 대한 서버의 응답을 반환한다.
    - requests 모듈을 이용하여 요청 한 다음 그에 대한 Response 결과들이 사용자가 좀 더 편하게 볼 수 있도록`request.modules.Response` 클래스를 이용하여 좀 더 편하게 정리.
- `Class requests.modules.Response`

✨**예시**
```python
import requests

response = requests.get("https://www.naver.com/")

# 서버 요청 결과 출력
print(response)
>>> <Response [200]>

# http 응답 코드 출력
print(response.status_code)
>>> 200

# 요청 / 응답 본문을 str 타입으로 반환
response.text

# 요청 / 응답 본문을 byte 타입으로 반환
response.content

# 요청 / 응답 본문을 json 형식으로 디코딩하여 반환
# 만약 올바른 json 형식이 아닌 경우 에러
response.json()

# 요청한 뒤 응답의 최종 URL을 반환
print(response.url)
>>> 'https://www.naver.com/'

# 요청 / 응답 코드가 200이면 True 아니면 False
print(response.ok)
>>> True

# 요청 / 응답 인코딩을 반환
print(response.apparent_encoding)
>>> 'Windows-1254'
```



<br>

## 5. requests 활용

### http 상태값 반환

- if 문 을 이용해 요청을 정상적으로 받아왔는지 판단할 수 있음
    
    ```python
    if response.status_code in range(200, 300):
        print("정상적으로 데이터를 수집하였습니다.")
    else:
        print(f"비정상 [코드 : {response.status_code}]")
    ```
    

### API호출 & 데이터 수집

- API에서 선택적으로 데이터를 긁어올 수 있음
(서울 미세먼지 데이터 open API에서 구 이름과 미세먼지 양만 뽑아옴)
    
    ```python
    import requests # requests 라이브러리 설치 필요
    
    r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
    rjson = r.json()
    
    citys = rjson["RealtimeCityAir"]["row"]
    
    for city in citys:
        gu_name = city["MSRSTE_NM"]
        gu_mise = city["IDEX_MVL"]
        print(gu_name, gu_mise)
    ```
    
- openweathermap API를 이용한 날씨 확인하기(1주차 실습)
    
    ```python
    import requests
    import json
    
    city = "Seoul"
    apikey = "개인 key"
    lang = "kr"
    
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"
    
    result = requests.get(api)
    data = json.loads(result.text)
    
    print(data["name"],"의 날씨입니다.")
    print("날씨는 ",data["weather"][0]["description"],"입니다.")
    print("현재 온도는 ",data["main"]["temp"],"입니다.")
    print("하지만 체감 온도는 ",data["main"]["feels_like"],"입니다.")
    print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
    print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
    print("습도는 ",data["main"]["humidity"],"입니다.")
    print("기압은 ",data["main"]["pressure"],"입니다.")
    print("풍향은 ",data["wind"]["deg"],"입니다.")
    print("풍속은 ",data["wind"]["speed"],"입니다.")
    ```
    

<br>

## 6. Reference

- **살펴보면 좋을 자료들**
    
   > [Python requests 모듈(module) 사용법](https://me2nuk.com/Python-requests-module-example/#requests-get-post-put--delete-head-options) <br>
   > [requests/api.py at main · psf/requests](https://github.com/psf/requests/blob/main/requests/api.py#L105-L117) <br>
   > [Requests :: Anaconda.org](https://anaconda.org/anaconda/requests) <br>
   > [GitHub - psf/requests: A simple, yet elegant, HTTP library.](https://github.com/psf/requests) <br>
   > [점프 투 파이썬](https://wikidocs.net/80841) <br>
   > [HTTP 상태 코드 - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/HTTP_%EC%83%81%ED%83%9C_%EC%BD%94%EB%93%9C) <br>
   > [HTTP - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/HTTP) <br>
   > [점프 투 파이썬](https://wikidocs.net/133287) <br>
   > [Quickstart - Requests 2.28.1 documentation](https://requests.readthedocs.io/en/latest/user/quickstart/#response-content)
