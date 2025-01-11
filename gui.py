import tkinter as tk
from tkinter import ttk, messagebox
from database import fetch_contacts, add_contact, delete_contact, add_project, fetch_projects, delete_project
import sv_ttk

def create_gui():
    def populate_table():
        # Clear the current table entries
        for row in table.get_children():
            table.delete(row)
        
        # Fetch contacts from the database and populate the table
        for contact in fetch_contacts():
            table.insert("", "end", values=contact)

    def populate_project_table():
        for row in table.get_children():
            table.delete(row)

        for project in fetch_projects():
            table.insert("", "end", values=project)

    def switch_tab(tab_name):
        for frame in frames.values():
            frame.grid_remove()
        frames[tab_name].grid(row=1, column=0, sticky="nsew")

    def add_contact_window():
        def submit_new_contact():
            business_name = business_name_entry.get()
            contact_name = contact_name_entry.get()
            email = email_entry.get()
            phone = phone_entry.get()
            status = status_entry.get()

            # Check if all fields are filled
            if not all([business_name, contact_name, email, phone, status]):
                messagebox.showerror("Error", "All fields are required.")
                return

            # Call the add_contact function from the database module
            add_contact(business_name, contact_name, email, phone, status)
            populate_table()
            add_window.destroy()

        # Create a new window for adding a contact
        add_window = tk.Toplevel(root)
        add_window.title("Add New Contact")
        add_window.configure()

        # Form elements for adding a contact
        tk.Label(add_window, text="Business Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        business_name_entry = tk.Entry(add_window, font=("Arial", 12))
        business_name_entry.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

        tk.Label(add_window, text="Contact Name:").grid(row=1, column=0, padx=20, pady=10, sticky="e")
        contact_name_entry = tk.Entry(add_window, font=("Arial", 12))
        contact_name_entry.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

        tk.Label(add_window, text="Email:").grid(row=2, column=0, padx=20, pady=10, sticky="e")
        email_entry = tk.Entry(add_window, font=("Arial", 12))
        email_entry.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

        tk.Label(add_window, text="Phone:").grid(row=3, column=0, padx=20, pady=10, sticky="e")
        phone_entry = tk.Entry(add_window, font=("Arial", 12))
        phone_entry.grid(row=3, column=1, padx=20, pady=10, sticky="ew")

        tk.Label(add_window, text="Status:").grid(row=4, column=0, padx=20, pady=10, sticky="e")
        status_entry = tk.Entry(add_window, font=("Arial", 12))
        status_entry.grid(row=4, column=1, padx=20, pady=10, sticky="ew")

        tk.Button(add_window, text="Add Contact", command=submit_new_contact, padx=10, pady=5).grid(row=5, column=0, columnspan=2, pady=20)

    def delete_selected_contact():
        selected_item = table.selection()
        if not selected_item:
            messagebox.showerror("Error", "No contact selected.")
            return
        else:
            response = messagebox.askyesnocancel("Confirm Delete", "Are you sure you want to delete this contact?")
            if response:
                contact_id = table.item(selected_item, "values")[0]
                # Call delete_contact function from the database module
                delete_contact(contact_id)
                populate_table()
            elif response is None or False:
                return
            
    def delete_selected_project():
        selected_item = table.selection()
        if not selected_item:
            messagebox.showerror("Error", "No contact selected.")
            return
        else:
            response = messagebox.askyesnocancel("Confirm Delete", "Are you sure you want to delete this contact?")
            if response:
                contact_id = table.item(selected_item, "values")[0]
                # Call delete_contact function from the database module
                delete_project(contact_id)
                populate_table()
            elif response is None or False:
                return
            

    def update_selected_contact():
        selected_item = table.selection()
        if not selected_item:
            messagebox.showerror("Error", "No contact selected.")
            return
        contact_id = table.item(selected_item, "values")[0]
        update_selected_contact(contact_id)
        populate_table()

    root = tk.Tk()
    root.title("pyt")
    root.attributes('-fullscreen', False)
    root.configure(border=2, borderwidth=7, padx=5, pady=12)

    # Modern Tabline
    tabline = tk.Frame(root)
    tabline.grid(row=0, column=0, sticky="ew")
    tabline.grid_propagate(False)

    tabs = ["Contacts", "Projects", "Activities", "Services", "Reports"]
    frames = {}

    for tab in tabs:
        btn = tk.Button(tabline, text=tab, command=lambda t=tab: switch_tab(t), padx=7, pady=3)
        btn.pack(side="left", padx=1, pady=1)
        frames[tab] = tk.Frame(root)

    # Contacts
    contacts = frames["Contacts"]

    table = ttk.Treeview(contacts, columns=("ID", "Business Name", "Contact Name", "Email", "Phone", "Status"), show="headings")
    table.heading("ID", text="ID")
    table.heading("Business Name", text="Business Name")
    table.heading("Contact Name", text="Contact Name")
    table.heading("Email", text="Email")
    table.heading("Phone", text="Phone")
    table.heading("Status", text="Status")
    table.pack(fill="both", expand=True)

    button_frame = tk.Frame(contacts)
    button_frame.pack(pady=20)

    tk.Button(button_frame, text="Add Contact", command=add_contact_window, padx=5, pady=1).pack(side="left", padx=5)
    tk.Button(button_frame, text="Delete Contact", command=delete_selected_contact, padx=5, pady=1).pack(padx=5)

    # Projects
    projects = frames["Projects"]

    proj_table = ttk.Treeview(projects, columns=("ID", "Project Name", "Email", "Phone", "Status"), show="headings")
    proj_table.heading("ID", text="ID")
    proj_table.heading("Project Name", text="Project Name")
    proj_table.heading("Email", text="Email")
    proj_table.heading("Phone", text="Phone")
    proj_table.heading("Status", text="Project Status")
    proj_table.pack(fill="both", expand=True)
    
    button_frame = tk.Frame(projects)
    button_frame.pack(pady=20)
    tk.Button(button_frame, text="Add Project", padx=5, pady=1).pack(side="left", padx=5)
    tk.Button(button_frame, text="Delete Project", command=delete_selected_project, padx=5, pady=1).pack(padx=5)

    # Theme
    sv_ttk.set_theme("dark")
    sv_ttk.use_dark_theme()
    populate_table()
    populate_project_table()

    switch_tab("Contacts")
    root.mainloop()
