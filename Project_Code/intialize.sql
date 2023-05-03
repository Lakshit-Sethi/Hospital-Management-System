CREATE DATABASE IF NOT EXISTS HOSPITAL;
USE HOSPITAL;


CREATE TABLE IF NOT EXISTS Department (
    Department_ID INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    Department_Name VARCHAR(255),
    Department_Head TEXT,
    Contact_Number BIGINT(10) CHECK (LENGTH(Contact_Number) = 10),
    PRIMARY KEY (Department_ID)
);
CREATE TABLE IF NOT EXISTS DOCTOR (
    Doctor_ID INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    Name TEXT,
    DOB DATE,
    Contact_Number BIGINT(10) CHECK (LENGTH(Contact_Number) = 10),
    Department_ID INTEGER NOT NULL ,
    FOREIGN KEY (Department_ID) REFERENCES Department (Department_ID),
    PRIMARY KEY (Doctor_ID)
);

CREATE TABLE IF NOT EXISTS Nurse (
    Nurse_ID INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    Name TEXT,
    DOB DATE,
    Contact_Number BIGINT(10) CHECK (LENGTH(Contact_Number) = 10),
    PRIMARY KEY (Nurse_ID)
);

CREATE TABLE IF NOT EXISTS Patient (
    Patient_ID INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    Name TEXT,
    Contact_Number BIGINT(10) CHECK (LENGTH(Contact_Number) = 10),
    DOB DATE,
    Gender VARCHAR(10),
    Insurance VARCHAR(10),
    PRIMARY KEY (Patient_ID)
);

CREATE TABLE IF NOT EXISTS Alloted_Room (
    Room_No INTEGER NOT NULL,
    Patient_ID INTEGER NOT NULL,
    Nurse_ID INTEGER NOT NULL,
    Doctor_ID INTEGER NOT NULL,
    PRIMARY KEY (Patient_ID),
    FOREIGN KEY (Patient_ID) REFERENCES Patient (Patient_ID),
    FOREIGN KEY (Nurse_ID) REFERENCES Nurse (Nurse_ID),
    FOREIGN KEY (Doctor_ID) REFERENCES DOCTOR (Doctor_ID)
);

CREATE TABLE IF NOT EXISTS credentials (
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    pass VARCHAR(255) NOT NULL,
    designation VARCHAR(255),
    PRIMARY KEY (email)
);

CREATE TABLE IF NOT EXISTS Diagnosis (
    Diagnosis VARCHAR(100),
    Treatment VARCHAR(100),
    PRIMARY KEY (Diagnosis)
);

CREATE TABLE IF NOT EXISTS Medical_History (
    History_ID INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    Date DATE,
    Diagnosis VARCHAR(100),
    Patient_ID INT,
    PRIMARY KEY (History_ID),
    FOREIGN KEY (Diagnosis) REFERENCES Diagnosis(Diagnosis),
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID)
);

CREATE TABLE IF NOT EXISTS Appointment (
    Appointment_ID INTEGER NOT NULL AUTO_INCREMENT,
    Patient_ID INTEGER NOT NULL,
    Doctor_ID INTEGER NOT NULL,
    A_date date NOT NULL,
    PRIMARY KEY (Appointment_ID),
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID),
    FOREIGN KEY (Doctor_ID) REFERENCES DOCTOR(Doctor_ID)
);

CREATE TABLE IF NOT EXISTS Billing (
    Patient_ID INTEGER,
    Bill_ID INTEGER NOT NULL AUTO_INCREMENT,
    Bill_Amount INTEGER,
    Doctor_ID INTEGER,
    PRIMARY KEY (Bill_ID),
    FOREIGN KEY (Patient_ID) REFERENCES Patient(Patient_ID),
    FOREIGN KEY (Doctor_ID) REFERENCES DOCTOR(Doctor_ID)
);

INSERT INTO Department (Department_Name, Department_Head, Contact_Number) 
VALUES 
    ('Cardiology', 'Dr. Suresh Sharma', 9876543210), 
    ('Oncology', 'Dr. Meera Singh', 8765432109), 
    ('Neurology', 'Dr. Sanjay Patel', 7654321098),
    ('Orthopedics', 'Dr. Ravi Kumar', 6543210987),
    ('Gynecology', 'Dr. Rekha Gupta', 5432109876),
    ('Pediatrics', 'Dr. Shalini Verma', 4321098765),
    ('General Medicine', 'Dr. Rakesh Singh', 3210987654),
    ('Dermatology', 'Dr. Pooja Sharma', 2109876543);


INSERT INTO DOCTOR (Name, DOB, Contact_Number, Department_ID) VALUES
  ('Dr. Ramesh Gupta', '1980-06-05', 9876543210, 1),
  ('Dr. Preeti Singh', '1992-08-12', 8765432101, 2),
  ('Dr. Rajesh Sharma', '1978-03-25', 7654321098, 1),
  ('Dr. Priya Patel', '1985-11-15', 6543210987, 3),
  ('Dr. Sanjay Verma', '1990-01-20', 5432109876, 2),
  ('Dr. Anjali Mehta', '1982-07-08', 4321098765, 1),
  ('Dr. Sameer Khan', '1995-04-03', 3210987654, 3),
  ('Dr. Nisha Choudhary', '1989-09-29', 2109876543, 2),
  ('Dr. Deepak Patel', '1983-12-18', 1098765432, 1),
  ('Dr. Shalini Gupta', '1993-02-28', 9876543210, 3),
  ('Dr. Rohit Singh', '1987-10-07', 8765432101, 2),
  ('Dr. Kiran Sharma', '1981-05-21', 7654321098, 1),
  ('Dr. Rohini Patel', '1994-11-01', 6543210987, 3),
  ('Dr. Vikas Verma', '1986-01-12', 5432109876, 2),
  ('Dr. Anuja Mehta', '1991-08-31', 4321098765, 1);


INSERT INTO Nurse (Name, DOB, Contact_Number) 
VALUES 
    ('Asha Singh', '1988-06-10', 9876543210), 
    ('Rohit Sharma', '1993-12-15', 8765432109), 
    ('Meena Patel', '1975-03-20', 7654321098),
    ('Komal Gupta', '1982-08-07', 6543210987),
    ('Manoj Kumar', '1990-11-25', 5432109876),
    ('Neha Singh', '1988-04-12', 4321098765),
    ('Sudha Sharma', '1986-01-30', 3210987654),
    ('Ravi Patel', '1979-09-05', 2109876543),
    ('Rekha Kumari', '1995-06-17', 1098765432),
    ('Anil Verma', '1983-12-22', 9876543210),
    ('Suman Singh', '1991-05-08', 8765432109),
    ('Amita Sharma', '1976-02-14', 7654321098),
    ('Rajeshwari Patel', '1989-10-01', 6543210987),
    ('Krishna Verma', '1981-07-18', 5432109876),
    ('Sanjay Kumar', '1977-04-05', 4321098765);
INSERT into credentials (email, name, pass, designation)
VALUES
    ('lakshit@gmail.com', 'Lakshit', 'lakshit', 'Admin'),
    ('Admin@Admin', 'Admin', 'Admin', 'Admin'),
    ('User@User', 'User', 'User', 'User');