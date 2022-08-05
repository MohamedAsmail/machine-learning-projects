import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor
#define name of the app
st.write("""
# House priceing regression
""")
st.write('----')

# load data to know boundries boston is data set from sklearn
#data columns
boston=datasets.load_boston()
X=pd.DataFrame(boston.data,columns=boston.feature_names)
#target outputs
Y=pd.DataFrame(boston.target,columns=['MEDV'])

# crate sidebar
# declare the input section user
# build function 
#sidebar slider ___________
st.sidebar.header('please Mohamed inter input')
#function to take input from user
def user_input_features():
    # declaration for variables to hold the data
    CRIM=st.sidebar.slider('CRIM', X.CRIM.min(), X.CRIM.max(), X.CRIM.mean())
    ZN=st.sidebar.slider('ZN', X.ZN.min(), X.ZN.max(), X.ZN.mean())
    INDUS=st.sidebar.slider('INDUS', X.INDUS.min(), X.INDUS.max(), X.INDUS.mean())
    CHAS=st.sidebar.slider('CHAS', X.CHAS.min(), X.CHAS.max(), X.CHAS.mean())
    NOX=st.sidebar.slider('NOX', X.NOX.min(), X.NOX.max(), X.NOX.mean())
    RM=st.sidebar.slider('RM', X.RM.min(), X.RM.max(), X.RM.mean())
    AGE=st.sidebar.slider('AGE', X.AGE.min(), X.AGE.max(), X.AGE.mean())
    DIS=st.sidebar.slider('DIS', X.DIS.min(), X.DIS.max(), X.DIS.mean())
    RAD=st.sidebar.slider('RAD', X.RAD.min(), X.RAD.max(), X.RAD.mean())
    TAX=st.sidebar.slider('TAX', X.TAX.min(), X.TAX.max(), X.TAX.mean())
    PTRATIO=st.sidebar.slider('PTRATIO', X.PTRATIO.min(), X.PTRATIO.max(), X.PTRATIO.mean())
    B=st.sidebar.slider('B', X.B.min(), X.B.max(), X.B.mean())
    LSTAT=st.sidebar.slider('LSTAT', X.LSTAT.min(), X.LSTAT.max(), X.LSTAT.mean())
    #preparing the output of the function
#bas data set EX: 'CRIM':CRIM    
    data={
        'CRIM':CRIM,
        'ZN':ZN,
        'INDUS':INDUS,
        'CHAS':CHAS,
        'NOX':NOX,
        'RM':RM,
        'AGE':AGE,
        'DIS':DIS,
        'RAD':RAD,
        'TAX':TAX,
        'PTRATIO':PTRATIO,
        'B':B,
        'LSTAT':LSTAT}
    # prepare to model
    features=pd.DataFrame(data,index=[0])
    return features
    
df=user_input_features()
# print the input to user
st.write('this is your input')
st.write(df)
# bulid line _____---------
st.write('----')

# load model train model-
model=RandomForestRegressor()
model.fit(X,Y)
prediction=model.predict(df)

#output section
st.header('predicton of MEDV')
st.write(prediction)
