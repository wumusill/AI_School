# 🦁 TIL

## 🔗 Link
> * [서울 코로나 통합사이트](https://www.seoul.go.kr/coronaV/coronaStatus.do)
> * [Series Accessors](https://pandas.pydata.org/docs/reference/series.html#accessors)

## ✅ 서울시 코로나19 발생 동향 EDA
> python0303


* `Series Accessors`
* `df.value_counts()`
* `pd.to_datetime(df["확진일"])`
* `weekday_cnt[list("월화수목금토일")].plot(kind="bar", figsize=(10, 3), rot=0)`


* indexing을 이용하여 Series 정렬
  * `weekday_cnt[list("월화수목금토일")]`


* 기준선 긋기 : `plt.axhline(1500, c='r', lw=0.5, ls="--") `
* `pd.date_range(start=first_day, end=last_day)`
* `df_all_day["확진수"].cumsum()`
* `df_all_day.plot(secondary_y="확진수", figsize=(10, 3))`