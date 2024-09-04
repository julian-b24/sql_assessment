INSERT INTO Chats (created_at, patient_id, chat_reason, feedback_score) VALUES
('2024-08-14 09:30:00', 1, 'Initial Consultation', 8),  -- Within the last 30 days
('2024-08-15 11:00:00', 2, 'Routine Check-in', 7),       -- Within the last 30 days
('2024-07-16 14:45:00', 3, 'Progress Evaluation', 6),    -- Within the last 3 months
('2024-06-17 16:20:00', 4, 'Crisis Intervention', 9),    -- Within the last 3 months
('2024-05-18 10:15:00', 5, 'Treatment Planning', 7),     -- Within the last 3 months
('2024-04-19 13:30:00', 6, 'Stress Management', 8),      -- More than 3 months ago, within the last year
('2024-03-20 15:00:00', 7, 'Post-Therapy Follow-up', 7), -- More than 3 months ago, within the last year
('2024-02-21 09:00:00', 2, 'Routine Check-in', 6),       -- More than 3 months ago, within the last year
('2023-12-22 11:30:00', 3, 'Stress Management', 8),      -- More than 6 months ago, within the last year
('2023-09-23 14:00:00', 4, 'Initial Consultation', 7),   -- More than a year ago
('2023-08-24 16:45:00', 5, 'Progress Evaluation', 9),    -- More than a year ago
('2023-07-25 10:30:00', 6, 'Crisis Intervention', 5),    -- More than a year ago
('2023-06-26 13:15:00', 7, 'Treatment Planning', 8),     -- More than a year ago
('2023-05-27 15:40:00', 1, 'Post-Therapy Follow-up', 7), -- More than a year ago
('2023-04-28 09:50:00', 2, 'Stress Management', 6),      -- More than a year ago
('2023-03-29 12:20:00', 3, 'Routine Check-in', 8),       -- More than a year ago
('2023-02-30 14:55:00', 4, 'Progress Evaluation', 7),    -- More than a year ago
('2023-01-01 17:10:00', 5, 'Crisis Intervention', 9),    -- More than a year ago
('2022-12-02 10:05:00', 6, 'Initial Consultation', 8),   -- More than a year ago
('2022-11-03 12:35:00', 7, 'Treatment Planning', 7),     -- More than a year ago
('2022-10-04 15:15:00', 1, 'Stress Management', 6),      -- More than a year ago
('2022-09-05 09:25:00', 2, 'Post-Therapy Follow-up', 8), -- More than a year ago
('2022-08-06 11:55:00', 3, 'Routine Check-in', 7),       -- More than a year ago
('2022-07-07 14:30:00', 4, 'Progress Evaluation', 8),    -- More than a year ago
('2022-06-08 16:50:00', 5, 'Crisis Intervention', 9),    -- More than a year ago
('2022-05-09 10:40:00', 6, 'Treatment Planning', 7),     -- More than a year ago
('2022-04-10 13:05:00', 7, 'Initial Consultation', 8),   -- More than a year ago
('2022-03-11 15:35:00', 1, 'Post-Therapy Follow-up', 7), -- More than a year ago
('2022-02-12 09:45:00', 2, 'Stress Management', 6),      -- More than a year ago
('2022-01-13 12:10:00', 3, 'Routine Check-in', 8);       -- More than a year ago



INSERT INTO Appointments (appointment_created_at, appointment_starts_at, chat_id, patient_id) VALUES
('2024-09-14 09:35:00', '2024-09-14 10:30:00', 1, 1),
('2024-09-15 11:05:00', '2024-09-15 12:00:00', 2, 2),
('2024-09-16 14:50:00', '2024-09-16 15:45:00', 3, 3),
('2024-09-17 16:25:00', '2024-09-17 17:20:00', 4, 4),
('2024-09-18 10:20:00', '2024-09-18 11:15:00', 5, 5),
('2024-09-19 13:35:00', '2024-09-19 14:30:00', 6, 6),
('2024-09-20 15:05:00', '2024-09-20 16:00:00', 7, 7),
('2024-09-21 09:05:00', '2024-09-21 10:00:00', 8, 2),
('2024-09-22 11:35:00', '2024-09-22 12:30:00', 9, 3),
('2024-09-23 14:05:00', '2024-09-23 15:00:00', 10, 4),
('2024-09-24 16:50:00', '2024-09-24 17:45:00', 11, 5),
('2024-09-25 10:35:00', '2024-09-25 11:30:00', 12, 6),
('2024-09-26 13:20:00', '2024-09-26 14:15:00', 13, 7),
('2024-09-27 15:45:00', '2024-09-27 16:40:00', 14, 1),
('2024-09-28 09:55:00', '2024-09-28 10:50:00', 15, 2),
('2024-09-29 12:25:00', '2024-09-29 13:20:00', 16, 3),
('2024-09-30 15:00:00', '2024-09-30 15:55:00', 17, 4),
('2024-10-01 17:15:00', '2024-10-01 18:10:00', 18, 5),
('2024-10-02 10:10:00', '2024-10-02 11:05:00', 19, 6),
('2024-10-03 12:40:00', '2024-10-03 13:35:00', 20, 7),
('2024-10-04 15:20:00', '2024-10-04 16:15:00', 21, 1),
('2024-10-05 09:30:00', '2024-10-05 10:25:00', 22, 2),
('2024-10-06 12:00:00', '2024-10-06 12:55:00', 23, 3),
('2024-10-07 14:35:00', '2024-10-07 15:30:00', 24, 4),
('2024-10-08 16:55:00', '2024-10-08 17:50:00', 25, 5),
('2024-10-09 10:45:00', '2024-10-09 11:40:00', 26, 6),
('2024-10-10 13:10:00', '2024-10-10 14:05:00', 27, 7),
('2024-10-11 15:40:00', '2024-10-11 16:35:00', 28, 1),
('2024-10-12 09:50:00', '2024-10-12 10:45:00', 29, 2),
('2024-10-13 12:15:00', '2024-10-13 13:10:00', 30, 3);
