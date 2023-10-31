import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('master.csv')


cat_cols = df.select_dtypes(include=['object']).columns.to_list()
cat_feat_choice = st.selectbox('choose catigorical feature', cat_cols)

num_cols = df.select_dtypes(include=['int64', 'float64']).columns.to_list()
num_feat_choice = st.selectbox('choose numerical feature', num_cols)

st.write(f"top 3 : {cat_feat_choice} vs {num_feat_choice}")
st.write(df.groupby(cat_feat_choice).max()[num_feat_choice].nlargest(3))
st.plotly_chart(px.box(df, x=cat_feat_choice, y=num_feat_choice, title=cat_feat_choice + ' vs ' + num_feat_choice))


st.write(f"the median : {cat_feat_choice} vs {num_feat_choice}")
st.write(df.groupby(cat_feat_choice)[num_feat_choice].median(3).sort_values(ascending=False))
st.plotly_chart(px.box(df, x=cat_feat_choice, y=num_feat_choice, title=cat_feat_choice + ' vs ' + num_feat_choice))

st.write(f"last 3 : {cat_feat_choice} vs {num_feat_choice}")
st.write(df.groupby(cat_feat_choice).min()[num_feat_choice].nsmallest(3))
st.plotly_chart(px.box(df, x=cat_feat_choice, y=num_feat_choice, title=cat_feat_choice + ' vs ' + num_feat_choice))

st.write(f"sum : {cat_feat_choice} vs {num_feat_choice}")
st.write(df.groupby(cat_feat_choice)[num_feat_choice].sum()) 
st.plotly_chart(px.box(df, x=cat_feat_choice, y=num_feat_choice, title=cat_feat_choice + ' vs ' + num_feat_choice))

st.write('#### summary :')
st.write('*sex :')
st.write('there is a relationship between gender and the number of suicides')
st.write('the suicide rate is significantly higher among males compared to females.')

st.write('*country :')
st.write('there is a relationship between the country and the number of suicides. The data indicates that suicide rates vary significantly between countries. Some countries have higher suicide rates than others')

st.write('*age :')
st.write('there is a relationship between age and the number of suicides. The data suggests that there is a clear variation in suicide rates across different age groups. Specifically, it appears that suicide rates are significantly higher in the "75+ years" age group compared to other age categories.')

st.write('*generation :')
st.write('There appears to be a relationship between the generation and the number of suicides.  there is variation in suicide rates among different generations. For instance, the "Silent Generation" and "Baby Boomers" seem to have higher suicide rates in general compared to other generations')



