import tkinter as tk
import mysql.connector
from tkinter import ttk
import os
import sys

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user=os.environ['USER'],
    password=os.environ['PASS'],
    database="HOSPITAL"
)
mycursor = mydb.cursor()

doctor_id = sys.argv[1]
mycursor.execute("SELECT * from DOCTOR where Doctor_ID= %s", (doctor_id,))
doctor = mycursor.fetchone()

mycursor.execute(
    "SELECT sum(Bill_Amount) from Billing where Doctor_ID= %s", (doctor_id,))
amount = mycursor.fetchone()[0]
mycursor.execute(
    "SELECT Department_Name from Department where Department_ID=%s", (doctor[4],))
doc_department = mycursor.fetchone()[0]
mycursor.execute("SELECT * from Appointment where Doctor_ID= %s", (doctor_id,))
appointments = mycursor.fetchall()
# Get the column names
column_names = [i[0] for i in mycursor.description]
# Calculate the maximum width of each column
max_widths = []
for i in range(len(column_names)):
    max_width = len(column_names[i])
    for result in appointments:
        if len(str(result[i])) > max_width:
            max_width = len(str(result[i]))
    max_widths.append(max_width)

# Create the Tkinter window
window = tk.Tk()
window.title("Doctor Information")

# Create the frame for the hospital name and number of doctors and nurses
header_frame = tk.Frame(window)
header_frame.pack(side=tk.TOP, fill=tk.X)

# Create the label for the Doctor Details
hospital_name_label = tk.Label(
    header_frame, text="Doctor Name: " + doctor[1], font=("Ariel", 14))
hospital_name_label.pack(side=tk.TOP)

hospital_name_label = tk.Label(
    header_frame, text="DOB: " + str(doctor[2]), font=("Ariel", 14))
hospital_name_label.pack(side=tk.TOP)

hospital_name_label = tk.Label(
    header_frame, text="Contact Number: " + str(doctor[3]), font=("Ariel", 14))
hospital_name_label.pack(side=tk.TOP)

hospital_name_label = tk.Label(
    header_frame, text="Department: " + doc_department, font=("Ariel", 14))
hospital_name_label.pack(side=tk.TOP)


# Create the label for the number of nurses
num_nurses_label = tk.Label(
    header_frame, text=f"Amount Earned: {amount}", font=("Ariel", 14))
num_nurses_label.pack(side=tk.TOP)

# Create the treeview
tree = ttk.Treeview(window, columns=column_names, show="headings")

# Set the column headings from the department table
for col in column_names:
    tree.heading(col, text=col)

# Set the column widths relative to the data
for i, width in enumerate(max_widths):
    tree.column(column_names[i], width=width*12)

# Align the columns to the center
tree.column("#0", anchor="center")
for col in column_names:
    tree.heading(col, anchor="center")

# Insert the data into the treeview
for result in appointments:
    tree.insert("", tk.END, values=result)

# Pack the treeview
tree.pack(fill="both", expand=True)

# Function to retrieve data from the selected row and print it to the console


def print_selected_data(event):
    selected_row = tree.focus()
    selected_data = tree.item(selected_row)['values']
    s = 'python3 Patient_Dets.py ' + str(selected_data[1])
    os.system(s)
    # print(s)


# Bind the on-click event to the treeview
tree.bind("<<TreeviewSelect>>", print_selected_data)

# Start the Tkinter event loop
window.mainloop()
