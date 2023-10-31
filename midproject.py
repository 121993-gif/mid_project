import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('master.csv')
st.title('Suicides Statistic Data Analysis ')
#st.image('download.jpeg')
st.write(''' This app performs simple EDA on suicides data
            * **Python libraries:** pandas, streamlit, numpy, matplotlib, seaborn
         * **Data source:** [Kaggle](https://www.kaggle.com/datasets/russellyates88/suicide-rates-overview-1985-to-2016)''')

st.subheader('top 3 country suicides')
top3 = df.nlargest(3, 'suicides/100k pop')[['country', 'suicides/100k pop']]

top_country_dict = top3.set_index('country').to_dict()




num_cols = df.select_dtypes(include=['int64', 'float64']).columns.to_list()



col1, col2 = st.columns(2)
with col1:
    num_feat_choice = st.selectbox('choose numerical feature', num_cols)
    
with col2:
    plot_type = st.selectbox('choose plot type:', ['histogram', 'barplot', 'boxplot'])
if plot_type == 'histogram':
    st.plotly_chart(px.histogram(df, x=num_feat_choice, title=num_feat_choice))
elif plot_type == 'bar plot':
     st.plotly_chart(px.bar(df, x=num_feat_choice, title=num_feat_choice))
else:
    st.plotly_chart(px.box(df, x=num_feat_choice, title=num_feat_choice))
  
 
cat_cols = df.select_dtypes(include=['object']).columns.to_list()
    
    
col1, col2 = st.columns(2)
with col1:
    cat_feat_choice = st.selectbox('choose categorical feature', cat_cols)

with col2:
    st.write(df[cat_feat_choice].value_counts().head(3))
    st.write('no of unique categorical:', df[cat_feat_choice].nunique())
    st.plotly_chart(px.bar(df, x=cat_feat_choice, title=cat_feat_choice))
    
    
num_cols = df.select_dtypes(include=['int64', 'float64']).columns.to_list()
col1, col2 = st.columns(2)
with col1:
    feat_choice1 = st.selectbox('choose numerical feature1', num_cols)
    
    
with col2:
     feat_choice2 = st.selectbox('choose numerical feature2', num_cols)


    
        
st.write('correlation:', df[feat_choice1].corr(df[feat_choice2]))
st.plotly_chart(px.scatter(df, x=feat_choice1, y=feat_choice2, title=feat_choice1+ ' vs '+feat_choice2))

st.write('#### summary :')
st.write('all correlations value is very weak')
    
    












    

    

    

    
    
    
    






    
    



    
    
    
 
    
    
    



  


             