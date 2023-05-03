import tkinter as tk
import mysql.connector
from tkinter import ttk
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
window.title("Appointments")
window.geometry("800x400")

# Create treeview for displaying data
treeview = ttk.Treeview(window)
treeview.pack(fill='both', expand=True)
treeview.heading('#0', text='Appointment ID')
treeview.configure(column=('Date', 'Patient ID', 'Doctor ID', 'Diagnosis'))
treeview.heading('Date', text='Date')
treeview.column('Date', width=100)
treeview.heading('Patient ID', text='Patient ID')
treeview.column('Patient ID', width=100)
treeview.heading('Doctor ID', text='Doctor ID')
treeview.column('Doctor ID', width=100)

# Fetch data from Appointment table and display it in treeview
appointment_cursor = mydb.cursor()
appointment_query = "SELECT * FROM Appointment"

appointment_cursor.execute(appointment_query)
rows = appointment_cursor.fetchall()
print(rows)
for row in rows:
    appointment_cursor.execute(
        "Select * from Patient where Patient_ID = %s", (row[1],))
    patient_name = appointment_cursor.fetchone()[1]
    appointment_cursor.execute(
        "Select * from DOCTOR where Doctor_ID = %s", (row[2],))
    doctor_name = appointment_cursor.fetchone()[1]
    treeview.insert(parent='', index='end', text=row[0], values=(
        row[3], patient_name, doctor_name))


# create a function to reschedule the appointment by taking date as input
def reschedule(event):
    item = treeview.selection()[0]
    data = treeview.item(item, 'values')
    appointment_id = treeview.item(item, 'text')
    appointment_cursor.execute(
        "Select * from Appointment where Appointment_ID = %s", (appointment_id,))
    appointment = appointment_cursor.fetchone()

    # create a pop up window to take date as input
    popup = tk.Tk()
    popup.title("Reschedule Appointment")
    popup.geometry("300x100")

    def reschedule_appointment():
        date = date_entry.get()
        appointment_cursor.execute(
            "Update Appointment set A_Date = %s where Appointment_ID = %s", (date, appointment_id))
        mydb.commit()
        treeview.item(item, values=(
            date, appointment[1], appointment[2], appointment[3]))
        popup.withdraw()

    date_label = tk.Label(popup, text="Date")
    date_label.grid(row=0, column=0)
    date_entry = tk.Entry(popup)
    date_entry.grid(row=0, column=1)
    reschedule_button = tk.Button(
        popup, text="Reschedule", command=reschedule_appointment)
    reschedule_button.grid(row=1, column=0)
    cancel_button = tk.Button(popup, text="Cancel", command=popup.withdraw)
    cancel_button.grid(row=1, column=1)
    popup.mainloop()


# Bind function to treeview click event
treeview.bind('<ButtonRelease-1>', reschedule)

window.mainloop()
