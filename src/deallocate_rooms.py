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

pid_label = tk.Label(window, text="Patient_ID:", font=label_font)
pid_label.grid(column=0, row=1, padx=10, pady=10)
pid_entry = tk.Entry(window, font=entry_font)
pid_entry.grid(column=1, row=1, padx=10, pady=10)


# Create button to insert data into MySQL database
def delete_data(room_no):
    pid = pid_entry.get()
    # Insert data into Doctor table
    room_cursor = mydb.cursor(buffered=True)
    room_query = "Delete from Alloted_Room  where Patient_ID=%s"
    room_values = (pid,)
    room_cursor.execute(room_query, room_values)
    mydb.commit()
    room_cursor.close()
    tk.messagebox.showinfo("Success", "Room " + str(room_no)+" has been freed")
    print("Data inserted successfully")
    window.withdraw()
    os.system('python3 allocate_room.py')


def check_data():
    pid = pid_entry.get()
    check_cursor = mydb.cursor(buffered=True)
    if pid == "":
        tk.messagebox.showerror("Error", "Please fill all the fields")
    else:
        check_cursor.execute(
            "SELECT * FROM Alloted_Room WHERE Patient_ID = %s", (pid,))
        result = check_cursor.fetchone()
        if result is None:
            tk.messagebox.showerror(
                "Error", "No Room was alloted to the patient")
        else:
            room_no = result[0]
            delete_data(room_no)


insert_button = tk.Button(window, text="Free room",
                          font=label_font, command=check_data)
insert_button.grid(column=1, row=4, padx=10, pady=10)

window.mainloop()
