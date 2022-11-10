# 🦁 TIL

## ✅ House Price

[데이터 출처](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/overview)

> Metric <br> 
Submissions are evaluated on Root-Mean-Squared-Error (RMSE) <br>
between the logarithm of the predicted value and the logarithm of the observed sales price. <br>
(Taking logs means that errors in predicting expensive houses and cheap houses will affect the result equally.)

<br>

### - Feature Engineering이란 
* 데이터에 대한 지식을 바탕으로 특성을 생성, 변경, 삭제하는 등 조작하여 사용하기 더 유용한 형태로 바꾸는 것

<br>

### - 기초 개념
* Feature Selection, 특성 선택
  * 전문가의 지식이나, 특성의 중요도에 따라 일부 특성을 버리거나 선택하는 것
* Feature Extraction, 특성 추출
  * 기존 특성들의 조합으로 아예 새로운 특성을 생성하는 것
  * 주성분 분석(PCA)이 특성 추출에 해당 
* Scaling, 범위 변환
  * 변수의 분포가 편향되어 있을 경우, 이상치가 많을 경우 등 여러 이유로 변수의 특성이 잘 드러나지 않아 활용이 어려울 때 변수의 범위를 바꿔주는 것
  * 트리 계열에서 Scaling은 큰 영향 미치지 않음 
* Transform, 변형
  * 기존 변수의 성질을 이용하여 새로운 변수를 생성하는 것
* Binning, 범주화
  * 연속형 변수를 범주형 변수로 변환하는 것
* Dummy, 숫자화
  * 범주형 변수를 연속형 변수로 변환하는 것

<br>


### - Feature 종류

|타입|서브타입|정의|예시|
|:----:|:----:|:----:|:----:|
|Categorical|Nominal|순서가 없는 범주형 변수|성별, 음료수 종류|
|Categorical|Ordinal|순서가 있는 범주형 변수|성적, 등급|
|Numerical|Discrete|유한하거나 개수를 헤아릴 수 있는 숫자형 변수|물건의 개수, 행동의 횟수|
|Numerical|Continuous|무한하거나 개수를 헤아릴 수 없는 숫자형 변수|물건의 가격, 시간|

<br>

### - 이상치
* Feature에서 일반적인 값 분포에서 벗어나는 경우
* 이상치를 찾는 두 가지 방법
  * 값의 범위를 지정하여 범위를 벗어나는 값 탐색
  * 데이터를 시각화하여 눈에 띄는 값 탐색


> ❓왜 이상치를 다뤄야할까❓ <br>
>   * 과대적합 우려
>   * 일반화하기 어려움
>   * 예측 정확도 저하

* `train label`에 이상치가 있다면
  * 제거 : `train`은 제거 가능, `test`는 제거 불가능
  * 평균 or 중앙값으로 대체하면 많이 왜곡될 수 있음 ex) 강남 아파트가 == 지방 아파트가 됨
    * 평균, 중앙값이 항상 정답은 아님


<br>

### - 희소값
* `Categorical Feature`에서 빈도가 낮은 값
* 일반적으로 희소값들을 적절한 값으로 대체함으로써 편리한 데이터 이용 가능
* 처리 방법
  * 결측치 처리
  * 기타 category로 묶음
> ❓왜 희소값 다뤄야할까❓ <br>
>   * 데이터 경향 파악 어려움
>   * 예측 정확도 저하
>   * 희소값에 대해 one-hot-encoding 을 하게 되면 과적합 발생
>   * 계산에 많은 자원 필요

<br>

