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

st.markdown("# Part1 서울시 구별 학업 중단율")

DATA_URL = "https://raw.githubusercontent.com/wumusill/Structure/main/dataset_eda/seoul_stop_school.csv"

@st.cache(allow_output_mutation=True)
def load_data():
    data = pd.read_csv(DATA_URL)
    data.index = ["2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]
    data = data.astype("float")
    return data


data = load_data()

st.markdown("## 조회 학교")
# 학교 조건
selected_school = st.selectbox("학교", ["초등학교", "중학교", "고등학교"])
condition = data.columns.str.contains(f"{selected_school} 학업중단율")
school_data = data.loc[:, condition]

if st.checkbox('Show data'):
    st.subheader('data')
    st.write(school_data)


st.markdown("## 조회 연도")
# 연도 조건
year_to_filter = st.slider('연도', 2011, 2020, 2015)
year_condition = school_data.index == str(year_to_filter)
year_school_data = school_data[year_condition].T

df_temp = year_school_data
df_temp = df_temp.reset_index()
df_temp = df_temp.rename(columns={'index':'name'})
df_temp = df_temp.drop(0)
df_temp["name"] = df_temp["name"].map(lambda x: x.split()[0])
# df_temp


st.markdown("## 시각화")
m = folium.Map(location=[37.566345, 126.977893],
    zoom_start = 11,
    tiles = 'Stamen Terrain')

# 구별 위경도 json
geo_url = 'https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json'
response = requests.get(geo_url)
geo_json = json.loads(response.content)


folium.GeoJson(geo_json,
              name="지역구").add_to(m)


# 행정구역 경계 표시, 중단율 색칠
m.choropleth(geo_data=geo_json,
                 name="지역구",
                 data=df_temp,
                 columns=[df_temp.columns[0], df_temp.columns[1]],
                 key_on="properties.name",
                 fill_color='YlGn',
                 fill_opacity=0.7,
                 line_opacity=0.2,
                 legend_name="구별 학업 중단율"
                 )


# 출력
st_data = st_folium(m, width=2100)