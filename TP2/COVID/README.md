# ๐ฆ TIL

## ๐ Link
> * [์์ธ ์ฝ๋ก๋ ํตํฉ์ฌ์ดํธ](https://www.seoul.go.kr/coronaV/coronaStatus.do)
> * [Series Accessors](https://pandas.pydata.org/docs/reference/series.html#accessors)

## โ ์์ธ์ ์ฝ๋ก๋19 ๋ฐ์ ๋ํฅ EDA
> python0303


* `Series Accessors`
* `df.value_counts()`
* `pd.to_datetime(df["ํ์ง์ผ"])`
* `weekday_cnt[list("์ํ์๋ชฉ๊ธํ ์ผ")].plot(kind="bar", figsize=(10, 3), rot=0)`


* indexing์ ์ด์ฉํ์ฌ Series ์ ๋ ฌ
  * `weekday_cnt[list("์ํ์๋ชฉ๊ธํ ์ผ")]`


* ๊ธฐ์ค์  ๊ธ๊ธฐ : `plt.axhline(1500, c='r', lw=0.5, ls="--") `
* `pd.date_range(start=first_day, end=last_day)`
* `df_all_day["ํ์ง์"].cumsum()`
* `df_all_day.plot(secondary_y="ํ์ง์", figsize=(10, 3))`