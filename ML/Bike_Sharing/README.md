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



* 마이너스 값에 로그를 취하고 싶다면?
  * 가장 작은 값이 1이 되도록 전체 값에 더해줌