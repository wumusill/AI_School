import folium
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import json
from streamlit_folium import st_folium
import koreanize_matplotlib

st.set_page_config(
    # page_title="Likelion AI School",
    layout="wide",
)

st.markdown("# Part5 PISA Score")

# 국제 학업성취도 성적
# 국어 로드
@st.cache(allow_output_mutation=True)
def load_national_reading():
    data = pd.read_excel("https://raw.githubusercontent.com/wumusill/Structure/main/dataset/international_test.xls", sheet_name=0)
    return data

national_reading = load_national_reading()
national_reading[["Average", "Standard Error"]] = national_reading[["Average", "Standard Error"]].astype("float")


# 수학 로드
@st.cache(allow_output_mutation=True)
def load_national_math():
    data = pd.read_excel("https://raw.githubusercontent.com/wumusill/Structure/main/dataset/international_test.xls", sheet_name=1)
    return data

national_math = load_national_math()
national_math[["Average", "Standard Error"]] = national_math[["Average", "Standard Error"]].astype("float")


# 과학 로드
@st.cache(allow_output_mutation=True)
def load_national_science():
    data = pd.read_excel("https://raw.githubusercontent.com/wumusill/Structure/main/dataset/international_test.xls", sheet_name=2)
    return data

national_science = load_national_science()
national_science[["Average", "Standard Error"]] = national_science[["Average", "Standard Error"]].astype("float")

# 읽기 top5
reading_top5 = national_reading.sort_values(["Year/Study", "Average"], ascending=[True, False])
reading_top5 = reading_top5.groupby("Year/Study").head()

# 수학 top5
math_top5 = national_math.sort_values(["Year/Study", "Average"], ascending=[True, False])
math_top5 = math_top5.groupby("Year/Study").head()

# 과학 top5
science_top5 = national_science.sort_values(["Year/Study", "Average"], ascending=[True, False])
science_top5 = science_top5.groupby("Year/Study").head()

# 읽기 시각화
reading = sns.lmplot(data=reading_top5, x="Year/Study", y="Average", hue='Jurisdiction', ci=None)
fig_reading = reading.fig
plt.title("reading score")

# 수학 시각화
math = sns.lmplot(data=math_top5, x="Year/Study", y="Average", hue='Jurisdiction', ci=None)
fig_math = math.fig
plt.title("math score")

# 과학 시각화
science = sns.lmplot(data=science_top5, x="Year/Study", y="Average", hue='Jurisdiction', ci=None)
fig_science = science.fig
plt.title("science score")


# Layout
container2 = st.container()
col3, col4, col5 = st.columns(3)

with container2:
    with col3:
        fig_reading
    with col4:
        fig_math
    with col5:
        fig_science
