from pydantic import BaseModel


class AppointmentChatReason(BaseModel):
    mes: str
    motivo: str
    num_citas: int


class AvgTimeChatAppointment(BaseModel):
    promedio_tiempo: list


class AnticipationAppointment(BaseModel):
    pass


class NPS(BaseModel):
    pass


class HistData(BaseModel):
    pass
