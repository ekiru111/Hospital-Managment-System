USE hms_db;

CREATE OR REPLACE VIEW daily_hospital_schedule AS
SELECT 
    a.AppointmentID,
    CONCAT(p.FirstName, ' ', p.LastName) AS Patient_Name,
    CONCAT('Dr. ', d.LastName) AS Attending_Doctor,
    d.Specialization,
    a.AppointmentDate,
    a.AppointmentStatus
FROM Appointments a
JOIN Patients p ON a.PatientID = p.PatientID
JOIN Doctors d ON a.DoctorID = d.DoctorID;