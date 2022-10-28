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

st.markdown("# Part4 서울시 사교육비와 학업 성취도의 관계")


# 사교육비 데이터 로드
@st.cache(allow_output_mutation=True)
def load_private_data():
    data = pd.read_csv("https://raw.githubusercontent.com/wumusill/Structure/main/dataset/seoul_private.csv")
    data = data.drop([0, 1, 2])
    return data


private_data = load_private_data()
private_data.columns = ["시점", "평균 사교육비", "평균 사교육 참여율(%)", 
                    "초등학교 사교육비", "초등 사교육 참여율(%)", 
                    "중학교 사교육비", "중등 사교육 참여율(%)", 
                    "고등학교 사교육비", "고등 사교육 참여율(%)", 
                    "일반고 사교육비", "일반고 사교육 참여율(%)"]
private_data = private_data.astype('float')

condition = private_data.columns.str.contains("사교육비")
cost_df = private_data.loc[:, condition]
cost_df.index = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]

cost_df

cost_mid = cost_df["중학교 사교육비"]




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
kr_mid_test
temp = kr_mid_test.groupby(["연도", "과목"])[["3수준", "2수준", "1수준"]].mean()
temp

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
col6, col7, col8 = st.columns(3)

# with container3:
#     with col6:
#         mid
#     with col7:
#         high
#     with col8:
#         general_high