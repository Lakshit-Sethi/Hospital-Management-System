import tkinter as tk
import os


class MainPage(tk.Frame):
    def __init__(self, parent, on_button_click):
        super().__init__(parent)

        # create widgets
        self.message_label = tk.Label(
            self, text="What would you like to do?", font=("msserif 33", 16))
        self.button1 = tk.Button(self, text="Make Appointements", font=(
            "msserif 33", 12), command=self.makeAppointments)
        self.button2 = tk.Button(self, text="Reschedule Appointements", font=(
            "msserif 33", 12), command=self.reschedule)
        self.button3 = tk.Button(self, text="Add Doctors", font=(
            "msserif 33", 12), command=self.newDoctor)
        self.button4 = tk.Button(self, text="Add Nurses", font=(
            "msserif 33", 12), command=self.newNurse)
        self.button5 = tk.Button(self, text="See Patient details", font=(
            "msserif 33", 12), command=self.patientdets)
        self.button6 = tk.Button(self, text="See Hospital details", font=(
            "msserif 33", 12), command=self.doctordets)
        self.button7 = tk.Button(self, text="Allocate Room", font=(
            "msserif 33", 12), command=self.allocateroom)
        self.button8 = tk.Button(self, text="Deallocat Room", font=(
            "msserif 33", 12), command=self.deallocateroom)

        # layout widgets
        self.message_label.pack(pady=20)
        self.button1.pack(pady=10)
        self.button2.pack(pady=10)
        self.button3.pack(pady=10)
        self.button4.pack(pady=10)
        self.button5.pack(pady=10)
        self.button6.pack(pady=10)
        self.button7.pack(pady=10)
        self.button8.pack(pady=10)

    def makeAppointments(self):
        self.master.withdraw()
        os.system('python3 appointment.py')

    def newDoctor(self):
        self.master.withdraw()
        os.system('python3 add_doctor.py')

    def newNurse(self):
        self.master.withdraw()
        os.system('python3 add_nurse.py')

    def patientdets(self):
        self.master.withdraw()
        os.system('python3 show_patient.py')

    def doctordets(self):
        self.master.withdraw()
        os.system('python3 Hospital.py')

    def reschedule(self):
        self.master.withdraw()
        os.system('python3 Reschedule.py')

    def allocateroom(self):
        self.master.withdraw()
        os.system('python3 allocate_room.py')

    def deallocateroom(self):
        self.master.withdraw()
        os.system('python3 deallocate_rooms.py')


def main():
    # create window
    root = tk.Tk()
    root.title("Main Page")

    # create main page
    main_page = MainPage(root, lambda x: print("Button {} clicked".format(x)))
    main_page.pack(expand=True)

    # run application
    root.mainloop()


if __name__ == "__main__":
    main()
