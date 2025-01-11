import tkinter as tk
from tkinter import messagebox

from database import add_contact, add_lead
from gui import create_gui

def add_contact_window():
        def submit_new_contact():
            business_name = business_name_entry.get()
            contact_name = contact_name_entry.get()
            email = email_entry.get()
            phone = phone_entry.get()
            status = status_entry.get()

            
            if not all([business_name, contact_name, email, phone, status]):
                messagebox.showerror("Error", "All fields are required.")
                return

            
            add_contact(business_name, contact_name, email, phone, status)
            create_gui.populate_table()
            add_window.destroy()

        
        add_window = tk.Toplevel(root)
        add_window.title("Add New Contact")
        add_window.configure()

        
        tk.Label(add_window, text="Business Name:").grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        business_name_entry = tk.Entry(add_window, font=("Arial", 12))
        business_name_entry.grid(row=0, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Contact Name:").grid(row=1, column=0, padx=20, pady=10, sticky="e")
        contact_name_entry = tk.Entry(add_window, font=("Arial", 12))
        contact_name_entry.grid(row=1, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Email:").grid(row=2, column=0, padx=20, pady=10, sticky="e")
        email_entry = tk.Entry(add_window, font=("Arial", 12))
        email_entry.grid(row=2, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Phone:").grid(row=3, column=0, padx=20, pady=10, sticky="e")
        phone_entry = tk.Entry(add_window, font=("Arial", 12))
        phone_entry.grid(row=3, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Status:").grid(row=4, column=0, padx=20, pady=10, sticky="e")
        status_entry = tk.Entry(add_window, font=("Arial", 12))
        status_entry.grid(row=4, column=1, padx=20, pady=10, sticky="e")

        tk.Button(add_window, text="Add Contact", command=submit_new_contact, padx=10, pady=5).grid(row=5, column=0, columnspan=2, pady=20)

def add_lead_window():
        def submit_new_lead():
            business_name = business_name_entry.get()
            contact_name = contact_name_entry.get()
            title = title_entry.get()
            email = email_entry.get()
            phone = phone_entry.get()
            status = status_entry.get()

            
            if not all([business_name, contact_name, title, email, phone, status]):
                messagebox.showerror("Error", "All fields are required.")
                return

            
            add_lead(business_name, contact_name, title, email, phone, status)
            create_gui.populate_lead_table()
            add_window.destroy()

        
        add_window = tk.Toplevel(root)
        add_window.title("Add New Lead")
        add_window.configure()

        
        tk.Label(add_window, text="Business Name:").grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        business_name_entry = tk.Entry(add_window, font=("Arial", 12))
        business_name_entry.grid(row=0, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Contact Name:").grid(row=1, column=0, padx=20, pady=10, sticky="e")
        contact_name_entry = tk.Entry(add_window, font=("Arial", 12))
        contact_name_entry.grid(row=1, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Title:").grid(row=2, column=0, padx=20, pady=10, sticky="e")
        title_entry = tk.Entry(add_window, font=("Arial", 12))
        title_entry.grid(row=2, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Email:").grid(row=3, column=0, padx=20, pady=10, sticky="e")
        email_entry = tk.Entry(add_window, font=("Arial", 12))
        email_entry.grid(row=3, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Phone:").grid(row=4, column=0, padx=20, pady=10, sticky="e")
        phone_entry = tk.Entry(add_window, font=("Arial", 12))
        phone_entry.grid(row=4, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Status:").grid(row=5, column=0, padx=20, pady=10, sticky="e")
        status_entry = tk.Entry(add_window, font=("Arial", 12))
        status_entry.grid(row=5, column=1, padx=20, pady=10, sticky="e")

        tk.Button(add_window, text="Add Lead", command=submit_new_lead, padx=10, pady=5).grid(row=6, column=0, columnspan=2, pady=20)
        
root = tk.Tk()