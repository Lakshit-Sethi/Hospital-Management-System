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
window.title("Allocate Room")
window.geometry("400x300")

# Create labels and entry boxes for input fields
label_font = ("Arial", 12)
entry_font = ("Arial", 12)

room_label = tk.Label(window, text="Room No.:", font=label_font)
room_label.grid(column=0, row=0, padx=10, pady=10)
room_entry = tk.Entry(window, font=entry_font)
room_entry.grid(column=1, row=0, padx=10, pady=10)

pid_label = tk.Label(window, text="Patient_ID:", font=label_font)
pid_label.grid(column=0, row=1, padx=10, pady=10)
pid_entry = tk.Entry(window, font=entry_font)
pid_entry.grid(column=1, row=1, padx=10, pady=10)

did_label = tk.Label(window, text="Doctor_ID:", font=label_font)
did_label.grid(column=0, row=2, padx=10, pady=10)
did_entry = tk.Entry(window, font=entry_font)
did_entry.grid(column=1, row=2, padx=10, pady=10)

nid_label = tk.Label(window, text="Nurse_ID:", font=label_font)
nid_label.grid(column=0, row=3, padx=10, pady=10)
nid_entry = tk.Entry(window, font=entry_font)
nid_entry.grid(column=1, row=3, padx=10, pady=10)
# Create button to insert data into MySQL database


def insert_data():
    room = room_entry.get()
    pid = pid_entry.get()
    nid = nid_entry.get()
    did = did_entry.get()
    # Insert data into Doctor table
    room_cursor = mydb.cursor(buffered=True)
    room_query = "INSERT INTO Alloted_Room (Room_No, Patient_ID, Nurse_ID, Doctor_ID) VALUES (%s, %s, %s, %s)"
    room_values = (room, pid, nid, did)
    room_cursor.execute(room_query, room_values)
    mydb.commit()
    room_cursor.close()
    tk.messagebox.showinfo("Success", "Room Allocated successfully")
    print("Data inserted successfully")
    window.withdraw()
    os.system('python3 allocate_room.py')


def check_data():
    room = room_entry.get()
    pid = pid_entry.get()
    nid = nid_entry.get()
    did = did_entry.get()
    check_cursor = mydb.cursor(buffered=True)
    if room == "" or pid == "" or nid == "" or did == "":
        tk.messagebox.showerror("Error", "Please fill all the fields")
    else:
        check_cursor.execute(
            "SELECT * FROM Alloted_Room WHERE Room_No = %s", (room,))
        result = check_cursor.fetchone()
        if result is not None:
            tk.messagebox.showerror("Error", "Room already alloted")
        else:
            check_cursor.execute(
                "SELECT * FROM Patient WHERE Patient_ID = %s", (pid,))
            row = check_cursor.fetchone()
            if row is None:
                tk.messagebox.showerror("Error", "Patient does not exist")
            else:
                check_cursor.execute(
                    "SELECT * FROM Nurse WHERE Nurse_ID = %s", (nid,))
                row = check_cursor.fetchone()
                if row is None:
                    tk.messagebox.showerror("Error", "Nurse does not exist")
                else:
                    check_cursor.execute(
                        "SELECT * FROM DOCTOR WHERE Doctor_ID = %s", (did,))
                    row = check_cursor.fetchone()
                    if row is None:
                        tk.messagebox.showerror(
                            "Error", "Doctor does not exist")
                    else:
                        insert_data()


insert_button = tk.Button(window, text="Allocate",
                          font=label_font, command=check_data)
insert_button.grid(column=1, row=4, padx=10, pady=10)

window.mainloop()