### - 변수 스케일링
[참고 자료](https://github.com/ashishpatel26/Amazing-Feature-Engineering/blob/master/A%20Short%20Guide%20for%20Feature%20Engineering%20and%20Feature%20Selection.md)
* `Feature`의 범위를 조정하여 정규화하는 것
* `Feature`의 분산과 표준편차를 조정하여 정규분포 형태를 띄게하는 것이 목표


* `Feature`의 범위가 다르면, `Feature`끼리 비교하기 어려움
* ML 모델 성능 저하
* 일부 `Feature Scaling`은 이상치에 대해 강점
* `Robust Scaling`
  * 사분위수를 기준으로 값을 스케일링 하기 때문에 이상치 완화하는 효과


* 정보 균일도를 기반으로 되어 있기 때문에 트리기반 모델은 피처 스케일링 불필요
* 트리기반 모델은 데이터의 절대적 크기보다 상대적 크기에 영향을 받기 때문
* 스케일링을 해도 상대적 크기 관계는 같음
* 스케일링 후 시각화를 해보면 x값의 범위만 달라지고 데이터 분포는 변함 없음

<br>

### - 자주 쓰이는 스케일링 기법 3가지

* `Normalization`
  * 평균울 빼고 표준 편차로 나누기
  * 평균 == 0
  * 표준 편차 == 0
* `Min-Max Scaling`
  * 최솟값을 빼고 (최댓값 - 최솟값)으로 나누기
  * 최솟값 == 0
  * 최댓값 == 1
* `Robust Scaling`
  * 중간값을 빼고 IQR로 나누기
  * 중앙값 == 0
  * 이상치의 영향을 덜 받음
  * 중앙값이 Robust하다, 강건하다

|이름|정의|장점|단점|
|:-----:|:-----:|:-----:|:------:|
|Normalization, <br> Standardization, <br> (Z-score scaling)|평균 제거, 데이터를 <br> 분산을 1로 맞게 조정|표준 편차가 1이고 0을 중심으로 <br> 표준 정규 분포를 갖도록 조정|변수를 왜곡하거나 이상치가 있으면 <br> 관측치를 압축하여 예측력 손상|
|Min-Max Scaling|Feature를 지정된 범위로 확장하여 <br> 기능을 변환, 기본값 = [0, 1]|-|변수가 왜곡되거나 이상치가 <br> 있으면 관측치를 압축하여 예측력 손상|
|Robust Scaling|중앙값을 제거하고 분위수 범위에 <br> 따라 데이터 크기 조정|편향된 변수에 대한 변환 후 <br> 변수의 분산을 더 잘 보존, <br> 이상치 제거에 효과적|-|


```python
# Python 권장 방법
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler

# 한번에 라이브러리 불러오기
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# 정규화 코드
rs = RobustScaler()
train[["SalePrice_rs"]] = rs.fit(train[["SalePrice"]]).transform(train[["SalePrice"]])
train[["SalePrice", "SalePrice_rs"]].head()

# 정규화된 값을 다시 원래대로 복원하는 코드
rs.inverse_transform(train[["SalePrice_rs"]])
```
* fit에는 matrix 형태로 넣어줘야 함 ➡️ 대괄호 두 개 
* 반환값도 matrix, 파생변수로 만들고 싶다면 마찬가지로 대괄호 두 개


* fit 은 계산하기 위한 평균, 중앙값, 표준편차를 데이터를 기준으로 기술통계값 계산
* 그 값을 기준으로 transform 으로 값 변환
* fit 은 train 에만 사용, transform 은 train, test 에 사용
* fit 은 test 에 사용 X, train이 기준
* test 에는 train을 기준으로 학습한 것을 바탕으로 transform

<br>

### - Log Transformation
* 표준 정규분포 형태로 만들기 위해서 필요
* x값에 대해 상대적으로 작은 스케일에서는 키우고, 큰 스케일에서는 줄여주는 효과
* x값이 작을수록 y의 변화량이 큼
* x값이 클수록 y의 변화량이 작음
* 작은 숫자들 사이는 벌어지고 큰 숫자들 사이는 좁아짐
* 데이터가 고르게 분포하면 y값을 예측하기 유용
  
#### 고르게 분포된 데이터가 중요한 이유
* 1, 4분위보다 2, 3분위가 상대적으로 더 중요
* 예측하려는 값이 중간값에 가까운 값일 확률이 높음
* 일반적으로 중간값을 잘 예측하는 모델이 예측 성능이 높은 모델

> 정규 분포 vs 표준 정규 분포 <br>
> * 트리 모델은 일반 정규 분포를 사용해도 무관
> * 스케일 값이 영향을 미치는 모델에서는 표준 정규 분포가 더 나은 성능을 낼 수도 있음
> * 표준 정규 분포는 값 왜곡 가능성이 있기 때문에 주의
> * 성능 향상을 보장하지 않음
> * 상황에 맞는 변환 방법 사용

<br>

### - 이산화
* Numerical Feature를 일정 기준으로 그룹화하는 것
* ex) 10대, 20대로 나이 그룹화
* 이산화 하는 이유?
  * 직관적
  * ML 모델 성능 개선
  * 너무 세분화된 수치는 과대적합 가능성
  * 그룹화함으로써 특정 Numerical Feature의 영향 감소

