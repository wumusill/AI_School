# ํ๋ก์ ๐โโ๏ธ (์ค์ )

ํ์: ๋์ฐ ๊ฐ, ์ํ ๊ตฌ, ์งํ ๊น, ์์ฐ ๋ฐ, ํ๋ฏผ ๋ฐ, ์ด์ ์ค
ํ์ฅ: ๊ถํ์ค

### ๊ฐ์ ์ค๋ ๋ฐฐ์ด ๋ด์ฉ์ ์ ๋ฆฌํด๋ณผ๊น์? (**T**oday **I** **L**earned)

| ์ด๋ฆ | **T**oday **I** **L**earned |
| --- | --- |
| ๋ฐํ๋ฏผ | ํฌ๋กค๋ง ๋ฐฉ๋ฒ(์ค์๊ฐ ๊ฒ์์ด ํฌ๋กค๋งํ๊ณ , ๋ณด๊ธฐ ์ข๊ฒ ์ถ๋ ฅํ๊ณ , ์ ์ฅํ๋ ๋ฐฉ๋ฒ๊น์ง) |
| ๋ฐ์์ฐ | bs4์ BeautifulSoup๋ฅผ ํตํด ์น ํฌ๋กค๋ง์ ์งํํ์์ผ๋ฉฐ, ์ค์๊ฐ ๊ฒ์์ด๋ฅผ ์ถ์ถํ์ฌ ํ์ผํ ํ์์ต๋๋ค. |
| ์ด์ ์ค | ํ์ด์ฌ์ ํ์ฉํ ์น ํฌ๋กค๋ง์ ๊ฐ๋๋ถํฐ ์ค์ต๊น์ง ํ์ตํ๊ณ  ์ธ ๊ฐ์ง ๋ชจ๋๋ก ์ ์ฅํ๋ ๋ฐฉ๋ฒ์ ๋ฐฐ์ ์ต๋๋ค. |
| ๊ตฌ์ํ | ๋ชจ๋ requests๋ฅผ ์ด์ฉํ์ฌ ์๋ฒ ์ปดํจํฐ๋ก๋ถํฐ ์ด๋ป๊ฒ ์ ๋ณด๋ฅผ ๋ฐ์์ค๋์ง ์๊ณ , ๋ฐ์์จ ์ ๋ณด๋ฅผ ๋ชจ๋ bs4๋ฅผ ์ด์ฉํ์ฌ ๊ฐ๊ณตํ์๋ค.  |
| ๊ถํ์ค | ํฌ๋กค๋ง์ ๊ฐ๋ ์ดํด ๋ฐ ํฌ๋กค๋ง ํ๋ ๋ฐฉ๋ฒ:
1) requestํจ์ ์ด์ฉํ๋ ๋ฒ
2) Beautiful soup์ด์ฉํ์ฌ ๋ถํ์ํ ๋ฐ์ดํฐ ์ ๋ฆฌํ๋ ๋ฒ
3) ์น์ฌ์ดํธ์์ ํน์  ๋ฐ์ดํฐ ๋ฐ ๊ฒ์ํ ๋น์ผ ๋ ์ง ์๋ ฅํ๋ ๋ฒ
3) ํฌ๋กค๋งํ ๋ฐ์ดํฐ ์ค ํน์  ๊ณตํต์  ์ฐพ์ ์ํ๋ ๋ฐ์ดํฐ๋ง ์ถ์ถํ๋ ๋ฒ
4) ํฌ๋กค๋ง ๋ง์๋์ ์น์ฌ์ดํธ ๋์ ํฌ๋กค๋ง ์์ฒญํ๋ ๋ฒ |
| ๊น์งํ | ํฌ๋กค๋ง ์ฝ๋๋ฅผ ํ๊ฐ์ฉ ๋ฏ์ด๋ณด๋ฉด์ ๊ฐ๊ฐ์ ํจ์์ ๋ชจ๋์ด ์ด๋ค ์๋ฏธ๋ฅผ ๊ฐ์ง๋์ง ๋ฐฐ์ฐ๊ณ  ๋ณด๊ธฐ ์ข๊ฒ ํํํ๋ ๋ฒ์ ์๊ฒ ๋์์ต๋๋ค. |

