import random
import string
import tkinter as tk
from tkinter import messagebox

# =========================
# Password Generator Logic
# =========================

def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    all_chars = lower + upper + digits + special

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)

    return ''.join(password)


# =========================
# Generate Password Button
# =========================

def generate():
    try:
        length = int(length_entry.get())

        if length < 8:
            messagebox.showwarning("Warning", "Password length must be at least 8")
            return

        password = generate_password(length)

        output_entry.delete(0, tk.END)
        output_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")


# =========================
# Copy Password
# =========================

def copy_password():
    password = output_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")


# =========================
# GUI Setup
# =========================

root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("500x300")
root.resizable(False, False)
root.config(bg="#1e1e2f")

# Title
title = tk.Label(
    root,
    text="🔐 Secure Password Generator",
    font=("Arial", 18, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=20)

# Length Input
length_label = tk.Label(
    root,
    text="Enter Password Length:",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="white"
)
length_label.pack()

length_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center"
)
length_entry.pack(pady=10)

# Generate Button
generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5,
    command=generate
)
generate_btn.pack(pady=10)

# Output Field
output_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=30,
    justify="center"
)
output_entry.pack(pady=10)

# Copy Button
copy_btn = tk.Button(
    root,
    text="Copy Password",
    font=("Arial", 12, "bold"),
    bg="#2196F3",
    fg="white",
    padx=10,
    pady=5,
    command=copy_password
)
copy_btn.pack(pady=10)

# Footer
footer = tk.Label(
    root,
    text="Made by Deepanshu Prajapati",
    font=("Arial", 10),
    bg="#1e1e2f",
    fg="gray"
)
footer.pack(side="bottom", pady=10)

# Run App
root.mainloop()
