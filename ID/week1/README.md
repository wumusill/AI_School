# 🦁 TIL

## ✅ Python list vs Numpy array
| 차이점   | Python list                                                               | Numpy array                                                                           |
|-------|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| 선언 조건 | 한 `list`에 `int`, `str` 등 여러 자료형 허용, <br> 2차원 이상의 구조에서 내부 배열의 원소 개수가 달라도 됨 | `int`와 `str`이 섞이면 모두 `str`로 전환 (한 가지 자료형만 허용) <br> 2차원 이상의 구조에서 내부 배열 원소 개수는 모두 같아야 함 |
| 연산    | 덧셈 시 항목을 이어 붙임 <br> 곱셈 시 원소 복사                                            | 사칙연산 모두 항목 간 연산 수행                                                                    |
| 메소드   | `mean`, `argmax`, `round` 등 array method 지원하지 않음                          | `append`, `remove`, `extend` 등 list method를 지원하지 않음                                   |
| 연산 속도 | Numpy array에 비해 연산 속도가 느림                                                 | 연산 최적화, 같은 연산을 수행할 경우 더 빠름                                                            |

<br><br>

## ✅ 정규 표현식
* 정규 표현식은 복잡한 문자열을 처리할 때 사용하는 기법
* 파이썬의 고유 문법이 아닌, 문자열을 처리하는 모든 곳에서 사용
### - 메타 문자
* 정규 표현식에 아래 메타 문자를 사용하면 특별한 의미를 가짐
* 정규 표현식에서 상용하는 메타 문자에는 아래와 같은 것이 있다.
```python
. ^ $ * + ? { } [ ] \ | ( )
```

#### a. 문자 클래스 [ ]
* `[ ] 사이의 문자들과 매치`라는 의미
    > 문자 클래스를 만드는 메타 문자, [] 사이에는 어떤 문자도 들어갈 수 있음
  * ex) [abc]
      * `"a"` : 매치
      * `"before"` : 매치
      * `"dude"` : 매치 X


* 하이픈(-)을 사용하면 두 문자 사이의 범위(From - To)를 의미
  * ex) `[a-c] == [abc]`, `[0-5] == [012345]`
  * ex) `[a-zA-Z] == 모든 알파벳`, `[0-9] == 모든 숫자`

* 문자 클래스 [ ] 안에는 모든 문자, 메타 문자 사용 가능
* `^` 사용에는 주의 할 것 
  * `^` == `NOT`의 의미, `[^0-9]` == 문자만 매치

> [자주 사용하는 문자 클래스]
> * `\d == [0-9]` : 숫자와 매치 
> * `\D == [^0-9]` : 숫자가 아닌 것과 매치  
> * `\s == [ \t\n\r\f\v]` : whitespace 문자와 매치, 맨 앞의 빈 칸은 공백문자를 의미
> * `\S == [^ \t\n\r\f\v]` : whitespace 문자가 아닌 것과 매치 
> * `\w == [a-zA-Z0-9_]` : 문자 + 숫자와 매치
> * `\W == [^a-zA-Z0-9_]` : 문자 + 숫자가 아닌 문자와 매치
> > 대문자로 사용된 것은 소문자의 반대! <br> `whitespace 문자` : 컴퓨터에서 콘솔이나 프린터로 찍었을 때 공백을 표현하는 문자

#### b. Dot(.)
* 줄바꿈 문자인 `\n`을 제외한 모든 문자와 매치됨을 의미
    > `re.DOTALL` 옵션을 주면 `\n` 문자와도 매치
* `a.b == "a + 모든 문자 + b"`
  * `"aab"` : 매치
  * `"a0b"` : 매치
  * `"abc"` : 매치 X

> `a[.]b` 와 같이 문자 클래스 내 메타 문자가 사용된다면 이것은 문자 `"."`을 의미, `"a.b"`와 매치

