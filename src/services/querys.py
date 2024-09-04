import pandas as pd

from sqlalchemy.orm import Session
from sqlalchemy import text

from services.schema import *


def get_number_appointments_by_chatreason(db: Session):
    appointment_summary: list[AppointmentChatReason] = db.execute(
        text(
        """
        SELECT TO_CHAR(a.appointment_starts_at, 'MM') as "mes", c.chat_reason as "motivo", count(*) as "num_citas"
        FROM Chats c, Appointments a
        WHERE c.chat_id = a.chat_id AND c.patient_id = a.patient_id
        GROUP BY c.chat_reason,  TO_CHAR(a.appointment_starts_at, 'MM')
        ORDER BY TO_CHAR(a.appointment_starts_at, 'MM');
        """
    )).fetchall()
    
    formated_data = {
        'Mes': [],
        'Motivo': [],
        'Número de Citas': []
    }

    for item in appointment_summary:
        formated_data['Mes'].append(item.mes)
        formated_data['Motivo'].append(item.motivo)
        formated_data['Número de Citas'].append(item.num_citas)

    df = pd.DataFrame(formated_data)

    return df


def get_avg_time_chat_appointment(db: Session):
    avg_time_chat_appointment: AvgTimeChatAppointment = db.execute(
        text(
            """
            SELECT avg(a.appointment_created_at - c.created_at) as "promedio_tiempo"
            FROM Chats c, Appointments a
            WHERE c.chat_id = a.chat_id AND c.patient_id = a.patient_id;
            """
    )).first()[0]

    return str(avg_time_chat_appointment)


def get_avg_time_anticipation(db: Session):
    avg_time_chat_anticipation: AnticipationAppointment = db.execute(
        text(
            """
            SELECT avg(a.appointment_starts_at - a.appointment_created_at) as "anticipacion_promedio"
            FROM Appointments a;
            """
    )).first()[0]

    return str(avg_time_chat_anticipation)


def get_nps(db: Session):
    nps_ranges_dates: NPS = db.execute(
        text(
            """
            WITH feedback_score_table as (
                SELECT '30 días' as "Intervalo",
                        count(case when c.feedback_score >= 9 then 1 end) as "Promotores",
                        count(case when c.feedback_score = 7 OR c.feedback_score = 8 then 1 end) as "Neutral",
                        count(case when c.feedback_score <= 6 then 1 end) as "Detractores",
                        count(*) as "Total Puntuaciones"
                FROM Chats c
                WHERE c.created_at <= now() and c.created_at >= (now() - INTERVAL '30 DAY')
                UNION
                SELECT '3 mes' as "Intervalo",
                        count(case when c.feedback_score >= 9 then 1 end) as "Promotores",
                        count(case when c.feedback_score = 7 OR c.feedback_score = 8 then 1 end) as "Neutral",
                        count(case when c.feedback_score <= 6 then 1 end) as "Detractores",
                        count(*) as "Total Puntuaciones"
                FROM Chats c
                WHERE c.created_at <= now() and c.created_at >= (now() - INTERVAL '90 DAY')
                UNION
                SELECT '1 año' as "Intervalo",
                        count(case when c.feedback_score >= 9 then 1 end) as "Promotores",
                        count(case when c.feedback_score = 7 OR c.feedback_score = 8 then 1 end) as "Neutral",
                        count(case when c.feedback_score <= 6 then 1 end) as "Detractores",
                        count(*) as "Total Puntuaciones"
                FROM Chats c
                WHERE c.created_at <= now() and c.created_at >= (now() - INTERVAL '365 DAY')
                UNION
                SELECT 'Todo el tiempo' as "Intervalo",
                        count(case when c.feedback_score >= 9 then 1 end) as "Promotores",
                        count(case when c.feedback_score = 7 OR c.feedback_score = 8 then 1 end) as "Neutral",
                        count(case when c.feedback_score <= 6 then 1 end) as "Detractores",
                        count(*) as "Total Puntuaciones"
                FROM Chats c
            )
            SELECT "Intervalo" as "intervalo",
                    CASE 
                            WHEN "Total Puntuaciones" = 0 THEN NULL 
                            ELSE (100 * "Promotores") / NULLIF("Total Puntuaciones", 0) - 
                            (100 * "Detractores") / NULLIF("Total Puntuaciones", 0)
                    END AS "nps"
            FROM feedback_score_table f;
            """
    )).fetchall()

    formated_data = {}
    for item in nps_ranges_dates:
        formated_data[item.intervalo] = item.nps

    return formated_data

def get_hist_data(db: Session):
    hist_data: HistData = db.execute(
        text(
            """
            WITH total_chats AS ( SELECT count(*) AS total FROM Chats)
            SELECT c.patient_id as "id_paciente", count(*) as "freq", 100 * count(*)/t.total as "proporcion"
            FROM Chats c, total_chats t
            GROUP BY c.patient_id, t.total;
            """
    )).fetchall()

    formated_data = {
        'ID Paciente': [],
        'Frecuencia': [],
        'Proporción (%)': []
    }

    for item in hist_data:
        formated_data['ID Paciente'].append(item.id_paciente)
        formated_data['Frecuencia'].append(item.freq)
        formated_data['Proporción (%)'].append(item.proporcion)

    df = pd.DataFrame(formated_data)
    df.sort_values(by='ID Paciente', inplace=True)
    
    return df
