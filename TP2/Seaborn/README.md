# π¦ TIL

## β seaborn μκ°ν
> python0107
* `countplot` : λΉλμ λΉκ΅ν  λ
* `unique`κ°μ΄ μμ²­ λ§μΌλ©΄ `wordcloud` or λ°μ΄ν° μ μ²λ¦¬ 
* `hue`λ₯Ό μ΄μ©ν  λ 3κ° μ΄νμ μμ μ¬μ©μ κΆμ₯ for μμΈμ±
* `df.nunique()`
* `series.unique()`


* `df.describe(include="object")`
  * νΉμ  λ°μ΄ν° νμμ μΆλ ₯νλ‘ μΆμ λ μ¬μ©
* `df.describe(exclude="object")`
  * νΉμ  λ°μ΄ν° νμμ μ μΈνκ³  μΆμ λ μ¬μ©


* `pd.crosstab(index=Series, columns=Series)`
* `df.unstack(), series.unstack()`
  * `MultiIndex`μμ `index`μ λ§μ§λ§ κ°μ `column`μΌλ‘ λμ΄μ¬λ¦Ό


* `pivot vs pivot_table`
  * `pivot` : λ°μ΄ν° κ·Έλλ‘ νμ΄λΈλ‘ μΆλ ₯
  * `pivot_table` : λ°μ΄ν°λ₯Ό μ°μ°/κ°κ³΅νμ¬ νμ΄λΈλ‘ μΆλ ₯
  ```python
    pd.pivot_table(data=df, index='origin', columns='cylinders', values='mpg')
  ```



* `boxplot`
* `boxenplot` : μμΌμ ν΄λΉνλ κ°λ boxλ‘ μΆλ ₯


* `scatterplot` : μ μ΄ κ²ΉμΉ  μ μλ€λ λ¨μ 
* `stripplot` : μ μ μμΌλ‘ μ°μ΄μ£Όμ§λ§ μ¬μ ν μ‘°κΈμ© κ²ΉμΉ¨
* `swarmplot` : μ μ μ ν κ²ΉμΉμ§ μκ² μμΌλ‘ μ°μ
* `countplot` : `x, y` λ μ€ νλλ§ μλ ₯ 
* `catplot` : κΈ°λ³Έκ° = `stripplot`

<br>

## β μΉ μ€ν¬λν, ν¬λ‘€λ§
> python0201

## π Link
> * [FinanceData/FinanceDataReader: Financial data reader](https://github.com/FinanceData/FinanceDataReader)
> * [FinanceDataReader μ¬μ©μ μλ΄μ | FinanceData](https://financedata.github.io/posts/finance-data-reader-users-guide.html)
> * https://pandas-datareader.readthedocs.io/en/latest/readers/index.html



* `HTTP`
* `requests`
* `finance-datareader`
* `fdr.StockListing()`


* `robot.txt`
  * λ‘λ΄ λ°°μ  νμ€
  * μΉ μ¬μ΄νΈμ λ‘λ΄μ΄ μ κ·Όνλ κ²μ λ°©μ§νκΈ° μν κ·μ½
  * μΌλ°μ μΌλ‘ μ κ·Ό μ νμ λν μ€λͺμ κΈ°μ 
  * λ€μ΄λ² κ·μ½ μ‘°ν 
  * `ex) naver.com/robots.txt`


* νλ²μ λ§μ νμ΄μ§λ₯Ό μμ²­νλ©΄ DDOS κ³΅κ²©μΌλ‘ μμ¬ λ°μ μ μμ
* μΌλ°μ μΌλ‘ `time.sleep()` μΌλ‘ μκ° κ°κ²©μ λκ³  κ°μ Έμ΄


  

<br>

## β λ€μ΄λ² λ΄μ€ μΉ μ€ν¬λν
> python0202


## π Link
> * https://github.com/tqdm/tqdm
* `html <table>` νκ·Έλ `pandas, μμ`λ‘ λ°λ‘ κ°μ Έμ¬ μ μμ


* `pd.concat()`
* `df.dropna()` : κ²°μΈ‘μΉ μ κ±°νλ λ°©λ²
* `~pd.Series([True, False])` == [False, True]
  * μμ `~`μ λΆμ΄λ©΄ λ°λλ‘ μΆλ ₯
* κΉμ λ³΅μ¬
  * `df2 = d1.copy()`
* μμ λ³΅μ¬
  * `df2 = df1`

* `df.reset_index(drop=True)`
* `df_news.drop_duplicates()` : μ€λ³΅ λ°μ΄ν° μ κ±°