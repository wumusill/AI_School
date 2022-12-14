# ๐ฆ TIL

## โ Bike Sharing

[๋ฐ์ดํฐ ์ถ์ฒ](https://www.kaggle.com/competitions/bike-sharing-demand)

### - ๋ฐ์ดํฐ ํด์
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
> * `casual`, `registered`์ max๊ฐ mean์ ๋นํด ํผ โก๏ธ ์ด์์น ๊ฐ๋ฅ์ฑ
> * `windspeed`, `humidity`์ min์ด 0์ โก๏ธ ๊ฒฐ์ธก์น๊ฐ 0์ผ๋ก ์ฑ์์ ธ ์์ ๊ฐ๋ฅ์ฑ


<br>

* ํ์ตํ  ๋ฐ์ดํฐ๊ฐ ์ปค์ ์ค๋ ๊ฑธ๋ฆฐ๋ค๋ฉด 10% ~ 20% ์ํ๋ง ํ cross validationํ๋ ๊ฒ๋ ๋ฐฉ๋ฒ

<br>

### - `RandomForestRegressor`
  * `criterion`์ ๊ธฐ๋ณธ๊ฐ๋ง `squared_error`
  * ๋๋จธ์ง๋ `RandomForestClassifier`์ ๋์ผ

<br>

### - `RMSLE (Root Mean Squared Log Error)`

$$ RMSLE = \sqrt{\frac{1}{n}\sum^n_{i=1}(\log(p_i+1) - \log(a_i+1))^2} $$

```python
sns.kdeplot(np.log(train["count"] + 1))
sns.kdeplot(np.log1p(train['count']))
```

* `RMSE`์ ๊ฑฐ์ ๋น์ทํ์ง๋ง ์ค์ฐจ๋ฅผ ๊ตฌํ๊ธฐ ์  ์์ธก๊ฐ๊ณผ ์ค์ ๊ฐ์ ๋ก๊ทธ๋ฅผ ์ทจํด์ฃผ๋ ๊ฒ๋ง ๋ค๋ฆ
* ์ต์๊ฐ๊ณผ ์ต๋๊ฐ์ ์ฐจ์ด๊ฐ ํฐ ๊ฐ์ ์ฃผ๋ก ์ฌ์ฉ ex) ๋ถ๋์ฐ ๊ฐ๊ฒฉ
* log๋ฅผ ์ทจํ๋ฉด
  * ๋ฐ์ดํฐ์ ์ค์ผ์ผ ๊ฐ์
  * skewed ๊ฐ์ด ๋ skewedํ๊ฒ, ๋ ์ฐ๊ทธ๋ฌ์ง๊ฒ ๋จ
  * ๋ถํฌ๊ฐ ์ข ๋ ์ ๊ท๋ถํฌ์ ๊ฐ๊น์์ง๊ธฐ๋ ํจ
* 1์ ๋ํ ๋ค log๋ฅผ ์ทจํ๋ ์ด์ ?
  * X๊ฐ 1๋ณด๋ค ์์ผ๋ฉด ์์๊ฐ ๋์ค๊ธฐ ๋๋ฌธ
  * 1์ ๋ํด์ 1 ์ดํ์ ๊ฐ์ด ๋์ค์ง ์๊ฒ ํ๊ธฐ ์ํด



