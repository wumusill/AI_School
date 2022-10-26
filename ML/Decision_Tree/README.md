# 🦁 TIL


## ✅ Decision Tree : 결정 트리


### 결정 트리 학습법
> decision_tree.ipynb

* `CART = Classification And Regression Tree` : 분류와 회귀 모두 가능한 알고리즘
* 관측값과 목표값을 연결시켜주는 예측 모델
* 분류트리 : 트리 모델 중 목표 변수가 유한한 수의 값을 가짐
* 회귀트리 : 결정 트리 중 목표 변수가 연속하는 값을 가짐, 일반적으로 실수


### 결정 트리 장점
* 결과를 해석하고 이해하기 쉬움
* 자료를 가공할 필요가 거의 없음
* 수치 자료와 범주 자료 모두 적용 가능
* 화이트박스 모델을 사용
* 안정적, 직관적
* 대규모 데이터 셋에도 잘 동작
* 학습 속도가 빠름

### 결정 트리 단점
* 과적합 가능성이 높음
* 결과 또는 성능의 변동 폭이 큼
* 랜덤성에 따라 매우 다름 ➡️ 일반화하여 사용하기 어려움
* 계층적 접근 방식이기 때문에 중간에 에러가 발생하면 다음 단계로 에러 전파

<br> 

## ✅ Feature Engineering
* `hyper parameter tuning`보다 `feature scaling`이 더 드라마틱한 변화를 불러옴

### 수치형 변수를 범주형 변수로 만들기
* 머신러닝 알고리즘에게 힌트 제공
* 결정 트리의 오버피팅 방지
  * 조건들이 잘게 나누어지는 것을 방지


### 결측치
* `NaN` 은 모델에 학습 불가능

### 이상치 제거

> 무조건 성능이 개선되는 것은 아님 <br>
> 다양한 시도 필요


<br> 

## ✅ Random Forest : Bagging
* `Bootstrap aggregating`의 약자
* 부트스트랩을 통해 조금씩 다른 훈련 데이터에 대해 훈련된 기초 분류기(base learner) 들을 결합시키는 방법
* 부트스트랩이란, 주어진 훈련 데이터에서 중복을 허용하여 원 데이터 셋과 같은 크기의 데이터 셋을 만드는 과정 
* 가장 중요한 파라미터는 트리의 개수
* 결정 트리가 가진 단점을 극복하고 좋은 일반화 성능을 갖도록 함


* 월등히 높은 정확성
* 간편하고 빠른 학습 및 테스트
* 변수 소거 없이 수천 개의 입력 변수들 다루는 것이 가능
* 다중 클래스 알고리즘 특성
* 임의화를 통한 좋은 일반화


* 시각화가 어렵다는 단점
  * [랜덤 포레스트 시각화 라이브러리](https://github.com/andosa/treeinterpreter)



<br> 

## ✅ Cross_Validation : 교차 검증
### - Hold-out Cross_Validation
* 특정 비율로 train/test data를 1회 분할하는 방법

#### 장점
* 빠른 속도
#### 단점
* 신뢰도가 떨어짐

<br>

### - K-Fold Cross_Validation
* 전체 데이터를 K개로 나누어 K번 서로 다른 1개의 셋을 test data로 사용

```python
cross_val_predict(
    estimator,
    X,
    y=None,
    *,
    groups=None,
    cv=None,
    n_jobs=None,
    verbose=0,
    fit_params=None,
    pre_dispatch='2*n_jobs',
    method='predict',
)

# cv = number of fold
# verbose : 로그를 찍을지 말지, 숫자가 높을수록 상세
```

#### 장점
* 높은 신뢰도
* 모든 데이터를 train/test에 활용하여 과소적합/과적합 방지
#### 단점
* 느린 속도 : 랜덤 포레스트로 학습한다면 `(트리의 수 * 폴드의 수)` 만큼 오래 걸림

<br>

### 오차 시각화

* `regplot`
```python
sns.regplot(x=y_train, y=y_predict)
```

* `residplot`
```python
# 오차를 시각화, 0애 가까워야 좋은 것
sns.residplot(x=y_train, y=y_predict)
```

* `r2_score` : 정확도 점수화, 1에 가까울수록 정확한 예측
```python
from sklearn.metrics import r2_score

r2_score(y_train, y_predict)

# 0.311
```
