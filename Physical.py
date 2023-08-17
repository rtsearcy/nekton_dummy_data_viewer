#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 17:17:40 2023

@author: rtsearcy
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import os

## Import data
tide = pd.read_csv('tide.csv')
tide['date'] = pd.to_datetime(tide['date'])
tide.set_index('date', inplace=True)

waves = pd.read_csv('waves.csv')
waves['date'] = pd.to_datetime(waves['date'])
waves.set_index('date', inplace=True)
waves['year'] = waves.index.year

wq = pd.read_csv('water_quality.csv')
wq['date'] = pd.to_datetime(wq['date'])
wq.set_index('date', inplace=True)
wq['year'] = wq.index.year
wq['month'] = wq.index.month


##  App
st.set_page_config(layout="wide", page_icon = 'nekton_logo.png')

# Title bar
title_col, logo_col = st.columns([7,1])
with title_col:
    st.title('''Physical Oceanography Data''')
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


tab1, tab2, tab3 = st.tabs(["Tide", "Waves", "Water Quality"])

with tab1: # Tide
      
    col1, col2 = st.columns([1,3.5])

    with col1:
        # Choose location
        site = st.selectbox('Site:', ['San Francisco', 'Virginia'])
        # Choose dates
        sd = st.date_input("Start Date:", tide.index[4000])
        ed = st.date_input("End Date:", tide.index[5000])
    
    with col2:      
        # Update Plot
        #st.line_chart(tide[sd:ed][site])
        plot_data = tide.loc[sd:ed]
        fig = px.line(plot_data, y=site,
                      labels = {
                          site: 'm above MLLW',
                          'date': ''
                          })
        fig.update_layout(margin=dict(l=10, t=10, b=5))
        st.plotly_chart(fig, use_container_width=True)

    st.write('Source: NOAA CO-OPS')
    st.table(tide[sd:ed][site].to_frame().head(10))


with tab2: # waves
    wave_site = st.multiselect('Site(s):', list(waves.site.unique()), default = None)
    params = ['Hs', 'Td', 'Ta', 'dir', 'temp']
    wave_var = st.radio('Parameter:', params, horizontal=True)
    wave_plot = waves[waves.site.isin(wave_site)]
    wave_plot= wave_plot.fillna(wave_plot[params].median())
    
    wave_fig = px.box(wave_plot, x="year", y=wave_var, color='site', 
                      notched=False, labels={'year':''})
    wave_fig.update_layout(margin=dict(l=10, t=10, b=5))
    st.plotly_chart(wave_fig, use_container_width=True)
    st.write('Source: CDIP')

with tab3:  # Water quality
    params = ['Chlorophyll', 'Salinity', 'Temperature']

    wq_col, wq_col2 = st.columns([1,3])
    with wq_col:
        wq_year = st.selectbox('Year:', wq.year.unique())
        
    with wq_col2:
        wq_params = st.multiselect('Parameters:', params)
    
    wq_plot = wq[wq.year == wq_year].groupby(['site','month']).mean().reset_index()
    wq_plot = wq_plot.interpolate()
    
    for p in wq_params:
        if p == 'Chlorophyll':
            c = 'algae'
        elif p == 'Salinity':
            c = 'dense'
        else:
            c = 'thermal'
        
        
        wq_plot_param = wq_plot[['site','month',p]] \
        .pivot(index='site', columns = 'month') \
        .loc[['Santa Cruz','Santa Monica','Newport']]
        wq_fig = px.imshow(wq_plot_param[p],
                       labels = {'y':'',
                                 'color':p},
                       title = p,
                       color_continuous_scale=c
                       )
        #wq_fig.update_layout(margin=dict(l=10, t=10, b=10))
        st.plotly_chart(wq_fig, use_container_width=True)
        
    
    st.write('Source: NOAA CO-OPS')
    

