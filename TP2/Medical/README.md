# π¦ TIL

## π Link
> [numpy generator κ³΅μλ¬Έμ](https://numpy.org/doc/stable/reference/random/generator.html) <br>
> [μ€μ΅ λ°μ΄ν°](https://www.data.go.kr/data/15007117/fileData.do) <br>
> [μ£Όμ±λΆμ½λ λΆμ¬λ°©λ²](https://www.health.kr/drug_info/basedrug/main_ingredient.html) <br>

## β μμ½ν μ²λ°©μ λ³΄ μνλ§
> python0306


* `np.random.seed(42)`
* `rng = np.random.default_rng(42)`
* `sample_no = np.random.choice(raw["κ°μμ μΌλ ¨λ²νΈ"].unique(), 10000)`
* `df_temp = raw[raw["κ°μμ μΌλ ¨λ²νΈ"].isin(sample_no)]`



<br>

## β μμ½ν μ²λ°©μ λ³΄ μ μ²λ¦¬, μκ°ν
> python0307


* `df['μ'] = df["μμκ°μμΌμ"].dt.month`
* `df['μΌ'] = df["μμκ°μμΌμ"].dt.day`
* `df['μμΌ'] = df["μμκ°μμΌμ"].dt.dayofweek`
* `df['μλ¬ΈμμΌ'] = df["μμκ°μμΌμ"].dt.day_name()`


* `pd.options.display.max_columns = None`
* `pd.options.display.max_rows = None`


* `age_dict = {int(i.split()[0]): i.split()[1] for i in age_list}`
* `df["μ°λ Ήλ"] = df["μ°λ Ήλμ½λ(5μΈλ¨μ)"].map(age_dict)`


* `np.triu : μμΌκ°νλ ¬`
* `np.tril : νμΌκ°νλ ¬`


* `sns.heatmap(df.corr(), annot=True, cmap="coolwarm", mask=mask, fmt=".2f", vmax=1, vmin=-1)`