import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

from database import get_db
from services.querys import *

db = next(get_db())

with st.sidebar:
    selected = option_menu(
        menu_title= 'Menu',
        options=['Analytics', 'New Registers'],
        default_index=0
    )

if selected == 'Analytics':
    st.title('⚡️ Chats & Appointments Analytics')
    st.markdown('Welcome to this dashboard where you can extract information easily from the chats and appointments')

    # First Query  
    row_chat_reason_header = st.columns([4, 1])
    with row_chat_reason_header[0]:
        st.subheader('No. de citas por mes y por motivo de chat')
    
    with row_chat_reason_header[1]:
        chat_reason_btn = st.button('Consultar', key='chat_reason')
    
    if chat_reason_btn:
        st.dataframe(get_number_appointments_by_chatreason(db))

    # Second Query    
    row_avg_time_chat_appointment = st.columns([4, 1])
    with row_avg_time_chat_appointment[0]:
        st.subheader('Tiempo promedio entre chat y cita')
    
    with row_avg_time_chat_appointment[1]:
        avg_time_chat_appointment_btn = st.button('Consultar', key='avg_time')
    
    if avg_time_chat_appointment_btn:

        st.write('Hey')
    

    #Third Query
    row_anticipation_appointment = st.columns([4, 1])
    with row_anticipation_appointment[0]:
        st.subheader('Tiempo de Anticipación promedio en citas')
    
    with row_anticipation_appointment[1]:
        anticipation_appointmen_btn = st.button('Consultar', key='anticipation_appointment')
    
    if anticipation_appointmen_btn:
        st.write('Hey')
    

    #Fourth Query
    row_nps = st.columns([4, 1])
    with row_nps[0]:
        st.subheader('No. de citas por mes y por motivo de chat')
    
    with row_nps[1]:
        nps_btn = st.button('Consultar', key='nps')
    
    if nps_btn:
        st.write('Hey')
    
    #Fifth Query
    row_hist_chats = st.columns([4, 1])
    with row_hist_chats[0]:
        st.subheader('Histograma Chats por usuario')
    
    with row_hist_chats[1]:
        hist_chats_btn = st.button('Graficar', key='hist_chats')
    
    if hist_chats_btn:
        st.write('Hey')
    