#### RMSLE์ ํน์ง
[์ฐธ๊ณ  ์๋ฃ](https://steadiness-193.tistory.com/277)
* ์ด์์น์ ๋ ๋ฏผ๊ฐํ๋ค : ์ด์์น๊ฐ ์๋๋ผ๋ ๊ฐ์ ๋ณ๋ํญ์ด ํฌ์ง ์์
* **์๋์  Error๋ฅผ ์ธก์ **
  * ๊ฐ์ ์ ๋์  ํฌ๊ธฐ๊ฐ ์ปค์ง๋ฉด RMSE์ ๊ฐ๋ ์ปค์ง์ง๋ง, RMSLE๋ **์๋์  ํฌ๊ธฐ๊ฐ ๋์ผํ๋ค๋ฉด RMSLE์ ๊ฐ๋ ๋์ผ**
  > * ์์ธก๊ฐ = 100, ์ค์ ๊ฐ = 90์ผ ๋, RMSLE = 0.1053, RMSE = 10
    > * ์์ธก๊ฐ = 10,000, ์ค์ ๊ฐ = 9,000์ผ ๋, RMSLE = 0.1053, RMSE = 1,000
* ์ค์ ๊ฐ๋ณด๋ค ์์ธก๊ฐ์ด ํด ๋๋ณด๋ค, ์์ธก๊ฐ์ด ๋ ์์ ๋ (Under Estimation) ๋ ํฐ ํจ๋ํฐ๋ฅผ ๋ถ์ฌ

> * MAE: ๊ฐ์ค์น ์์(์ ๊ณฑ, ๋ก๊ทธ ๋ ๋ค ์์)
> * RMSE: ์ค์ฐจ๊ฐ ํด์๋ก ๊ฐ์ค์น๋ฅผ ์ฃผ๊ฒ ๋จ(์ค์ฐจ ์ ๊ณฑ์ ํจ๊ณผ)
> * RMSLE: ์ค์ฐจ๊ฐ ์์์๋ก ๊ฐ์ค์น๋ฅผ ์ฃผ๊ฒ ๋จ(๋ก๊ทธ์ ํจ๊ณผ)


<br>
<br>

## โ Bike-log

* log๋ฅผ ์ทจํด์ฃผ๋ฉด ํ์ชฝ์ ๋ชฐ๋ ค์๊ณ , ๋พฐ์กฑํ ๋ถํฌ๊ฐ ์ข ๋ ์๋งํ๊ณ , ์ ๊ท๋ถํฌ์ ๊ฐ๊น์ด ๋ชจ์ต์ด ๋จ
* ๋ง์ด๋์ค ๊ฐ์ ๋ก๊ทธ๋ฅผ ์ทจํ๊ณ  ์ถ๋ค๋ฉด?
  * ๊ฐ์ฅ ์์ ๊ฐ์ด 1์ด ๋๋๋ก ์ ์ฒด ๊ฐ์ ๋ํด์ค
> ์ ๊ท๋ถํฌ๊ฐ ์ ์ข์ ๊ฒ์ธ๊ฐโ <br>
>   * ๋จธ์ ๋ฌ๋, ๋ฅ๋ฌ๋์์ ๋์ฒด๋ก ๋ ์ข์ ์ฑ๋ฅ์ ๋
>   * ๊ฐ์ ๋ณผ ๋ ํ์ชฝ์ ์น์ฐ์น๊ณ  ๋พฐ์กฑํ๋ค๋ฉด ํน์ฑ์ ์ ๋๋ก ํ์ตํ๊ธฐ๊ฐ ์ด๋ ค์
>   * ์ ๊ท๋ถํฌ๋ก ๋์ด ์๋ค๋ฉด ํน์ฑ์ ๊ณ ๋ฅด๊ฒ ํ์ตํ  ์ ์์

<br>

### - `np.exp`

[np.exp ๊ณต์ ๋ฌธ์](https://numpy.org/doc/stable/reference/generated/numpy.exp.html) <br>
[์ฐธ๊ณ  ์๋ฃ](https://codetorial.net/numpy/functions/numpy_exp.html)

* `np.exp` ๋ ์ง์ํจ์
* `np.log` ๋ฅผ ์ด์ฉํ์ฌ ๋ก๊ทธ๋ฅผ ์ทจํ๋ ๊ฐ์ ๋ค์ ์๋๋๋ก ๋ณต์
* `log` ๋ฅผ ์ทจํ  ๋๋ 1์ ๋ํ๊ณ  ๋ก๊ทธ๋ฅผ ์ทจํ๋๋ฐ ์ง์ํจ์๋ฅผ ์ ์ฉํ  ๋๋ ๋ฐ๋๋ก ์ง์ํจ์๋ฅผ ์ทจํ๊ณ  1์ ๋บ
> โ์ ์ง์ํจ์๋ฅผ ์ทจํ ๊นโ <br>
>   * feature์ log๋ฅผ ์ทจํ๊ณ  ์์ธก๋ ๊ฐ์ ๋ค์ ๋ณต์ํ๊ธฐ ์ํด

```python
# +1 ํ ๋ก๊ทธ
train["count_log1p"] = np.log(train["count"] + 1)

# ์ง์ํจ์ ์ทจํด์ฃผ๊ณ  -1 == train["count"]
train["count_expml"] = np.exp(train["count_log1p"]) - 1
```


> โ์ค๋ฌด์์ ์ด๋ค ํ๊ฐ์งํ๋ฅผ ์ฌ์ฉํด์ผํ ์ง ์ค์ค๋ก ๊ฒฐ์ ํด์ผํ ํ๋ฐ, ์ฌ๋ฌ๊ฐ์ง ํ๊ฐ์งํ๋ฅผ ์ฌ์ฉํ๋์ ์๋๋ฉด ๋ฐ์ดํฐ๋ฅผ ๋ณด๊ณ  ๋ถ์ ์ ์ ๊ฒฐ์ ํ๋์โ <br>
>   * ์ค๋ฌด์์๋ ๋ณดํต ๋น์ฆ๋์ค ํ๊ฐ์งํ๋ฅผ ๋ ๋ง์ด ์ฌ์ฉ
>   * ๊ฒฝ์ง๋ํ๋ ์ค์ต์์ ์ฌ์ฉํ๋ ํ๊ฐ์งํ๋ ๋ชจ๋ธ์ ์ฑ๋ฅ์ ์ธก์ ํด์ ๊ฐ๊ดํ๋ฅผ ์ํด ์ฌ์ฉ
>   * ๋ชจ๋ธ์ ๋ง๋๋ ๋ชฉ์ ์ ๋น์ฆ๋์ค ๋ฌธ์  ํด๊ฒฐ
>   * ๋ชจ๋ธ์ ๋ชฉ์ ์ด DAU(Daily Active User)๋ฅผ ์ฌ๋ฆฌ๋ ๊ฒ์ด๋ผ๋ฉด DAU๋ฅผ ์ธก์ 
>   * ๋งค์ถ์ ๋๋ฆฌ๊ณ  ์ถ๋ค๋ฉด ๋งค์ถ์ก์ด ๋์ด๋ฌ๋์ง, ๊ตฌ๋งค์์๊ฐ ๋์ด๋ฌ๋์ง ๋ฑ์ ํ๊ฐ

<br>

### - `RandomizedSearchCV`
```python
from sklearn.model_selection import RandomizedSearchCV

param_distributions = {
    "n_estimators":np.random.randint(100, 1000, 10),
    "max_depth":np.random.randint(3, 14, 5),
    "max_features":np.random.uniform(0.5, 1, 5)
}

# RMSE๋ฅผ ์ด์ฉํ์ง๋ง, ์ด๋ฏธ count์ log๋ฅผ ์ทจํด ์ฃผ์๊ธฐ ๋๋ฌธ์ RMSLE๋ก ๊ณ์ฐํ๋ ๊ฒ๊ณผ ๋์ผ
reg = RandomizedSearchCV(model, param_distributions=param_distributions, 
                   scoring="neg_root_mean_squared_error", n_iter=10, cv=5, verbose=2, random_state=42)

reg.fit(X_train, y_train)
```

```python
# scoring ํ๋ผ๋ฏธํฐ์ ๋ค์ด๊ฐ ์ ์๋ ๊ฐ ์กฐํ
import sklearn

sklearn.metrics.SCORERS.keys()
```

```python
# score๊ฐ ์์
# neg(ative)_root_mean_squared_error
# ์ถ์ธก : ์๋ง๋ ์ ๋ ฌ์ ์ํด ์์ ์์๋ฅผ ๋ถ์ฌ์ค ๊ฒ์ด ์๋๊น
reg.best_score_

>>> -0.5875572401188127
```

> * ํผ์ฒ๋ฅผ ์ถ๊ฐํ๊ณ  ์ ์ธํ๋ ๊ฒ์ EDA ๋ฅผ ํ๊ณ  ์ ์ฉํด ๋ณด๋ ๊ฒ๋ ์ค์ํ์ง๋ง
> * ์ง์  ๋ชจ๋ธ์ ์ถ๊ฐํ๊ณ  ์ ๊ฑฐํด ๋ณด๋ฉด์ ๊ฒ์ฆํด ๋ณด๋ ๊ฒ๋ ์ข์ ๋ฐฉ๋ฒ