import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()
    print(f"Username: {username}, Password: {password}")

root = tk.Tk()
root.title("Login Page")

username_label = tk.Label(root, text="Username:", font=("Arial", 12))
username_label.place(x=50, y=50)

username_entry = tk.Entry(root, font=("Arial", 12))
username_entry.place(x=150, y=50)

password_label = tk.Label(root, text="Password:", font=("Arial", 12))
password_label.place(x=50, y=100)

password_entry = tk.Entry(root, show="*", font=("Arial", 12))
password_entry.place(x=150, y=100)

login_btn = tk.Button(root, text="Login", command=login, font=("Arial", 12))
login_btn.place(x=150, y=150)

root.mainloop()
