USE hms_db;

CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(50) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL, -- In a real app, we would hash this!
    Role ENUM('Admin', 'Receptionist', 'Doctor') DEFAULT 'Receptionist'
);

-- Let's add a test user
INSERT INTO Users (Username, Password, Role)
VALUES ('admin', 'hms123', 'Admin'), 
       ('ekiru', 'secure456', 'Receptionist');