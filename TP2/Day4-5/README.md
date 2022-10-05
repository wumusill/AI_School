# 🦁 TIL

## 🔗 Link
> [서울정보소통광장 120 주요질문](https://opengov.seoul.go.kr/civilappeal/list)


## ✅ 서울120 제목, 날짜, 조회수 수집
> python0205

<br>

## ✅ 서울120 각 글에 대한 내용 수집
> python0206


### - `map` vs `apply` vs `applymap`
* 반복문보다 훨씬 빠르다는 장점이 있음

| 함수  \  타입 | Series | DataFrame |            Ex             |
|:---------:|:------:|:---------:|:-------------------------:|
|    map    |   O    |     X     | df["col"].map(함수 or dict) |
|   apply   |   O    |     O     |       df.apply(함수)        |
| applymap  |   X    |     O     |      df.applymap(함수)      |


### - 데이터프레임 병합 방법
> [판다스 병합 공식 문서](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html) <br>
> [병합 사용 예시](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html)


* `pd.merge(df1, df2)`
* `pd.concat([df1, df2], axis=1, join="inner")`