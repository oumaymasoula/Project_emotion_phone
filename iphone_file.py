import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
df = pd.read_csv('data_out\iphone\commentIphone_csv')
st.title('Iphone react')
st.subheader('Dataset')
st.dataframe(df)
st.subheader('Data Numerical Statistic')
st.dataframe(df.describe())
st.subheader('Data Visualization with respect to sentiment')
left_column, right_column = st.columns(2)
with left_column:
    'Numerical Plot'
    num_feat = st.selectbox(
        'Select Numerical Feature', df.select_dtypes('number').columns)
    fig = px.histogram(df, x = num_feat, color = 'sentiment')
    st.plotly_chart(fig, use_container_width=True)
with right_column:
    'Categorical column'
    cat_feat = st.selectbox(
    'Select Categorical Feature', df.select_dtypes(exclude ='number').columns)
    fig = px.histogram(df, x=cat_feat, color = 'sentiment' )
st.plotly_chart(fig, use_container_width=True)

df=pd.read_csv('data_out\iphone\commentIphone_csv')
fig = px.pie(df, names=df['sentiment'])
fig.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig, use_container_width=True)