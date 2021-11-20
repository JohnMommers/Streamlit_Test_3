# My first streamlit application

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl


header = st.container()
dataset = st.container()
features = st.container()
modeltraining = st.container()

with header:
    st.title('ASAP - DATA - PROCESSING')
    st.text('John Mommers, 2021, version 1.0 (concept)')

with dataset:
    uploaded_file = st.file_uploader("Upload Data File", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        df.columns = ['accurate mass', 'mass intensity']
        np = df.shape[0]
        np = 'Number of mass peaks: ' + str(np)
        st.write(np)
        st.write(df.head(5))

        x = df['accurate mass']
        y = df['mass intensity']

        fig = plt.figure(figsize=(10, 4), dpi=80)
        plt.scatter(x, y, color='green', s=5, alpha=0.5)
        plt.xlabel('Accurate mass')
        plt.ylabel('Mass intensity')
        plt.title('Mass Spectrum')
        plt.show()
        st.pyplot(fig)