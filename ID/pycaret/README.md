# 🦁 TIL

## ✅ pycaret
[pycaret docs](https://pycaret.gitbook.io/docs/)

### - pycaret이란
[참고 자료_1](https://dsbook.tistory.com/360) <br>
[참고 자료_2](https://velog.io/@gyounghwan1002/python-AutoML%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC-pycaret-%EC%82%AC%EC%9A%A9%EB%B2%95)

* ML Workflow를 자동화하는 오픈 소스 라이브러리
* Classification, Regression, Clustering 등 여러 모델들을 동일한 환경에서 한 줄의 코드로 실행할 수 있도록 자동화한 라이브러리
* 여러 모델과 비교 가능
* 각 모델 별로 튜닝 가능


<br>

### - pycaret 설치

* Full version은 꼭 필요한 패키기만 설치하는 일반 버전과 달리 부가적인 패키지도 설치

```python
# pip
pip install pycaret

# full version
pip install pycaret[full]

# conda
conda install -c conda-forge pycaret
```


<br>

## ✅ pycaret 주요 함수
> ~~실습 파일은 ../week4/FIFA.ipynb~~ <br>
> numpy랑 버전 충돌 발생, 선 정리 후 실습

### `setup()`
[setup 공식 문서](https://pycaret.readthedocs.io/en/latest/api/regression.html#pycaret.regression.setup)
* train, test, label 등을 설정
* Nomalization, Transformation, Fold Strategy 등 여러 전처리 기법 적용 가능


#### parameter
* data
  * input data 입력
  * train, test를 분리하지 않으면 `train_size` 파라미터로 분리 가능
  * 분리되어 있다면 `test_data` 에 test data 입력
* Target
  * label column
  * train data에 존재해야 함
* session_id
  * seed 값 고정
  * `random_state` 와 같은 기능 
* normalize
  * 데이터 정규화를 할 것인지 True/False로 선택
* normalize_method
  * `normalize=True` 인 경우 어떤 방식으로 진행할 것인지 선택
  * `zscore`, `minmax`, `maxabs`, `robust`
* transformation
  * Power Transformation을 통해 데이터 샘플들의 분포가 정규 분포에 가까워지도록 처리
* fold_strategy
  * pycaret은 기본적으로 10 fold Cross Validation 수행
  * 다른 Fold Strategy 설정
* use_gpu
  * GPU를 사용할 것인지 설정


<br>

### `models()`
* `setup()` 실행 이후 어떤 모델들을 사용할 수 있는지 확인
* `setup()` 함수를 실행하지 않으면 호출 불가능



<br>

### `compare_models()`
* `models()` 에서 제공하는 모델이나, `scikit-learn` 에서 제공하는 모델을 별도로 선언 후, 입력받은 모델들의 성능을 DF형태로 제공
  
#### parameter
* n_select=`30`
  * 학습을 수행한 후 가장 좋은 성능의 모델을 입력받은 수만큼 저장
* sort=`RMSE`
  * 모델들을 출력할 때 어떤 성능을 기준으로 정렬할지 입력
* include
  * 어떤 모델들을 비교할지 설정
  * `models()` 에서 확인 가능한 ID나 미리 선언한 모델을 리스트 형식으로 입력


<br>

### `create_model()`
* 여러 모델이 아닌 하나의 모델에 대해서 `setup()` 의 설정대로 학습
```python
LGBM = create_model("lightgbm")
```

<br>

### `tune_model()`
* 입력한 모델에 대해서 Hyper-parameter Tuning 을 수행


#### parameter
* n_iter
  * 성능을 비교할 후보군의 수를 의미
  * 크게 해줄수록 성능이 더 좋아질 가능성은 높지만, 시간이 오래 걸림
  * Task에 맞게 적절한 값 설정 필요
* optimize=`"RMSE"`
  * Tuning 할 때 어떤 Metric을 기준으로 할지 설정

<br>

### `evaluate_model()`
* 모델의 학습 및 평가 정보 확인
* feature importance도 그래프로 확인 가능


<br>

### `predict_model()`
* `setup()` 에서 설정한 test 데이터에 대한 label 값 예측

#### parameter
* data
  * `setup()`에 설정된 데이터 말고 다른 데이터로 예측 결과를 보고 싶다면 입력


<br>

### `save_model()`
* 학습한 모델을 저장해주는 pickle file(.pkl)로 지정한 디렉토리에 저장
* 경로를 입력하는 경우 .pkl을 써주지 않아도 됨


<br>

### `load_model()`

* `save_model()`을 불러오는 메서드
