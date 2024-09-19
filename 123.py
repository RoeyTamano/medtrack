# import pandas as pd
#
# #
# df = pd.read_csv("Drug.csv",
#                  header=0,
#                  usecols=["Drug", "Information", "Effective"])
# drags = df.Drug.unique()
# drags = list(drags)
# print(drags)
# drag_choice = ''
# drag_ind = drags.index("Azithromycin")
# print(df.loc[drag_ind + 1])
# print()
#
# # import sys module
# import pygame
# import sys
#
# # pygame.init() will initialize all
# # imported module
# pygame.init()
#
# clock = pygame.time.Clock()
#
# # it will display on screen
# screen = pygame.display.set_mode([600, 500])
#
# # basic font for user typed
# base_font = pygame.font.Font(None, 32)
# user_text = ''
#
# # create rectangle
# input_rect = pygame.Rect(200, 200, 140, 32)
#
# # color_active stores color(lightskyblue3) which
# # gets active when input box is clicked by user
# color_active = pygame.Color('lightskyblue3')
#
# # color_passive store color(chartreuse4) which is
# # color of input box.
# color_passive = pygame.Color('chartreuse4')
# color = color_passive
# lst = []
# active = False
#
# while True:
#     for event in pygame.event.get():
#
#         # if user types QUIT then the screen will close
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if input_rect.collidepoint(event.pos):
#                 active = True
#                 color = color_active
#             else:
#                 active = False
#                 color = color_passive
#
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_BACKSPACE:
#                 user_text = user_text[:-1]
#             else:
#                 user_text += event.unicode
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RETURN:
#                 drag_choice = user_text.strip()
#                 df = pd.read_csv("Drug.csv",
#                                  header=0,
#                                  usecols=["Drug", "Information", "Effective"])
#                 drags = list(df.Drug.unique())
#                 print(str(drag_choice) in drags)
#                 if drag_choice in drags:
#                     print("hh")
#                     drag_ind = drags.index(drag_choice)
#                     print(df.loc[drag_ind + 1])
#                     print()
#                     user_text = ''
#                     print(drag_choice)
#
#         screen.fill((255, 255, 255))
#         pygame.draw.rect(screen, color, input_rect)
#         text_surface = base_font.render(user_text, True, (255, 255, 255))
#         screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
#         input_rect.w = max(100, text_surface.get_width() + 10)
#
#     pygame.display.flip()

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


def search_drug():
    drug_name = drug_entry.get().strip()
    if drug_name in drugs:
        drug_info = df[df['Drug'] == drug_name].iloc[0]
        display_info(drug_info)
    else:
        messagebox.showinfo("Not Found", "The drug you entered is not in the database.")


def display_info(drug_info):
    # Clear the info frame
    for widget in info_frame.winfo_children():
        widget.destroy()

    # Center frame layout configuration
    info_frame.grid_columnconfigure(0, weight=1)

    # Display drug information in categories
    drug_label = tk.Label(info_frame, text=f"Drug: {drug_info['Drug']}",
                          font=font.Font(family="welcome_font", size=16, weight="bold"))
    drug_label.grid(row=0, column=0, pady=(10, 5), sticky="nsew")  # Centering the label

    info_label = tk.Label(info_frame, text=f"Information: {drug_info['Information'].split('.')[0]}",
                          font=font.Font(family="welcome_font", size=17), wraplength=500, justify="center")
    info_label.grid(row=1, column=0, pady=(5, 10), padx=100, sticky="nsew")


def show_page():
    global page
    global drug_entry
    global info_frame

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
        title_label = ctk.CTkLabel(root, text="Search for a Drug", font=ctk.CTkFont(size=36))
        title_label.pack(pady=(50, 20))

        drug_entry = ctk.CTkEntry(root, font=ctk.CTkFont(size=20))
        drug_entry.pack(pady=(10, 20))

        search_button = ctk.CTkButton(root, text="Search", font=ctk.CTkFont(size=24), command=search_drug)
        search_button.pack(pady=(10, 30))

        # Frame to display drug information
        info_frame = ctk.CTkFrame(root)
        info_frame.pack(pady=(0, 0))

        next_button = ctk.CTkButton(root, text="Next", font=ctk.CTkFont(size=24), command=next_page)
        next_button.pack(pady=250)


show_page()

root.mainloop()
