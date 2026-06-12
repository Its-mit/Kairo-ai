# setup_gui.py
import tkinter as tk
from tkinter import messagebox
from memory import save_profile

def open_setup_gui():

    root = tk.Tk()
    root.title("KAIRO AI Setup")
    root.geometry("400x300")

    tk.Label(root, text="Enter Your Name").pack(pady=5)
    name_entry = tk.Entry(root)
    name_entry.pack()

    tk.Label(root, text="Gender (Male/Female)").pack(pady=5)
    gender_entry = tk.Entry(root)
    gender_entry.pack()

    tk.Label(root, text="Preferred Wake Word").pack(pady=5)
    wake_entry = tk.Entry(root)
    wake_entry.pack()

    def save_data():

        profile = {
            "name": name_entry.get(),
            "gender": gender_entry.get().lower(),
            "wake_word": wake_entry.get()
        }

        save_profile(profile)

        messagebox.showinfo("Saved", "Profile Saved Successfully")

        root.destroy()

    tk.Button(root, text="Save", command=save_data).pack(pady=20)

    root.mainloop()