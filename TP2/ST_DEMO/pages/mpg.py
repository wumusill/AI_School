import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
import plotly.express as px


# page 설정
# 무조건 상단에 위치해야 함
# html header 태그 안에 들어갈 내용
st.set_page_config(
    page_title="Likelion AI School 자동차 연비 App",
    page_icon="🚗",
    layout="wide",
)


# 메인 화면 제목 마크다운
st.markdown("# 자동차 연비 🚗")

# 왼쪽 사이드바 제목 마크다운
st.sidebar.markdown("# 자동차 연비 🚗")

# 데이터 URL
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"


# 데이터를 로드할 때 캐시 적용하는 함수
@st.cache
def load_data(nrows):
   data = pd.read_csv(url, nrows=nrows)
   return data

# 데이터 호출
data = load_data(1000)


# 사이드바 검색 기능
st.sidebar.header("검색 조건")
# 연도 검색 기준
l = list(reversed(range(data["model_year"].min(), data["model_year"].max())))
# l.append("All")
selected_year = st.sidebar.selectbox("Year", l)
# 지역 검색 기준
sorted_unique_origin = sorted(data["origin"].unique())
selected_origin = st.sidebar.multiselect("origin", sorted_unique_origin, sorted_unique_origin)


# 설정된 검색 기준으로 데이터 준비
if selected_year > 0 :
   mpg = data[data.model_year == selected_year]
# else:
#    mpg = data

if len(selected_origin) > 0:
   mpg = mpg[data.origin.isin(selected_origin)]


# 데이터 출력
st.dataframe(mpg)

# 데이터 시각화
st.line_chart(mpg["mpg"])
st.bar_chart(mpg["mpg"])

fig, ax = plt.subplots(figsize=(10, 3))
sns.barplot(data=mpg, x="origin", y="mpg").set_title("origin 별 자동차 연비")
st.pyplot(fig)

pxh = px.histogram(data, x="origin", title="지역별 자동차 연비 데이터 수")
st.plotly_chart(pxh)

mph = px.histogram(data, x="origin", y="horsepower", title="마력", histfunc="avg")
st.plotly_chart(mph)

plt.title("그래프 제목")
plt.figure(figsize=(10, 3))
lm = sns.lmplot(data=data, x="mpg", y="weight", hue="origin", ci=None)
st.pyplot(lm)