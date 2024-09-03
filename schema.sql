-- Create the Chats table
CREATE TABLE Chats (
    chat_id UUID PRIMARY KEY,
    created_at TIMESTAMP NOT NULL,
    patient_id UUID NOT NULL,
    chat_reason VARCHAR(255),
    feedback_score INT CHECK(feedback_score BETWEEN 0 AND 10)
);

-- Create the Appointments table
CREATE TABLE Appointments (
    appointment_id UUID PRIMARY KEY,
    appointment_created_at TIMESTAMP NOT NULL,
    appointment_starts_at TIMESTAMP NOT NULL,
    chat_id UUID REFERENCES Chats(chat_id),
    patient_id UUID NOT NULL
);