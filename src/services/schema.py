from pydantic import BaseModel
from datetime import timedelta, datetime


class AppointmentChatReason(BaseModel):
    mes: str
    motivo: str
    num_citas: int


class AvgTimeChatAppointment(BaseModel):
    promedio_tiempo: timedelta


class AnticipationAppointment(BaseModel):
    anticipacion_promedio: timedelta


class NPS(BaseModel):
    intervalo: str
    nps: int


class HistData(BaseModel):
    id_paciente: int
    freq: int
    proporcion: int


class NewChat(BaseModel):
    patient_id: int
    chat_reason: str
    feedback_score: int


class NewAppointment(BaseModel):
    appointment_starts_at: datetime
    chat_id: int
    patient_id: int
