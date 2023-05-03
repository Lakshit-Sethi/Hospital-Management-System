import os
import tkinter as tk
import mysql.connector
import tkinter.messagebox


class LoginPage(tk.Frame):
    def __init__(self, parent, on_login):
        super().__init__(parent)
        self.on_login = on_login

        # create widgets
        self.username_label = tk.Label(
            self, text="MYSQL Username", font=("Arial", 16))
        self.username_entry = tk.Entry(self, font=("Arial", 16), width=20)
        self.password_label = tk.Label(
            self, text="MYSQL Password", font=("Arial", 16))
        self.password_entry = tk.Entry(
            self, show="*", font=("Arial", 16), width=20)
        self.login_button = tk.Button(self, text="Login", font=(
            "Arial", 16), command=self.login, width=10)

        # layout widgets
        self.username_label.grid(row=0, column=0, padx=20, pady=20)
        self.username_entry.grid(row=0, column=1, padx=20, pady=20)
        self.password_label.grid(row=1, column=0, padx=20, pady=20)
        self.password_entry.grid(row=1, column=1, padx=20, pady=20)
        self.login_button.grid(row=2, column=1, padx=20, pady=20)

    def login(self):
        # perform login validation
        username = self.username_entry.get()
        password = self.password_entry.get()
        os.environ['USER'] = username
        os.environ['PASS'] = password
        self.master.withdraw()
        os.system('python3 start.py')


def main():
    # create window
    root = tk.Tk()
    root.title("My Sql Login Page")
    root.geometry("600x300")
    # create login page
    login_page = LoginPage(root, lambda: print("Login successful!"))
    login_page.pack(expand=True)

    # run application
    root.mainloop()


if __name__ == "__main__":
    main()
