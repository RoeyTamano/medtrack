from tkinter import font
import pandas as pd
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import yagmail


name = None
name_list1 = []
drug_list = []
# Load the data
df = pd.read_csv("Drug.csv", header=0, usecols=["Drug", "Information", "Effective"])
drugs = df.Drug.unique()
drugs = list(drugs)

# Initialize CustomTkinter window
ctk.set_appearance_mode("system")  # "dark", "light", or "system"
ctk.set_default_color_theme("blue")  # Color theme
root = ctk.CTk()
root.title("MedTrack")
root.geometry("700x900")

page = 1

remind = {}

# Define global variables for the Entry and Label widgets
drug_entry = None
info_frame = None
name_entry = None
morning_list = []
afternoon_list = []
night_list = []

def next_page():
    global page
    page += 1
    show_page()

def reminder(choice, value):
    if choice == "Morning":
        morning_list.append(value)
    if choice == "Afternoon":
        morning_list.append(value)
    if choice == "Night":
        morning_list.append(value)

def search_drug():
    drug_name = drug_entry.get().strip()
    if drug_name in drugs:
        drug_info = df[df['Drug'] == drug_name].iloc[0]
        display_info(drug_info)
    else:
        messagebox.showinfo("Not Found", "The drug you entered is not in the database.")

def add_page():
    drug = drug_entry.get().strip()
    drug_list.append(drug)

def name_list():
    name = name_entry.get().strip()
    name_list1.append(name)
    print(name_list1)

def display_info(drug_info):
    for widget in info_frame.winfo_children():
        widget.destroy()
    info_frame.grid_columnconfigure(0, weight=1)
    drug_label = tk.Label(info_frame, text=f"Drug: {drug_info['Drug']}",
                          font=font.Font(family="welcome_font", size=16, weight="bold"))
    drug_label.grid(row=0, column=0, pady=(10, 5), sticky="nsew")  # Centering the label
    info_label = tk.Label(info_frame, text=f"Information: {drug_info['Information'].split('.')[0]}",
                          font=font.Font(family="welcome_font", size=17), wraplength=500, justify="center")
    info_label.grid(row=1, column=0, pady=(5, 10), padx=100, sticky="nsew")


yag = yagmail.SMTP('roitamano@gmail.com', 'jyhq bjds omap imgb')
def send_email(to_email, subject, body):
    yag.send(to=to_email, subject=subject, contents=body)

send_email('shakedmaliah@gmail.com', 'medication reminder test', 'dont forget your medication!')

def show_page():
    global page
    global drug_entry
    global info_frame
    global name_entry

    for widget in root.winfo_children():
        widget.destroy()

    if page == 1:
        welcome_label = ctk.CTkLabel(root, text="Welcome to", font=ctk.CTkFont(size=56, weight="bold"))
        welcome_label.pack(pady=(50, 10))

        medtrack_label = ctk.CTkLabel(root, text="MedTrack", font=ctk.CTkFont(size=52, weight="bold"),
                                      text_color="dark red")
        medtrack_label.pack(pady=(10, 10))

        description_label = ctk.CTkLabel(root, text="This app will make your life easier!",
                                         font=ctk.CTkFont(size=20, weight="bold"))
        description_label.pack(pady=(10, 20))

        info_label = ctk.CTkLabel(root, text=(
            "In our app, you can search information about medicines.\n\n"
            "A user who decides to take a medicine\n\n can enter it into the system.\n\n"
            "The app will remind you to take the medicine\n\n by sending a daily message\n\n"
            "about which medicine to take and when."
        ), font=ctk.CTkFont(size=20), justify="center")
        info_label.pack(pady=(20, 30))

        next_button = ctk.CTkButton(root, text="Next", font=ctk.CTkFont(size=24), command=next_page)
        next_button.pack(pady=5)

    elif page == 2:
        lon_in = ctk.CTkLabel(root, text="LOG IN ", font=ctk.CTkFont(size=56, weight="bold"))
        lon_in.pack(pady=(50, 10))
        lon_in1 = ctk.CTkLabel(root, text="Please fill in the following details in order to register!",
                               font=ctk.CTkFont(size=20, weight="bold"))
        lon_in1.pack(pady=(10, 20))
        lon_in1 = ctk.CTkLabel(root, text="Please enter your full name:", font=ctk.CTkFont(size=20, weight="bold"))
        lon_in1.pack(padx=(0, 250), pady=(10, 40))

        name_entry = ctk.CTkEntry(root, font=ctk.CTkFont(size=20))
        name_entry.pack(padx=(0, 400), pady=(10, 10))

        enter1_button = ctk.CTkButton(root, text="ENTER", font=ctk.CTkFont(size=24), command=name_list)
        enter1_button.pack(padx=(0, 400), pady=(10, 20))

        lon_in2 = ctk.CTkLabel(root, text="Please enter your email:", font=ctk.CTkFont(size=20, weight="bold"))
        lon_in2.pack(padx=(0, 300), pady=(10, 60))

        email_entry = ctk.CTkEntry(root, font=ctk.CTkFont(size=20))
        email_entry.pack(padx=(0, 400), pady=(10, 10))

        enter1_button = ctk.CTkButton(root, text="ENTER", font=ctk.CTkFont(size=24), command=search_drug)
        enter1_button.pack(padx=(0, 400), pady=(10, 20))

        next_button = ctk.CTkButton(root, text="Next", font=ctk.CTkFont(size=24), command=next_page)
        next_button.pack(pady=5)

    elif page == 3:
        title_label = ctk.CTkLabel(root, text="Search for a Drug", font=ctk.CTkFont(size=36))
        title_label.pack(pady=(50, 20))

        drug_entry = ctk.CTkEntry(root, font=ctk.CTkFont(size=20))
        drug_entry.pack(pady=(10, 20))

        search_button = ctk.CTkButton(root, text="Search", font=ctk.CTkFont(size=24), command=search_drug)
        search_button.pack(pady=(10, 30))

        info_frame = ctk.CTkFrame(root)
        info_frame.pack(pady=(0, 0))

        add_button = ctk.CTkButton(root, text="add", font=ctk.CTkFont(size=24), command=add_page)
        add_button.pack(pady=(10, 20))

        next_button = ctk.CTkButton(root, text="Next", font=ctk.CTkFont(size=24), command=next_page)
        next_button.pack(pady=(10, 20))
        progressbar = ctk.CTkProgressBar(root, orientation="horizontal")
        progressbar.pack()

    elif page == 4:
        schedule = ctk.CTkLabel(root, text="Choose your schedule", font=ctk.CTkFont(size=56, weight="bold"))
        schedule.pack(pady=(50, 10))

        schedule1 = ctk.CTkLabel(root,
                                 text="Enter the name of the medicine you need to take in at least one of the following options",
                                 font=ctk.CTkFont(size=32, weight="bold"), wraplength=500)
        schedule1.pack(pady=(50, 10))

        morning = ctk.CTkLabel(root, text="Enter the medicine you want to take",
                               font=ctk.CTkFont(size=22))
        morning.pack(pady=(50, 10))

        segemented_button = ctk.CTkSegmentedButton(root, values=drug_list)
        segemented_button.pack()

        combobox = ctk.CTkComboBox(root, values=["Morning", "Afternoon", "Night"])
        combobox.pack()

        enter1_button = ctk.CTkButton(root, text="ENTER", font=ctk.CTkFont(size=24), command=search_drug)
        enter1_button.pack(padx=(0,0), pady=(10, 20))


show_page()

root.mainloop()
