# π¦ TIL

## π Link
> [μμΈμ λ³΄μν΅κ΄μ₯ 120 μ£Όμμ§λ¬Έ](https://opengov.seoul.go.kr/civilappeal/list)


## β μμΈ120 μ λͺ©, λ μ§, μ‘°νμ μμ§
> python0205

<br>

## β μμΈ120 κ° κΈμ λν λ΄μ© μμ§
> python0206


### - `map` vs `apply` vs `applymap`
* λ°λ³΅λ¬Έλ³΄λ€ ν¨μ¬ λΉ λ₯΄λ€λ μ₯μ μ΄ μμ

| ν¨μ  \  νμ | Series | DataFrame |            Ex             |
|:---------:|:------:|:---------:|:-------------------------:|
|    map    |   O    |     X     | df["col"].map(ν¨μ or dict) |
|   apply   |   O    |     O     |       df.apply(ν¨μ)        |
| applymap  |   X    |     O     |      df.applymap(ν¨μ)      |


### - λ°μ΄ν°νλ μ λ³ν© λ°©λ²
> [νλ€μ€ λ³ν© κ³΅μ λ¬Έμ](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html) <br>
> [λ³ν© μ¬μ© μμ](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html)


* `pd.merge(df1, df2)`
* `pd.concat([df1, df2], axis=1, join="inner")`