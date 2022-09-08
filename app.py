import streamlit as st
import pandas as pd
import numpy as np
import time
from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.datasets import fetch_openml

with st.spinner('Loading...'):
    time.sleep(1)
st.title('Weather Prediction using Python')
st.caption('Predicting Weather using the uploaded csv file')
st.info("Developed by NANDHAKUMAR S, SUJITH V, MOHAMED RAFEEK S, DHIVAKAR S [Daisi Hackathon]")
st.snow()
   
weather = datasets.fetch_openml(name='weather', version=2)
st.write('Features:',   weather.feature_names)
st.write('Target(s):',  weather.target_names)

df = pd.DataFrame( np.c_[weather.data, weather.target],columns=np.append(weather.feature_names, weather.target_names) )
df

st.write('Values:')
st.write(df['outlook'])
st.write('\nFrequencies:')
st.write( df['outlook'].value_counts() )
st.write('\nFrequencies grouped by target:')
st.write( df.groupby(['play','outlook']).size() )

st.write('Values:')
st.write(df['windy'])
st.write('\nFrequencies:')
st.write(df['windy'].value_counts())
st.write('\nFrequencies grouped by target:')
st.write( df.groupby(['play','windy']).size() )

st.write('Values:')
st.write(df['play'])
st.write('\nFrequencies:')
st.write(df['play'].value_counts())

st.write( 'Instances where play=yes:')
st.write( df.query('play == "yes"') )
meanYtemp = df.query('play == "yes"').temperature.mean()
stdYtemp  = df.query('play == "yes"').temperature.std()
st.write( '\nmean temperature (play=yes) ={:10.6f}'.format(meanYtemp) )
st.write( ' std temperature (play=yes) ={:10.6f}'.format( stdYtemp) )
st.write( '\nInstances where play=no:')
st.write( df.query('play == "no"') )
meanNtemp = df.query('play == "no"').temperature.mean()
stdNtemp  = df.query('play == "no"').temperature.std()
st.write( '\nmean temperature (play=no)  ={:10.6f}'.format(meanNtemp) )
st.write( ' std temperature (play=no)  ={:10.6f}'.format( stdNtemp) )


    

    
    
    
    
    
    
    
    
    
    
    
    


