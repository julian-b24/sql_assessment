from pydantic import BaseModel
from datetime import timedelta


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
