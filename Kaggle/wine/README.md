# ๐ฆ Wine quality

* [ํ์ฌ ์๋ณธ ๋งํฌ](https://www.kaggle.com/code/vishalyo990/prediction-of-quality-of-wine/notebook)

### ๋ฐ์ดํฐ ํด์ 
* index : ๊ตฌ๋ถ์
* quality : ํ์ง
* fixed acidity : ์ฐ๋
* volatile acidity : ํ๋ฐ์ฑ์ฐ
* citric acid : ์ํธ๋ฅด์ฐ
* residual sugar ์๋น : ๋ฐํจ ํ ์์ธ ์์ ๋จ์์๋ ๋น๋ถ
* chlorides : ์ผํ๋ฌผ
* free sulfur dioxide : ๋๋ฆฝ ์ด์ฐํํฉ
* total sulfur dioxide : ์ด ์ด์ฐํํฉ
* density : ๋ฐ๋
* pH : ์์์ด์จ๋๋
* sulphates : ํฉ์ฐ์ผ
* alcohol : ๋์
* type : ์ข๋ฅ

<br>

## โ ๋ฐ์ดํฐ ์ ์ฒ๋ฆฌ : ์ฐ์ํ์ ๋ฒ์ฃผํ์ผ๋ก ๋ณํ
[์ฐธ๊ณ  ์๋ฃ](https://rfriend.tistory.com/521)


### - `pd.cut()`
* `bins=(a, b)` : a ์ด๊ณผ b ์ดํ
* bin ๋ฒ์ ๋ฐ์ ๊ฐ์ `NaN`
* label option์ผ๋ก ์ฌ์ฉ์ ์ง์  ๊ฐ๋ฅ
* return a list of categories with labels

```python
df = pd.DataFrame({'col': np.arange(10)})

bins=(0, 5, 8)
pd.cut(df["col"], bins=bins)

>>> 0           NaN
    1    (0.0, 5.0]
    2    (0.0, 5.0]
    3    (0.0, 5.0]
    4    (0.0, 5.0]
    5    (0.0, 5.0]
    6    (5.0, 8.0]
    7    (5.0, 8.0]
    8    (5.0, 8.0]
    9           NaN
    Name: col, dtype: category
    Categories (2, interval[int64, right]): [(0, 5] < (5, 8]]
```
<br>


## โ `LabelEncoder()`
[์ฐธ๊ณ  ์๋ฃ](https://mizykk.tistory.com/10)

* `One-Hot-Encoder`์ ๋ฌ๋ฆฌ ํ๋์ ์ด์ ์๋ก ๋ค๋ฅธ ์ซ์๋ฅผ ์๋ ฅ

```python
from sklearn.preprocessing import LabelEncoder


labelenc = LabelEncoder()

df["col"] = labelenc.fit_transform(df["col"])
```




<br>

## โ `classification_report` ํด์
[์ฐธ๊ณ  ์๋ฃ](https://velog.io/@ljs7463/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%EB%AA%A8%EB%8D%B8-%ED%8F%89%EA%B0%80%EC%A0%95%EB%B0%80%EB%8F%84%EC%9E%AC%ED%98%84%EC%9C%A8f1-score%EB%93%B1)

### - ์ ๋ฐ๋, Precision
  * Positive๋ก ์์ธกํ ๊ฒฝ์ฐ ์ค ์ค์ ๋ก Positive์ธ ๋น์จ
  * ์์ธก๊ฐ์ด ์ผ๋ง๋ ์ ํํ๊ฐ 
  * TP / (TP + FP)
### - ์ฌํ์จ, Recall
  * ์ค์ ๋ก Positive์ธ ๊ฒ ์ค ์ฌ๋ฐ๋ฅด๊ฒ Positive๋ฅผ ๋ง์ถ ๊ฒ์ ๋น์จ
  * ์ค์  ์ ๋ต์ ์ผ๋ง๋ ๋ง์ท๋๊ฐ
  * TP / (TP + FN)
  
> ์์ <br>
> * ์ ๊ฒ์ฌ์ ๊ฒฝ์ฐ ์ฌํ์จ์ด ์ค์
> * ์ค์ ๋ก ์์ธ๋ฐ ์์ด ์๋๋ผ๊ณ  ์์ธกํ๋ฉด ํฐ์ผ๋๊ธฐ ๋๋ฌธ
> * ์คํธ ๋ฉ์ผ ์ฌ๋ถ ํ๋จ์ ๊ฒฝ์ฐ ์ ๋ฐ๋๊ฐ ์ค์


### - f1-score
* Precision๊ณผ Recall์ ์กฐํํ๊ท ์ผ๋ก ๋ถ๋ฅ ํด๋์ค ๊ฐ์ ๋ฐ์ดํฐ๊ฐ ๋ถ๊ท ํ์ด ์ฌ๊ฐํ  ๋ ์ฌ์ฉ
* ์ ํ๋์ ๊ฒฝ์ฐ, ๋ฐ์ดํฐ ๋ถ๋ฅ ํด๋์ค๊ฐ ๊ท ์ผํ์ง ๋ชปํ๋ฉด ์ฑ๋ฅ ๋ฐํ ๋ถ๊ฐ๋ฅ
* ๋์์๋ก ์ข์ ๋ชจ๋ธ
* 2 * precision * recall / (precision + recall)

<br>

## โ ML
### - SVC
[์ฐธ๊ณ  ์๋ฃ](https://inuplace.tistory.com/600)

### - SGDClassifier
[์ฐธ๊ณ  ์๋ฃ](https://codingsmu.tistory.com/97)

<br>

## โ skew, ์๋

* ์๋๋ฅผ ์กฐ์ ํด์ผํ๋ ์ด์  
  * ์ด์์น๋ฅผ ์ ๊ฑฐํ๊ธฐ ์ํจ
* ๋ถ๋ฅ์์๋ ์ ๊ท๋ถํฌ๋ฅผ ๋ง์ถฐ์ผํ๋๊ฐ?
* ์ ๊ท๋ถํฌ๋ก ๋ง์ถ๋ ์ด์ 
  * ์ค์ผ์ผ์ ํตํด ๋ฒ์๋ฅผ ์ขํ์ ๋ชจ๋ธ์ด ์ข ๋ ์ ์์ธกํ๊ฒ ํ๊ธฐ ์ํด