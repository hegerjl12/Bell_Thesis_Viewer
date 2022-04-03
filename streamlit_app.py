import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from deta import Deta
import random
import time

@st.cache(ttl=10)
def refreshDB():

    res1 = Image1DB.fetch()
    all_items1 = res1.items


    res2 = Image2DB.fetch()
    all_items2 = res2.items


    res3 = Image3DB.fetch()
    all_items3 = res3.items

    return all_items1, all_items2, all_items3



# set page config details
st.set_page_config(
     page_title="Bell Thesis",
     page_icon="🔔",
     layout="wide",
)

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Selina's Thesis")


# connect to databases
with st.spinner("Connecting to database..."):
     deta = Deta(st.secrets["deta_key"])
     Image1DB = deta.Base("testdb1")
     Image2DB = deta.Base("testdb2")
     Image3DB = deta.Base("testdb3")

# make columns
with st.container():
    col1, col2, col3 = st.columns(3)
    
    all_items1, all_items2, all_items3 = refreshDB()  

    # image1 wordcloud
    with col1:
        total_words = []
        #res = Image1DB.fetch()
        #all_items = res.items
        for item in all_items1:
            total_words.append(item.get('words'))
            
        text = " ".join(total_words)
        word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
        fig = plt.imshow(word_cloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt.show())

    # image 2 wordcloud
    with col2:
        total_words = []
        #res = Image2DB.fetch()
       # all_items = res.items
        for item in all_items2:
            total_words.append(item.get('words'))

        text = " ".join(total_words)
        word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
        fig = plt.imshow(word_cloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt.show())

    #image 3 wordcloud
    with col3:
        total_words = []
       # res = Image3DB.fetch()
       # all_items = res.items
        for item in all_items3:
            total_words.append(item.get('words'))

        text = " ".join(total_words)
        word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
        fig = plt.imshow(word_cloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt.show())  

#time.sleep(10)
#st.experimental_rerun()