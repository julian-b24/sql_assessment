import pandas as pd
from sqlalchemy.orm import Session, joinedload
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

    print(avg_time_chat_appointment)

    return str(avg_time_chat_appointment)


def get_avg_time_anticipation(db: Session):
    pass


def get_nps(db: Session):
    pass


def get_hist_data(db: Session):
    pass
