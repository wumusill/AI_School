# 🦁 TIL

## ✅ 머신러닝 분류 모델링
### - 기계학습 유형
* 문제 상황(Task)에 따라 크게 3가지로 분류
  * Supervised Learning
    * Classification
    * Regression
  * Unsupervised Learning
    * Clustering : 군집화
    * Anomaly Detection : 이상치 탐지
  * Reinforcement Learning
    * Markov Decision Process
    * DQN
    * A3C


### - Supervised Learning
* 학습 데이터로부터 함수 $F$ 를 찾는 방법론
* 종속변수 $Y$ 가 연속형이면 `Regression`, 범주형이면 `Classification`
* 특정 모델이 모든 경우에 대해 항상 좋은 성능을 내지 않음
* 문제상황에 따라 적합한 모델 선택

### - Bias-Variance Tradeoff
* 모든 모델은 복잡도를 통제할 수 있는 Hyperparameter를 갖고 있음
* 가장 좋은 성능을 낼 수 있는 모델을 학습하기 위해 최적의 Hyperparameter를 결정해야 함 
* 모델이 복잡할수록 편향은 감소 분산은 증가

<br>

## ✅ K-Nearest Neighbors
* 두 관측치의 거리가 가까우면 Y도 비슷하다
* K 개의 주변 관측치의 Class에 대한 `majority voting(다수결)`
* Distance-based model, instance-based learning
* K에 따라 결과가 달라질 수 있음
* 범주형 변수는 `Dummy Variable`으로 변환하여 거리 계산

<br>

* Lazy Learning Algorithm
  * train data를 학습함으로써 함수 식을 업데이트 하는 선형 모델과 달리 test data가 들어와야만 train data들과의 거리를 측정하고 예측
  * 빅데이터로는 효과적이지 못함

<br>

### - K의 영향
* K : Hyperparameter of KNN
* K가 클수록 과소적합, 작을수록 과대적합
* Validation dataset으로 최적의 K 결정


<br>

## ✅ Logistic Regression
### - Logistic Regression의 필요성
* 범주형 반응 변수
  * 이진 변수
  * 멀티 변수
* 일반회귀분석과는 다른 방식으로 접근해야 될 필요성
* 종속변수가 이진 변수일 때, 확률값을 선형 회귀분석의 종속변수로 사용하는 것이 타당한가?
  * Y가 무한대로 감에 따라 특정 기준치를 넘어가면 오차가 더욱 커지게 됨
  * 선형회귀분석의 우변은 범위에 대한 제한이 없기 때문에 우변과 좌변의 범위가 다른 문제점 발생
  
<br>

* 로지스틱 회귀분석의 목적
  * 이진형의 형태를 갖는 종속변수에 대해 회귀식의 형태로 모형을 추정
* 왜 회귀식으로 표현해야 하는가
  * 회귀식으로 표현될 경우 변수의 통계적 유의성 분석 및 종속 변수에 미치는 영향력 등을 알아볼 수 있음
* 로지스틱 회귀분석의 특징
  * Y를 그대로 사용하는 것이 아니라 Y에 logit function을 회귀식의 종속변수로 사용
