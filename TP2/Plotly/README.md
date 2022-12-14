# π¦ TIL

## π Link
> * [FinanceDataReader Tutorial](https://nbviewer.org/github/FinanceData/FinanceDataReader/blob/master/tutorial/FinanceDataReader%20Tutorial%20-%20%EC%97%AC%EB%9F%AC%20%EC%A2%85%EB%AA%A9%EC%9D%98%20%EA%B0%80%EA%B2%A9%EC%9D%84%20%ED%95%9C%EB%B2%88%EC%97%90.ipynb)
> * [μ€μ΅ URL](http://finance.naver.com/sise/entryJongmok.naver?page=1)
> * [koreanize-matplotlib](https://github.com/ychoi-kr/koreanize-matplotlib) 
> * [κ·Έλν λ€μν style μ€μ ](https://matplotlib.org/stable/tutorials/introductory/customizing.html)
> * [Plotly κ³΅μλ¬Έμ](https://plotly.com/python/)
> * [Plotly μμ ](https://plotly.com/python/time-series/)


## β FinanceDataReaderλ₯Ό ν΅ν μ¬λ¬ μ’λͺ© μμ΅λ₯  λΉκ΅
> python0301


* `%pwd` : Jupyterμμ νμ¬ νμΌ κ²½λ‘ νμΈ λ°©λ²
* `finder > cmd + shift + g` : κ²½λ‘ λ³΅μ¬
* `koreanize-matplotlib`
* `df1.merge(df2, left_on="co1", right_on="COL1", how="left")`
* `plt.style.available`
* `plt.style.use("ggplot")`
* `df_norm.resample("Q").mean()`


* νμ€ν(standardization) : 
  * λ°μ΄ν°κ° νκ· μΌλ‘ λΆν° μΌλ§λ λ¨μ΄μ Έ μλμ§ λνλ΄λ κ°μΌλ‘ λ³ν
  * (Z-score νμ€ν) : (μΈ‘μ κ° - νκ· ) / νμ€νΈμ°¨
* μ κ·ν(normalization) : 
    * λ°μ΄ν°μ μλμ  ν¬κΈ°μ λν μν₯μ μ€μ΄κΈ° μν΄ 0~1λ‘ λ³ν
    * (μΈ‘μ κ° - μ΅μκ°) / (μ΅λκ° - μ΅μκ°)



* μλ, skewness λ μ€μ κ° νλ₯  λ³μμ νλ₯  λΆν¬ λΉλμΉ­μ±μ λνλ΄λ μ§ν 
  * μλμ κ°μ μμλ μμκ° λ  μ μμΌλ©° μ μλμ§ μμ μλ μμ
  * μλκ° μμμΌ κ²½μ°μλ μΌμͺ½ λΆλΆμ κΈ΄ κΌ¬λ¦¬, μ€μκ°μ ν¬ν¨ν μλ£κ° μ€λ₯Έμͺ½μ λ λ§μ΄ λΆν¬ 
  * μλκ° μμμΌ λλ μ€λ₯Έμͺ½ λΆλΆμ κΈ΄ κΌ¬λ¦¬, μλ£κ° μΌμͺ½μ λ λ§μ΄ λΆν¬ 
  * νκ· κ³Ό μ€μκ°μ΄ κ°μΌλ©΄ μλλ 0


* μ²¨λ, kurtosis λ νλ₯ λΆν¬μ λΎ°μ‘±ν μ λλ₯Ό λνλ΄λ μ²λ
  * κ΄μΈ‘μΉλ€μ΄ μ΄λ μ λ μ§μ€μ μΌλ‘ μ€μ¬μ λͺ°λ € μλκ°λ₯Ό μΈ‘μ  
  * μ²¨λκ°(K)μ΄ 3μ κ°κΉμ°λ©΄ μ°ν¬λκ° μ κ·λΆν¬μ κ°κΉλ€. 
  * 3λ³΄λ€ μμ κ²½μ°μλ(K<3) μ κ·λΆν¬λ³΄λ€ λ μλ§νκ² λ©μν λΆν¬ 
  * μ²¨λκ°μ΄ 3λ³΄λ€ ν° μμμ΄λ©΄(K>3) μ°ν¬λ μ κ·λΆν¬λ³΄λ€ λ λΎ°μ‘±ν λΆν¬


<br>


## β Plotlyλ₯Ό μ΄μ©ν Python λμ  μκ°ν
> python0302


* `plotly`
* `cufflinks`
* `px.line(df, x="date", y="GOOG", title="μΌλ³ μμΈ")`
* `facet_col="company"`
* `facet_col_wrap=2`
* `hover_data = {"date": "|%Y-%m-%d"}`