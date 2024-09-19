from tkinter import font
import pandas as pd
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, ttk
import yagmail
from tkcalendar import DateEntry
import schedule
import time
import threading

name = None
email = None
email_list1 = []
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
    global info_frame, reminder_time, reminder_minute, reminder_date

    # Clear the info frame
    for widget in info_frame.winfo_children():
        widget.destroy()

    # Center frame layout configuration
    info_frame.grid_columnconfigure(0, weight=1)

    drug_label = tk.Label(info_frame, text=f"Drug: {drug_info['Drug']}",
                          font=font.Font(family="welcome_font", size=16, weight="bold"))
    drug_label.grid(row=0, column=0, pady=(10, 5), sticky="nsew")
    info_label = tk.Label(info_frame, text=f"Information: {drug_info['Information'].split('.')[0]}",
                          font=font.Font(family="welcome_font", size=17), wraplength=500, justify="center")
    info_label.grid(row=1, column=0, pady=(5, 10), padx=100, sticky="nsew")

    effective_label = tk.Label(info_frame, text=f"Effective: {drug_info['Effective']}",
                               font=font.Font(family="welcome_font", size=14))
    effective_label.grid(row=2, column=0, pady=(5, 10), sticky="nsew")

    # Add reminder controls
    time_label = tk.Label(info_frame, text="Set Reminder Time:", font=font.Font(family="welcome_font", size=14))
    time_label.grid(row=3, column=0, pady=(5, 10), sticky="nsew")

    reminder_time = tk.StringVar()
    reminder_minute = tk.StringVar()

    menu_font = font.Font(family="welcome_font", size=10)

    time_options = [f"{i:02d}" for i in range(24)]
    minute_options = [f"{i:02d}" for i in range(60)]


    reminder_time = ttk.Combobox(info_frame, values=time_options, font=menu_font, width=2)
    reminder_time.set("00")  # ברירת מחדל לשעה
    reminder_time.grid(row=4, column=0, padx=200, pady=(10, 5), sticky="w")


    reminder_minute = ttk.Combobox(info_frame, values=minute_options, font=menu_font, width=2)
    reminder_minute.set("00")  #
    reminder_minute.grid(row=4, column=0, padx=(5, 10), sticky="e")

    date_label = tk.Label(info_frame, text="Set Date (Optional):", font=font.Font(family="welcome_font", size=14),
                          wraplength=200)
    date_label.grid(row=5, column=0, pady=(20, 10), sticky="nsew")

    reminder_date = DateEntry(info_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    reminder_date.grid(row=6, column=0, pady=(10, 20), sticky="nsew")

    reminder_button = tk.Button(info_frame, text="Set Reminder", command=lambda: set_reminder(drug_info['Drug']))
    reminder_button.grid(row=7, column=0, pady=(20, 20), sticky="nsew")


def send():
    yag = yagmail.SMTP('roitamano@gmail.com', '**********')

    def send_email(to_email, subject, body):
        yag.send(to=to_email, subject=subject, contents=body)

    send_email("roitamano@gmail.com", 'medication reminder test', 'dont forget your medication!')


def set_reminder(drug_name):
    global reminder_time, reminder_minute, reminder_date

    hour = reminder_time.get()
    minute = reminder_minute.get()
    if not hour or not minute:
        messagebox.showerror("Error", "Please select both hour and minute for the reminder.")
        return

    time_str = f"{int(hour):02d}:{int(minute):02d}"

    date_str = reminder_date.get_date() if reminder_date else ""

    schedule_reminder(drug_name, time_str, date_str)
    messagebox.showinfo("Reminder Set",
                        f"Reminder set for {drug_name} at {time_str} on {date_str if date_str else 'daily'}.")
    send()


def schedule_reminder(drug_name, time_str, date_str):
    try:
        schedule.every().day.at(time_str).do(send_reminder, drug_name=drug_name)
    except schedule.ScheduleValueError as e:
        messagebox.showerror("Schedule Error", f"Invalid time format: {time_str}. Please enter a valid time.")
        print(e)


def send_reminder(drug_name):
    messagebox.showerror("Schedule Error", f"Dont forget to take your medicn {drug_name}")
    print(f"Reminder: Time to take {drug_name}!")
    send()


def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)


def show_page():
    global page
    global drug_entry
    global info_frame
    global name_entry
    global email_entry

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

        enter1_button = ctk.CTkButton(root, text="ENTER", font=ctk.CTkFont(size=24))
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


schedule_thread = threading.Thread(target=run_schedule, daemon=True)
schedule_thread.start()

show_page()

root.mainloop()