#### c. 반복 (*)
* `ca*t` : a가 0부터 무한대로 반복될 수 있다는 의미
    > 사실 메모리 제한으로 2억 개 정도만 가능하단다.

* `ca*t`
  * `ct` : 매치
  * `cat` : 매치
  * `caaaaaaaaaaat` : 매치



#### d. 반복 (+)
* `ca+t` : a가 최소 1번 이상 반복

* `ca+t`
  * `ct` : 매치 X
  * `cat` : 매치
  * `caaaaaaaaaaat` : 매치

#### e. 반복 ({m, n}, ?)
* 반복의 횟수를 제한하는 방법
  * `{2}` : 2번 반복만 매치
  * `{2,}` : 2번 이상 반복만 매치
  * `{,2}` : 2번 이하 반복만 매치
* `? == {0, 1}` : 있어도 매치, 없어도 매치
* `ab?c`
  * `abc` : 매치
  * `ac` : 매치

<br>

### - re 모듈
* Python은 정규 표현식을 지원하기 위해 re(regular expression) 모듈 제공
```python
import re
p = re.compile('ab*')
```

<br>

### - 정규식을 이용한 문자열 검색
| Method     | 목적                                  |
|------------|-------------------------------------|
| match()    | 문자열의 처음부터 정규식과 매치되는지 조사             |
| search()   | 문자열 전체를 검색하여 정규식과 매치되는지 조사          |
| findall()  | 정규식과 매치되는 모든 문자열을 리스트로 return       |
| finditer() | 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 return |

* 아래와 같은 패턴으로 메소드 활용
```python
import re
p = re.compile('[a-z]+')
```

#### a. match
* 정규식에 부합하면 match 객체를 return
* 부합하지 않으면 return None
```python
m = p.match("python")
print(m)

>>> <re.Match object; span=(0, 6), match='python'>
```
```python
m = p.match("3 python")
print(m)

>>> None
```

#### b. search
```python
m = p.search("python")
print(m)

>>> <re.Match object; span=(0, 6), match='python'>
```
```python
m = p.search("3 python")
print(m)

>>> <re.Match object; span=(2, 8), match='python'>
```
#### c. findall
```python
result = p.findall("life is too short")
print(result)

>>> ['life', 'is', 'too', 'short']
```

#### d. finditer
```python
result = p.finditer("life is too short")
print(result)

for res in result:
    print(res)

>>> <callable_iterator object at 0x113f1ed60>
>>> <re.Match object; span=(0, 4), match='life'>
>>> <re.Match object; span=(5, 7), match='is'>
>>> <re.Match object; span=(8, 11), match='too'>
>>> <re.Match object; span=(12, 17), match='short'>
```

<br>

### - `match` 객체의 메소드
* 어떤 문자열이 매치되었는가?
* 매치된 문자열의 인덱스는 어디서부터 어디까지인가?

| Method  | 목적           |
|---------|--------------|
| group() | 매치된 문자열을 돌려줌 |
| start() | 매치된 문자열의 시작 위치를 돌려줌          |
| end()   | 매치된 문자열의 끝 위치를 돌려줌           |
| span()  | 매치된 문자열의 위치를 튜플로 (시작, 끝) 돌려줌 |

```python
m = p.match("python")
m.group()
>>> 'python'

m.start()
>>> 0

m.end()
>>> 6

m.span()
>>> (0, 6)
```

```python
import re

# 본 코드
p = re.compile('[a-z]+')
m = p.match("python")

# 축약형 코드
m = re.match('[a-z]+', 'python')
```


<br>

### - `compile` 옵션
* 정규식을 컴파일할 때 사용 가능한 옵션

|Option| 역할                                                            |
|------|---------------------------------------------------------------|
|DOTALL, S| 줄바꿈 문자를 포함하여 모든 문자와 매치                                        |
|IGNORECASE, I| 대소문자에 관계없이 매치                                                 |
|MULTILINE, M| 여러줄과 매치                                                       |
|VERBOSE, X| verbose 모드를 사용할 수 있도록 함 (정규식을 보기 편하게 만들 수 있고 주석등을 사용할 수 있게 됨) |


