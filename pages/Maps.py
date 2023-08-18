#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 17:17:40 2023

@author: rtsearcy
"""

import streamlit as st
import pandas as pd
import os
from PIL import Image
#from leafmap import leafmap
import leafmap.foliumap as leafmap
#import leafmap
from datetime import datetime, timedelta


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
    
    bc_img = Image.open('./pages/BC_wealth_nations.png')
    st.image(bc_img, use_column_width='always')
    st.write('Source: [Bertram et al. (2021)]'+\
             '(https://doi.org/10.1038/s41558-021-01089-4)'
             )
    
with st.expander('Soil Data'):
    st.header('Soil Data')
    
    soil_img = Image.open('./pages/soil_core_map.png')
    st.image(soil_img)
    st.write('Source: [Fourqurean et al. (2012)]'+\
             '(https://doi.org/10.1038/ngeo1477)'
             )
    
with st.expander('Remote Sensing'):
    st.header('Remote Sensing')
    
    col1, col2 = st.columns([1,2])
    with col1:
        site = st.selectbox('Site:', ['Tomales Bay','Virginia'])
        if site == 'Tomales Bay':
            map_center = [38.123214, -122.883453]
        elif site == 'Virginia':
            map_center = [37.16, -75.93]
   
    with col2:
        slider = st.slider('Date:', 
                           value=datetime(2018, 1, 1, 1, 1),
                           min_value=datetime(2018, 1, 1, 1, 1), 
                           max_value=datetime(2023, 12, 1, 1, 1),
                           step=timedelta(days=30),
                           format="MM/YYYY")
    
    tab1, tab2, tab3 = st.tabs(["Planet", "Sentinel", "NAIP"])
    

    with tab1:
        st.write('Resolution: 3m / daily') 
    
        os.environ["PLANET_API_KEY"] = '6b4d53883da74c35852dc7a342c42c74'
        
        m = leafmap.Map(center=map_center, zoom=11)
        m.add_planet_by_month(year=slider.year, month=slider.month)
        
        #st.write(m)
        m.to_streamlit(height=500)
        
        
        #m.to_html('./temp_html.html')
        
        # st.write('''
        #          [link](temp_html.html)
        #          ''')
    
    with tab2:
        st.write('Source: European Space Agency')
        st.write('Resolution: 10m / XX days')
        
        st.subheader('Data TBD')
    
        
    with tab3:
        st.write('Source: National Agriculture Imagery Program')
        st.write('Resolution: < 1m / 1x per 4 years')
        
        st.subheader('Data TBD')