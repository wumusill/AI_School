# ๐ฆ TIL

[TensorFlow Regression Tutorial](https://www.tensorflow.org/tutorials/keras/regression)
## ์ค์ต ๋ชฉ์ , ์์๊ฐ์ผ ํ๋ ๊ฒ
* ์ ํ ๋ฐ์ดํฐ ์๋ ฅ์ธต : `input_shape`
* ์ ๊ทํ ๋ ์ด์ด ์ฌ์ฉ โก๏ธ ์ง์  ์ ๊ทํ ๊ฐ๋ฅ
* ๋ถ๋ฅ์ ๋ค๋ฅธ ์ถ๋ ฅ์ธต
* ๋ถ๋ฅ์ ๋ค๋ฅธ loss ์ค์ 
* ์๋ ฅ๋ณ์๋ฅผ ํ๋๋ง ์ฌ์ฉํ์ ๋๋ณด๋ค ๋ ์ข์ ์ฑ๋ฅ
  * ๋ณ์์ ๊ฐ์๋ ์ฑ๋ฅ์ด ๋น๋กํ์ง ์์
  * ๊ทธ๋ ์ง๋ง ์ ์ ๋ณ์๋ก๋ ์์ธก๋ชจ๋ธ์ ์ ๋ง๋ค๊ธฐ ์ด๋ ค์ 

## โ Regression
### - ์ ๊ทํ 

* `tensorflow` ์์ ์ ๊ณตํ๋ ์ ๊ทํ ์ ์ฒ๋ฆฌ ์ฝ๋
```python
normalizer = tf.keras.layers.Normalization(axis=-1)
```
* ( 2์ฐจ์, 1์ฐจ์ ) ์ ๊ฒฝ์ฐ
* ( axis=0 , axis=1 )
* ( axis=-2 , axis =-1 )

<br>

* 3์ฐจ์์ ๊ฒฝ์ฐ
* ( 3์ฐจ, 2์ฐจ, 1์ฐจ )
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
* ์ ์ฒ๋ฆฌ ๋ ์ด์ด๋ฅผ ์ถ๊ฐํด์ ๋ชจ๋ธ์ ์ ์ฒ๋ฆฌ ๊ธฐ๋ฅ ์ฌ์ฉ ๊ฐ๋ฅ
* ์ ๊ทํ ๋ฐฉ๋ฒ์ ๋ชฐ๋ผ๋ ์ถ์ํ๋ ๊ธฐ๋ฅ ์ด์ฉํ์ฌ ์ฝ๊ฒ ์ ๊ทํ ๊ฐ๋ฅ
* ์์ค์ฝ๋๋ฅผ ์ด์ด๋ณด๊ธฐ ์ ๊น์ง ์ด๋ค ๊ธฐ๋ฅ์ธ์ง ์๊ธฐ ์ด๋ ต๋ค๋ ๋จ์ 
* `scikit-learn` ์ `pipeline` ๊ธฐ๋ฅ๊ณผ ์ ์ฌ

<br>

### - ์ถ๋ ฅ์ธต
* ๋ถ๋ฅ๋ ํ์ฑํ ํจ์๋ก ์ํํธ๋งฅ์ค, ์๊ทธ๋ชจ์ด๋๋ฅผ ์ฌ์ฉํ ๋ฐ๋ฉด
* ํ๊ท ์ถ๋ ฅ์ธต์ ๊ฒฝ์ฐ ํญ๋ฑํจ์


<br>

### - compile

```python
horsepower_model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.1),
    loss='mean_absolute_error')
```
* `optimizer` ๋ฅผ `"adam"` ์ผ๋ก ์ง์ ํ๋ฉด `learning_rate` ๊ธฐ๋ณธ๊ฐ ์ฌ์ฉ, ์ง์  ๋ถ๊ฐ๋ฅ

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

* `val_loss` : ๊ฒ์ฆ ์์ค ๊ฐ
* `fit` ๋จ๊ณ์์ `validation_split` ์ผ๋ก ์ง์ 


<br>

### - flatten()
[์ฐธ๊ณ  ์๋ฃ](https://m.blog.naver.com/wideeyed/221533365486) <br>
[numpy tutorial](https://numpy.org/doc/stable/user/absolute_beginners.html)

```python
test_predictions = dnn_model.predict(test_features).flatten()
```
* 2์ฐจ์์ 1์ฐจ์์ผ๋ก ๋ง๋ค์ด์ฃผ๋ ํจ์
* ์์ธก๊ฐ์ด ๊ธฐ๋ณธ์ ์ผ๋ก 2์ฐจ์์ผ๋ก ๋์ด 


<br>

### - Earlystopping
```python
early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_mse', patience=100)

history = model.fit(x_train, y_train, epochs=1000, verbose=0, 
                    callbacks=[early_stop], validation_split=0.2)
```


