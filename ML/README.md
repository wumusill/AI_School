# 🦁 TIL

## 🔗 Link
> [scikit-learn](https://scikit-learn.org/stable/)

## ✅ ML 기초

### 머신러닝 알고리즘 유형
* 분류, Classification
* 회귀, Regression
* 군집화, Clustering
* 차원축소, Dimensionality reduction
* 모델 선택 및 평가, Model selection and evaluation
* 전처리, Preprocessing

|분류| 범주형 | 수치형  |
|:-----:|:---:|:----:|
| 지도학습 | 분류  |  회귀  |
|비지도학습 | 군집화 | 차원축소 |

<br>

## ✅ Supervised Learning

### 머신러닝 알고리즘 : 지도학습 ➡️ 분류
* 고객의 구매/비구매 여부
* 광고 클릭/클릭 X 여부
* 당뇨병 여부
* 스팸메일 여부
* 고객센터 문의 내용 분류

### 머신러닝 알고리즘 : 지도학습 ➡️ 회귀
* 기간별 매출액
* 재고량
* 판매량
* 기온/강수량
* 원유 가격
* 광고 클릭률


### ML process
> `fit` ➡️ `predict` ➡️ `evaluate` <br>

* `scikit-learn` 공식문서에서 **X는 대문자, y는 소문자 사용**
  * 보통 `X는 행렬`, `y는 벡터` 형태라서


* `X_train` : 기출문제 ➡️ 모델에 학습
* `y_train` : 기출문제 정답 ➡️ 모델에 학습
* `X_test` : 실전문제 ➡️ 학습을 바탕으로 `X_test`로 `y_test`를 예측 ➡️ `y_pred`
* `y_test` : 실전문제의 정답 ➡️ 예측해야 하는 값, 맞았는지 `evaluation`



### Basic API
| estimator.predict | estimator.transform  |
|:----------------:|:----:|
|  Classification  |  Preprocessing  |
|    Regression    | Dimensionality reduction |
|    Clustering    | Feature selection |
|                  |Feature extraction|


[//]: # (<br>)

[//]: # (## ✅ )

