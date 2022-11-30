# 🦁 TIL

[TensorFlow Regression Tutorial](https://www.tensorflow.org/tutorials/keras/regression)
## 실습 목적, 알아가야 하는 것
* 정형 데이터 입력층 : `input_shape`
* 정규화 레이어 사용 ➡️ 직접 정규화 가능
* 분류와 다른 출력층
* 분류와 다른 loss 설정
* 입력변수를 하나만 사용했을 때보다 더 좋은 성능
  * 변수의 개수랑 성능이 비례하진 않음
  * 그렇지만 적은 변수로는 예측모델을 잘 만들기 어려움 

## ✅ Regression
### - 정규화 

* `tensorflow` 에서 제공하는 정규화 전처리 코드
```python
normalizer = tf.keras.layers.Normalization(axis=-1)
```
* ( 2차원, 1차원 ) 의 경우
* ( axis=0 , axis=1 )
* ( axis=-2 , axis =-1 )

<br>

* 3차원의 경우
* ( 3차, 2차, 1차 )
* ( axis=0, axis=1, axis=2)
* ( axis=-3, axis=-2 , axis =-1 )

<br>


```python
horsepower = np.array(train_features['Horsepower'])

horsepower_normalizer = layers.Normalization(input_shape=[1,], axis=None)
horsepower_normalizer.adapt(horsepower)


horsepower_model = tf.keras.Sequential([
    horsepower_normalizer,
    layers.Dense(units=1)
])

horsepower_model.summary()
```
* 전처리 레이어를 추가해서 모델에 전처리 기능 사용 가능
* 정규화 방법을 몰라도 추상화된 기능 이용하여 쉽게 정규화 가능
* 소스코드를 열어보기 전까지 어떤 기능인지 알기 어렵다는 단점
* `scikit-learn` 의 `pipeline` 기능과 유사

<br>

### - 출력층
* 분류는 활성화 함수로 소프트맥스, 시그모이드를 사용한 반면
* 회귀 출력층의 경우 항등함수


<br>

### - compile

```python
horsepower_model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.1),
    loss='mean_absolute_error')
```
* `optimizer` 를 `"adam"` 으로 지정하면 `learning_rate` 기본값 사용, 지정 불가능

<br>

### - val_loss

```python
%%time
history = dnn_model.fit(
    train_features,
    train_labels,
    validation_split=0.2,
    verbose=0, epochs=100)
```

* `val_loss` : 검증 손실 값
* `fit` 단계에서 `validation_split` 으로 지정


<br>

### - flatten()
[참고 자료](https://m.blog.naver.com/wideeyed/221533365486) <br>
[numpy tutorial](https://numpy.org/doc/stable/user/absolute_beginners.html)

```python
test_predictions = dnn_model.predict(test_features).flatten()
```
* 2차원을 1차원으로 만들어주는 함수
* 예측값이 기본적으로 2차원으로 나옴 


<br>

### - Earlystopping
```python
early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_mse', patience=100)

history = model.fit(x_train, y_train, epochs=1000, verbose=0, 
                    callbacks=[early_stop], validation_split=0.2)
```


