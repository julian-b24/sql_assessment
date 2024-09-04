import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

from database import get_db
from services.querys import *

db = next(get_db())

with st.sidebar:
    selected = option_menu(
        menu_title= 'Menu',
        options=['Analítica', 'Agregar Registros'],
        default_index=0
    )

if selected == 'Analítica':
    st.title('⚡️ Chats & Citas - Centro de Analítica')
    st.markdown('**Bienvenido!** En este dashboard podrás extraer información de la base de datos de manera sencilla y a un solo click 📊.')
    st.header('')

    # First Query  
    row_chat_reason_header = st.columns([4, 1])
    with row_chat_reason_header[0]:
        st.subheader('No. de citas por mes y por motivo de chat')
    
    with row_chat_reason_header[1]:
        chat_reason_btn = st.button('Consultar', key='chat_reason')
    
    if chat_reason_btn:
        st.dataframe(get_number_appointments_by_chatreason(db))

    st.divider()

    # Second Query    
    row_avg_time_chat_appointment = st.columns([4, 1])
    with row_avg_time_chat_appointment[0]:
        st.subheader('Tiempo promedio entre chat y cita')
    
    with row_avg_time_chat_appointment[1]:
        avg_time_chat_appointment_btn = st.button('Consultar', key='avg_time')
    
    if avg_time_chat_appointment_btn:
        row_avg_time_chat_appointment_content = st.columns([2, 3])
        avg_time_chat_appointment = get_avg_time_chat_appointment(db)
        with row_avg_time_chat_appointment_content[0]:
            st.metric('Tiempo promedio', avg_time_chat_appointment)
        
        with row_avg_time_chat_appointment_content[1]:
            st.markdown(f'El tiempo promedio desde que una persona crea un chat hasta que se agenda una cita es de {avg_time_chat_appointment}')
    
    st.divider()

    #Third Query
    row_anticipation_appointment = st.columns([4, 1])
    with row_anticipation_appointment[0]:
        st.subheader('Tiempo de Anticipación promedio en citas')
    
    with row_anticipation_appointment[1]:
        anticipation_appointment_btn = st.button('Consultar', key='anticipation_appointment')
    
    if anticipation_appointment_btn:
        row_anticipation_appointment_content = st.columns([2, 3])
        anticipation_appointment = get_avg_time_anticipation(db)
        with row_anticipation_appointment_content[0]:
            st.metric('Tiempo promedio', anticipation_appointment)
        
        with row_anticipation_appointment_content[1]:
            st.markdown(f'El tiempo promedio desde que una persona agenda una cita hasta que la tiene es de **{anticipation_appointment}**.')
    
    
    st.divider()

    #Fourth Query
    row_nps = st.columns([4, 1])
    with row_nps[0]:
        st.subheader('No. de citas por mes y por motivo de chat')
    
    with row_nps[1]:
        nps_btn = st.button('Consultar', key='nps')
    
    if nps_btn:
        st.write('Hey')
    
    st.divider()


    #Fifth Query
    row_hist_chats = st.columns([4, 1])
    with row_hist_chats[0]:
        st.subheader('Histograma Chats por usuario')
    
    with row_hist_chats[1]:
        hist_chats_btn = st.button('Graficar', key='hist_chats')
    
    if hist_chats_btn:
        st.write('Hey')
    