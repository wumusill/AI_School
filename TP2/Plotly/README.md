# 🦁 TIL

## 🔗 Link
> * [FinanceDataReader Tutorial](https://nbviewer.org/github/FinanceData/FinanceDataReader/blob/master/tutorial/FinanceDataReader%20Tutorial%20-%20%EC%97%AC%EB%9F%AC%20%EC%A2%85%EB%AA%A9%EC%9D%98%20%EA%B0%80%EA%B2%A9%EC%9D%84%20%ED%95%9C%EB%B2%88%EC%97%90.ipynb)
> * [실습 URL](http://finance.naver.com/sise/entryJongmok.naver?page=1)
> * [koreanize-matplotlib](https://github.com/ychoi-kr/koreanize-matplotlib) 
> * [그래프 다양한 style 설정](https://matplotlib.org/stable/tutorials/introductory/customizing.html)
> * [Plotly 공식문서](https://plotly.com/python/)
> * [Plotly 예제](https://plotly.com/python/time-series/)


## ✅ FinanceDataReader를 통한 여러 종목 수익률 비교
> python0301


* `%pwd` : Jupyter에서 현재 파일 경로 확인 방법
* `finder > cmd + shift + g` : 경로 복사
* `koreanize-matplotlib`
* `df1.merge(df2, left_on="co1", right_on="COL1", how="left")`
* `plt.style.available`
* `plt.style.use("ggplot")`
* `df_norm.resample("Q").mean()`


* 표준화(standardization) : 
  * 데이터가 평균으로 부터 얼마나 떨어져 있는지 나타내는 값으로 변환
  * (Z-score 표준화) : (측정값 - 평균) / 표준편차
* 정규화(normalization) : 
    * 데이터의 상대적 크기에 대한 영향을 줄이기 위해 0~1로 변환
    * (측정값 - 최소값) / (최대값 - 최소값)



* 왜도, skewness 는 실수 값 확률 변수의 확률 분포 비대칭성을 나타내는 지표 
  * 왜도의 값은 양수나 음수가 될 수 있으며 정의되지 않을 수도 있음
  * 왜도가 음수일 경우에는 왼쪽 부분에 긴 꼬리, 중앙값을 포함한 자료가 오른쪽에 더 많이 분포 
  * 왜도가 양수일 때는 오른쪽 부분에 긴 꼬리, 자료가 왼쪽에 더 많이 분포 
  * 평균과 중앙값이 같으면 왜도는 0


* 첨도, kurtosis 는 확률분포의 뾰족한 정도를 나타내는 척도
  * 관측치들이 어느 정도 집중적으로 중심에 몰려 있는가를 측정 
  * 첨도값(K)이 3에 가까우면 산포도가 정규분포에 가깝다. 
  * 3보다 작을 경우에는(K<3) 정규분포보다 더 완만하게 납작한 분포 
  * 첨도값이 3보다 큰 양수이면(K>3) 산포는 정규분포보다 더 뾰족한 분포


<br>


## ✅ Plotly를 이용한 Python 동적 시각화
> python0302


* `plotly`
* `cufflinks`
* `px.line(df, x="date", y="GOOG", title="일별 시세")`
* `facet_col="company"`
* `facet_col_wrap=2`
* `hover_data = {"date": "|%Y-%m-%d"}`