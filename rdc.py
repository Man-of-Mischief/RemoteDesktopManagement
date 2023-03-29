import os
import subprocess
from tkinter import *
from tkinter import messagebox

# ...

def open_mstsc(ip_address):
    subprocess.run(["mstsc", "/v:" + ip_address])

def show_software_list(software_list):
    message = "\n".join(software_list)
    messagebox.showinfo("Software List", message)

def open_baadal():
    subprocess.run(["mstsc"])

ip_addresses = ["10.223.52.52", "10.223.52.53", "10.223.52.54",
                "10.223.52.55", "10.223.52.56", "10.223.52.57", "10.223.52.59"]

software_lists = {
    "10.223.52.52": ["Anylogic", "Maplesoft", "Adobe CC", "Office 365", "Flexsim", "Smartdraw","NodeXL", "IBM Cplex", "SPSS", "Artelys Knitro", "Matlab"],
    "10.223.52.53": ["Anylogic", "Maplesoft", "Wolfram Mathematica", "Office 365", "Flexsim", "Smartdraw","NodeXL", "IBM Cplex", "SPSS", "Artelys Knitro", "Matlab", "Manifold"],
    "10.223.52.54": ["Anylogic", "Maplesoft", "Adobe CC", "Wolfram Mathematica", "Office 365", "Flexsim", "Smartdraw","NodeXL", "IBM Cplex", "SPSS", "Artelys Knitro", "Matlab", "Manifold"],
    "10.223.52.55": ["Rstudio Workbench Server", "Anylogic"],
    "10.223.52.56": ["Anylogic"],
    "10.223.52.57": ["MySQL", "Office 365"],
    "10.223.52.59": ["Office 365", "IBM Cplex", "Anaconda", "Matlab", "Flexsim", "SmartDraw", "SPSS", "NodeXL", "Adobe CC", "Artelys Knitro"],
}

root = Tk()
root.title("Remote Desktop")
root.geometry("800x500")
root.configure(background='#ffffff')

# Add header
header_font = ("Playball", 30, "italic", "bold")
header_label = Label(root, text= "REMOTE SERVER LOGIN", font=header_font, bg="#ffffff")
header_label.pack(pady=20)

frame = Frame(root, bg='#ffffff')
frame.pack(pady=20)

button_width = 25
button_height = 3
button_color = '#0D6EFD'
text_color = '#ffffff'
info_color = '#87CEFA'  # Lighter shade of button color

servers = ['Windows Server ' + str(i) for i in range(1, len(ip_addresses) + 1)]
servers[3] = 'Ubuntu Server 1'
servers[4] = 'Ubuntu Server 2'
servers[5] = 'Windows Server 4'
servers[6] = 'Windows Server 5'

# Create the buttons for each server
buttons = []
for i, server in enumerate(servers):
    ip_address = ip_addresses[i]

    # Create the server name button
    name_button = Button(frame, text=server + "\n(" + ip_address + ")", width=button_width, height=button_height,
                     bg=button_color, fg=text_color, font=("Arial", 12, "bold"),
                     command=lambda ip=ip_address: open_mstsc(ip), relief=RAISED, borderwidth=2, highlightthickness=2)
    buttons.append(name_button)

    # Create Baadal Login button
    baadal_button = Button(frame, text="Baadal Login", width=button_width, height=button_height,
                       bg=button_color, fg=text_color, font=("Arial", 12, "bold"),
                       command=open_baadal)

    # Create the info button for software list
    info_button = Button(frame, text="ℹ", width=button_height, height=button_height,
                     bg=button_color, fg=text_color, font=("Arial", 12, "bold"),
                     command=lambda software_list=software_lists[ip_address]: show_software_list(software_list), relief=RAISED, borderwidth=2, highlightthickness=2)
    buttons.append(info_button)

    # Set the border radius of info button to make it circular
    info_button.config(border=0, highlightthickness=0, bd=0)
    info_button.config(highlightbackground=info_color, highlightcolor=info_color)
    info_button.config(highlightthickness=1)

    # Set the position of buttons
    row = i // 2
    col = i % 2
    padx = 20
    pady = 10

    name_button.grid(row=row, column=col * 2, padx=padx, pady=pady)
    info_button.grid(row=row, column=col * 2 + 1, padx=padx, pady=pady)

    # Set the position of the Baadal Login button
    baadal_button.grid(row=len(ip_addresses) // 2, column=2, padx=padx, pady=pady)

    # Add the Baadal Login button to the list of buttons
    buttons.append(baadal_button)


# Add a footer on bottom
footer_font = ("Playball", 24, "bold italic")
footer_label = Label(root, text="Thank you, Come again", font=footer_font, bg="#ffffff")
footer_label.pack(side=BOTTOM, pady=20)

root.mainloop()

