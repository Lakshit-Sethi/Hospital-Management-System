import os
import tkinter as tk
import mysql.connector
import tkinter.messagebox


class LoginPage(tk.Frame):
    def __init__(self, parent, db_connection, on_login):
        super().__init__(parent)
        self.db_connection = db_connection
        self.on_login = on_login

        # create widgets
        self.username_label = tk.Label(
            self, text="Username", font=("Arial", 16))
        self.username_entry = tk.Entry(self, font=("Arial", 16), width=20)
        self.password_label = tk.Label(
            self, text="Password", font=("Arial", 16))
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

        cursor = self.db_connection.cursor()
        cursor.execute(
            "SELECT * FROM credentials WHERE name=%s AND pass=%s", (username, password))
        result = cursor.fetchone()

        if result is not None:

            tkinter.messagebox.showinfo(
                "Login Successful", "Welcome back, {}!".format(username))
            self.master.withdraw()
            if result[2] == "Admin":
                os.system('python3 funcs.py')
            else:
                os.system('python3 user_funcs.py')
        else:
            tkinter.messagebox.showerror(
                "Login Error", "Invalid username or password.")


def main():
    # create window
    root = tk.Tk()
    root.title("Login Page")
    root.geometry("400x300")

    # create database connection
    db_connection = mysql.connector.connect(
        host="localhost",
        user=os.environ['USER'],
        password=os.environ['PASS'],
        database="HOSPITAL"
    )

    # create login page
    login_page = LoginPage(root, db_connection,
                           lambda: print("Login successful!"))
    login_page.pack(expand=True)

    # run application
    root.mainloop()


if __name__ == "__main__":
    main()
