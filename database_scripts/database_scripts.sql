-- =======================================
-- HOSPITAL MANAGEMENT SYSTEM DATABASE SCRIPT
-- =======================================

DROP DATABASE IF EXISTS hms_db;


-- 1. Create the Database
CREATE DATABASE hms_db;
USE hms_db;

-- 2. Create Patients Table (Note: VARCHAR for custom IDs)
CREATE TABLE Patients (
    PatientID VARCHAR(20) PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    Gender VARCHAR(10),
    Phone VARCHAR(20)
);

-- 3. Create Doctors Table
CREATE TABLE Doctors (
    DoctorID VARCHAR(20) PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Gender VARCHAR(10),
    Specialization VARCHAR(50),
    Department VARCHAR(50),
    Phone VARCHAR(20)
);

-- 4. Create Appointments Table
CREATE TABLE Appointments (
    AppointmentID VARCHAR(20) PRIMARY KEY,
    PatientID VARCHAR(20),
    DoctorID VARCHAR(20),
    AppointmentDate DATE,
    AppointmentStatus VARCHAR(20),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
);

USE hms_db;
SELECT 
    a.AppointmentID, 
    p.FirstName AS Patient, 
    d.LastName AS Doctor, 
    d.Specialization,
    a.AppointmentDate, 
    a.AppointmentStatus
FROM Appointments a
JOIN Patients p ON a.PatientID = p.PatientID
JOIN Doctors d ON a.DoctorID = d.DoctorID
ORDER BY a.AppointmentDate DESC;