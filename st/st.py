import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('외식 프랜차이즈 정보')

data_path = 'data.csv'

@st.cache
def load_data(nrows) -> pd.DataFrame:
    data = pd.read_csv(data_path, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    # 데이터 전처리
    data['sales_volume'] = data['sales_volume'].apply(lambda x: x.replace(',', '') if not pd.isna(x) else 0).astype(int)
    data['sales_volume_per_unit'] = data['sales_volume_per_unit'].apply(lambda x: x.replace(',', '') if not pd.isna(x) else 0).astype(int)
    data['new'] = data['new'].astype(int)
    data['termination'] = data['termination'].astype(int)
    data['cost'] = data['cost'].apply(lambda x: x.replace(',', '')).astype(int)
    return data

# 데이터 불러오기
data = load_data(10000)

# raw data 확인 (개발용)
# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

st.subheader('카테고리 별 가맹점사업자 부담금 단위(천원)')
group1 = data[['category', 'cost']].groupby(['category']).mean()
group1[' '] = group1.index
group1 = group1.sort_values(by='cost')
st.altair_chart(alt.Chart(group1).mark_bar().encode(x=alt.X(' ', sort=None), y='cost'), use_container_width=True)

st.subheader('프랜차이즈 별 평균매출액 Top 10 단위(천원)')
radio = st.radio('선택하세요', ('평균매출액', '면적(3.3m^2)당 평균매출액'))
if radio == '평균매출액':
    kind = 'sales_volume'
else:
    kind = 'sales_volume_per_unit'
category = data['category'].unique()
options = st.multiselect('카테고리를 선택하세요', category, category[0])
group2 = data[data['category'].isin(options)]
group2 = group2.sort_values(by=kind, ascending=False)[:10]
st.altair_chart(alt.Chart(group2).mark_bar().encode(x=alt.X('brand', sort=None), y=kind), use_container_width=True)