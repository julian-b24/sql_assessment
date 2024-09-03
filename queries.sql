SELECT TO_CHAR(a.appointment_starts_at, 'MM') as "Mes", c.chat_reason as "Motivo de Chat", count(*) as "Numero de Citas"
FROM Chats c, Appointments a
WHERE c.chat_id = a.chat_id
GROUP BY c.chat_reason,  TO_CHAR(a.appointment_starts_at, 'MM')
ORDER BY TO_CHAR(a.appointment_starts_at, 'MM');


SELECT avg(a.appointment_created_at - c.created_at) as "Promedio Tiempo Chat hasta Agendamiento"
FROM Chats c, Appointments a
WHERE c.chat_id = a.chat_id;