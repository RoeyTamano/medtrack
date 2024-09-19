from tkinter import font
import pandas as pd
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox


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

# Define global variables for the Entry and Label widgets
drug_entry = None
info_frame = None


def next_page():
    global page
    page += 1
    show_page()



def show_page():
    global page
    global drug_entry
    global info_frame

    # Clear the frame
    for widget in root.winfo_children():
        widget.destroy()

    if page == 1:
        # Welcome page
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




# Initial display of the welcome page
show_page()

# Start the Tkinter main loop
root.mainloop()