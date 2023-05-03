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
window.title("Doctor Information")
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

# Specialization drop-down list
specialization_label = tk.Label(
    window, text="Specialization Required:", padx=10, pady=10)
specialization_label.grid(row=3, column=0)
specialization_var = tk.StringVar(window)
specialization_var.set("")  # Set default value to empty string
# Fetch department names from database
cursor = mydb.cursor()
cursor.execute("SELECT Department_Name FROM Department")
departments = cursor.fetchall()

# Set size of the drop-down list relative to the number of departments
size = len(departments) if len(departments) < 10 else 10
specialization_menu = tk.OptionMenu(
    window, specialization_var, *departments[:size])
specialization_menu.grid(row=3, column=1, padx=10, pady=10)

# Create button to insert data into MySQL database


def insert_data():
    name = name_entry.get()
    dob = dob_entry.get()
    contact_number = contact_entry.get()
    specialization = specialization_var.get()
    cursor = mydb.cursor(buffered=True)
    cursor.execute(
        "SELECT Department_ID FROM Department WHERE Department_Name = %s", (specialization[2:-3],))
    dept_id = cursor.fetchone()[0]

    # Insert data into Doctor table
    doctor_cursor = mydb.cursor(buffered=True)
    doctor_query = "INSERT INTO DOCTOR (Name, DOB, Contact_Number, Department_ID) VALUES (%s, %s, %s, %s)"
    doctor_values = (name, dob, contact_number, dept_id)
    doctor_cursor.execute(doctor_query, doctor_values)
    mydb.commit()
    doctor_cursor.close()
    tk.messagebox.showinfo("Success", "Doctor added successfully")
    print("Data inserted successfully")
    window.withdraw()
    os.system('python3 add_doctor.py')


insert_button = tk.Button(window, text="Add Doctor",
                          font=label_font, command=insert_data)
insert_button.grid(column=1, row=4, padx=10, pady=10)

window.mainloop()
