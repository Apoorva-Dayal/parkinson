"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd 

# Import necessary functions from web_functions
from web_functions import predict

hide_st_style = """
<style>
MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                Predict the disease by entering the values !!!!!
            </p>
        """, unsafe_allow_html=True)
    with st.expander("View attribute details"):
        st.markdown("""MDVP:Fo(Hz) - Average vocal fundamental frequency\n
MDVP:Fhi(Hz) - Maximum vocal fundamental frequency\n
MDVP:Flo(Hz) - Minimum vocal fundamental frequency\n
MDVP:Jitter(%),MDVP:Jitter(Abs),MDVP:RAP,MDVP:PPQ,Jitter:DDP - Several
measures of variation in fundamental frequency\n
MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA - Several measures of variation in amplitude\n
NHR,HNR - Two measures of ratio of noise to tonal components in the voice\n
status - Health status of the subject (one) - Parkinson's, (zero) - healthy\n
RPDE,D2 - Two nonlinear dynamical complexity measures\n
DFA - Signal fractal scaling exponent\n
spread1,spread2,PPE - Three nonlinear measures of fundamental frequency variation""")
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    col1,col2 = st.columns(2)
    # Take input of features from the user.

    with col1:
        number_input_avff = st.number_input("AVFF",88,260,value=88)
        avff = st.slider("Average vocal fundamental frequency", int(df["AVFF"].min()), int(df["AVFF"].max()),value=number_input_avff)
        number_input_mavff = st.number_input("mavff",102,592,value=102)
        mavff = st.slider("Maximum vocal fundamental frequency", int(df["MAVFF"].min()), int(df["MAVFF"].max()),value=number_input_mavff)
        number_input_mivff = st.number_input("mivff",65,239,value=69)
        mivff = st.slider("Minimum vocal fundamental frequency", int(df["MIVFF"].min()), int(df["MIVFF"].max()),value=number_input_mivff)
        number_input_jitddp = st.number_input("JITTER",0.00,0.06,value=0.00)
        jitddp = st.slider("Jitter:DDP", float(df["Jitter:DDP"].min()), float(df["Jitter:DDP"].max()),value=number_input_jitddp)
        number_input_MDVPJIT = st.number_input("MVP",0.00,0.03,value=0.00)
        mdvpjit = st.slider("Multidimensional Voice Program:Jitter(%)", float(df["MDVP:Jitter(%)"].min()), float(df["MDVP:Jitter(%)"].max()),value=number_input_MDVPJIT)
        number_input_MDVPRAP = st.number_input("MDVP-RAP",0.00,0.02,value=0.00)
        mdvprap = st.slider("MDVP-RAP", float(df["MDVP:RAP"].min()), float(df["MDVP:RAP"].max()),value=number_input_MDVPRAP)
        number_input_MDVPAPQ = st.number_input("MDVP-APQ",0.01,0.14,value=0.01)
        mdvpapq = st.slider("MDVP-APQ", float(df["MDVP:APQ"].min()), float(df["MDVP:APQ"].max()),value=number_input_MDVPAPQ)
        number_input_MDVPPPQ = st.number_input("MDVP-PPQ",0.00,0.02,value=0.00)
        mdvpppq = st.slider("MDVP-PPQ", float(df["MDVP:PPQ"].min()), float(df["MDVP:PPQ"].max()),value=number_input_MDVPPPQ)
        number_input_mdvpshim = st.number_input("MDVP-Shimmer",0.01,0.12,value=0.01)
        mdvpshim = st.slider("MDVP-Shimmer", float(df["MDVP:Shimmer"].min()), float(df["MDVP:Shimmer"].max()),value=number_input_mdvpshim)
        
   
    with col2:
        number_input_shimdda = st.number_input("Shimmer-DDA",0.01,0.17,value=0.01)
        shimdda = st.slider("Shimmer-DDA", float(df["Shimmer:DDA"].min()), float(df["Shimmer:DDA"].max()),value=number_input_shimdda)
        number_input_shimapq3 = st.number_input("Shimmer-APQ3",0.00,0.06,value=0.00)
        shimapq3 = st.slider("Shimmer-APQ3", float(df["Shimmer:APQ3"].min()), float(df["Shimmer:APQ3"].max()),value=number_input_shimapq3)
        number_input_shimapq5 = st.number_input("Shimmer-APQ5",0.01,0.08,value=0.01)
        shimapq5 = st.slider("Shimmer-APQ5", float(df["Shimmer:APQ5"].min()), float(df["Shimmer:APQ5"].max()),value=number_input_shimapq5)
        number_input_nhr = st.number_input("NHR",0.00,0.31,value=0.00)
        nhr = st.slider("NHR", float(df["NHR"].min()), float(df["NHR"].max()),value=number_input_nhr)
        number_input_hnr = st.number_input("HNR",8.44,33.05,value=8.44)
        hnr = st.slider("HNR", float(df["HNR"].min()), float(df["HNR"].max()),value=number_input_hnr)
        number_input_rpde = st.number_input("RPDE",0.26,0.69,value=0.26)
        rpde = st.slider("RPDE", float(df["RPDE"].min()), float(df["RPDE"].max()),value=number_input_rpde)
        number_input_dfa = st.number_input("DFA",0.57,0.83,value=0.57)
        dfa = st.slider("DFA", float(df["DFA"].min()), float(df["DFA"].max()),value=number_input_dfa)
        number_input_d2 = st.number_input("D2",1.42,3.67,value=1.42)
        d2 = st.slider("D2", float(df["D2"].min()), float(df["D2"].max()),value=number_input_d2)
        number_input_ppe = st.number_input("PPE",0.04,0.53,value=0.04)
        ppe = st.slider("PPE", float(df["PPE"].min()), float(df["PPE"].max()),value=number_input_ppe)

    # Create a list to store all the features
    features = [avff, mavff, mivff, jitddp, mdvpjit, mdvprap,mdvpapq,mdvpppq,mdvpshim,shimdda,shimapq3,shimapq5,nhr,hnr,rpde,dfa,d2,ppe]
    col1,col2 = st.columns(2)
    # Take input of features from the user.

    with col1:
        st.write("AVFF IS ", avff)
        st.write("MAVFF IS ", mavff)
        st.write("MIVFF IS ", mivff)
        st.write("JITTER IS ",jitddp)
        st.write("MVP IS ", mdvpjit)
        st.write("MDVP-RAP IS ",mdvprap)
        st.write("MDVP-APQ IS ",mdvpapq)
        st.write("MDVP-PPQ IS ",mdvpppq)
        st.write("MDVP-SHIMMER IS ",mdvpshim)

    with col2:    
        st.write("SHIMMER-DDA IS ",shimdda)
        st.write("SHIMMER-APQ3 IS ",shimapq3)
        st.write("SHIMMER-APQ5 IS ",shimapq5)
        st.write("NHR IS ", nhr)
        st.write("HNR IS ", hnr)
        st.write("RPDE IS ",rpde)
        st.write("DFA IS ",dfa)
        st.write("D2 IS ",d2)
        st.write("PPE",ppe)

    st.header("The values entered by user")
    st.cache_data()
    df3 = pd.DataFrame(features).transpose()
    df3.columns=["AVFF", "MAVFF", "MIVFF","Jitter:DDP","MDVP:Jitter(%)","MDVP:RAP","MDVP:APQ","MDVP:PPQ","MDVP:Shimmer","Shimmer:DDA","Shimmer:APQ3","Shimmer:APQ5","NHR","HNR","RPDE","DFA","D2","PPE"]
    st.dataframe(df3)
    with st.expander("View attribute details"):
        st.markdown("""MDVP:Fo(Hz) - Average vocal fundamental frequency\n
MDVP:Fhi(Hz) - Maximum vocal fundamental frequency\n
MDVP:Flo(Hz) - Minimum vocal fundamental frequency\n
MDVP:Jitter(%),MDVP:Jitter(Abs),MDVP:RAP,MDVP:PPQ,Jitter:DDP - Several
measures of variation in fundamental frequency\n
MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA - Several measures of variation in amplitude\n
NHR,HNR - Two measures of ratio of noise to tonal components in the voice\n
status - Health status of the subject (one) - Parkinson's, (zero) - healthy\n
RPDE,D2 - Two nonlinear dynamical complexity measures\n
DFA - Signal fractal scaling exponent\n
spread1,spread2,PPE - Three nonlinear measures of fundamental frequency variation""")

    st.sidebar.info("The parameters which have the major contribution to Parkinson\'s disease detection are the D2-Receptor Data and PPE (Combination of 3 Non-linear fundamental frequency variation)")
    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        

        # Print the output according to the prediction
        if (prediction == 1):
            st.error("The person either has Parkison's disease or prone to get Parkinson's disease")
            if (ppe > 0.13 or d2 > 2.0):
                st.warning("There is a risk of Early-onset of Parkinson\'s Disease")
            elif (ppe > 0.26):
                st.warning("There is a risk of Idiopathic Parkinson\'s Disease. There is also a risk of Schizophrenia")
            elif (ppe > 0.37):
                st.warning("There is a risk of Acute Parkinson\'s Disease")
            elif ((mdvpshim + shimdda + shimapq3 + shimapq5) > 0.20 and d2 > 2):
                st.warning("There is a risk of slight tremor in fingers")
            
        else:
            st.success("The person is safe from Parkinson's disease")
            if(avff > 240):
                st.warning("But, there is a risk of vocal trembling or Secondary PD")


        # Print teh score of the model 
        st.sidebar.write("The model used is trusted by doctor and has an accuracy of ", round((score*100),2),"%")
