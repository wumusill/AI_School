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

st.markdown("# Part2 서울시 사교육")


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
ratio_df = private_data.loc[:, ~condition]
ratio_df.index = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]

cost_df = private_data.loc[:, condition]
cost_df.index = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"]



# 1인당 평균 사교육비 그래프

fig1 = plt.figure(figsize=(10, 5))
sns.lineplot(data=cost_df, x=cost_df.index, y="평균 사교육비", label="평균")
sns.lineplot(data=cost_df, x=cost_df.index, y="초등학교 사교육비", label="초등학교")
sns.lineplot(data=cost_df, x=cost_df.index, y="중학교 사교육비", label="중학교")
sns.lineplot(data=cost_df, x=cost_df.index, y="고등학교 사교육비", label="고등학교")
sns.lineplot(data=cost_df, x=cost_df.index, y="일반고 사교육비", label="일반고")
plt.legend(bbox_to_anchor=(1, 1))
plt.title("1인당 평균 사교육비 (만원)")
plt.axvline(x = '15',linestyle='--')
plt.axvline(x = '19',linestyle='--')

# 사교육 참여율 그래프
fig2 = plt.figure(figsize=(10, 5))
sns.lineplot(data=ratio_df, x=ratio_df.index, y="평균 사교육 참여율(%)", label="평균")
sns.lineplot(data=ratio_df, x=ratio_df.index, y="초등 사교육 참여율(%)", label="초등")
sns.lineplot(data=ratio_df, x=ratio_df.index, y="중등 사교육 참여율(%)", label="중등")
sns.lineplot(data=ratio_df, x=ratio_df.index, y="고등 사교육 참여율(%)", label="고등")
sns.lineplot(data=ratio_df, x=ratio_df.index, y="일반고 사교육 참여율(%)", label="일반고")
plt.legend(bbox_to_anchor=(1, 1))
plt.title("사교육 참여율 (%)")
plt.axvline(x = '15',linestyle='--')
plt.axvline(x = '19',linestyle='--')


# Layout
container1 = st.container()
col1, col2 = st.columns(2)

with container1:
    with col1:
        fig1
    with col2:
        fig2