import tkinter as tk

def on_button_click():
    label.config(text="Nice the button worked!")

root = tk.Tk()
root.title("Basic Tkinter Example")

label = tk.Label(root, text="Tkinter window", font=("Helvetica", 14))
label.pack(padx=20, pady=20)

button = tk.Button(root, text="Click me sudz!", command=on_button_click)
button.pack(pady=10)

root.mainloop()