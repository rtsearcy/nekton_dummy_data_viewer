#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 17:17:40 2023

@author: rtsearcy
"""

import streamlit as st
import pandas as pd
import os

# Import  data


# Streamlit App Setup
st.set_page_config(layout="wide", page_icon = 'nekton_logo.png')

# Title bar
title_col, logo_col = st.columns([7,1])
with title_col:
    st.title('''GIS Data''')
with logo_col:
    st.image('nekton_logo.png')
# hide streamlit components

# # # Sidebar
def add_sidebar_title():
    st.markdown(
        """
        <style>
            
              [data-testid="stSidebarNav"]::before {
                content: "Nekton Data System";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 50px;
                
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
add_sidebar_title()

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Maps
with st.expander('Blue Carbon Potential'):
    st.header('Blue Carbon Potential')
    
with st.expander('Soil Data'):
    st.header('Soil Data')
    
with st.expander('Remote Sensing'):
    st.header('Remote Sensing')
    
    col1, col2 = st.columns([1,2])
    with col1:
        site = st.selectbox('Site:', ['CA','VA'])
    with col2:
        year = st.radio('Year:', [2020,2021,2022], horizontal=True)
    
    tab1, tab2, tab3 = st.tabs(["Sentinel", "Planet", "NAIP"])
    
    with tab1:
        st.write('Source: European Space Agency')
        st.write('Resolution: 10m / XX days')
    
    with tab2:
        st.write('Source: Planet')
        st.write('Resolution: 3m / daily')
        
    with tab3:
        st.write('Source: National Agriculture Imagery Program')
        st.write('Resolution: < 1m / 1x per 4 years')