# 🦁 TIL

## ✅ Introduction to Machine Learning
### - 머신러닝이란 무엇인가
* 유용한 함수를 학습하는 것
* 데이터가 있고 컴퓨터를 학습시킬 수 있는 알고리즘을 컴퓨터에게 입력
* 컴퓨터가 스스로 데이터 속 유용한 패턴을 찾아 함수 학습
* Data ➡️ Learning ➡️ Function ➡️ Solving ➡️ Output

<br>

### - 머신러닝의 네 가지 구성요소
1. 환경
   * 머신러닝 알고리즘에 경험을 제공
2. 데이터
   * 환경과 상호작용 하면서 얻어진 일련의 패턴
   * 기억해야 되는 활동의 저장 결과
3. 모델
   * 함수, 데이터를 통해 함수 학습
   * 함수의 대략적인 형태만 잡아주고 데이터를 통해 쓸모 있게 만듦
4. Performance
   * 학습된 함수가 좋은 함수인지 평가
   * 모델 성능을 평가할 수 있는 기준

<br>

### - Category of Machine Learning
* Supervised Learning
  * Classification ➡️ 범주형 레이블
  * Regression ➡️ 수치형 레이블
* Unsupervised Learning
  * Clustering
* Reinforcement Learning
  * Markov Decision
  * Process
  * DQN
  * Policy Gradient

<br>

### - Generalization Error and Hyperparameter
* Training error
  * 학습 데이터에 대한 오류
  * 함수, 모델이 복잡해질수록 감소
* Validation error
  * 일반화 오류
  * 함수, 모델이 복잡해질수록 감소하다가 어느 순간 증가 ➡️ 과적합

<br>

## ✅ Machine Learning Pipeline
### - Data 관련 용어
* Dataset
  * 정의된 구조로 모아져 있는 데이터 집합
* Data Point(Observation)
  * 데이터 세트에 속해 있는 하나의 관측치
* Feature(Variable, Attribute)
  * 데이터를 구성하는 하나의 특성
  * 숫자형, 범주형, 시간, 텍스트, 이진형
* Label(Target, Response)
  * 입력 변수들에 의해 예측, 분류되는 출력 변수


<br>

### - 분류와 회귀
||분류, Classification|회귀, Regression|
|:----:|:----:|:----:|
|결과|종속변수(y)가 범주형일 때 사용하는 모델|종속변수(y)가 연속형일 때 사용하는 모델|
|예제|입력된 보험 청구권에 대해서<br>자동심사와 인심사 분류|날씨, 유가, 경제 지표 등|

<br>

### - Data 준비 과정
* Dataset Exploration (EDA)
  * 데이터 모델링을 하기 전 데이터 변수 별 기본적인 특성들을 탐색
  * 데이터의 분포적인 특징 이해
* Missing Value
  * 데이터를 수집하다 보면 결측치 발생
  * 결측치 부분 보정 필요
* Data Types and Conversion
  * 데이터셋 안에 여러 종류의 데이터 타입을 분석 가능한 형태로 변환 후 사용해야 함 
* Normalization
  * 데이터 변수들의 단위가 크게 다른 경우 활용
  * 스케일의 차이가 크면 모델 학습에 영향을 주는 경우가 있어 정규화
* Outliers
  * 관측치 중에서 다른 관측치와 크게 차이가 나는 관측치들은 모델링 전 처리 필요
* Feature Selection
  * 많은 변수 중 모델링을 할 때 중요한 변수와 그렇지 않은 변수 선택
* Data Sampling
  * 모델링을 할 때 데이터의 일부분을 추출하는 과정을 거치기도 함


<br>
