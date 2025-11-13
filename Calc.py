import tkinter as tk

# Create window
window = tk.Tk()
window.title("Alpha's Calculator")
window.geometry("400x600")
window.config(bg="#f0f0f0")  # light gray background

# Text widget (like Entry) with undo enabled
entry = tk.Text(window, width=16, height=1, font=("Arial", 24), borderwidth=2, relief="ridge", undo=True)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Functions
def button_click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete("1.0", tk.END)

def calculate():
    try:
        expression = entry.get("1.0", tk.END).strip()
        result = eval(expression)
        entry.delete("1.0", tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete("1.0", tk.END)
        entry.insert(tk.END, "Error")

def undo():
    try:
        entry.edit_undo()
    except:
        pass

def redo():
    try:
        entry.edit_redo()
    except:
        pass

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(
            window, text=text, width=5, height=2, bg="#4CAF50", fg="white",
            font=("Arial", 18), command=calculate
        ).grid(row=row, column=col, padx=5, pady=5)
    elif text in "+-*/":
        tk.Button(
            window, text=text, width=5, height=2, bg="#FFA500", fg="white",
            font=("Arial", 18), command=lambda t=text: button_click(t)
        ).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(
            window, text=text, width=5, height=2, bg="#E0E0E0", fg="black",
            font=("Arial", 18), command=lambda t=text: button_click(t)
        ).grid(row=row, column=col, padx=5, pady=5)

# Clear button
tk.Button(
    window, text="C", width=22, height=2, bg="#FF4C4C", fg="white",
    font=("Arial", 18), command=clear
).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Undo button
tk.Button(
    window, text="Undo", width=10, height=2, bg="#2196F3", fg="white",
    font=("Arial", 12), command=undo
).grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Redo button
tk.Button(
    window, text="Redo", width=10, height=2, bg="#9C27B0", fg="white",
    font=("Arial", 12), command=redo
).grid(row=6, column=2, columnspan=2, padx=5, pady=5)

# Run the window
window.mainloop()
