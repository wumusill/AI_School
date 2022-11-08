# 🦁 Wine quality

* [필사 원본 링크](https://www.kaggle.com/code/vishalyo990/prediction-of-quality-of-wine/notebook)

### 데이터 해석 
* index : 구분자
* quality : 품질
* fixed acidity : 산도
* volatile acidity : 휘발성산
* citric acid : 시트르산
* residual sugar 잔당 : 발효 후 와인 속에 남아있는 당분
* chlorides : 염화물
* free sulfur dioxide : 독립 이산화황
* total sulfur dioxide : 총 이산화황
* density : 밀도
* pH : 수소이온농도
* sulphates : 황산염
* alcohol : 도수
* type : 종류

<br>

## ✅ 데이터 전처리 : 연속형을 범주형으로 변환
[참고 자료](https://rfriend.tistory.com/521)


### - `pd.cut()`
* `bins=(a, b)` : a 초과 b 이하
* bin 범위 밖의 값은 `NaN`
* label option으로 사용자 지정 가능
* return a list of categories with labels

```python
df = pd.DataFrame({'col': np.arange(10)})

bins=(0, 5, 8)
pd.cut(df["col"], bins=bins)

>>> 0           NaN
    1    (0.0, 5.0]
    2    (0.0, 5.0]
    3    (0.0, 5.0]
    4    (0.0, 5.0]
    5    (0.0, 5.0]
    6    (5.0, 8.0]
    7    (5.0, 8.0]
    8    (5.0, 8.0]
    9           NaN
    Name: col, dtype: category
    Categories (2, interval[int64, right]): [(0, 5] < (5, 8]]
```
<br>


## ✅ `LabelEncoder()`
[참고 자료](https://mizykk.tistory.com/10)

* `One-Hot-Encoder`와 달리 하나의 열에 서로 다른 숫자를 입력

```python
from sklearn.preprocessing import LabelEncoder


labelenc = LabelEncoder()

df["col"] = labelenc.fit_transform(df["col"])
```




<br>

## ✅ `classification_report` 해석
[참고 자료](https://velog.io/@ljs7463/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%EB%AA%A8%EB%8D%B8-%ED%8F%89%EA%B0%80%EC%A0%95%EB%B0%80%EB%8F%84%EC%9E%AC%ED%98%84%EC%9C%A8f1-score%EB%93%B1)

### - 정밀도, Precision
  * Positive로 예측한 경우 중 실제로 Positive인 비율
  * 예측값이 얼마나 정확한가 
  * TP / (TP + FP)
### - 재현율, Recall
  * 실제로 Positive인 것 중 올바르게 Positive를 맞춘 것의 비율
  * 실제 정답을 얼마나 맞췄는가
  * TP / (TP + FN)
  
> 예시 <br>
> * 암 검사의 경우 재현율이 중요
> * 실제로 암인데 암이 아니라고 예측하면 큰일나기 때문
> * 스팸 메일 여부 판단의 경우 정밀도가 중요


### - f1-score
* Precision과 Recall의 조화평균으로 분류 클래스 간의 데이터가 불균형이 심각할 때 사용
* 정확도의 경우, 데이터 분류 클래스가 균일하지 못하면 성능 발휘 불가능
* 높을수록 좋은 모델
* 2 * precision * recall / (precision + recall)

<br>

## ✅ ML
### - SVC
[참고 자료](https://inuplace.tistory.com/600)

### - SGDClassifier
[참고 자료](https://codingsmu.tistory.com/97)

<br>

## ✅ skew, 왜도

* 왜도를 조절해야하는 이유 
  * 이상치를 제거하기 위함
* 분류에서는 정규분포를 맞춰야하는가?
* 정규분포로 맞추는 이유
  * 스케일을 통해 범위를 좁혀서 모델이 좀 더 잘 예측하게 하기 위해