### ํ๋ก์ ํธ ๊ฒฐ๊ณผ๋ฌผ์ ๋ณด์ฌ์ฃผ์ธ์.

- ์ค์๊ฐ ๊ฒ์์ด ํ์ธํ๊ธฐ
    
    ```python
    from bs4 import BeautifulSoup
    import requests
    from datetime import datetime
    
    url = "http://www.daum.net/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rank = 1
    
    results = soup.findAll('a','link_favorsch')
    
    print(datetime.today().strftime("%Y๋ %m์ %d์ผ์ ์ค์๊ฐ ๊ฒ์์ด ์์์๋๋ค.\n"))
    
    for result in results:
        print(rank,"์ : ",result.get_text(),"\n")
        rank += 1
    ```
    
- YTN ์ธ๊ธฐ ๋ด์ค
    
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
    
    print(datetime.today().strftime("%Y๋ %m์ %d์ผ์ YTN ๋ด์ค ์์์๋๋ค.\n"))
    
    for result in results:
        search_rank_file.write(str(rank)+"์:"+result.get_text()+"\n")
        print(rank,"์ : ",result.get_text(),"\n")
        rank += 1
    ```
    
- ๋ค์ด๋ฒ ๋ฐ์ดํฐ๋ฉ 20๋ ๊ฒ์์ด
    
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
    
    print(datetime.today().strftime("%Y๋ %m์ %d์ผ์ ์ค์๊ฐ ๊ฒ์์ด ์์์๋๋ค.\n"))
    
    for result in results:
        search_rank_file.write(str(rank)+"์:"+result.get_text()+"\n")
        print(rank,"์ : ",result.get_text(),"\n")
        rank += 1
    ```
    

### ์ค๋ ๋ฐฐ์ด ๋ด์ฉ์ ๋ํด์ ์กฐ๊ธ ๋ ์๊ณ  ์ถ์๋ฐ, ์ฐธ๊ณ ํ  ๋งํ ์๋ฃ๋ ๋ญ๊ฐ ์์๊น์?

