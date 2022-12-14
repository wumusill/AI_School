# ๐ฆ TIL

## โ pycaret
[pycaret docs](https://pycaret.gitbook.io/docs/)

### - pycaret์ด๋
[์ฐธ๊ณ  ์๋ฃ_1](https://dsbook.tistory.com/360) <br>
[์ฐธ๊ณ  ์๋ฃ_2](https://velog.io/@gyounghwan1002/python-AutoML%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC-pycaret-%EC%82%AC%EC%9A%A9%EB%B2%95)

* ML Workflow๋ฅผ ์๋ํํ๋ ์คํ ์์ค ๋ผ์ด๋ธ๋ฌ๋ฆฌ
* Classification, Regression, Clustering ๋ฑ ์ฌ๋ฌ ๋ชจ๋ธ๋ค์ ๋์ผํ ํ๊ฒฝ์์ ํ ์ค์ ์ฝ๋๋ก ์คํํ  ์ ์๋๋ก ์๋ํํ ๋ผ์ด๋ธ๋ฌ๋ฆฌ
* ์ฌ๋ฌ ๋ชจ๋ธ๊ณผ ๋น๊ต ๊ฐ๋ฅ
* ๊ฐ ๋ชจ๋ธ ๋ณ๋ก ํ๋ ๊ฐ๋ฅ


<br>

### - pycaret ์ค์น

* Full version์ ๊ผญ ํ์ํ ํจํค๊ธฐ๋ง ์ค์นํ๋ ์ผ๋ฐ ๋ฒ์ ๊ณผ ๋ฌ๋ฆฌ ๋ถ๊ฐ์ ์ธ ํจํค์ง๋ ์ค์น

```python
# pip
pip install pycaret

# full version
pip install pycaret[full]

# conda
conda install -c conda-forge pycaret
```


<br>

## โ pycaret ์ฃผ์ ํจ์
> ~~์ค์ต ํ์ผ์ ../week4/FIFA.ipynb~~ <br>
> numpy๋ ๋ฒ์  ์ถฉ๋ ๋ฐ์, ์  ์ ๋ฆฌ ํ ์ค์ต

### `setup()`
[setup ๊ณต์ ๋ฌธ์](https://pycaret.readthedocs.io/en/latest/api/regression.html#pycaret.regression.setup)
* train, test, label ๋ฑ์ ์ค์ 
* Nomalization, Transformation, Fold Strategy ๋ฑ ์ฌ๋ฌ ์ ์ฒ๋ฆฌ ๊ธฐ๋ฒ ์ ์ฉ ๊ฐ๋ฅ


#### parameter
* data
  * input data ์๋ ฅ
  * train, test๋ฅผ ๋ถ๋ฆฌํ์ง ์์ผ๋ฉด `train_size` ํ๋ผ๋ฏธํฐ๋ก ๋ถ๋ฆฌ ๊ฐ๋ฅ
  * ๋ถ๋ฆฌ๋์ด ์๋ค๋ฉด `test_data` ์ test data ์๋ ฅ
* Target
  * label column
  * train data์ ์กด์ฌํด์ผ ํจ
* session_id
  * seed ๊ฐ ๊ณ ์ 
  * `random_state` ์ ๊ฐ์ ๊ธฐ๋ฅ 
* normalize
  * ๋ฐ์ดํฐ ์ ๊ทํ๋ฅผ ํ  ๊ฒ์ธ์ง True/False๋ก ์ ํ
* normalize_method
  * `normalize=True` ์ธ ๊ฒฝ์ฐ ์ด๋ค ๋ฐฉ์์ผ๋ก ์งํํ  ๊ฒ์ธ์ง ์ ํ
  * `zscore`, `minmax`, `maxabs`, `robust`
* transformation
  * Power Transformation์ ํตํด ๋ฐ์ดํฐ ์ํ๋ค์ ๋ถํฌ๊ฐ ์ ๊ท ๋ถํฌ์ ๊ฐ๊น์์ง๋๋ก ์ฒ๋ฆฌ
* fold_strategy
  * pycaret์ ๊ธฐ๋ณธ์ ์ผ๋ก 10 fold Cross Validation ์ํ
  * ๋ค๋ฅธ Fold Strategy ์ค์ 
* use_gpu
  * GPU๋ฅผ ์ฌ์ฉํ  ๊ฒ์ธ์ง ์ค์ 


<br>

### `models()`
* `setup()` ์คํ ์ดํ ์ด๋ค ๋ชจ๋ธ๋ค์ ์ฌ์ฉํ  ์ ์๋์ง ํ์ธ
* `setup()` ํจ์๋ฅผ ์คํํ์ง ์์ผ๋ฉด ํธ์ถ ๋ถ๊ฐ๋ฅ



<br>

### `compare_models()`
* `models()` ์์ ์ ๊ณตํ๋ ๋ชจ๋ธ์ด๋, `scikit-learn` ์์ ์ ๊ณตํ๋ ๋ชจ๋ธ์ ๋ณ๋๋ก ์ ์ธ ํ, ์๋ ฅ๋ฐ์ ๋ชจ๋ธ๋ค์ ์ฑ๋ฅ์ DFํํ๋ก ์ ๊ณต
  
#### parameter
* n_select=`30`
  * ํ์ต์ ์ํํ ํ ๊ฐ์ฅ ์ข์ ์ฑ๋ฅ์ ๋ชจ๋ธ์ ์๋ ฅ๋ฐ์ ์๋งํผ ์ ์ฅ
* sort=`RMSE`
  * ๋ชจ๋ธ๋ค์ ์ถ๋ ฅํ  ๋ ์ด๋ค ์ฑ๋ฅ์ ๊ธฐ์ค์ผ๋ก ์ ๋ ฌํ ์ง ์๋ ฅ
* include
  * ์ด๋ค ๋ชจ๋ธ๋ค์ ๋น๊ตํ ์ง ์ค์ 
  * `models()` ์์ ํ์ธ ๊ฐ๋ฅํ ID๋ ๋ฏธ๋ฆฌ ์ ์ธํ ๋ชจ๋ธ์ ๋ฆฌ์คํธ ํ์์ผ๋ก ์๋ ฅ


<br>

### `create_model()`
* ์ฌ๋ฌ ๋ชจ๋ธ์ด ์๋ ํ๋์ ๋ชจ๋ธ์ ๋ํด์ `setup()` ์ ์ค์ ๋๋ก ํ์ต
```python
LGBM = create_model("lightgbm")
```

<br>

### `tune_model()`
* ์๋ ฅํ ๋ชจ๋ธ์ ๋ํด์ Hyper-parameter Tuning ์ ์ํ


#### parameter
* n_iter
  * ์ฑ๋ฅ์ ๋น๊ตํ  ํ๋ณด๊ตฐ์ ์๋ฅผ ์๋ฏธ
  * ํฌ๊ฒ ํด์ค์๋ก ์ฑ๋ฅ์ด ๋ ์ข์์ง ๊ฐ๋ฅ์ฑ์ ๋์ง๋ง, ์๊ฐ์ด ์ค๋ ๊ฑธ๋ฆผ
  * Task์ ๋ง๊ฒ ์ ์ ํ ๊ฐ ์ค์  ํ์
* optimize=`"RMSE"`
  * Tuning ํ  ๋ ์ด๋ค Metric์ ๊ธฐ์ค์ผ๋ก ํ ์ง ์ค์ 

<br>

### `evaluate_model()`
* ๋ชจ๋ธ์ ํ์ต ๋ฐ ํ๊ฐ ์ ๋ณด ํ์ธ
* feature importance๋ ๊ทธ๋ํ๋ก ํ์ธ ๊ฐ๋ฅ


<br>

### `predict_model()`
* `setup()` ์์ ์ค์ ํ test ๋ฐ์ดํฐ์ ๋ํ label ๊ฐ ์์ธก

#### parameter
* data
  * `setup()`์ ์ค์ ๋ ๋ฐ์ดํฐ ๋ง๊ณ  ๋ค๋ฅธ ๋ฐ์ดํฐ๋ก ์์ธก ๊ฒฐ๊ณผ๋ฅผ ๋ณด๊ณ  ์ถ๋ค๋ฉด ์๋ ฅ


<br>

### `save_model()`
* ํ์ตํ ๋ชจ๋ธ์ ์ ์ฅํด์ฃผ๋ pickle file(.pkl)๋ก ์ง์ ํ ๋๋ ํ ๋ฆฌ์ ์ ์ฅ
* ๊ฒฝ๋ก๋ฅผ ์๋ ฅํ๋ ๊ฒฝ์ฐ .pkl์ ์จ์ฃผ์ง ์์๋ ๋จ


<br>

### `load_model()`

* `save_model()`์ ๋ถ๋ฌ์ค๋ ๋ฉ์๋
