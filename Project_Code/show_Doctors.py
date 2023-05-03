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

Department = sys.argv[1]
mycursor.execute(
    "SELECT * from Department where Department_ID= %s", (Department,))
department_name = mycursor.fetchone()[1]
# Get the number of doctors
mycursor.execute(
    "SELECT COUNT(*) FROM DOCTOR where Department_ID= %s", (Department,))
num_doctors = mycursor.fetchone()[0]

# Get the number of nurses
mycursor.execute(
    "SELECT sum(Bill_Amount) from Billing where Doctor_ID in(select Doctor_ID FROM DOCTOR where Department_ID= %s) ", (Department,))
amount = mycursor.fetchone()[0]

# Query the database for all entries in the departments table
mycursor.execute("SELECT * FROM DOCTOR where Department_ID= %s", (Department,))
department_results = mycursor.fetchall()

# Get the column names
column_names = [i[0] for i in mycursor.description]

# Calculate the maximum width of each column
max_widths = []
for i in range(len(column_names)):
    max_width = len(column_names[i])
    for result in department_results:
        if len(str(result[i])) > max_width:
            max_width = len(str(result[i]))
    max_widths.append(max_width)

# Create the Tkinter window
window = tk.Tk()
window.title("Department Information")

# Create the frame for the hospital name and number of doctors and nurses
header_frame = tk.Frame(window)
header_frame.pack(side=tk.TOP, fill=tk.X)

# Create the label for the hospital name
hospital_name_label = tk.Label(
    header_frame, text="Department Name: " + department_name, font=("Ariel", 14))
hospital_name_label.pack(side=tk.TOP)

# Create the label for the number of doctors
num_doctors_label = tk.Label(
    header_frame, text=f"Number of Doctors: {num_doctors}", font=("Ariel", 14))
num_doctors_label.pack(side=tk.TOP)

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
for result in department_results:
    tree.insert("", tk.END, values=result)

# Pack the treeview
tree.pack(fill="both", expand=True)

# Function to retrieve data from the selected row and print it to the console


def print_selected_data(event):
    selected_row = tree.focus()
    selected_data = tree.item(selected_row)['values']
    s = 'python3 Doctor_Dets.py ' + str(selected_data[0])
    os.system(s)


# Bind the on-click event to the treeview
tree.bind("<<TreeviewSelect>>", print_selected_data)

# Start the Tkinter event loop
window.mainloop()