<br>
  
### - 이산화 종류
|방법|정의|장점|단점|
|:----:|:----:|:----:|:----:|
|Equal width binning <br> ex) 절대평가, 히스토그램, pd.cut()|동일한 너비의 <br> 범위로 그룹화|-|편향된 분포에 민감|
|Equal frequency binning<br> ex) 상대평가, pd.qcut()|동일한 데이터 <br> 개수로 그룹화|알고리즘 성능 향상에 도움|임의의 binning은 대상과의 <br> 관계를 방해할 수 있음|

```python
train["SalePrice_cut"] = pd.cut(train["SalePrice"], bins=4, labels=[1, 2, 3, 4])
train["SalePrice_qcut"]= pd.qcut(train["SalePrice"], q=4, labels=[1, 2, 3, 4])
```

<br>
  
### - 인코딩
[참고 자료](https://techblog-history-younghunjo1.tistory.com/99)
* `Categorical Feature`를 `Numerical Feature`로 변환하는 것
* 인코딩 하는 이유?
  * 데이터 시각화에 유리
  * 머신 모델에 유리
    * 부스팅 3대장 : Xgboost, LightGBM, catBoost
    * 부스팅 3대장과 같이 범주형 데이터를 알아서 처리해 주는 알고리즘도 있지만 sklearn에서는 별도의 처리 필요


* 사이킷런을 사용할 경우 train을 기준으로 fit, test 는 transform 만 함
* test 에만 있는 값은 ohe 되지 않음
* fit 하는 기준은 꼭 train
* test 는 미래의 데이터, 어떤 데이터가 들어올지 모름


|encoding|장점|단점|
|:----:|:-----:|:-----:|
|Ordinal-Encoding|복잡하지 않고 직관적, 간단함|순서가 없는 데이터에 사용할 경우 순서, 크기를 학습하게 됨 <br> 데이터에 추가적인 가치르 더해주지 않음 <br> 일대일 대응하는 숫자로 바뀌었을 뿐 데이터 정보 자체는 동일|
|One-Hot-Encoding|Feature의 모든 정보를 유지|고유값이 너무 많은 경우 Feature를 지나치게 많이 사용|

<br>

#### pandas
```python
# Ordinal Encoding
train["MSZoning"].astype("category").cat.codes

# One-Hot-Encoding
pd.get_dummies(train["MSZoning"])
```

#### sklearn
```python
# Ordinal Encoding
oe = OrdinalEncoder()
MSZoning_oe = oe.fit_transform(train[["MSZoning"]])

# One-Hot-Encoding
enc = OneHotEncoder()
MSZoning_enc = enc.fit_transform(train[["MSZoning"]])
```

> pandas 대비 sklearn 장점 <br>
>   * get_dummies ➡️ train, test 따로 인코딩
>   * train 학습을 기반으로 test와 동일하게 feature를 생성해주어야 함
>   * 하지만 train, test feature의 수와 종류가 다를 수 있음
>   * 학습, 예측을 할 때는 동일한 개수의 피처를 입력해야 함
>   * 동일하게 맞춰주는 것이 상당히 복잡 ➡️ sklearn은 train에만 있는 feature로만 test에 알아서 적용



<br>
  
### - 다항식 전개
[polynomial 공식 문서](https://scikit-learn.org/stable/modules/preprocessing.html#polynomial-features)
* 히스토그램을 그렸을 때 어딘가는 많고 적은 데이터가 있다면 그것도 특징이 될 수 있는데
* 특징이 잘 구분되지 않는다면 power transform 등을 통해 값을 제곱을 해주거나 하면 특징이 좀 더 구분되어 보임
* 주어진 다항식의 차수 값에 기반하여 파생변수를 생성할 수 있음
* 다항식 전개하는 이유?
  * 데이터를 분석할 때 다항식 전개에 기반한 파생변수 생성 방법은 다소 유용하지 않을 수 있음
  * 원래 변수를 보는 게 더 직관적, 이해하기 쉬움
* 그러나 머신러닝 모델을 이용할 때 이것이 유용할 수 있음
* 머신러닝 모델에서 유용한 이유?
  * 머신러닝 모델은 label에 대해서 설명력이 높은 한 두가지 Feature에 의지할 때보다 여러가지 Feature에 기반할 때 성능 향상
  * 소수의 Feature에 기반하게 되면 과대적합이 일어날 확률이 높아짐