- ํฌ๋กค๋ง
    
    [ํฌ๋กค๋ง(crawling) ์ดํด ๋ฐ ๊ธฐ๋ณธ](https://www.fun-coding.org/crawl_basic2.html)
    
- header ๊ฐ, ๋์ user-agent ์กฐํ
    
    [what is my user agent](https://www.whatismybrowser.com/detect/what-is-my-user-agent/)
    
- BeautifulSoup
    
    [๋ทฐํฐํ์ํ ๋ฌธ์ - ๋ทฐํฐํ์ํ 4.0.0 ๋ฌธ์](https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/)
    
- requests
    
    [Developer Interface - Requests 2.28.1 documentation](https://requests.readthedocs.io/en/latest/api/#requests.Response)
    

### ์ค๋ ๋ฐฐ์ด ๋ด์ฉ์ ์์ผ๋ก ์ด๋์ ์ด๋ป๊ฒ ์ ์ฉํ  ์ ์์๊น์?

ํฌ๋กค๋ง์ ํตํด ์๋์ผ๋ก ๋ฐ์ดํฐ๋ฅผ ์์งํ  ์ ์๋ค.

๊ฒ์ ์ ํฌ๋ ฅ ๋ญํน ํฌ๋กค๋ง

ํ๋ก์ ํธ๋ฅผ ํ  ๋ SNS ๊ด๋ จ ์ต์  ์ ๋ณด๋ ๊ธฐ์กด์ ์๋ ๋ฐ์ดํฐ๋ฅผ ์ง์  ์ค์๊ฐ์ผ๋ก ์์ง ๊ฐ๋ฅ


<br>
<br>
<br>

# ํ๋ก์ ๐โโ๏ธ (์คํ)

### ๊ฐ์ ์ค๋ ๋ฐฐ์ด ๋ด์ฉ์ ์ ๋ฆฌํด๋ณผ๊น์? (**T**oday **I** **L**earned)

| ์ด๋ฆ | **T**oday **I** **L**earned |
| --- | --- |
| ๋ฐํ๋ฏผ | ๋ ์จ ์ ๋ณด ๊ฐ์ ธ์ค๊ธฐ, ๋ฒ์ญ, ์ด๋ฉ์ผ ๋ณด๋ด๊ธฐ(์ค๋ฅ ๋๋ฌด ๋ง์ด ๋์ ์ค์ต์ ํ๋๋ ๋ชปํ์ด์. ๋ค์ ํด๋ด์ผ๊ฒ ์ต๋๋ค) |
| ๋ฐ์์ฐ | api๋ฅผ ์ด์ฉํ์ฌ ๋ ์จ ๊ฐ์ ธ์ค๊ธฐ, ์ด๋ฉ์ผ ์ ์กํ๊ธฐ, ๋ฒ์ญํ๋ ํจ์๋ฅผ ๋ง๋ค๊ณ  ํ์ตํ์์ต๋๋ค. |
| ์ด์ ์ค | API ๊ฐ๋, ์ฌ์ฉ๋ฐฉ๋ฒ <br> API key, API doc<br>API ๋งํฌ๋ฅผ ํตํด ์์ฒญ ๋ณด๋ด๊ธฐ<br>์์ฒญ์ ๋ณด๋ผ ๋ ํ์ํ ์ ๋ณด ๋งํฌ์ ํฌํจ์ํค๋ ๋ฐฉ๋ฒ<br>json์ ์ด์ฉํ ํ์ด์ฌ ๋ฌธ์์ด์ ํ์ ๋ณ๊ฒฝ<br>lang ํ๋ผ๋ฏธํฐ ์ถ๊ฐ๋ก ์ธ์ด๋ฅผ ๋ณ๊ฒฝํ๋ ๋ฐฉ๋ฒ<br>googletrans ๋ผ์ด๋ธ๋ฌ๋ฆฌ import<br>translate ํจ์ : translate(text, dect, src)<br>SMTP : ๊ฐ๋จํ๊ฒ ์ด๋ฉ์ผ์ ๋ณด๋ด๊ธฐ ์ํ ์ฝ์<br>SMTP ์๋ฒ ์ฐ๊ฒฐ์ ์ํ ์ฌ๋ฃ : Address, Port<br>smtplib : SMTP์ ์ฝ๊ฒ ์ ๊ทผํ  ์ ์๋ ๋ผ์ด๋ธ๋ฌ๋ฆฌ<br>MIME : ๋ฉ์ผ ํ์ค. SMTP์ ์ด ํํ๋ก๋ง ๋ฉ์ผ ์์ฒญ ๊ฐ๋ฅ<br>email.message ๋ชจ๋์ EmailMessage ๊ธฐ๋ฅ ํ์ฉ<br>Header : MIME ํํ ์ค ํ๋๋ก Subject, From, To<br>๋ฉ์ผ์ ์ฌ์ง ์ฒจ๋ถํ๋ ํจ์ add_attachment<br>add_attachment ์ฌ๋ฃ : image, maintype(์ฒจ๋ถํ ํ์ผ์ ์ ํ), subtype(ํ์ฅ์)<br>binary : ์ปดํจํฐ๊ฐ ์ฝ๊ณ  ์ดํดํ๊ธฐ ๊ฐ์ฅ ํธํ ๋ฌธ์<br>imghdr : ํ์ฅ์๋ฅผ ํ์ํด์ฃผ๋ ํ์ด์ฌ ๋ด์ฅ ๋ชจ๋ |
| ๊ตฌ์ํ | Package(email, googletrans) ์ฌ์ฉ ๋ฐฉ๋ฒ์ ์ค์ต์ ํตํด ์์๋ดค๋ค.<br>API๋ฅผ ์ด์ฉํ์ฌ ์ธ๋ถ ์๋ฒ์์ ๋ฐ์ดํฐ๋ฅผ ๊ฐ์ ธ์ฌ ์ ์๋ค.<br>์ ๊ท์์ ์ด์ฉํด ์ฌ์ฉ์ ์๋ ฅ๊ฐ ์ ํ์ ์ฝ๋ ํ ์ค๋ก ํ  ์ ์๋ค.<br>json.loads() ํจ์๋ dictionary ์๋ฃํ์ return ํ๋ค. |
| ๊ถํ์ค | ๋ ์จ ์ ๋ณด ๋ฐ์์ค๊ธฐ:<br>api์ ๋ํ ๊ฐ๋ ์ดํด<br>f๋ฅผ ์ด์ฉํด ํ์คํธ์ ๋ณ์ ๋ฃ๊ธฐ<br>requests.get() ์ด์ฉํ api๋ฐ์ดํฐ ๊ฐ์ ธ์ค๊ธฐ<br>json์ ์ด์ฉํ ๋ฐ์ดํฐ str->๋์๋๋ฆฌ ํํ ์ ์ฅ<br>json ๋ด๋ถ ํน์  ๋ฐ์ดํฐ ์ถ์ถ<br>api ํ๋ผ๋ฏธํฐ ์ถ๊ฐ ์ด์ฉํด ๋ฐ์ดํฐ ํ์ ๋ฐ๊พธ๊ธฐ<br>๋ฒ์ญ๊ธฐ:<br>Translator() ์ฌ์ฉํ๋ ๋ฒ<br>translateํจ์ ์ฌ์ฉ๋ฒ<br>์ธ์ด ๊ฐ์งํ๋ ๋ฒ ๋ฐ ๋ฒ์ญํ๋ ๋ฒ<br>ํ์ด์ฌ์ผ๋ก ๋ฉ์ผ ๋ณด๋ด๊ธฐ:<br>SMTP์๋ ์๋ฆฌ<br>SMTP์๋ฒ ์ฐ๊ฒฐํ๋ ๋ฒ<br>MIME๊ฐ๋ ์ดํด& ๋ณํ ๋ฐฉ๋ฒ<br>smtp.send_message()ํจ์ ์ฌ์ฉ๋ฒ<br>read, write, append๊ธฐ๋ฅ ๊ณต๋ถ<br>์ด๋ฏธ์ง ํ์ผ ๋ฐ์ด๋๋ฆฌ ํ์ ์ ํ<br>์ ๊ท ํํ์ ํตํ ๋ฉ์ผ ์ ํจ์ฑ ๊ฒ์ฆ<br>bool ํจ์ ์ฌ์ฉ ๋ฐฉ๋ฒ |
| ๊น์งํ | 1. API<br>application programming interface<br>์์ฉ ํ๋ก๊ทธ๋๋ฐ ์ธํฐํ์ด์ค<br>ํ๋ก๊ทธ๋จ๊ณผ ํ๋ก๊ทธ๋จ์ ์ด์ด์ฃผ๋ ์ธํฐํ์ด์ค!<br>ex) api ์ฌ์ฉํ์ฌ ๋ ์จ ์ ๋ณด ์ถ๋ ฅํ๋ ํ๋ก๊ทธ๋จ<br>ํฌ๋กค๋ง์ ํ์ ์ ์ด๊ณ , ์ฌ์ดํธ์ ํ๊ธฐ๋ ๊ฒ๋ง ๊ธ์ด์ฌ ์ ์๋ ๋ฐ๋ฉด<br>api๋ ๋๊ตฐ๊ฐ ๋ง๋ค์ด๋ ํ๋ก๊ทธ๋จ์ ํตํด์ api key๋ก ๋ฐ์ดํฐ๋ฅผ ๊ฐ์ ธ์ ์ธ ์ ์๋ค<br>api doc: ์ฌ์ฉ๋ฐฉ๋ฒ ์ค๋ช์<br>https://openweathermap.org/current<br>1) ๋งํฌ๋ฅผ ๋ง๋ ๋ค<br>๊ณตํต url+?+์ฌ๋ฃ(ํ๋ผ๋ฏธํฐ)<br>2) ์๋ฒ์ ๋งํฌ๋ก ์์ฒญํ๋ค<br>requests ๋ชจ๋<br>3) ์์๊ฒ ๋ง๋ค์ด ํ์คํธ ํ์ผ๋ก ์ ์ฅ<br>json: ๋ฐ์ดํฐ๋ฅผ ์ฃผ๊ณ ๋ฐ์ ๋ ์ฌ์ฉํ๋ ํฌ๋งท<br>4) ํํ์์ ์ธ์ด, ๊ฐ ๋จ์ ๋ฑ๋ ๋ฐ๊ฟ ์ ์์<br><br>2. ๋ฒ์ญํ๊ธฐ (์ธ์ด ๊ฐ์ง/๋ฒ์ญ ๋ผ์ด๋ธ๋ฌ๋ฆฌ)<br>library: ๋ชจ๋์ ํฐ ๊ธฐ๋ฅ ๋จ์๋ก ๋ฌถ์ด๋์ ๊ฒ<br>๋ผ์ด๋ธ๋ฌ๋ฆฌ > ๋ชจ๋ > ๊ธฐ๋ฅ > ํจ์<br>Translator() : ๋ฒ์ญ๊ธฐ ๊ธฐ๋ฅ<br>detect(text) : ์ธ์ด ๊ฐ์ง<br>translate(text, dest, src) : ๋ฒ์ญํ  ๋ฌธ์ฅ, ๋ชฉ์  ์ธ์ด, ํ์คํธ ์ธ์ด(์๋ต ๊ฐ๋ฅ)<br><br>3. ํ์ด์ฌ์ผ๋ก ๋ฉ์ผ ๋ณด๋ด๊ธฐ<br>SMTP : ๊ฐ๋จํ๊ฒ ๋ฉ์ผ์ ๋ณด๋ด๊ธฐ ์ํ ์ฝ์<br>SMTP ์๋ฒ์๋ ์ฃผ์์ ํฌํธ๋ฒํธ(์ด๋ค ๋ฌธ์ ์ด๊ณ  ๋ค์ด๊ฐ๊น?)๊ฐ ์กด์ฌ<br>https://velog.io/@smearth18/๋ฉ์์ด์ฌ์์ฒ๋ผ-ai-์ค์ฟจ-220916 |


### ํ๋ก์ ํธ ๊ฒฐ๊ณผ๋ฌผ์ ๋ณด์ฌ์ฃผ์ธ์.

- ๋ ์จ์ ๋ณด ๋ฐ์์ค๊ธฐ
    
    ```python
    import requests
    import json
    
    city = "Seoul"
    apikey = "################################"
    lang = "kr"
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"
    
    result = requests.get(api)
    
    data = json.loads(result.text)
    
    # ์ง์ญ : name
    print(data["name"],"์ ๋ ์จ์๋๋ค.")
    # ์์ธํ ๋ ์จ : weather - description
    print("๋ ์จ๋ ",data["weather"][0]["description"],"์๋๋ค.")
    # ํ์ฌ ์จ๋ : main - temp
    print("ํ์ฌ ์จ๋๋ ",data["main"]["temp"],"์๋๋ค.")
    # ์ฒด๊ฐ ์จ๋ : main - feels_like
    print("ํ์ง๋ง ์ฒด๊ฐ ์จ๋๋ ",data["main"]["feels_like"],"์๋๋ค.")
    # ์ต์  ๊ธฐ์จ : main - temp_min
    print("์ต์  ๊ธฐ์จ์ ",data["main"]["temp_min"],"์๋๋ค.")
    # ์ต๊ณ  ๊ธฐ์จ : main - temp_max
    print("์ต๊ณ  ๊ธฐ์จ์ ",data["main"]["temp_max"],"์๋๋ค.")
    # ์ต๋ : main - humidity
    print("์ต๋๋ ",data["main"]["humidity"],"์๋๋ค.")
    # ๊ธฐ์ : main - pressure
    print("๊ธฐ์์ ",data["main"]["pressure"],"์๋๋ค.")
    # ํํฅ : wind - deg
    print("ํํฅ์ ",data["wind"]["deg"],"์๋๋ค.")
    # ํ์ : wind - speed
    print("ํ์์ ",data["wind"]["speed"],"์๋๋ค.")
    ```
    
- ๋ฒ์ญํ๊ธฐ
    
    ```python
    from googletrans import Translator
    
    translator = Translator()
    
    sentence = input("๋ฒ์ญ์ ์ํ๋ ๋ฌธ์ฅ์ ์๋ ฅํด์ฃผ์ธ์ : ")
    dest = input("์ด๋ค ์ธ์ด๋ก ๋ฒ์ญ์ ์ํ์๋์? : ")
    
    result = translator.translate(sentence, dest)
    detected = translator.detect(sentence)
    
    print("============์ถ ๋ ฅ ๊ฒฐ ๊ณผ============")
    print(detected.lang,":",sentence)
    print(result.dest,":",result.text)
    print("=================================")
    ```
    
- ๋ฉ์ผ ๋ณด๋ด๊ธฐ
    
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
            print("์ ์์ ์ผ๋ก ๋ฉ์ผ์ด ๋ฐ์ก๋์์ต๋๋ค.")
        else:
            print("์ ํจํ ์ด๋ฉ์ผ ์ฃผ์๊ฐ ์๋๋๋ค.")
    
    message = EmailMessage()
    message.set_content("์ฝ๋๋ผ์ด์ธ ์์์ค์๋๋ค.")
    
    message["Subject"] = "์ด๊ฒ์ ์ ๋ชฉ์๋๋ค."
    message["From"] = "###@gmail.com"
    message["To"] = "###@gmail.com"
    
    with open("codelion.png","rb") as image:
        image_file = image.read()
    
    image_type = imghdr.what('codelion',image_file)
    message.add_attachment(image_file,maintype='image',subtype=image_type)
    
    smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
    smtp.login("###@gmail.com","######")
    
    # ๋ฉ์ผ์ ๋ณด๋ด๋ sendEmail ํจ์๋ฅผ ํธ์ถํด์ ์คํํด๋ณด๊ธฐ
    sendEmail("###@gmail.com")
    smtp.quit()
    ```
    

### ์ค๋ ๋ฐฐ์ด ๋ด์ฉ์ ๋ํด์ ์กฐ๊ธ ๋ ์๊ณ  ์ถ์๋ฐ, ์ฐธ๊ณ ํ  ๋งํ ์๋ฃ๋ ๋ญ๊ฐ ์์๊น์?

- ์ด๋ฉ์ผ์ ์ฌ์ง ์ฒจ๋ถ ์์ฉ ์๋ฃ
    
    [Python 22(์ด๋ฉ์ผ์ ์ฌ์ง์ฒจ๋ถ)](https://velog.io/@gcgang0303/Python-22%EC%9D%B4%EB%A9%94%EC%9D%BC%EC%97%90-%EC%82%AC%EC%A7%84%EC%B2%A8%EB%B6%80)
    
- googletrans `AttributeError: 'NoneType' object has no attribute 'group'` ํด๊ฒฐ ๋ฐฉ๋ฒ
    
    [googletrans AttributeError](https://velog.io/@kir315/googletrans-%EC%98%A4%EB%A5%98-%ED%95%B4%EA%B2%B0)
    
- ์ ๊ทํํ์
    
    [์ ํ ํฌ ํ์ด์ฌ](https://wikidocs.net/4308)
    
- Python ๋ฌธ์์ด ํฌ๋งทํ ์ฌ๋ฌ๊ฐ์ง ๋ฐฉ๋ฒ๋ค
    
    [[Python] ๋ฌธ์์ด ํฌ๋งทํ ๋ฐฉ๋ฒ๋ค (%, str.format, f-string)](https://brownbears.tistory.com/421)
    

### ์ค๋ ๋ฐฐ์ด ๋ด์ฉ์ ์์ผ๋ก ์ด๋์ ์ด๋ป๊ฒ ์ ์ฉํ  ์ ์์๊น์?

- ํ๋ก์ ํธ์ ํ์ํ ๋ฐ์ดํฐ๋ฅผ api๋ก ๊ฐ์ ธ์ ์ฌ์ฉํ  ์ ์๋ค.
- ์ ๊ท์์ ์ด์ฉํ์ฌ ์ฌ์ฉ์ ์๋ ฅ๊ฐ์ ๋ํด ์ ์ฝ ์กฐ๊ฑด์ ๋ง๋ค ์ ์๋ค.