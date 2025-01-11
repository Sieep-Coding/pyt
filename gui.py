import tkinter as tk
from tkinter import ttk, messagebox, Menu
from database import fetch_contacts, add_contact, delete_contact, add_project, fetch_projects, delete_project, fetch_leads, add_lead, update_lead
import sv_ttk

def create_gui():
    def populate_table():
        """Populate the contacts table."""
        table.delete(*table.get_children())
        for contact in fetch_contacts():
            table.insert("", "end", values=contact)

    def populate_project_table():
        """Populate the projects table."""
        proj_table.delete(*proj_table.get_children())
        for project in fetch_projects():
            proj_table.insert("", "end", values=project)

    def populate_lead_table():
        """Populate the leads table."""
        lead_table.delete(*proj_table.get_children())
        for lead in fetch_leads():
            lead_table.insert("", "end", values=lead)

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

            
            if not all([business_name, contact_name, email, phone, status]):
                messagebox.showerror("Error", "All fields are required.")
                return

            
            add_contact(business_name, contact_name, email, phone, status)
            populate_table()
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
            populate_table()
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
    
    menubar = Menu(root) 
  
    file = Menu(menubar, tearoff=False) 
    menubar.add_cascade(label="File", menu=file) 
    file.add_command(label="New") 
    file.add_command(label="Exit", command=root.quit) 
    
    edit = Menu(menubar, tearoff=False)
    menubar.add_cascade(label="Edit", menu=edit) 
    edit.add_command(label="Cut") 
    edit.add_command(label="Copy") 
    edit.add_command(label="Paste")

    selection = Menu(menubar, tearoff=False)
    menubar.add_cascade(label="Selection", menu=selection) 
    selection.add_command(label="Select All") 
    
    view = Menu(menubar, tearoff=False)
    menubar.add_cascade(label="View", menu=view) 
    view.add_command(label="Reports")
    
    root.configure(borderwidth=5, menu=menubar)

    
    tabline = tk.Frame(root)
    tabline.grid(row=0, column=0, sticky="nsew")
    tabline.grid_propagate(False)

    tabs = ["Contacts", "Leads", "Projects", "Activities", "Services", "Reports"]
    frames = {}

    for tab in tabs:
        btn = tk.Button(tabline, text=tab, command=lambda t=tab: switch_tab(t), padx=7, pady=3, cursor="plus")
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
    tk.Button(button_frame, text="Delete Contact", command=delete_selected_contact, padx=5, pady=1).pack(side="left",padx=5)
    tk.Button(button_frame, text="Reload Table", command=populate_table, padx=5, pady=1).pack(side="left",padx=5)

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

    # Leads
    leads = frames["Leads"]

    lead_table = ttk.Treeview(leads, columns=("ID", "Business Name", "Contact Name", "Title", "Email", "Phone", "Status"))
    lead_table.heading("ID", text="ID")
    lead_table.heading("Contact Name", text="Project Name")
    lead_table.heading("Email", text="Email")
    lead_table.heading("Phone", text="Phone")
    lead_table.heading("Status", text="Status")
    lead_table.pack(fill="both", expand=True)

    button_frame = tk.Frame(leads)
    button_frame.pack(pady=20)
    tk.Button(button_frame, text="Add Lead", command=add_lead_window, padx=5, pady=1).pack(side="left",padx=5)
    tk.Button(button_frame, text="Reload Table", command=populate_table, padx=5, pady=1).pack(side="left",padx=5)

    # Theme
    sv_ttk.set_theme("dark")
    sv_ttk.use_dark_theme()
    populate_table()
    populate_project_table()
    populate_lead_table()

    switch_tab("Contacts")
    root.resizable(True, True)
    root.mainloop()