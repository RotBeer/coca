import streamlit as st
import pandas as pd
import numpy as np

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



if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('프랜차이즈 별 가맹점사업자 부담금 (천원)')

category = data['category'].unique()

options = st.multiselect('카테고리를 선택하세요', category, category[0])