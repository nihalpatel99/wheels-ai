#importing required libraries
import streamlit as st 
import os
from together import Together
from llama_index.llms.together import TogetherLLM
import nltk
from io import BytesIO
from PIL import Image
import base64


api_key = ""

#Function for generating a response
def generate_response(question, response_style, api_key):
    prompt_template = """
You're an expert in motorsport knowledge of championships, cars, drivers, teams and tracks spanning from Formual 1 to World Endurance Championship to NASCAR
Your job is to answer the queries or questions asked by the users and provided detailed analysis, facts and insights on them.
Keep the topics related to motorsports only and if the user asks any topic other than motorsport, just say "Sorry i am only allowed to answer motorsport queries only".
The response style shoud be in {response_style} and in bullet points. 
Question: {question}

Answer:
"""
    
    prompt = prompt_template.format(question=question,response_style=response_style)
    llm = TogetherLLM(
    model="meta-llama/Meta-Llama-3-8B-Instruct-Lite", api_key=api_key
)

    resp = llm.complete(prompt)

    st.write(resp)
#Function for motorsport page
def motorsport():
    st.header("Motorsport Analysis")
    options = ["Lewis Hamilton (F1 Driver)", "Max Verstappen (F1 Driver)", "Sebastian Vettel (F1 Driver)", "Lando Norris (F1 Driver)", "Charles Leclerc (F1 Driver)", "Sébastien Buemi (WEC Driver)", "Mike Conway (WEC Driver)", "Brendon Hartley (WEC Driver)", "Bobby Labonte (NASCAR Driver)", "Jeff Gordon (NASCAR Driver)", "Jimmie Johnson (NASCAR Driver)", "Jeremy Clarkson (Top Gear)", "James May (Top Gear)", "Richard Hammond (Top Gear)", "Álex Palou (IndyCar Driver)", "Scott Dixon (IndyCar Driver)", "Sebastian Bourdaris (IndyCar Driver)", "Sébastien Loeb (WRC Driver)", "Sébastien Ogier (WRC Driver)", "Tommi Mäkinen (WRC Driver)"]
    
    choice = st.radio("Select your driver response style", options)
    
    st.write(f"You selected: {choice}")
    
    question = st.text_input("Enter your question")
    
    button_response = st.button("Generate Response")
    
    if button_response:
        if api_key and len(api_key) == 64:
            with st.spinner("Starting up engine and revving up the car"):
                generate_response(question,choice,api_key)
        else:
            st.error("Please specify your Together AI API Key")

#Convert response bytes to an image         
def b64_to_image(b64):
    image_data = base64.b64decode(b64)
    image = Image.open(BytesIO(image_data))
    return image

#Generate an image        
def generate_image(prompt):
    
     prompt_template = """
You're an expert in motorsport knowledge of designing amazing racing tracks
Your job is design a 2d race track {question} queried by the user
Keep the topics related to motorsports only and if the user asks any topic other than motorsport, just say "Sorry i am only allowed to answer motorsport queries only".
"""
     img_prompt = prompt_template.format(question=prompt)
     client = Together(api_key=api_key)
     response = client.images.generate(
     prompt=img_prompt,
     model="stabilityai/stable-diffusion-xl-base-1.0",
     width=832,
     height=1024,
     steps=40,
     n=4,
     seed=2001
)
     b64 = response.data[0].b64_json
     image = b64_to_image(b64)
     
     st.image(image, caption="RaceTrack", use_column_width=True)
 
#Function for generating racetrack page           
def track():
    st.header("Generate Racetrack")
    
    img_prompt = st.text_input("Enter your question")
    
    button_image = st.button("Generate RaceTrack")
    
    if button_image:
        if api_key and len(api_key) == 64:
            with st.spinner("Creating your amazing racetrack"):
                generate_image(img_prompt)
        else:
            st.error("Please specify your Together AI API Key")

if __name__ == "__main__":
    
    
    
    image = Image.open("WHEELSAI.png")
   
    st.image(image,width=200)
    
    st.markdown(
    """
    <style>
    .stApp {
        background-color: #a23e1e;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    
    st.title("WheelsAI: Providing detailed analysis and facts on motorsports and also Racetrack Generation")
    
   
    api_key_input = st.sidebar.text_input("Paste your Together AI API Key here:",type="password")
    
    api_key = api_key_input

    
    
    page = st.sidebar.radio("Drive to",["Motorsport Analysis","Racetrack Generation"])
    if page=="Racetrack Generation":
        track()
    elif page=="Motorsport Analysis":
        motorsport()          
       