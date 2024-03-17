"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Parkinson's Detection by AAP")

    # Add image to the home page
    st.image("./images/home.png",width=700)

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;background-color:gray;text-align:left;padding:12px;border-radius:13px">
Parkinson's disease is a neurodegenerative disorder that primarily affects movement. It gradually progresses over time, causing a variety of symptoms that can significantly impact a person's quality of life. 
<p style="font-size:20px;background-color:gray;text-align:left;padding:12px;border-radius:13px">
Here's a detailed overview of Parkinson's disease:<br><br>Causes:
Parkinson's disease is caused by the gradual degeneration of nerve cells in the brain, particularly those that produce dopamine. The exact cause of this degeneration is not fully understood, but it is believed to involve a combination of genetic and environmental factors. 
<p style="font-size:20px;background-color:gray;text-align:left;padding:12px;border-radius:13px">
Some potential contributors to Parkinson's disease include:<br><br>
Genetics: While most cases of Parkinson's disease are sporadic, meaning they occur without a known cause, a small percentage of cases are thought to be hereditary, with mutations in certain genes increasing the risk of developing the condition.
Environmental Factors: Exposure to certain environmental toxins, such as pesticides and herbicides, may increase the risk of Parkinson's disease, though the evidence is not conclusive.<br>
Age: Parkinson's disease most commonly develops in people over the age of 60, although it can occur at a younger age, known as early-onset Parkinson's.
Symptoms:
Parkinson's disease affects each individual differently, and the severity and progression of symptoms can vary widely. <br>Common symptoms include:
Tremors: Involuntary shaking, usually starting in the hands or fingers, that occurs at rest.<br>
Bradykinesia: Slowness of movement, which can make simple tasks like walking or getting out of a chair difficult.<br>
Muscle Rigidity: Stiffness and tension in the muscles, which can cause pain and limit range of motion.<br>
Postural Instability: Impaired balance and coordination, leading to difficulty standing and an increased risk of falls.
Impaired Speech and Writing: Changes in speech patterns, such as softening of the voice or slurring of words, and difficulty writing.<br>
Loss of Automatic Movements: Difficulty with unconscious movements like blinking, smiling, or swinging the arms while walking.
Non-Motor Symptoms: Parkinson's disease can also cause a range of non-motor symptoms, including cognitive impairment, depression, anxiety, sleep disturbances, and gastrointestinal problems.
<p style="font-size:20px;background-color:gray;text-align:left;padding:12px;border-radius:13px">
Summary ::--
Parkinson's disease is a progressive condition, meaning symptoms typically worsen over time. However, the rate of progression can vary widely among individuals. With proper treatment and management strategies, many people with Parkinson's disease are able to maintain a good quality of life for many years after diagnosis.
Research into Parkinson's disease continues, with ongoing efforts to better understand the underlying causes of the condition, develop more effective treatments, and ultimately find a cure.
        </p>
    """, unsafe_allow_html=True)