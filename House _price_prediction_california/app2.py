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
    MedInc=st.sidebar.slider('MedInc',float(X.MedInc.min()),float(X.MedInc.max()),float(X.MedInc.mean()))
    HouseAge=st.sidebar.slider('HouseAge',float(X.HouseAge.min()),float(X.HouseAge.max()),float(X.HouseAge.mean()))
    AveRooms=st.sidebar.slider('AveRooms',float(X.AveRooms.min()),float(X.AveRooms.max()),float(X.AveRooms.mean())) 
    AveBedrms=st.sidebar.slider('AveBedrms',float(X.AveBedrms.min()),float(X.AveBedrms.max()),float(X.AveBedrms.mean())) 
    Population=st.sidebar.slider('Population',float(X.Population.min()),float(X.Population.max()),float(X.Population.mean())) 
    AveOccup=st.sidebar.slider('AveOccup',float(X.AveOccup.min()),float(X.AveOccup.max()),float(X.AveOccup.mean()))
    Latitude=st.sidebar.slider('Latitude',float(X.Latitude.min()),float(X.Latitude.max()),float(X.Latitude.mean())) 
    Longitude=st.sidebar.slider('Longitude',float(X.MedInc.min()),float(X.Longitude.max()),float(X.Longitude.mean()))
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
