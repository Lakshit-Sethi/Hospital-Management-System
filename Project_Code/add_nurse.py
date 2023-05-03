import tkinter as tk
import mysql.connector
import tkinter.messagebox
import os

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user=os.environ['USER'],
    password=os.environ['PASS'],
    database="HOSPITAL"
)

# Create Tkinter window
window = tk.Tk()
window.title("Nurse Information")
window.geometry("400x300")

# Create labels and entry boxes for input fields
label_font = ("Arial", 12)
entry_font = ("Arial", 12)

name_label = tk.Label(window, text="Name:", font=label_font)
name_label.grid(column=0, row=0, padx=10, pady=10)
name_entry = tk.Entry(window, font=entry_font)
name_entry.grid(column=1, row=0, padx=10, pady=10)

dob_label = tk.Label(window, text="DOB:", font=label_font)
dob_label.grid(column=0, row=1, padx=10, pady=10)
dob_entry = tk.Entry(window, font=entry_font)
dob_entry.grid(column=1, row=1, padx=10, pady=10)

contact_label = tk.Label(window, text="Contact Number:", font=label_font)
contact_label.grid(column=0, row=2, padx=10, pady=10)
contact_entry = tk.Entry(window, font=entry_font)
contact_entry.grid(column=1, row=2, padx=10, pady=10)

# Create button to insert data into MySQL database


def insert_data():
    name = name_entry.get()
    dob = dob_entry.get()
    contact_number = contact_entry.get()
    # Insert data into Doctor table
    doctor_cursor = mydb.cursor()
    doctor_query = "INSERT INTO Nurse (Name, DOB, Contact_Number) VALUES (%s, %s, %s)"
    doctor_values = (name, dob, contact_number)
    doctor_cursor.execute(doctor_query, doctor_values)
    mydb.commit()
    doctor_cursor.close()
    tk.messagebox.showinfo("Success", "Nurse added successfully")
    print("Data inserted successfully")
    window.withdraw()
    os.system('python3 add_nurse.py')


insert_button = tk.Button(window, text="Add Nurse",
                          font=label_font, command=insert_data)
insert_button.grid(column=1, row=4, padx=10, pady=10)

window.mainloop()
