import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from deta import Deta
import random

# set page config details
st.set_page_config(
     page_title="Bell Thesis",
     page_icon="🔔",
     layout="wide",
)

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Selina's Thesis")

with st.spinner("Connecting to database..."):
     # connect to databases
     deta = Deta(st.secrets["deta_key"])
     Image1DB = deta.Base("image1db")
     Image2DB = deta.Base("image2db")
     Image3DB = deta.Base("image3db")
     Image4DB = deta.Base("image4db")
     Image5DB = deta.Base("image5db")


with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        total_words = []
        res = Image1DB.fetch()
        all_items = res.items
        for item in all_items:
            total_words.append(item.get('words'))
            
        text = " ".join(total_words)
        word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
        fig = plt.imshow(word_cloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt.show())

    with col2:
        total_words = []
        res = Image2DB.fetch()
        all_items = res.items
        for item in all_items:
            total_words.append(item.get('words'))

        text = " ".join(total_words)
        word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
        fig = plt.imshow(word_cloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt.show())

    with col3:
        total_words = []
        res = Image3DB.fetch()
        all_items = res.items
        for item in all_items:
            total_words.append(item.get('words'))

        text = " ".join(total_words)
        word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
        fig = plt.imshow(word_cloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt.show())