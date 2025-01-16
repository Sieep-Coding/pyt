import csv
import tkinter as tk
from tkinter import ttk, messagebox, Menu, filedialog
import tkinter.font
from backend.database import (
    fetch_contacts,
    add_contact,
    delete_contact,
    fetch_projects,
    delete_project,
    fetch_leads,
    add_lead,
    delete_lead,
    add_account,
    fetch_accounts,
    delete_account,
    update_contact
)
import sv_ttk
from collections import Counter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # type: ignore
import matplotlib.pyplot as plt  # type: ignore


def create_gui():
    def populate_contact_table():
        """Populate the contacts table."""
        table.delete(*table.get_children())
        for contact in fetch_contacts():
            table.insert("", "end", values=contact)

    def populate_project_table():
        """Populate the projects table."""
        proj_table.delete(*proj_table.get_children())
        for project in fetch_projects():
            proj_table.insert("", "end", values=project)

    def populate_account_table():
        """Populate the projects table."""
        acct_table.delete(*acct_table.get_children())
        for account in fetch_accounts():
            acct_table.insert("", "end", values=account)

    def populate_lead_table():
        """Populate the leads table."""
        lead_table.delete(*lead_table.get_children())
        for lead in fetch_leads():
            lead_table.insert("", "end", values=lead)

    def switch_tab(tab_name):
        """Identify the frame value and seamlessly switch to it."""
        for frame in frames.values():
            frame.grid_remove()
        frames[tab_name].grid(row=1, column=0, sticky="nsew")

    def add_contact_window():
        """Prompt the user to fill out a new contact."""
        def submit_new_contact():
            """Send the new contact data to the db"""
            business_name = business_name_entry.get()
            contact_name = contact_name_entry.get()
            email = email_entry.get()
            phone = phone_entry.get()
            status = status_entry.get()

            if not all([business_name, contact_name, email, phone, status]):
                messagebox.showerror("Error", "All fields are required.")
                return

            add_contact(business_name, contact_name, email, phone, status)
            populate_contact_table()
            add_window.destroy()

        add_window = tk.Toplevel(root)
        add_window.title("spark - Add New Contact")
        add_window.configure()

        tk.Label(add_window, text="Business Name:").grid(
            row=0, column=0, padx=10, pady=5, sticky="nsew"
        )
        business_name_entry = tk.Entry(add_window, font=font)
        business_name_entry.grid(row=0, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Contact Name:").grid(
            row=1, column=0, padx=20, pady=10, sticky="e"
        )
        contact_name_entry = tk.Entry(add_window, font=font)
        contact_name_entry.grid(row=1, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Email:").grid(
            row=2, column=0, padx=20, pady=10, sticky="e"
        )
        email_entry = tk.Entry(add_window, font=font)
        email_entry.grid(row=2, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Phone:").grid(
            row=3, column=0, padx=20, pady=10, sticky="e"
        )
        phone_entry = tk.Entry(add_window, font=font)
        phone_entry.grid(row=3, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Status:").grid(
            row=4, column=0, padx=20, pady=10, sticky="e"
        )
        status_entry = tk.Entry(add_window, font=font)
        status_entry.grid(row=4, column=1, padx=20, pady=10, sticky="e")

        tk.Button(
            add_window, text="Add Contact",
            command=submit_new_contact,
            padx=10,
            pady=5,
            font=font
        ).grid(row=5, column=0, columnspan=2, pady=20)

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
            populate_lead_table()
            add_window.destroy()

        add_window = tk.Toplevel(root)
        add_window.title("spark - Add New Lead")
        add_window.configure()

        tk.Label(add_window, text="Business Name:").grid(
            row=0, column=0, padx=10, pady=5, sticky="nsew"
        )
        business_name_entry = tk.Entry(add_window, font=font)
        business_name_entry.grid(row=0, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Contact Name:").grid(
            row=1, column=0, padx=20, pady=10, sticky="e"
        )
        contact_name_entry = tk.Entry(add_window, font=font)
        contact_name_entry.grid(row=1, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Title:").grid(
            row=2, column=0, padx=20, pady=10, sticky="e"
        )
        title_entry = tk.Entry(add_window, font=font)
        title_entry.grid(row=2, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Email:").grid(
            row=3, column=0, padx=20, pady=10, sticky="e"
        )
        email_entry = tk.Entry(add_window, font=font)
        email_entry.grid(row=3, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Phone:").grid(
            row=4, column=0, padx=20, pady=10, sticky="e"
        )
        phone_entry = tk.Entry(add_window, font=font)
        phone_entry.grid(row=4, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Status:").grid(
            row=5, column=0, padx=20, pady=10, sticky="e"
        )
        status_entry = tk.Entry(add_window, font=font)
        status_entry.grid(row=5, column=1, padx=20, pady=10, sticky="e")

        tk.Button(
            add_window,
            text="Add Lead",
            command=submit_new_lead,
            padx=10,
            pady=5,
            font=font
        ).grid(row=6, column=0, columnspan=2, pady=20)

    def add_account_window():
        def submit_new_account():
            business_name = business_name_entry.get()
            contact_name = contact_name_entry.get()
            email = email_entry.get()
            phone = phone_entry.get()
            status = status_entry.get()

            if not all([business_name, contact_name, email, phone, status]):
                messagebox.showerror("Error", "All fields are required.")
                return

            add_account(business_name, contact_name, email, phone, status)
            messagebox.showinfo("Success", "Account added successfully!")
            populate_account_table()
            add_window.destroy()

        add_window = tk.Toplevel(root)
        add_window.title("spark - Add New Account")
        add_window.configure()

        tk.Label(add_window, text="Business Name:").grid(
            row=0, column=0, padx=10, pady=5, sticky="nsew"
        )
        business_name_entry = tk.Entry(add_window, font=font)
        business_name_entry.grid(row=0, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Contact Name:").grid(
            row=1, column=0, padx=20, pady=10, sticky="e"
        )
        contact_name_entry = tk.Entry(add_window, font=font)
        contact_name_entry.grid(row=1, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Email:").grid(
            row=3, column=0, padx=20, pady=10, sticky="e"
        )
        email_entry = tk.Entry(add_window, font=font)
        email_entry.grid(row=3, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Phone:").grid(
            row=4, column=0, padx=20, pady=10, sticky="e"
        )
        phone_entry = tk.Entry(add_window, font=font)
        phone_entry.grid(row=4, column=1, padx=20, pady=10, sticky="e")

        tk.Label(add_window, text="Status:").grid(
            row=5, column=0, padx=20, pady=10, sticky="e"
        )
        status_entry = tk.Entry(add_window, font=font)
        status_entry.grid(row=5, column=1, padx=20, pady=10, sticky="e")

        tk.Button(
            add_window,
            text="Add Account",
            command=submit_new_account,
            padx=10,
            pady=5,
            font=font
        ).grid(row=6, column=0, columnspan=2, pady=20)

    def delete_selected_contact():
        selected_item = table.selection()
        if not selected_item:
            messagebox.showerror(
                "Error", "No contact selected.")
            return
        if len(selected_item) > 1:
            messagebox.showerror(
                "Error", "Please select one contact, this feature will be added soon.")
            return
        else:
            response = messagebox.askyesnocancel(
                "Confirm Delete", "Are you sure you want to delete this contact?"
            )
            if response:
                contact_id = table.item(selected_item, "values")[0]
                delete_contact(contact_id)
                populate_contact_table()
            elif response is None or False:
                return

    def delete_selected_account():
        selected_item = acct_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "No account selected.")
            return
        if len(selected_item) > 1:
            messagebox.showerror(
                "Error", "Please select one contact, this feature will be added soon.")
            return
        else:
            response = messagebox.askyesnocancel(
                "Confirm Delete", "Are you sure you want to delete this account?"
            )
            if response:
                acct_id = acct_table.item(selected_item, "values")[0]
                delete_account(acct_id)
                populate_account_table()
            elif response is None or False:
                return

    def delete_selected_lead():
        selected_lead = lead_table.selection()
        if not selected_lead:
            messagebox.showerror("Error", "No lead selected.")
            return
        if len(selected_lead) > 1:
            messagebox.showerror(
                "Error", "Please select one contact, this feature will be added soon.")
            return
        else:
            response = messagebox.askyesnocancel(
                "Confirm Delete", "Are you sure you want to delete this lead?"
            )
            if response:
                lead_id = lead_table.item(selected_lead, "values")[0]
                delete_lead(lead_id)
                messagebox.showinfo("Success", "Lead deleted successfully!")
                populate_lead_table()
            elif response is None or False:
                return

    def delete_selected_project():
        selected_item = proj_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "No project selected.")
            return
        else:
            response = messagebox.askyesnocancel(
                "Confirm Delete", "Are you sure you want to delete this project?"
            )
            if response:
                contact_id = proj_table.item(selected_item, "values")[0]
                delete_project(contact_id)
                messagebox.showinfo("Success", "Project Deleted successfully!")
                populate_project_table()
            elif response is None or False:
                return

    def update_selected_contact_window():
        selected_item = table.selection()
        if not selected_item:
            messagebox.showerror("Error", "No contact selected.")
            return

        def update_selected_contact():
            # Get the selected contact's ID
            selected_item = table.selection()
            if not selected_item:
                messagebox.showerror("Error", "No contact selected.")
                return

            contact_id = table.item(selected_item, "values")[0]

            # Retrieve updated data from entry fields
            business_name = business_name_entry.get()
            contact_name = contact_name_entry.get()
            email = email_entry.get()
            phone = phone_entry.get()
            status = status_entry.get()

            # Ensure all fields are filled
            if not all([business_name, contact_name, email, phone, status]):
                messagebox.showerror("Error", "All fields are required.")
                return

            try:
                # Pass all six parameters to update_contact
                update_contact(contact_id, business_name,
                               contact_name, email, phone, status)
                messagebox.showinfo("Success", "Contact updated successfully!")
                populate_contact_table()  # Refresh the table
                add_window.destroy()  # Close the update window
            except Exception as e:
                messagebox.showerror(
                    "Database Error", f"Failed to update contact: {e}")

        # Create the update contact window
        add_window = tk.Toplevel(root)
        add_window.title("spark - Update Contact")
        add_window.configure(padx=20, pady=20)

        # UI elements
        tk.Label(add_window, text="Business Name:").grid(
            row=0, column=0, padx=10, pady=5, sticky="e")
        business_name_entry = tk.Entry(add_window, font=font)
        business_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(add_window, text="Contact Name:").grid(
            row=1, column=0, padx=10, pady=5, sticky="e")
        contact_name_entry = tk.Entry(add_window, font=font)
        contact_name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(add_window, text="Email:").grid(
            row=2, column=0, padx=10, pady=5, sticky="e")
        email_entry = tk.Entry(add_window, font=font)
        email_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(add_window, text="Phone:").grid(
            row=3, column=0, padx=10, pady=5, sticky="e")
        phone_entry = tk.Entry(add_window, font=font)
        phone_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(add_window, text="Status:").grid(
            row=4, column=0, padx=10, pady=5, sticky="e")
        status_entry = tk.Entry(add_window, font=font)
        status_entry.grid(row=4, column=1, padx=10, pady=5)

        # Add button to submit the update
        tk.Button(
            add_window,
            text="Update Contact",
            command=update_selected_contact,
            padx=10,
            pady=5,
            font=font
        ).grid(row=5, column=0, columnspan=2, pady=20)

    def export_to_csv():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"),
                       #    ("Excel", "*.xlsx"),
                       #    ("JSON", "*.json"),
                       ("All files", "*.*")],
        )
        if file_path:
            try:
                with open(file_path, "w", newline="") as file:
                    writer = csv.writer(file)

                    if frames["Contacts"].winfo_ismapped():
                        writer.writerow(
                            [
                                "ID",
                                "Business Name",
                                "Contact Name",
                                "Email",
                                "Phone",
                                "Status",
                            ]
                        )
                        for row_id in table.get_children():
                            writer.writerow(table.item(row_id)["values"])
                    elif frames["Projects"].winfo_ismapped():
                        writer.writerow(
                            ["ID", "Project Name", "Email", "Phone", "Status"]
                        )
                        for row_id in proj_table.get_children():
                            writer.writerow(proj_table.item(row_id)["values"])
                    elif frames["Leads"].winfo_ismapped():
                        writer.writerow(
                            [
                                "ID",
                                "Business Name",
                                "Contact Name",
                                "Title",
                                "Email",
                                "Phone",
                                "Status",
                            ]
                        )
                        for row_id in lead_table.get_children():
                            writer.writerow(lead_table.item(row_id)["values"])
                    else:
                        messagebox.showwarning(
                            "Warning", "No active table to export data from."
                        )

                messagebox.showinfo("Success", "Data exported successfully!")
            except Exception as e:
                messagebox.showerror(
                    "Error", f"Failed to export data: {str(e)}")

    def populate_and_export():
        populate_contact_table()
        populate_lead_table()
        populate_account_table()
        populate_project_table()
        export_to_csv()

    root = tk.Tk()
    root.title("spark - Home")
    font = tkinter.font.Font(family="Ubuntu Light",
                             size=14,
                             weight="bold")
    font_menu = tkinter.font.Font(family="Ubuntu",
                                  size=10,
                                  underline=True)
    menubar = Menu(root, font=font_menu, cursor="plus")

    file = Menu(menubar, tearoff=False, font=font_menu, cursor="plus")
    menubar.add_cascade(label="File", menu=file)
    file.add_command(label="Save", command=populate_and_export)
    file.add_command(label="Exit", command=root.quit)

    edit = Menu(menubar, tearoff=False, font=font_menu, cursor="plus")
    menubar.add_cascade(label="Edit", menu=edit)
    edit.add_command(label="Cut")
    edit.add_command(label="Copy")
    edit.add_command(label="Paste")

    selection = Menu(menubar, tearoff=False, font=font_menu, cursor="plus")
    menubar.add_cascade(label="Selection", menu=selection)
    selection.add_command(label="Select All")

    view = Menu(menubar, tearoff=False, font=font_menu, cursor="plus")
    menubar.add_cascade(label="View", menu=view)
    view.add_command(label="Leads")
    view.add_command(label="Reports")

    root.configure(borderwidth=5, menu=menubar, cursor="plus")

    tabline = tk.Frame(root)
    tabline.grid(row=0, column=0, sticky="nsew")
    tabline.grid_propagate(False)

    tabs = [
        "Contacts",
        "Leads",
        "Projects",
        "Accounts",
        "Activities",
        "Services",
        "Reports",
    ]
    frames = {}

    for tab in tabs:
        btn = tk.Button(
            tabline,
            text=tab,
            command=lambda t=tab: switch_tab(t),
            padx=7,
            pady=3,
            cursor="plus",
            font=font
        )
        btn.pack(side="left", padx=1, pady=1)
        frames[tab] = tk.Frame(root)

    # Contacts
    contacts = frames["Contacts"]

    table = ttk.Treeview(
        contacts,
        columns=("ID", "Business Name", "Contact Name",
                 "Email", "Phone", "Status"),
        show="headings",
        selectmode='browse',
    )
    table.heading("ID", text="ID")
    table.heading("Business Name", text="Business Name")
    table.heading("Contact Name", text="Contact Name")
    table.heading("Email", text="Email")
    table.heading("Phone", text="Phone")
    table.heading("Status", text="Status")
    table.pack(fill="both", expand=True)

    button_frame = tk.Frame(contacts)
    button_frame.pack(pady=20)

    tk.Button(
        button_frame,
        text="Add Contact",
        command=add_contact_window,
        padx=5,
        pady=1,
        font=font
    ).pack(side="left", padx=5)
    tk.Button(
        button_frame,
        text="Update Contact",
        command=update_selected_contact_window,
        padx=5,
        pady=1,
        font=font
    ).pack(side="left", padx=5)
    tk.Button(
        button_frame,
        text="Delete Contact",
        command=delete_selected_contact,
        padx=5,
        pady=1,
        font=font
    ).pack(side="left", padx=5)
    tk.Button(
        button_frame, text="Export",
        command=populate_and_export,
        padx=5,
        pady=1,
        font=font
    ).pack(side="left", padx=5)
    tk.Button(
        button_frame,
        text="Reload Table",
        command=populate_contact_table,
        padx=5,
        pady=1,
        font=font
    ).pack(side="left", padx=5)

    # Accounts
    accounts = frames["Accounts"]

    acct_table = ttk.Treeview(
        accounts,
        columns=("ID", "Business Name", "Contact Name",
                 "Email", "Phone", "Status"),
        show="headings",
    )
    acct_table.heading("ID", text="ID")
    acct_table.heading("Business Name", text="Business Name")
    acct_table.heading("Contact Name", text="Contact Name")
    acct_table.heading("Email", text="Email")
    acct_table.heading("Phone", text="Phone")
    acct_table.heading("Status", text="Status")
    acct_table.pack(fill="both", expand=True)

    button_frame = tk.Frame(accounts)
    button_frame.pack(pady=20)

    tk.Button(
        button_frame,
        text="Add Account",
        command=add_account_window,
        padx=5,
        pady=1,
        font=font
    ).pack(side="left", padx=5)
    tk.Button(
        button_frame,
        text="Delete Account",
        command=delete_selected_account,
        padx=5,
        pady=1,
        font=font
    ).pack(side="left", padx=5)
    tk.Button(
        button_frame, text="Export",
        command=populate_and_export,
        padx=5,
        pady=1,
        font=font
    ).pack(side="left", padx=5)
    tk.Button(
        button_frame,
        text="Reload Table",
        command=populate_account_table,
        padx=5,
        pady=1,
        font=font
    ).pack(side="left", padx=5)
    # Projects
    projects = frames["Projects"]

    proj_table = ttk.Treeview(
        projects,
        columns=("ID", "Project Name", "Email", "Phone", "Status"),
        show="headings",
        selectmode='browse'
    )
    proj_table.heading("ID", text="ID")
    proj_table.heading("Project Name", text="Project Name")
    proj_table.heading("Email", text="Email")
    proj_table.heading("Phone", text="Phone")
    proj_table.heading("Status", text="Project Status")
    proj_table.pack(fill="both", expand=True)

    button_frame = tk.Frame(projects)
    button_frame.pack(pady=20)
    tk.Button(
        button_frame,
        text="Add Project",
        padx=5,
        pady=1,
        font=font
    ).pack(side="left", padx=5)
    tk.Button(
        button_frame,
        text="Delete Project",
        command=delete_selected_project,
        padx=5,
        pady=1,
        font=font
    ).pack(padx=5)

    # Leads
    leads = frames["Leads"]

    lead_table = ttk.Treeview(
        leads,
        columns=(
            "ID",
            "Business Name",
            "Contact Name",
            "Title",
            "Email",
            "Phone",
            "Status",
        ),
        show="headings",
        selectmode='browse',
    )
    lead_table.heading("ID", text="ID")
    lead_table.heading("Business Name", text="Business Name")
    lead_table.heading("Contact Name", text="Contact Name")
    lead_table.heading("Title", text="Title")
    lead_table.heading("Email", text="Email")
    lead_table.heading("Phone", text="Phone")
    lead_table.heading("Status", text="Lead Status")
    lead_table.pack(fill="both", expand=True)

    button_frame = tk.Frame(leads)
    button_frame.pack(pady=20)
    tk.Button(
        button_frame,
        text="Add Lead",
        command=add_lead_window,
        padx=5,
        pady=1,
        font=font
    ).pack(side="left", padx=5)
    tk.Button(
        button_frame,
        text="Delete Lead",
        command=delete_selected_lead,
        padx=5,
        pady=1,
        font=font
    ).pack(side="left", padx=5)
    tk.Button(
        button_frame,
        text="Export",
        command=populate_and_export,
        padx=5,
        pady=1,
        font=font
    ).pack(side="left", padx=5)
    tk.Button(
        button_frame,
        text="Reload Table",
        command=populate_contact_table,
        padx=5,
        pady=1,
        font=font
    ).pack(side="left", padx=5)

    # Reports
    reports = frames["Reports"]

    dashboard_frame = tk.Frame(reports)
    dashboard_frame.pack(fill="both", expand=True)

    tk.Label(
        dashboard_frame,
        text="Reports Dashboard",
    ).pack()
    tk.Label(
        dashboard_frame,
        text="Restart app to update charts.",
    ).pack()

    def save_chart():
        """Save the current chart to a file."""
        filename = filedialog.asksaveasfilename(
            initialfile="Untitled.png",
            defaultextension=".png",
            filetypes=[
                ("Portable Graphics Format", "*.png"),
                ("All Files", "*.*"),
            ],
        )
        if filename:
            try:
                plt.savefig(filename)
                tk.messagebox.showinfo("Success", f"Chart saved as {filename}")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to save chart: {e}")

    def generate_leads_status_pie_chart():
        """Generate a pie chart breaking down the status column of the leads table."""

        all_leads = fetch_leads()

        if all_leads == None:
            tk.messagebox.showinfo("Error", "There are no leads!")

        titles = [lead[6] for lead in all_leads if lead[6]]

        status_counts = Counter(titles)

        labels = status_counts.keys()
        sizes = status_counts.values()

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.pie(
            sizes,
            labels=labels,
            autopct='%1.1f%%',
            startangle=75,
            colors=plt.cm.Paired.colors,
            counterclock=False
        )
        ax.set_title("Leads Status Breakdown", fontsize=14)

        chart_widget = FigureCanvasTkAgg(fig, master=dashboard_frame)
        chart_widget.draw()
        chart_widget.get_tk_widget().pack()

        tk.Button(
            dashboard_frame,
            text="Save Chart",
            command=save_chart,
            fg="white",
        ).pack(pady=10)

    generate_leads_status_pie_chart()

    def generate_leads_titles_pie_chart():
        """Generate a pie chart breaking down the status column of the leads table."""

        all_leads = fetch_leads()

        if all_leads == None:
            tk.messagebox.showinfo("Error", "There are no leads!")

        titles = [lead[3] for lead in all_leads if lead[3]]

        status_counts = Counter(titles)

        labels = status_counts.keys()
        sizes = status_counts.values()

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.pie(
            sizes,
            labels=labels,
            autopct='%1.1f%%',
            startangle=75,
            colors=plt.cm.Paired.colors,
            counterclock=False
        )
        ax.set_title("Leads Titles Breakdown", fontsize=14)

        chart_widget = FigureCanvasTkAgg(fig, master=dashboard_frame)
        chart_widget.draw()
        chart_widget.get_tk_widget().pack()

        tk.Button(
            dashboard_frame,
            text="Save Chart",
            command=save_chart,
            fg="white",
        ).pack(pady=10)

    generate_leads_titles_pie_chart()

    # Theme
    sv_ttk.set_theme("dark")
    sv_ttk.use_dark_theme()
    populate_contact_table()
    populate_project_table()
    populate_lead_table()

    switch_tab("Contacts")
    root.resizable(False, False)
    root.mainloop()