#### a. DOTALL, S
```python
p = re.compile('a.b')
m = p.match('a\nb')
print(m)

>>> None
```
```python
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)

>>> <re.Match object; span=(0, 3), match='a\nb'>
```
```python
p = re.compile('a.b', re.S)
m = p.match('a\nb')
print(m)

>>> <re.Match object; span=(0, 3), match='a\nb'>
```
#### b. IGNORECASE, I

```python
p = re.compile('[a-z]+', re.I)
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))

>>> <re.Match object; span=(0, 6), match='Python'>
>>> <re.Match object; span=(0, 6), match='Python'>
>>> <re.Match object; span=(0, 6), match='Python'>
```
#### c. MULTILINE, M
* `^` : 문자열의 처음을 의미
  * `^python` : 문자열의 처음은 항상 `python`으로 시작해야 함
* `$` : 문자열의 마지막을 의미
  * `python$` : 문자열의 마지막은 항상 `python`으로 끝나야 함

```python
# ^python\s\w+ : python이라는 문자열로 시작하고 그 뒤에 whitespace, 그 뒤에 단어가 와야 한다는 의미
p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python 
python three"""

print(p.findall(data))

>>> ['python one']
```

```python
p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python 
python three"""

print(p.findall(data))

>>> ['python one', 'python two', 'python three']
```



#### d. VERBOSE, X
* 이해하기 어려운, 길이가 긴 정규식을 주석 또는 줄 단위로 구분하기 위한 방법
* 문자열에 사용된 whitespace는 컴파일할 때 제거 (단, `[ ]`안에 사용된 whitespace는 제외)
* 줄 단위로 `#` 기호를 사용하여 주석문 작성 가능
```python
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE))
```

<br>

### - 백슬래시 (\\) 문제
* 어떤 파일 안에 있는 `\section` 문자열을 찾기 위한 정규식
* `\s` 문자가 whitespace로 해석되고 아래와 같은 의미가 됨
  * `[ \t\n\r\f\v]ection`
* 의도대로 매치하고 싶다면 다음과 같이 변경
  * `\\section`
```python
p = re.compile('\\section')
```

* `\\section` 을 찾고 싶다면 : `\\\\section`
  * 백슬래시가 너무 많으면 복잡하고 이해하기 어려움
  * 이런 문제를 해결하기 위한 규칙
    * 문자열 앞에 `r`문자를 삽입하면 백슬래시 2개 대신 1개만 써도 2개를 쓴 것과 동일한 의미
```python
re.compile(r'\\section')
```

<br>
<br>

## ✅ 데이터 종류
![자료 분류](https://blog.kakaocdn.net/dn/XAn9T/btrdC4Pn2mS/qvRvjIgzsIi1GFgCujpYrk/img.png)

### - 수치형 자료
> 관측된 값이 `수치로 측정`되는 자료
* 연속형 자료
  > 매출, 키, 몸무게와 같이 연속적인 자료
* 이산형 자료
    > 건수, 개수와 같이 값을 셀 수 있는 자료
  
### - 범주형 자료
> 관측 결과가 몇 개의 `범주 또는 항목의 형태`로 나타나는 자료
* 순위형 자료
    > 범주간 순서의 의미가 있는 자료 <br> `ex)` 선호도 : 매우좋다, 좋다, 싫다, 매우 싫다

* 명목형 자료
    > 범주간 순서의 의미가 없는 자료 <br> `ex)` 혈액형

<br>

### - 정형 데이터
> 데이터베이스의 정해진 규칙에 맞게 데이터를 들어간 데이터 중에 `수치 만으로 의미 파악이 쉬운 데이터`

### - 비정형 데이터
> 정해진 규칙이 없어서 값의 의미를 쉽게 파악하기 힘든 데이터 <br> `ex)` 텍스트, 음성, 영상
