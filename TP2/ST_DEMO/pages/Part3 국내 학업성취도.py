import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib

st.set_page_config(
    # page_title="Likelion AI School",
    layout="wide",
)

st.markdown("# Part3 국내 학업성취도")
st.markdown("* 국내 학업성취도의 경우 2016년 까지 전국 모든 학교에서 실시하여 지역별 데이터가 있음")
st.markdown("* 2017년 이후 학교 줄 세우기 논란에 의한 전국 3% 표집 평가로 지역별 데이터가 없음")
st.markdown("* 서울 데이터가 전국 데이터와 큰 차이를 보이지 않아 전국 데이터로 진행")

# 국내 학업성취도 성적 
# 중등 로드
@st.cache(allow_output_mutation=True)
def load_kr_mid_test():
    data = pd.read_excel("https://raw.githubusercontent.com/wumusill/Structure/main/dataset/kr_test.xls", sheet_name="중등")
    return data


# 고등 로드
@st.cache(allow_output_mutation=True)
def load_kr_high_test():
    data = pd.read_excel("https://raw.githubusercontent.com/wumusill/Structure/main/dataset/kr_test.xls", sheet_name="고등")
    return data

# 데이터 로드
kr_mid_test = load_kr_mid_test()
kr_high_test = load_kr_high_test()


# 사이드바 검색 기능
st.sidebar.header("검색 조건")
# 수준 검색
l = ["3수준", "2수준", "1수준"]
# l.append("All")
selected_level = st.sidebar.selectbox("Level", l)


mid_3 = sns.lmplot(data=kr_mid_test, x="연도", y=selected_level, hue='과목', ci=None)
fig_mid_3 = mid_3.fig
plt.title(f"국내 중학생 학업성취도 평가 {selected_level}")


high_3 = sns.lmplot(data=kr_high_test, x="연도", y=selected_level, hue='과목', ci=None)
fig_high_3 = high_3.fig
plt.title(f"국내 고등학교 학업성취도 평가 {selected_level}")

# Layout
container3 = st.container()
col6, col7 = st.columns(2)

with container3:
    with col6:
        fig_mid_3
    with col7:
        fig_high_3


# mid_2 = sns.lmplot(data=kr_mid_test, x="연도", y="2수준", hue='과목', ci=None)
# fig_mid_2 = mid_2.fig
# plt.title("국내 중학생 학업성취도 평가 2수준")

# high_2 = sns.lmplot(data=kr_high_test, x="연도", y="2수준", hue='과목', ci=None)
# fig_high_2 = high_2.fig
# plt.title("국내 고등학교 학업성취도 평가 2수준")

# # Layout
# container4 = st.container()
# col8, col9 = st.columns(2)

# with container4:
#     with col8:
#         fig_mid_2
#     with col9:
#         fig_high_2


# mid_1 = sns.lmplot(data=kr_mid_test, x="연도", y="1수준", hue='과목', ci=None)
# fig_mid_1 = mid_1.fig
# plt.title("국내 중학생 학업성취도 평가 1수준")

# high_1 = sns.lmplot(data=kr_high_test, x="연도", y="1수준", hue='과목', ci=None)
# fig_high_1 = high_1.fig
# plt.title("국내 고등학교 학업성취도 평가 1수준")

# # Layout
# container5 = st.container()
# col10, col11 = st.columns(2)

# with container5:
#     with col10:
#         fig_mid_1
#     with col11:
#         fig_high_1