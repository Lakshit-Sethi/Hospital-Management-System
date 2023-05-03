import tkinter as tk
import mysql.connector
import tkinter.messagebox
import os

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user=os.environ['USER'],
    password=os.environ['PASS'],
    database="HOSPITAL"
)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Patient name input field
        self.patient_name_label = tk.Label(
            self, text="Patient name:", padx=10, pady=10)
        self.patient_name_label.grid(row=0, column=0)
        self.patient_name_entry = tk.Entry(self, width=30)
        self.patient_name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Contact number input field
        self.contact_number_label = tk.Label(
            self, text="Contact number:", padx=10, pady=10)
        self.contact_number_label.grid(row=1, column=0)
        self.contact_number_entry = tk.Entry(self, width=30)
        self.contact_number_entry.grid(row=1, column=1, padx=10, pady=10)

        # Date of birth input field
        self.dob_label = tk.Label(
            self, text="Date of birth:", padx=10, pady=10)
        self.dob_label.grid(row=2, column=0)
        self.dob_entry = tk.Entry(self, width=30)
        self.dob_entry.grid(row=2, column=1, padx=10, pady=10)

        # Gender input field
        self.gender_label = tk.Label(self, text="Gender:", padx=10, pady=10)
        self.gender_label.grid(row=3, column=0)
        self.gender_entry = tk.Entry(self, width=30)
        self.gender_entry.grid(row=3, column=1, padx=10, pady=10)

        # Insurance input field
        self.insurance_label = tk.Label(
            self, text="Insurance:", padx=10, pady=10)
        self.insurance_label.grid(row=4, column=0)
        self.insurance_entry = tk.Entry(self, width=30)
        self.insurance_entry.grid(row=4, column=1, padx=10, pady=10)

        # Specialization drop-down list
        self.specialization_label = tk.Label(
            self, text="Specialization Required:", padx=10, pady=10)
        self.specialization_label.grid(row=5, column=0)
        self.specialization_var = tk.StringVar(self)
        self.specialization_var.set("")  # Set default value to empty string

        # Fetch department names from database
        cursor = db.cursor()
        cursor.execute("SELECT Department_Name FROM Department")
        departments = cursor.fetchall()

        # Set size of the drop-down list relative to the number of departments
        size = len(departments) if len(departments) < 10 else 10
        self.specialization_menu = tk.OptionMenu(
            self, self.specialization_var, *departments[:size])
        self.specialization_menu.grid(row=5, column=1, padx=10, pady=10)

        # Submit button
        self.submit_button = tk.Button(
            self, text="Submit", command=self.submit_form, padx=10, pady=10)
        self.submit_button.grid(
            row=6, column=0, columnspan=2, padx=10, pady=10)

    def submit_form(self):
        # Get values from input fields
        patient_name = self.patient_name_entry.get()
        contact_number = self.contact_number_entry.get()
        dob = self.dob_entry.get()
        gender = self.gender_entry.get()
        insurance = self.insurance_entry.get()
        specialization = self.specialization_var.get()

        # Validate input fields
        if not patient_name:
            tk.messagebox.showerror("Error", "Please enter a patient name.")
            return
        if not contact_number:
            tk.messagebox.showerror("Error", "Please enter a contact number.")
            return
        if not dob:
            tk.messagebox.showerror("Error", "Please enter a date of birth.")
            return
        if not gender:
            tk.messagebox.showerror("Error", "Please enter a gender.")
            return
        if not insurance:
            tk.messagebox.showerror("Error", "Please enter an insurance.")
            return
        if not specialization:
            tk.messagebox.showerror("Error", "Please select a specialization.")
            return
        cursor = db.cursor()
        cursor.execute("SELECT * from Patient where Name= %s and Contact_Number=%s and DOB=%s and Gender=%s",
                       (patient_name, contact_number, dob, gender,))
        result = cursor.fetchone()
        # check if patient already exists
        if result is None:
            # Insert data into the database

            sql = "INSERT INTO Patient (name, contact_number, dob, gender, insurance) VALUES (%s, %s, %s, %s, %s)"
            val = (patient_name, contact_number, dob, gender, insurance)
            cursor.execute(sql, val)
            db.commit()

        # Get the generated Patient_ID
        cursor.execute("SELECT * from Patient where Name= %s and Contact_Number=%s and DOB=%s and Gender=%s",
                       (patient_name, contact_number, dob, gender,))
        result = cursor.fetchone()
        patient_id = result[0]

        # Clear input fields
        self.patient_name_entry.delete(0, tk.END)
        self.contact_number_entry.delete(0, tk.END)
        self.dob_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)
        self.insurance_entry.delete(0, tk.END)
        # Set drop-down list value back to default
        self.specialization_var.set("")

        # Show success message
        tk.messagebox.showinfo(
            "Success", "Patient record added to the database.")

        # Store the patient ID in a variable for future use
        self.patient_id = patient_id
        self.master.withdraw()
        Spec = specialization[2:-3]
        cursor.execute(
            "SELECT * from Department where Department_Name= %s", (Spec,))
        department_name = cursor.fetchone()[0]
        s = 'python3 appointment2.py ' + \
            str(patient_id)+' ' + str(department_name)
        os.system(s)
        # print(s)


root = tk.Tk()
root.title("Appointment Form")
app = Application(master=root)
app.mainloop()
