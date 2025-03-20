import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def generate_password():
    try:
        l = int(length_entry.get())
        if l < 4:
            messagebox.showerror("Error", "Password length must be at least 4")
            return

        c = string.ascii_lowercase  # Always include lowercase letters

        if uppercase_var.get():
            c += string.ascii_uppercase
        if digits_var.get():
            c += string.digits
        if special_var.get():
            c += string.punctuation

        # Ensure password includes at least one character from each selected category
        p = []
        if uppercase_var.get():
            p.append(random.choice(string.ascii_uppercase))
        if digits_var.get():
            p.append(random.choice(string.digits))
        if special_var.get():
            p.append(random.choice(string.punctuation))

        # Fill the rest of the password
        p += random.choices(c, k=l - len(p))
        random.shuffle(p)

        password_entry.delete(0, tk.END)
        password_entry.insert(0, ''.join(p))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length")

# Function to copy password to clipboard
def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(password_entry.get())
    window.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create GUI window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")
window.resizable(False, False)

# Password length input
tk.Label(window, text="Enter Password Length:", font=("Times New Roman", 12)).pack(pady=5)
length_entry = tk.Entry(window, font=("Times New Roman", 12))
length_entry.pack(pady=5)

# Check buttons for options
uppercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

tk.Checkbutton(window, text="Include Uppercase Letters", variable=uppercase_var).pack()
tk.Checkbutton(window, text="Include Numbers", variable=digits_var).pack()
tk.Checkbutton(window, text="Include Special Characters", variable=special_var).pack()

# Generate button
generate_btn = tk.Button(window, text="Generate Password", font=("Times New Roman", 12), command=generate_password)
generate_btn.pack(pady=10)

# Display password
password_entry = tk.Entry(window, font=("Times New Roman", 14), justify="center")
password_entry.pack(pady=5)

# Copy button
copy_btn = tk.Button(window, text="Copy to Clipboard", font=("Times New Roman", 12), command=copy_to_clipboard)
copy_btn.pack(pady=5)

# Run the application
window.mainloop()