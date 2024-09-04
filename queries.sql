SELECT TO_CHAR(a.appointment_starts_at, 'MM') as "Mes", c.chat_reason as "Motivo de Chat", count(*) as "Numero de Citas"
FROM Chats c, Appointments a
WHERE c.chat_id = a.chat_id AND c.patient_id = a.patient_id
GROUP BY c.chat_reason,  TO_CHAR(a.appointment_starts_at, 'MM')
ORDER BY TO_CHAR(a.appointment_starts_at, 'MM');


SELECT avg(a.appointment_created_at - c.created_at) as "Promedio Tiempo Chat hasta Agendamiento"
FROM Chats c, Appointments a
WHERE c.chat_id = a.chat_id AND c.patient_id = a.patient_id;


SELECT avg(a.appointment_starts_at - a.appointment_created_at) as "Anticipación Promedio"
FROM Appointments a;

WITH feedback_score_table as (
    SELECT '30 días' as "Intervalo",
            count(case when c.feedback_score >= 9 then 1 end) as "Promotores",
            count(case when c.feedback_score = 7 OR c.feedback_score = 8 then 1 end) as "Neutral",
            count(case when c.feedback_score <= 6 then 1 end) as "Detractores",
            count(*) as "Total Puntuaciones"
    FROM Chats c
    WHERE c.created_at BETWEEN now() AND  now() - INTERVAL '30 DAY'
    UNION
    SELECT '3 mes' as "Intervalo",
            count(case when c.feedback_score >= 9 then 1 end) as "Promotores",
            count(case when c.feedback_score = 7 OR c.feedback_score = 8 then 1 end) as "Neutral",
            count(case when c.feedback_score <= 6 then 1 end) as "Detractores",
            count(*) as "Total Puntuaciones"
    FROM Chats c
    WHERE c.created_at BETWEEN now() AND  now() - INTERVAL '90 DAY'
    UNION
    SELECT '1 año' as "Intervalo",
            count(case when c.feedback_score >= 9 then 1 end) as "Promotores",
            count(case when c.feedback_score = 7 OR c.feedback_score = 8 then 1 end) as "Neutral",
            count(case when c.feedback_score <= 6 then 1 end) as "Detractores",
            count(*) as "Total Puntuaciones"
    FROM Chats c
    WHERE c.created_at BETWEEN now() AND  now() - INTERVAL '365 DAY'
    UNION
    SELECT 'Todo el tiempo' as "Intervalo",
            count(case when c.feedback_score >= 9 then 1 end) as "Promotores",
            count(case when c.feedback_score = 7 OR c.feedback_score = 8 then 1 end) as "Neutral",
            count(case when c.feedback_score <= 6 then 1 end) as "Detractores",
            count(*) as "Total Puntuaciones"
    FROM Chats c
)
SELECT "Intervalo", (100 * ("Promotores")/"Total Puntuaciones") - (100 * "Detractores"/"Total Puntuaciones") as "NPS"
FROM feedback_score_table f;

WITH total_chats AS ( SELECT count(*) AS total FROM Chats)
SELECT c.patient_id as "Paciente", count(*) as "Frecuencua", 100 * count(*)/t.total as "Proporción (%)"
FROM Chats c, total_chats t
GROUP BY c.patient_id, t.total;