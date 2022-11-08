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