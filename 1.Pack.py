import tkinter as tk

def button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.config(state=tk.NORMAL)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
            entry.config(state=tk.DISABLED)
        except Exception as e:
            entry.config(state=tk.NORMAL)
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
            entry.config(state=tk.DISABLED)
    else:
        entry.config(state=tk.NORMAL)
        entry.insert(tk.END, text)
        entry.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=20, state=tk.DISABLED, font=("Arial", 16))
entry.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

for i in range(4):
    frame = tk.Frame(root)
    frame.pack()
    for j in range(4):
        btn = tk.Button(frame, text=buttons[i * 4 + j], width=5, height=2, font=("Arial", 12))
        btn.pack(side=tk.LEFT)
        btn.bind("<Button-1>", button_click)

root.mainloop()
