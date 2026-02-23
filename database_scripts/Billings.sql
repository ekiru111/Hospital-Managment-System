USE hms_db;

CREATE TABLE Billing (
    BillID INT AUTO_INCREMENT PRIMARY KEY,
    AppointmentID VARCHAR(50),
    ConsultationFee DECIMAL(10, 2) DEFAULT 50000.00,
    PharmacyCharges DECIMAL(10, 2) DEFAULT 0.00,
    TotalAmount DECIMAL(10, 2),
    PaymentStatus ENUM('Pending', 'Paid', 'Partially Paid') DEFAULT 'Pending',
    BillingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID)
);


