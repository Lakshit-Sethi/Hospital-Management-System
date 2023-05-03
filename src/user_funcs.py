import tkinter as tk
import os


class MainPage(tk.Frame):
    def __init__(self, parent, on_button_click):
        super().__init__(parent)

        # create widgets
        self.message_label = tk.Label(
            self, text="What would you like to do?", font=("msserif 33", 16))
        self.button1 = tk.Button(self, text="Make Appointments", font=(
            "msserif 33", 12), command=self.makeAppointments)
        self.button2 = tk.Button(self, text="Reschedule Appointments", font=(
            "msserif 33", 12), command=self.reschedule)
        self.button7 = tk.Button(self, text="Allocate Room", font=(
            "msserif 33", 12), command=self.allocateroom)
        self.button8 = tk.Button(self, text="Deallocate Room", font=(
            "msserif 33", 12), command=self.deallocateroom)

        # layout widgets
        self.message_label.pack(pady=20)
        self.button1.pack(pady=10)
        self.button2.pack(pady=10)
        self.button7.pack(pady=10)
        self.button8.pack(pady=10)

    def makeAppointments(self):
        self.master.withdraw()
        os.system('python3 appointment.py')

    def reschedule(self):
        self.master.withdraw()
        os.system('python3 Reschedule.py')

    def allocateroom(self):
        self.master.withdraw()
        os.system('python3 allocate_room.py')

    def deallocateroom(self):
        self.master.withdraw()
        os.system('python3 deallocate_room.py')


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
