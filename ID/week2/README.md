# ๐ฆ TIL

# โ Seaborn ์๊ฐํ ์ฐ์ต
> * [seaborn ๊ทธ๋ํ ์ข๋ฅ, ๊ณต์ ๋ฌธ์ ๋ณด๊ธฐ](https://seaborn.pydata.org/examples/index.html)



<br>

# โ requests


### ๐ Link
> * [Requests ๊ณต์ ๋ฌธ์](https://requests.readthedocs.io/en/latest/)

* ์ ์๋ ์ถ์ฒ `URL about REST API`
> * https://spoqa.github.io/2012/02/27/rest-introduction.html
> * https://meetup.toast.com/posts/92
> * https://blog.naver.com/ydot/222738115724


* ํ์๋ ์ถ์ฒ `URL about Module of requests`
> * https://me2nuk.com/Python-requests-module-example/#requests-get-post-put--delete-head-options


## 1. requests๋ ?

> ***Requests** is an elegant and simple HTTP library for Python, built for human beings.*

- Python์์ ํน์  ์น์ฌ์ดํธ์ HTTP ์์ฒญ์ ๋ณด๋ด๋ ๋ชจ๋
- ํน์  ์น์ฌ์ดํธ์ HTTP ์์ฒญ์ ๋ณด๋ด HTML ๋ฌธ์๋ฅผ ๋ฐ์์ฌ ์ ์๋ ๋ผ์ด๋ธ๋ฌ๋ฆฌ
    - ์ ํํ๋ HTML ๋ฌธ์๊ฐ ์๋ ๋จ์ํ String ํ์์ ์๋ฃ
        - `BeautifulSoup`๊ณผ ๊ฐ์ ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ฅผ ํตํด HTML ๋ฌธ์๋ก ๋ฐ๊ฟ ์ ์๋ค.

<br>


## 2. requests ๋ผ์ด๋ธ๋ฌ๋ฆฌ ์ค์น ๋ฐ ๋ก๋

- Requests officially supports Python 3.7+.
    - Python 3.7 ์ด์์ ๋ฒ์ ์์ ์ง์๋๋ค.
* ๊ธฐ๋ณธ์ ์ผ๋ก `pip`๋ฅผ ์ด์ฉํด ์ค์นํ๋ฉฐ, ์ดํ import๋ฅผ ํตํด ํธ์ถํ  ์ ์๋ค. 

```python
!pip install requests
```

<br>

## 3. http ํต์  ๋ฐฉ์

### http๋?

- ํด๋ผ์ด์ธํธ๊ฐ ์น ์๋ฒ์๊ฒ ์ฌ์ฉ์ ์์ฒญ์ ๋ชฉ์ ์ด๋ ํ๋์ ๋ํด ์๋ฆฌ๋ ์๋จ.
- ์ต์ด์ http์๋ GET() ํ๋๋ง ์ฌ์ฉ, ์ดํ ๋ค์ํ ๋ฉ์๋ ๊ฐ๋ฐ
    
    ### http ๋ฉ์๋์ ์ข๋ฅ 5๊ฐ์ง
    
    ### `GET`
    
    : ํ์ํ ๋ฐ์ดํฐ๋ฅผ Query String ์ ๋ด์ ์ ์กํ๋ฉฐ, ๋ฆฌ์์ค๋ฅผ ์กฐํํ๋๋ฐ ์ฌ์ฉํ๋ค. 
    
    ### `POST`
    
    :  ์์ฒญํ ๋ฐ์ดํฐ๋ฅผ ์ฒ๋ฆฌํ๋ฉฐ, ๋ฐ์ดํฐ๋ฅผ ๋ฑ๋กํ๋ ๋ฐ ์ฃผ๋ก ์ฌ์ฉํ๋ค. 
    
    ### `PUT`
    
     :  POST์ ์ ์ฌํ ์ ์ก ๊ตฌ์กฐ๋ฅผ ๊ฐ์ง์ง๋ง ๋ณดํต ๋ด์ฉ์ ๊ฐฑ์ ํ๋ ์์ฃผ๋ก ์ฌ์ฉ๋๋ค.
    
    ### `PATCH`
    
    : ๋ฆฌ์์ค๋ฅผ ๋ถ๋ถ์ ์ผ๋ก ๋ณ๊ฒฝํ๋ค.
    
    ### `DELETE`
    
    : ์น ๋ฆฌ์์ค๋ฅผ ์ ๊ฑฐํ๋ค.
    
    - ์ด์ธ์ http ๋ฉ์๋๋ [์ํคํผ๋์](https://ko.wikipedia.org/wiki/HTTP)๋ฅผ ์ฐธ๊ณ ํ์.
    
    ### http ์ํ์ฝ๋
    
    ํด๋ผ์ด์ธํธ๊ฐ ๋ณด๋ธ ์์ฒญ์ ์ฒ๋ฆฌ ์ํ๋ฅผ ์๋ต์์ ์๋ ค์ฃผ๋ ๊ธฐ๋ฅ์ด๋ฉฐ, `100 ~ 500๋ฒ๋`์ ๋๋ฒ๋ฅผ ์ฌ์ฉํ๋ค.
    
    <aside>
  
    ๐ก **์ํ์ฝ๋ ์ข๋ฅ**
    
   > **1xx (์ ๋ณด)** : ์์ฒญ์ ๋ฐ์์ผ๋ฉฐ ํ๋ก์ธ์ค๋ฅผ ๊ณ์ํ๋ค. <br>
   > **2xx (์ฑ๊ณต) :** ์์ฒญ์ ์ฑ๊ณต์ ์ผ๋ก ๋ฐ์์ผ๋ฉฐ ์ธ์ํ๊ณ  ์์ฉํ์๋ค. <br>
   > **3xx (๋ฆฌ๋ค์ด๋ ์)** : ์์ฒญ ์๋ฃ๋ฅผ ์ํด ์ถ๊ฐ ์์ ์กฐ์น๊ฐ ํ์ํ๋ค. <br>
   > **4xx (ํด๋ผ์ด์ธํธ ์ค๋ฅ)** : ์์ฒญ์ ๋ฌธ๋ฒ์ด ์๋ชป๋์๊ฑฐ๋ ์์ฒญ์ ์ฒ๋ฆฌํ  ์ ์๋ค. <br>
   > **5xx (์๋ฒ ์ค๋ฅ)** : ์๋ฒ๊ฐ ๋ช๋ฐฑํ ์ ํจํ ์์ฒญ์ ๋ํด ์ถฉ์กฑ์ ์คํจํ๋ค.
    
    โ ๋ฐ์ดํฐ ์์ง์์๋ `200 OK` ๊ฐ ๋์ค๋์ง ํ์ธ ํ๋ ๊ฒ์ด ์ค์!!
    
    </aside>
    
    ```python
    import requests
    
    # ๋ค์ด๋ฒ ๊ธ์ต ์ผ๋ณ์์ธ ์ฌ์ดํธ
    url = "https://finance.naver.com/item/sise_day.naver?code=005930&page=10"
    
    response = requests.get(url, headers = {"user-agent":"Mozilla/5.0"})
    response
    
    >>> <Response [200]>
    ```
    
    - ๊ตฌ์ฒด์ ์ธ http ์ํ์ฝ๋๋ [์ํคํผ๋์](https://ko.wikipedia.org/wiki/HTTP_%EC%83%81%ED%83%9C_%EC%BD%94%EB%93%9C)๋ฅผ ์ฐธ๊ณ ํ์


<br>


## 4. requests ๋ฉ์๋
* ์์ธํ๊ฑด [์ฌ๊ธฐ](https://me2nuk.com/Python-requests-module-example/#requests-get-post-put--delete-head-options)๋ฅผ ํ์ธ!

### `Response()`

### `requests.Response()`

- HTTP ์์ฒญ์ ๋ํ ์๋ฒ์ ์๋ต์ ํฌํจํ ๊ฐ์ฒด
- ํด๋น ๊ฐ์ฒด์๋ HTTP ์์ฒญ์ ๋ํ ์๋ฒ์ ์๋ต์ ๋ฐํํ๋ค.
    - requests ๋ชจ๋์ ์ด์ฉํ์ฌ ์์ฒญ ํ ๋ค์ ๊ทธ์ ๋ํ Response ๊ฒฐ๊ณผ๋ค์ด ์ฌ์ฉ์๊ฐ ์ข ๋ ํธํ๊ฒ ๋ณผ ์ ์๋๋ก`request.modules.Response`ย ํด๋์ค๋ฅผ ์ด์ฉํ์ฌ ์ข ๋ ํธํ๊ฒ ์ ๋ฆฌ.
- `Class requests.modules.Response`

โจ**์์**
```python
import requests

response = requests.get("https://www.naver.com/")

# ์๋ฒ ์์ฒญ ๊ฒฐ๊ณผ ์ถ๋ ฅ
print(response)
>>> <Response [200]>

# http ์๋ต ์ฝ๋ ์ถ๋ ฅ
print(response.status_code)
>>> 200

# ์์ฒญ / ์๋ต ๋ณธ๋ฌธ์ str ํ์์ผ๋ก ๋ฐํ
response.text

# ์์ฒญ / ์๋ต ๋ณธ๋ฌธ์ byte ํ์์ผ๋ก ๋ฐํ
response.content

# ์์ฒญ / ์๋ต ๋ณธ๋ฌธ์ json ํ์์ผ๋ก ๋์ฝ๋ฉํ์ฌ ๋ฐํ
# ๋ง์ฝ ์ฌ๋ฐ๋ฅธ json ํ์์ด ์๋ ๊ฒฝ์ฐ ์๋ฌ
response.json()

# ์์ฒญํ ๋ค ์๋ต์ ์ต์ข URL์ ๋ฐํ
print(response.url)
>>> 'https://www.naver.com/'

# ์์ฒญ / ์๋ต ์ฝ๋๊ฐ 200์ด๋ฉด True ์๋๋ฉด False
print(response.ok)
>>> True

# ์์ฒญ / ์๋ต ์ธ์ฝ๋ฉ์ ๋ฐํ
print(response.apparent_encoding)
>>> 'Windows-1254'
```



<br>

## 5. requests ํ์ฉ

### http ์ํ๊ฐ ๋ฐํ

- if ๋ฌธ ์ ์ด์ฉํด ์์ฒญ์ ์ ์์ ์ผ๋ก ๋ฐ์์๋์ง ํ๋จํ  ์ ์์
    
    ```python
    if response.status_code in range(200, 300):
        print("์ ์์ ์ผ๋ก ๋ฐ์ดํฐ๋ฅผ ์์งํ์์ต๋๋ค.")
    else:
        print(f"๋น์ ์ [์ฝ๋ : {response.status_code}]")
    ```
    

### APIํธ์ถ & ๋ฐ์ดํฐ ์์ง

- API์์ ์ ํ์ ์ผ๋ก ๋ฐ์ดํฐ๋ฅผ ๊ธ์ด์ฌ ์ ์์
(์์ธ ๋ฏธ์ธ๋จผ์ง ๋ฐ์ดํฐ open API์์ ๊ตฌ ์ด๋ฆ๊ณผ ๋ฏธ์ธ๋จผ์ง ์๋ง ๋ฝ์์ด)
    
    ```python
    import requests # requests ๋ผ์ด๋ธ๋ฌ๋ฆฌ ์ค์น ํ์
    
    r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
    rjson = r.json()
    
    citys = rjson["RealtimeCityAir"]["row"]
    
    for city in citys:
        gu_name = city["MSRSTE_NM"]
        gu_mise = city["IDEX_MVL"]
        print(gu_name, gu_mise)
    ```
    
- openweathermap API๋ฅผ ์ด์ฉํ ๋ ์จ ํ์ธํ๊ธฐ(1์ฃผ์ฐจ ์ค์ต)
    
    ```python
    import requests
    import json
    
    city = "Seoul"
    apikey = "๊ฐ์ธ key"
    lang = "kr"
    
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"
    
    result = requests.get(api)
    data = json.loads(result.text)
    
    print(data["name"],"์ ๋ ์จ์๋๋ค.")
    print("๋ ์จ๋ ",data["weather"][0]["description"],"์๋๋ค.")
    print("ํ์ฌ ์จ๋๋ ",data["main"]["temp"],"์๋๋ค.")
    print("ํ์ง๋ง ์ฒด๊ฐ ์จ๋๋ ",data["main"]["feels_like"],"์๋๋ค.")
    print("์ต์  ๊ธฐ์จ์ ",data["main"]["temp_min"],"์๋๋ค.")
    print("์ต๊ณ  ๊ธฐ์จ์ ",data["main"]["temp_max"],"์๋๋ค.")
    print("์ต๋๋ ",data["main"]["humidity"],"์๋๋ค.")
    print("๊ธฐ์์ ",data["main"]["pressure"],"์๋๋ค.")
    print("ํํฅ์ ",data["wind"]["deg"],"์๋๋ค.")
    print("ํ์์ ",data["wind"]["speed"],"์๋๋ค.")
    ```
    

<br>

## 6. Reference

- **์ดํด๋ณด๋ฉด ์ข์ ์๋ฃ๋ค**
    
   > [Python requests ๋ชจ๋(module) ์ฌ์ฉ๋ฒ](https://me2nuk.com/Python-requests-module-example/#requests-get-post-put--delete-head-options) <br>
   > [requests/api.py at main ยท psf/requests](https://github.com/psf/requests/blob/main/requests/api.py#L105-L117) <br>
   > [Requests :: Anaconda.org](https://anaconda.org/anaconda/requests) <br>
   > [GitHub - psf/requests: A simple, yet elegant, HTTP library.](https://github.com/psf/requests) <br>
   > [์ ํ ํฌ ํ์ด์ฌ](https://wikidocs.net/80841) <br>
   > [HTTP ์ํ ์ฝ๋ - ์ํค๋ฐฑ๊ณผ, ์ฐ๋ฆฌ ๋ชจ๋์ ๋ฐฑ๊ณผ์ฌ์ ](https://ko.wikipedia.org/wiki/HTTP_%EC%83%81%ED%83%9C_%EC%BD%94%EB%93%9C) <br>
   > [HTTP - ์ํค๋ฐฑ๊ณผ, ์ฐ๋ฆฌ ๋ชจ๋์ ๋ฐฑ๊ณผ์ฌ์ ](https://ko.wikipedia.org/wiki/HTTP) <br>
   > [์ ํ ํฌ ํ์ด์ฌ](https://wikidocs.net/133287) <br>
   > [Quickstart - Requests 2.28.1 documentation](https://requests.readthedocs.io/en/latest/user/quickstart/#response-content)
