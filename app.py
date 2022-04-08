import streamlit as st
import pandas as pd
import pickle
from sklearn.compose import ColumnTransformer
pipe=pickle.load(open("pipe.pkl",'rb'))

team=['Sunrisers Hyderabad', 'Royal Challengers Bangalore',
       'Kolkata Knight Riders', 'Kings XI Punjab', 'Delhi Capitals',
       'Mumbai Indians', 'Chennai Super Kings', 'Rajasthan Royals']


city=['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

st.header("IPL win predictor by over")

col1,col2=st.columns(2)
with col1:
    batting=st.selectbox('Battign Team',sorted(team))

with col2:
    bowling=st.selectbox("Bowling team",sorted(team))

city_selected=st.selectbox("Select City ",sorted(city))

total=st.number_input('Target Score')

col1,col2,col3,col4=st.columns(4)

with col1:
    st.header('Run')
    run=st.number_input('Run')
with col2:
    st.header('Wicket')
    wicket=st.number_input("Wicket")
with col3:
    st.header('over')
    over=st.number_input("Over",)
with col4:
    st.header('ball')
    ball=st.number_input("ball",)

if st.button("Predict"):
    run_left=(total-run)
    wicket_left=11-wicket
    ball_left=120-(over*6+ball)
    crr=run*6/(over*6+ball) 
    rrr=run_left*6/(ball_left)          

    dic={
        "batting_team":[batting],
        "bowling_team":[bowling],
        'city':[city_selected],
        "run_left":[run_left],
        'ball_left':[ball_left],
        'wicket_left':[wicket_left],
        'total_runs_x':[total],
        'crr':[crr],
        'rrr':[rrr],
    }   
    data=pd.DataFrame(dic)
    if ball_left*6>run_left and wicket<10:
        value=pipe.predict_proba(data)      
    elif wicket>=10 or ball_left*6<run_left :
        value=[[1,0]]
    
    st.text('winning probability of :-'+batting+" "+str(round(value[0][1]*100)))
    st.text('winning probalility of :-'+bowling+' '+str(round(value[0][0]*100)))

