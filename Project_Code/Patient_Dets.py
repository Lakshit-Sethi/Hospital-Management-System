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

patient_id = sys.argv[1]
mycursor.execute("SELECT * from Patient where Patient_ID= %s", (patient_id,))
patient = mycursor.fetchone()

mycursor.execute(
    "SELECT sum(Bill_Amount) from Billing where Doctor_ID= %s", (patient_id,))
amount = mycursor.fetchone()[0]

mycursor.execute(
    "SELECT * from Medical_History where Patient_ID= %s", (patient_id,))
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
window.title("Patient Information")

# Create the frame for the hospital name and number of doctors and nurses
header_frame = tk.Frame(window)
header_frame.pack(side=tk.TOP, fill=tk.X)

# Create the label for the Patient Details
hospital_name_label = tk.Label(
    header_frame, text="Patient Name: " + patient[1], font=("Ariel", 14))
hospital_name_label.pack(side=tk.TOP)

hospital_name_label = tk.Label(
    header_frame, text="DOB: " + str(patient[3]), font=("Ariel", 14))
hospital_name_label.pack(side=tk.TOP)

hospital_name_label = tk.Label(
    header_frame, text="Contact Number: " + str(patient[2]), font=("Ariel", 14))
hospital_name_label.pack(side=tk.TOP)

hospital_name_label = tk.Label(
    header_frame, text="Gender: " + patient[4], font=("Ariel", 14))
hospital_name_label.pack(side=tk.TOP)

hospital_name_label = tk.Label(
    header_frame, text="Insurance: " + str(patient[5]), font=("Ariel", 14))
hospital_name_label.pack(side=tk.TOP)

# Create the label for the number of nurses
num_nurses_label = tk.Label(
    header_frame, text=f"Bill: {amount}", font=("Ariel", 14))
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
    # make a popup window with showing diagnosis and taking treatment from the diagnosis table
    diagnosis = selected_data[2]
    mycursor.execute(
        "SELECT * from Diagnosis where Diagnosis= %s", (diagnosis,))
    diagnosis_result = mycursor.fetchone()
    diagnosis = diagnosis_result[0]
    treatment = diagnosis_result[1]

    # create a popup window with the diagnosis and treatment
    popup = tk.Tk()
    popup.wm_title("Diagnosis")
    popup.geometry("400x200")

    label1 = ttk.Label(popup, text="Diagnosis:", font=("Ariel", 14))
    label1.pack(side="top", pady=10)
    diagnosis_label = ttk.Label(popup, text=diagnosis, font=("Ariel", 12))
    diagnosis_label.pack(side="top", pady=10)

    label2 = ttk.Label(popup, text="Treatment:", font=("Ariel", 14))
    label2.pack(side="top", pady=10)
    treatment_label = ttk.Label(popup, text=treatment, font=("Ariel", 12))
    treatment_label.pack(side="top", pady=10)

    B1 = ttk.Button(popup, text="Okay", command=popup.withdraw)
    B1.pack(side="bottom", pady=10)

    popup.mainloop()


# Bind the on-click event to the treeview
tree.bind("<<TreeviewSelect>>", print_selected_data)

# Start the Tkinter event loop
window.mainloop()
