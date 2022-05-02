import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from deta import Deta
import random
import time
from streamlit_autorefresh import st_autorefresh

if 'images_choice' not in st.session_state:
     st.session_state.images_choice = [1, 2, 3, 4, 5]

if 'i' not in st.session_state:
     st.session_state.i = 0
    
def refreshDB():

    res1 = Image1DB.fetch()
    all_items1 = res1.items

    res2 = Image2DB.fetch()
    all_items2 = res2.items

    res3 = Image3DB.fetch()
    all_items3 = res3.items

    res4 = Image4DB.fetch()
    all_items4 = res4.items

    res5 = Image5DB.fetch()
    all_items5 = res5.items

    return all_items1, all_items2, all_items3, all_items4, all_items5



# set page config details
st.set_page_config(
     page_title="Bell Thesis",
     page_icon="🔔",
     layout="wide",
)

st.set_option('deprecation.showPyplotGlobalUse', False)

# connect to databases
with st.spinner("Connecting to database..."):
     deta = Deta(st.secrets["deta_key"])
     Image1DB = deta.Base("image1db")
     Image2DB = deta.Base("image2db")
     Image3DB = deta.Base("image3db")
     Image4DB = deta.Base("image4db")
     Image5DB = deta.Base("image5db")



# make columns
with st.container():
       
    all_items1, all_items2, all_items3, all_items4, all_items5 = refreshDB()  

    st.session_state.i = (st.session_state.i + 1) % 6 

    #random.choice(st.session_state.images_choice)
    #st.write(st.session_state.i)

    if st.session_state.i == 1:
        total_words = []
        for item in all_items1:
            total_words.append(item.get('words'))
            
        text = " ".join(total_words)
        word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
        fig = plt.imshow(word_cloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt.show())

    if st.session_state.i == 2:
        total_words = []
        for item in all_items2:
            total_words.append(item.get('words'))

        text = " ".join(total_words)
        word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
        fig = plt.imshow(word_cloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt.show())

    if st.session_state.i == 3:
        total_words = []
        for item in all_items3:
            total_words.append(item.get('words'))

        text = " ".join(total_words)
        word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
        fig = plt.imshow(word_cloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt.show())

    if st.session_state.i == 4:
        total_words = []
        for item in all_items4:
            total_words.append(item.get('words'))
            
        text = " ".join(total_words)
        word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
        fig = plt.imshow(word_cloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt.show())

    if st.session_state.i == 5:
        total_words = []
        for item in all_items5:
            total_words.append(item.get('words'))

        text = " ".join(total_words)
        word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
        fig = plt.imshow(word_cloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt.show())

    if st.session_state.i == 0:
        st.experimental_rerun()



count = st_autorefresh(interval=10000, limit=100, key="fizzbuzzcounter")