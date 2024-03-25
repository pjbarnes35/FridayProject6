import tkinter as tk

def sign_up():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    print(f"Name: {name}, Email: {email}, Password: {password}")

root = tk.Tk()
root.title("Sign Up Page")

labels = ["Name:", "Email:", "Password:"]
for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text, font=("Arial", 12))
    label.grid(row=i, column=0, padx=10, pady=10, sticky=tk.E)

name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=10, pady=10)

email_entry = tk.Entry(root, font=("Arial", 12))
email_entry.grid(row=1, column=1, padx=10, pady=10)

password_entry = tk.Entry(root, show="*", font=("Arial", 12))
password_entry.grid(row=2, column=1, padx=10, pady=10)

signup_btn = tk.Button(root, text="Sign Up Now", command=sign_up, font=("Arial", 12))
signup_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
