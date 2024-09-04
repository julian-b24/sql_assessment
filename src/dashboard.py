import pandas as pd
import streamlit as st
import plotly.express as px
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
        _, chat_reason_content,_ = st.columns([1,4,0.1])
        with chat_reason_content:
            st.dataframe(get_number_appointments_by_chatreason(db), hide_index=True)

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
        st.subheader('NPS de los últimos periodos')
    
    with row_nps[1]:
        nps_btn = st.button('Consultar', key='nps')
    
    if nps_btn:
        row_nps_content = st.columns(4)
        nps_content = get_nps(db)

        for (index, col) in enumerate(row_nps_content):
            with col:
                st.metric(list(nps_content.keys())[index], list(nps_content.values())[index])
    
    st.divider()


    #Fifth Query
    row_hist_chats = st.columns([4, 1])
    with row_hist_chats[0]:
        st.subheader('Histograma Chats por usuario')
    
    with row_hist_chats[1]:
        hist_chats_btn = st.button('Graficar', key='hist_chats')
    
    if hist_chats_btn:
        row_hist_content = st.columns([3, 2])
        hist_data = get_hist_data(db)

        with row_hist_content[0]:
            tab_freq, tab_percentage = st.tabs(['Frecuencia', 'Porcentaje'])
            with tab_freq:
                fig = px.bar(hist_data, y='Frecuencia', x='ID Paciente', text_auto='.2s',
                            title="Frecuencia con la que cada paciente crea un chat")
                fig.update_layout(height=300)
                st.plotly_chart(fig)

            with tab_percentage:
                fig = px.bar(hist_data, y='Proporción (%)', x='ID Paciente', text_auto='.2s',
                            title="Frecuencia con la que cada paciente crea un chat")
                fig.update_layout(height=300)
                st.plotly_chart(fig, use_container_width=True)

        with row_hist_content[1]:
            st.dataframe(hist_data, hide_index=True)
        
        
    