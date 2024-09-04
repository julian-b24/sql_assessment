import pandas as pd
from sqlalchemy.orm import Session

from services.schema import NewAppointment, NewChat
from models import Chats, Appointments

def add_new_chat(new_chat: NewChat, db: Session):
    chat: Chats = Chats(
        patient_id = new_chat.patient_id,
        chat_reason =  new_chat.chat_reason,
        feedback_score = new_chat.feedback_score
        )
    db.add(chat)
    db.commit

    return chat


def add_new_appointment(new_appointment: NewAppointment, db: Session):
    appointment: Appointments = Appointments(
        patient_id = new_appointment.patient_id,
        appointment_starts_at =  new_appointment.appointment_starts_at,
        chat_id = new_appointment.chat_id
        )
    db.add(appointment)
    db.commit

    return appointment


def get_all_chats(db: Session):
    chats = db.query(Chats).all()
    print(chats)

    chats_formated = {
        'chat_id': [],
        'created_at': [],
        'patient_id': [],
        'chat_reason': [],
        'feedback_score': []
    }

    for chat in chats:
        chats_formated['chat_id'].append(chat.chat_id)
        chats_formated['created_at'].append(chat.created_at)
        chats_formated['patient_id'].append(chat.patient_id)
        chats_formated['chat_reason'].append(chat.chat_reason)
        chats_formated['feedback_score'].append(chat.feedback_score)

    df = pd.DataFrame(chats_formated)
    return df


def get_all_appointments(db: Session):
    appointments = db.query(Appointments).all()
    print(appointments)

    appointments_formated = {
        'appointment_id': [],
        'appointment_created_at': [],
        'appointment_starts_at': [],
        'chat_id': [],
        'patient_id': []
    }

    for appointment in appointments:
        appointments_formated['appointment_id'].append(appointment.appointment_id)
        appointments_formated['appointment_created_at'].append(appointment.appointment_created_at)
        appointments_formated['appointment_starts_at'].append(appointment.appointment_starts_at)
        appointments_formated['chat_id'].append(appointment.chat_id)
        appointments_formated['patient_id'].append(appointment.patient_id)

    df = pd.DataFrame(appointments_formated)
    return df
