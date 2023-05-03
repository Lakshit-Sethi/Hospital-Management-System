import tkinter as tk
import mysql.connector
import sys
import os

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user=os.environ['USER'],
    password=os.environ['PASS'],
    database="HOSPITAL"
)

patient_ID = sys.argv[1]
doctor_ID = sys.argv[2]
print(patient_ID)
# Create Tkinter window
window = tk.Tk()
window.title("Appointment and Billing")
window.geometry("400x300")

# Create labels and entry boxes for input fields
font_style = ("Helvetica", 12)
padding = {"padx": 10, "pady": 10}

date_label = tk.Label(window, text="Date", font=font_style)
date_label.grid(column=0, row=0, **padding)
date_entry = tk.Entry(window, font=font_style, width=25)
date_entry.grid(column=1, row=0, **padding)

diagnosis_label = tk.Label(window, text="Diagnosis", font=font_style)
diagnosis_label.grid(column=0, row=1, **padding)
diagnosis_entry = tk.Entry(window, font=font_style, width=25)
diagnosis_entry.grid(column=1, row=1, **padding)

bill_label = tk.Label(window, text="Bill", font=font_style)
bill_label.grid(column=0, row=2, **padding)
bill_entry = tk.Entry(window, font=font_style, width=25)
bill_entry.grid(column=1, row=2, **padding)

# Create button to insert data into MySQL database


def insert_data():
    # Get input values from the entry boxes
    date = date_entry.get()
    diagnosis = diagnosis_entry.get()
    bill = bill_entry.get()

    # Insert data into Appointment table
    appointment_cursor = mydb.cursor()
    appointment_query = "INSERT INTO Appointment (Patient_ID, Doctor_ID ,A_date) VALUES (%s, %s, %s)"
    appointment_values = (patient_ID, doctor_ID, date)
    appointment_cursor.execute(appointment_query, appointment_values)
    mydb.commit()
    # check if diagnosis is present in the Diagnosis table
    diagnosis_cursor = mydb.cursor()
    diagnosis_query = "SELECT * FROM Diagnosis WHERE Diagnosis = %s"
    diagnosis_values = (diagnosis,)
    diagnosis_cursor.execute(diagnosis_query, diagnosis_values)
    diagnosis_result = diagnosis_cursor.fetchone()
    print(diagnosis_result)
    if diagnosis_result is None:
        # create a popup window to enter treatment
        treatment_window = tk.Tk()
        treatment_window.title("Treatment")
        treatment_window.geometry("400x300")
        treatment_label = tk.Label(
            treatment_window, text="Treatment", font=font_style)
        treatment_label.grid(column=0, row=0, **padding)
        treatment_entry = tk.Entry(treatment_window, font=font_style, width=25)
        treatment_entry.grid(column=1, row=0, **padding)

        def insert_treatment():
            treatment = treatment_entry.get()
            # Insert data into Diagnosis table
            diagnosis_cursor = mydb.cursor()
            diagnosis_query = "INSERT INTO Diagnosis (Diagnosis, Treatment) VALUES (%s, %s)"
            diagnosis_values = (diagnosis, treatment)
            diagnosis_cursor.execute(diagnosis_query, diagnosis_values)
            mydb.commit()
            treatment_window.withdraw()
        treatment_button = tk.Button(
            treatment_window, text="Submit", font=font_style, command=insert_treatment)
        treatment_button.grid(column=1, row=1, **padding)
        treatment_window.mainloop()
    else:
        pass
    # Insert data into Bill table
    bill_cursor = mydb.cursor()
    bill_query = "INSERT INTO Billing (Patient_ID, Doctor_ID, Bill_Amount) VALUES (%s, %s, %s)"
    bill_values = (patient_ID, doctor_ID, bill)
    bill_cursor.execute(bill_query, bill_values)
    mydb.commit()
    # insert data into medical history table
    medical_history_cursor = mydb.cursor()
    medical_history_query = "INSERT INTO Medical_History (Date,Patient_ID, Diagnosis) VALUES (%s,%s, %s)"
    medical_history_values = (date, patient_ID, diagnosis)
    medical_history_cursor.execute(
        medical_history_query, medical_history_values)
    mydb.commit()
    # Print success message and close window
    success_label = tk.Label(
        window, text="Data inserted successfully", font=font_style)
    success_label.grid(column=1, row=4, **padding)
    window.after(2000, success_label.withdraw)
    window.withdraw()

    # Restart the application
    os.system('python3 appointment.py')


insert_button = tk.Button(window, text="Insert Data",
                          font=font_style, command=insert_data)
insert_button.grid(column=1, row=3, **padding)

window.mainloop()
