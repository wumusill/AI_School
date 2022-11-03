# 🦁 TIL

## ✅ Titanic
> python0501 & 0502 <br>

[Titanic 데이터 출처](https://www.kaggle.com/competitions/titanic/data)
* Kaggle data 활용, submission 실습
* 하루 10번까지 제출 가능   
* 서버 무리, 점수 조작, 어뷰징 방지     

<br>

### - 데이터 셋이 너무 클 경우 column 차이를 알아보는 방법
```python
set(train.columns) - set(test.columns)

>>> {'Survived'}
```

<br>

### - Accuracy : 정확도
$Accuracy = \frac{올바르게 예측한 샘플 개수}{전체 샘플 개수} = \frac{TP + TN}{TP + TN + FP + FN}$

<br>

### - 데이터 전처리
* `object` type은 학습에 사용할 수 없음 : 머신러닝 내부에서 연산을 할 수 없음 ➡️ 수치 데이터로 변환
* 성별 데이터를 사용하기 위해 `binary encoding` = 0과 1을 사용하여 인코딩하는 기법
* 머신러닝 알고리즘에서 `bool` 값은 수치 데이터 취급
  ```python
    train["Gender"] = train["Sex"] == 'female'
    test["Gender"] = test["Sex"] == 'female'

    >>> {"male":False, "female":True}
  ```

* `feature engineering` 많이 할수록 높은 점수 보장 X ➡️ 더 낮아질 수 있음
* 도메인 지식, EDA를 통해 예측값에 중요한 역할을 하는 변수를 찾아 전처리 해주어야 성능 향상

<br>

### - y_test가 없을 때 Accuracy를 측정하는 방법
* `hold out validation`
  * `valid`가 한 조각
* `cross val predict`
  * `valid`가 여러 조각


<br>

## ✅ 지니 불순도 & 엔트로피 

* 지니 불순도 & 엔트로피를 사용하는 목적
  * 분류의 품질을 평가하기 위해

### - 지니 불순도
* 지니 불순도는 집합에 이질적인 것이 얼마나 섞였는지 측정하는 지표
* CART 알고리즘에서 사용
* 무작위로 label을 추정할 때 틀릴 확률
* 집합에 있는 항목이 모두 같다면 지니 불순도 = 0
* 최악은 정확하게 반씩 섞여 있는 경우 = 0.5


### - 로그(log)
* 지수 함수의 역함수
* 어떤 수를 나타내기 위해 고정된 밑을 몇 번 곱하여 하는지 나타냄
* **x가 1일 때 y는 0**
* **x는 0보다 큰 값을 가짐**
* **x가 1보다 작을 때 y는 마이너스 무한대로 수렴**
### - 엔트로피 : 정보획득량

* [위키백과 : 정보 엔트로피](https://ko.wikipedia.org/wiki/%EC%A0%95%EB%B3%B4_%EC%97%94%ED%8A%B8%EB%A1%9C%ED%94%BC)
* ID3, C4.5, C5.0 트리 생성 알고리즘에서 사용
* 정보 획득량은 정보 이론의 엔트로피의 개념에 근거
* 기술적인 관점에서 보면 정보는 발생 가능한 사건이나 메시지의 확률 분포의 음의 로그로 정의
* 각 사건의 정보량은 그 기댓값, 또는 평균이 섀넌 엔트로피인 확률변수를 형성
  * 섀넌의 엔트로피
    * 2 개의 공정한 동전을 던질 때 정보 엔트로피는 발생 가능한 모든 결과의 개수에 밑이 2 인 로그를 취한 것
    * 2 개의 동전을 던지면 4 가지 결과가 발생할 수 있고, 엔트로피는 2 비트 
    * 일반적으로 정보 엔트로피는 모든 발생가능한 결과의 평균적인 정보

<br>

* 클래스가 많아지면 로그의 밑은 동일하되 엔트로피 최댓값이 달라짐
  * 클래스 ➡️ 분류되는 범주
    * 암이다 아니다  ➡️ 이진 분류
    * 생존 여부 ➡️ 이진 분류
    * 쇼핑 카테고리 19개 ➡️ 19개로 클래스로 분류
* 클래스를 예측할 때 True, False로 예측하기 함
* 멀티클래스의 경우 특정 클래스의 확률을 예측하기도 함
* 다중 클래스 분류 모델을 평가하는 `logloss`라는 공식 사용, 엔트로피와 비슷하지만 다름

|클래스 개수|최소 엔트로피|최대 엔트로피|
|:------:|:--------:|:-------:|
|2|0|1|
|8|0|3|
|16|0|4|
|6|0|2.5849..|


$$ I_E(f) = -\sum^m_{i=1}f_i\log_2f_i $$
* 이진 분류의 엔트로피 예시
```python
# 엔트로피 - 확실하게 구분이 될 때, 불확실성이 낮을 때, 이진 분류의 경우 최상의 값
# 뒷쪽 확률에 1/2을 적어준 이유는
# 0으로 나누기 오류가 발생하기 때문에 결과값이 nan 으로 나와서 결과를 설명하기 위해 작은 값을 넣음
# 하지만 0과 곱하기 때문에 무엇을 넣어도 사라짐
- ((2/2) * np.log2(2/2) + (0/2) * np.log2(1/2))
- ((2/2) * np.log2(2/2))
>>> -0.0

# 엔트로피 - 구분이 되지 않을 때, 불확실성이 높을 때, 이진 분류의 경우 최악의 값
- ((1/2) * np.log2(1/2) + (1/2) * np.log2(1/2))
>>> 1.0

# 두 종류의 데이터가 50개 중에 1개 & 50개 중 49개
- ((1/50) * np.log2(1/50) + (49/50) * np.log2(49/50))
>>> 0.14144054254182067
```


* 클래스가 3개일 때
```python
# 최상의 경우
- ((3/3) * np.log2(3/3) + (0/3) * np.log2(1/3) + (0/3) * np.log2(1/3))
>>> -0.0

# 최악의 경우
- ((1/3) * np.log2(1/3) + (1/3) * np.log2(1/3) + (1/3) * np.log2(1/3))
>>> 1.584962500721156

# 엔트로피 최댓값
np.log2(3)
>>> 1.584962500721156
```


<br>

## ✅ One-Hot Encoding
> python0503 <br>

[pandas get_dummies 공식 문서](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html) 


### - One-hot encoding이란
* 범주형 데이터일 때, 각 카테고리를 하나의 새로운 열로 만들어 주는 방법
  
### - One-Hot Encoding을 하는 이유
* 많은 머신러닝 알고리즘은 **입력 변수의 값이 수치형 데이터**여야 함
* 그래야 손실 함수, 경사 하강법 등을 적용할 수 있음
> * ex) {"A형" : 1, "B형" : 2, "O형" : 3, "AB형" : 4} == `Ordinal-Encoding`
> * 하지만 위와 같이 변경하면 혈액형 사이에 크고 작다는 개념과 순서가 생김
> * 엉뚱한 관계가 생기는 것을 방지하면서 수치형 데이터로 변환하기 위한 방법이 `One-Hot Encoding`

### - One-Hot Encoding 전 데이터 전처리
* 데이터 전처리를 할 때는 **train을 기준으로 진행**
* 현실 세계의 test는 아직 모르는 데이터이기 때문
* train 에만 등장하는 호칭은 학습을 해도 test 에 없기 때문에 예측에 큰 도움이 되지 않음
* train 에만 등장하는 호칭은 피처로 만들어 주게 되면 피처의 개수 늘어남
* 불필요한 피처가 생기기도 하고 데이터의 크기가 커지기 때문에 학습에 오랜 시간 소요
* train과 test의 **피처 개수가 같아야 함, 다르면 오류**
* 원핫 인코딩을 할 때 train, test **피처의 개수와 종류**가 같은지 확인해야 함
* 너무 적게 등장하는 값을 피처로 만들면 일반화에 문제, 오버피팅 문제 발생



### - `sklearn` vs `pandas`
* `sklearn`을 사용하게 되면 일단 학습을 하고 전처리
* 어떤 피처가 있는지 확인하고 test에 없는 값이라면 해당 피처를 생성


* `pandas`의 `get_dummies`를 사용하면 train, test 각각 전처리를 하기 때문에 다른 값이 있다면 다른 컬럼으로 생성
* 피처가 만들어지고 나서 다른 컬럼은 제외해주는 방법도 있음
* 수치형 데이터는 제외하고 범주형 데이터만 알아서 Encoding 진행


<br>

> ❗️ 주의할 점 <br>
> * 현실 세계에세 분석하는 데이터에 함부로 결측치를 채우는 것에 주의해야 함
> * 머신러닝 알고리즘에서 오류가 발생하지 않게 하기 위해 결측치를 채우는 것
> * 분석할 때도 채운다고 생각하면 안됨


<br>

### - kaggle 점수와 `cross validation` 점수가 다르다면 <br>
* `cross validation` 점수가 더 높다면 ➡️ `train data`에 과적합


<br>

## ✅ 보간법
> python0504 <br>

[pandasa 보간법, interpolate 공식 문서](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html)

* 이전 값과 다음 값을 이용하여 결측치를 채움
* 대부분 시계열 데이터에서 데이터가 순서대로 있을 때 사용
* 데이터가 앞, 뒤 값에 영향을 받는 데이터일 경우 사용 
  * ex) 주식 데이터, 순서가 있는 센서 데이터

<br>

### - `df.fillna(method=)`
```python
# method로 채우는 방법
# 앞에 있는 값으로 결측치 채움
train["Age_ffill"] = train["Age"].fillna(method="ffill")
# 뒤에 있는 값으로 결측치 채움
train["Age_bfill"] = train["Age"].fillna(method="bfill")
train[["Age", "Age_ffill", "Age_bfill"]]
```


<br>

### - `interpolate`
  
```python
# forward 방향으로 채우게 되면 맨 앞이 결측치일 경우 채워지지 않음
train["Age"].interpolate(method="linear", limit_direction="forward")

# both는 위, 아래 결측치를 모두 채우고 나머지는 채울 방향 설정
train["Age_interpolate"] = train["Age"].interpolate(method="linear", limit_direction="both")
```