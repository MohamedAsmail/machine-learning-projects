import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
st.write("""
# House priceing regression in colifornia
""")
st.write('-----')
# load the dataset
cal_housing = fetch_california_housing()
X=pd.DataFrame(cal_housing.data, columns=cal_housing.feature_names)
Y=pd.DataFrame(cal_housing.target,columns=['MEDV'])
#declare the input section
st.sidebar.header('please enter input')
#function take input from user
def user_input_features():
    #declaration for variables to hold the data
    MedInc=st.sidebar.slider('MedInc',X.MedInc.min(),X.MedInc.max(),X.MedInc.mean())
    HouseAge=st.sidebar.slider('HouseAge',X.HouseAge.min(),X.HouseAge.max(),X.HouseAge.mean())
    AveRooms=st.sidebar.slider('AveRooms',X.AveRooms.min(),X.AveRooms.max(),X.AveRooms.mean()) 
    AveBedrms=st.sidebar.slider('AveBedrms',X.AveBedrms.min(),X.AveBedrms.max(),X.AveBedrms.mean()) 
    Population=st.sidebar.slider('Population',X.Population.min(),X.Population.max(),X.Population.mean()) 
    AveOccup=st.sidebar.slider('AveOccup',X.AveOccup.min(),X.AveOccup.max(),X.AveOccup.mean())
    Latitude=st.sidebar.slider('Latitude',X.Latitude.min(),X.Latitude.max(),X.Latitude.mean()) 
    Longitude=st.sidebar.slider('Longitude',X.MedInc.min(),X.Longitude.max(),X.Longitude.mean())
    #preparing the output of the function
    data={
        'MedInc':MedInc,
        'HouseAge':HouseAge,
        'AveRooms':AveRooms,
        'AveBedrms':AveBedrms,
        'Population':Population,
        'AveOccup':AveOccup,
        'Latitude':Latitude,
        'Longitude':Longitude
    }
    features=pd.DataFrame(data,index=[0])
    return features
    
df=user_input_features()
st.write('this is your input')
st.write(df)
st.write('-----')

# load model -train model-
model=RandomForestRegressor()
model.fit(X,Y)

#this is the predictionj
prediction=model.predict(df)
st.header("prediction")
st.write(prediction)
st.write("متوسط سعر المنزل")
st.balloons()
