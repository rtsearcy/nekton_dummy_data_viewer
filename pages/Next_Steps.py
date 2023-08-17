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


# Streamlit App
st.set_page_config(layout="wide", page_icon = 'nekton_logo.png')

# Title bar
title_col, logo_col = st.columns([7,1])
with title_col:
    st.title('''Next Steps''')
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

