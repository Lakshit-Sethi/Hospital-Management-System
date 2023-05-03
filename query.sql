/*Insertion of doctor with specialization*/

-- This query inserts a new record for a doctor in the DOCTOR table, along with their date of birth, contact number, and department ID.

INSERT INTO DOCTOR (Name,DOB,Contact_Number,Department_ID) VALUES ('Dr. Ramesh Gupta', '1980-06-05', 9876543210, 1);


/*insertion of Diagnosis and Patient records*/

-- This query inserts a new record for a diagnosis in the DiagnosisTable table, along with its treatment.

INSERT INTO DiagnosisTable (Diagnosis, Treatment) VALUES ('Cancer', 'Chemotherapy');

-- This query inserts a new record for a medical history in the Medical_History table, along with the date of diagnosis, diagnosis itself, and patient ID.

INSERT INTO Medical_History (Date, Diagnosis, Patient_ID) VALUES ('2018-01-01', 'Cancer', 1);


/*Insertion of hospital staff*/

-- This query inserts a new record for a nurse in the Nurse table, along with their name, date of birth, and contact number.

INSERT INTO Nurse (Name,DOB,Contact_Number) VALUES ('Roopali Malik', '1980-06-05', 9876543210);


/*Booking an appointment with specialized doctor*/

-- This query inserts a new record for an appointment in the Appointment table, along with the patient ID, doctor ID, and appointment date.

INSERT INTO Appointment (Patient_ID,Doctor_ID,A_date) VALUES (1, 1, '2018-01-01');


/*Rescheduling appointment date/time*/

-- This query updates the appointment date of an existing record in the Appointment table based on the appointment ID.

UPDATE Appointment SET A_date='2018-01-02' WHERE Appointment_ID=1;


/*Updating Room Status(Availability)*/

-- This query checks if a particular room is already allotted to a patient or not.

SELECT IF(EXISTS(SELECT * FROM Alloted_Room WHERE Room_No = 2), 'YES', 'NO') AS Room_Allotted;


/*Allot staff to a particular room*/

-- This query inserts a new record in the Alloted_Room table, specifying the room number, patient ID, nurse ID, and doctor ID.

INSERT INTO Alloted_Room (Room_No, Patient_ID, Nurse_ID, Doctor_ID) VALUES (1, 1, 1, 1);


/*Generating Bills*/

-- This query inserts a new record in the Billing table, specifying the patient ID, doctor ID, and bill amount.

INSERT INTO Billing (Patient_ID, Doctor_ID, Bill_Amount) VALUES (1, 1, 1000);


/*trigger to update the amount in billing table*/

-- This query creates a trigger that automatically calculates the tax amount of 18% and updates the bill amount accordingly, before inserting a new record in the Billing table.

DELIMITER $$
CREATE TRIGGER add_tax_on_insert BEFORE INSERT ON Billing
FOR EACH ROW
BEGIN
    SET NEW.Bill_Amount = NEW.Bill_Amount * 1.18;
END $$
DELIMITER ; 


/*View all doctors in the hospital*/

-- This query creates a view named All_Doctors that selects all records from the DOCTOR table.

CREATE VIEW All_Doctors AS
SELECT * FROM DOCTOR;


/*View all patients join their medical history*/

-- This query creates a view named All_Patients that selects all records from the Patient table and joins them with their respective medical history records.

CREATE VIEW All_Patients AS
SELECT * FROM Patient NATURAL JOIN Medical_History;


/*Total amount earned by a specific doctor*/

-- This query calculates the total bill amount earned by a specific doctor

SELECT SUM(Bill_Amount) FROM Billing WHERE Patient_ID=(SELECT Patient_ID FROM Appointment WHERE Doctor_ID=(SELECT Doctor_ID FROM DOCTOR WHERE Name='Dr. Ramesh Gupta'));

/*Total amount earned by a specific specialization*/
SELECT sum(Bill_Amount) from Billing where Doctor_ID in(select Doctor_ID FROM DOCTOR where Department_ID= 'Cardiology');

/*Function/Procedure to find all patients a specific doctor has treated*/
DELIMITER $$
CREATE PROCEDURE Patients_Treated_By_Doctor(IN Doctor_Name VARCHAR(50))
BEGIN
    SELECT Name FROM Patient WHERE Patient_ID IN (SELECT Patient_ID FROM Appointment WHERE Doctor_ID IN(SELECT Doctor_ID FROM DOCTOR WHERE Name=Doctor_Name));
END $$
DELIMITER ;

CALL Patients_Treated_By_Doctor('Dr. Ramesh Gupta');

/*Function/Procedure to fetch all previous appointment diagnosis*/
DELIMITER $$
CREATE PROCEDURE Previous_Appointment_Diagnosis(IN Patien_ID INT)
BEGIN
    SELECT Diagnosis FROM Medical_History WHERE Patient_ID=Patien_ID;
END $$
DELIMITER ;

CALL Previous_Appointment_Diagnosis(1);