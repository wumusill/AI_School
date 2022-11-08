# 🦁 TIL

## ✅ Bike Sharing

[데이터 출처](https://www.kaggle.com/competitions/bike-sharing-demand)

### - 데이터 해석
* `datetime` - hourly date + timestamp
* `season`
  * 1 = spring 
  * 2 = summer
  * 3 = fall 
  * 4 = winter 
* `holiday` - whether the day is considered a holiday
* `workingday` - whether the day is neither a weekend nor holiday
* `weather` 
  * 1: Clear, Few clouds, Partly cloudy, Partly cloudy
  * 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
  * 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
  * 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog 
* `temp` - temperature in Celsius
* `atemp` - "feels like" temperature in Celsius
* `humidity` - relative humidity
* `windspeed` - wind speed
* `casual` - number of non-registered user rentals initiated
* `registered` - number of registered user rentals initiated
* `count` - number of total rentals

> train.describe() <br>
> * `casual`, `registered`의 max가 mean에 비해 큼 ➡️ 이상치 가능성
> * `windspeed`, `humidity`의 min이 0임 ➡️ 결측치가 0으로 채워져 있을 가능성


<br>

* 학습할 데이터가 커서 오래 걸린다면 10% ~ 20% 샘플링 후 cross validation하는 것도 방법

<br>

### - `RandomForestRegressor`
  * `criterion`의 기본값만 `squared_error`
  * 나머지는 `RandomForestClassifier`와 동일

<br>

### - `RMSLE (Root Mean Squared Log Error)`

$$ RMSLE = \sqrt{\frac{1}{n}\sum^n_{i=1}(\log(p_i+1) - \log(a_i+1))^2} $$

```python
sns.kdeplot(np.log(train["count"] + 1))
sns.kdeplot(np.log1p(train['count']))
```

* `RMSE`와 거의 비슷하지만 오차를 구하기 전 예측값과 실제값에 로그를 취해주는 것만 다름
* 최솟값과 최댓값의 차이가 큰 값에 주로 사용 ex) 부동산 가격
* log를 취하면
  * 데이터의 스케일 감소
  * skewed 값이 덜 skewed하게, 덜 찌그러지게 됨
  * 분포가 좀 더 정규분포에 가까워지기도 함
* 1을 더한 뒤 log를 취하는 이유?
  * X가 1보다 작으면 음수가 나오기 때문
  * 1을 더해서 1 이하의 값이 나오지 않게 하기 위해



#### RMSLE의 특징
[참고 자료](https://steadiness-193.tistory.com/277)
* 이상치에 덜 민감하다 : 이상치가 있더라도 값의 변동폭이 크지 않음
* **상대적 Error를 측정**
  * 값의 절대적 크기가 커지면 RMSE의 값도 커지지만, RMSLE는 **상대적 크기가 동일하다면 RMSLE의 값도 동일**
  > * 예측값 = 100, 실제값 = 90일 때, RMSLE = 0.1053, RMSE = 10
    > * 예측값 = 10,000, 실제값 = 9,000일 때, RMSLE = 0.1053, RMSE = 1,000
* 실제값보다 예측값이 클 때보다, 예측값이 더 작을 때 (Under Estimation) 더 큰 패널티를 부여

> * MAE: 가중치 없음(제곱, 로그 둘 다 없음)
> * RMSE: 오차가 클수록 가중치를 주게 됨(오차 제곱의 효과)
> * RMSLE: 오차가 작을수록 가중치를 주게 됨(로그의 효과)


<br>
<br>

## ✅ Bike-log

* log를 취해주면 한쪽에 몰려있고, 뾰족한 분포가 좀 더 완만하고, 정규분포에 가까운 모습이 됨
* 마이너스 값에 로그를 취하고 싶다면?
  * 가장 작은 값이 1이 되도록 전체 값에 더해줌
> 정규분포가 왜 좋은 것인가❓ <br>
>   * 머신러닝, 딥러닝에서 대체로 더 좋은 성능을 냄
>   * 값을 볼 때 한쪽에 치우치고 뾰족하다면 특성을 제대로 학습하기가 어려움
>   * 정규분포로 되어 있다면 특성을 고르게 학습할 수 있음

<br>

### - `np.exp`

[np.exp 공식 문서](https://numpy.org/doc/stable/reference/generated/numpy.exp.html) <br>
[참고 자료](https://codetorial.net/numpy/functions/numpy_exp.html)

* `np.exp` 는 지수함수
* `np.log` 를 이용하여 로그를 취했던 값을 다시 원래대로 복원
* `log` 를 취할 때는 1을 더하고 로그를 취했는데 지수함수를 적용할 때는 반대로 지수함수를 취하고 1을 뺌
> ❓왜 지수함수를 취할까❓ <br>
>   * feature에 log를 취하고 예측된 값을 다시 복원하기 위해

```python
# +1 후 로그
train["count_log1p"] = np.log(train["count"] + 1)

# 지수함수 취해주고 -1 == train["count"]
train["count_expml"] = np.exp(train["count_log1p"]) - 1
```


> ❓실무에서 어떤 평가지표를 사용해야할지 스스로 결정해야할텐데, 여러가지 평가지표를 사용하나요 아니면 데이터를 보고 분석 전에 결정하나요❓ <br>
>   * 실무에서는 보통 비즈니스 평가지표를 더 많이 사용
>   * 경진대회나 실습에서 사용하는 평가지표는 모델의 성능을 측정해서 객관화를 위해 사용
>   * 모델을 만드는 목적은 비즈니스 문제 해결
>   * 모델의 목적이 DAU(Daily Active User)를 올리는 것이라면 DAU를 측정
>   * 매출을 늘리고 싶다면 매출액이 늘어났는지, 구매자수가 늘어났는지 등을 평가

<br>

### - `RandomizedSearchCV`
```python
from sklearn.model_selection import RandomizedSearchCV

param_distributions = {
    "n_estimators":np.random.randint(100, 1000, 10),
    "max_depth":np.random.randint(3, 14, 5),
    "max_features":np.random.uniform(0.5, 1, 5)
}

# RMSE를 이용하지만, 이미 count에 log를 취해 주었기 때문에 RMSLE로 계산하는 것과 동일
reg = RandomizedSearchCV(model, param_distributions=param_distributions, 
                   scoring="neg_root_mean_squared_error", n_iter=10, cv=5, verbose=2, random_state=42)

reg.fit(X_train, y_train)
```

```python
# scoring 파라미터에 들어갈 수 있는 값 조회
import sklearn

sklearn.metrics.SCORERS.keys()
```

```python
# score가 음수
# neg(ative)_root_mean_squared_error
# 추측 : 아마도 정렬을 위해 앞에 음수를 붙여준 것이 아닐까
reg.best_score_

>>> -0.5875572401188127
```

> * 피처를 추가하고 제외하는 것은 EDA 를 하고 적용해 보는 것도 중요하지만
> * 직접 모델에 추가하고 제거해 보면서 검증해 보는 것도 좋은 방법