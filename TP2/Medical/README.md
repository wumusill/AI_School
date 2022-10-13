# 🦁 TIL

## 🔗 Link
> [numpy generator 공식문서](https://numpy.org/doc/stable/reference/random/generator.html) <br>
> [실습 데이터](https://www.data.go.kr/data/15007117/fileData.do) <br>
> [주성분코드 부여방법](https://www.health.kr/drug_info/basedrug/main_ingredient.html) <br>

## ✅ 의약품 처방정보 샘플링
> python0306


* `np.random.seed(42)`
* `rng = np.random.default_rng(42)`
* `sample_no = np.random.choice(raw["가입자 일련번호"].unique(), 10000)`
* `df_temp = raw[raw["가입자 일련번호"].isin(sample_no)]`



<br>

## ✅ 의약품 처방정보 전처리, 시각화
> python0307


* `df['월'] = df["요양개시일자"].dt.month`
* `df['일'] = df["요양개시일자"].dt.day`
* `df['요일'] = df["요양개시일자"].dt.dayofweek`
* `df['영문요일'] = df["요양개시일자"].dt.day_name()`


* `pd.options.display.max_columns = None`
* `pd.options.display.max_rows = None`


* `age_dict = {int(i.split()[0]): i.split()[1] for i in age_list}`
* `df["연령대"] = df["연령대코드(5세단위)"].map(age_dict)`


* `np.triu : 상삼각행렬`
* `np.tril : 하삼각행렬`


* `sns.heatmap(df.corr(), annot=True, cmap="coolwarm", mask=mask, fmt=".2f", vmax=1, vmin=-1)`