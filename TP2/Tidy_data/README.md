# 🦁 TIL

## 🔗 Link
> [데이터 위치](https://www.data.go.kr/data/15061057/fileData.do) <br>
> [마이크로 데이터 통합서비스](https://mdis.kostat.go.kr/index.do)


## ✅ Tidy data?
> python0304

* 각 `변수가 열`이고 `관측치가 행`이 되도록 배열된 데이터 

<br>



* `df_last["전용면적"] = df_last["규모구분"].str.replace("전용면적|제곱미터이하", "", regex=True)`
* `df_last["전용면적"] = df_last["전용면적"].str.replace("제곱미터초과", "~")`
* `df_last["전용면적"] = df_last["전용면적"].str.replace(" ", "")`
* `df_last["분양가격"] = df_last["분양가격"].str.replace("[^0-9]", "", regex=True)`
* `df_last["분양가격"] = pd.to_numeric(df_last["분양가격"], errors='coerce')`


* `df_last = df_last.drop(labels=["규모구분", "분양가격"], axis=1)`
* `df_last = df_last.drop(columns=["규모구분", "분양가격"])`


* `pd.options.display.max_columns = None`
* `pd.melt(df_first, id_vars="지역")`


* `df_first_melt["기간"].str.split("년", expand=True)`
* `df_first_melt["기간"].str.split("년").map(lambda x: int(x[0]))`
* `df_first_melt["기간"].str.split("년", expand=True)[1].str[:-1].astype(int)`


* `sns.heatmap(y_r_pt, annot=True, fmt=",.0f")`


* `df["항목"] = df["항목"].str.slice(start=0, stop=2)`
* `df["항목"] = df["항목"].str.replace("액\[\$\]", "", regex=True)`