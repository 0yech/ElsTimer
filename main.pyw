import ctypes
import os
import sys
import traceback
from tkinter import *
from tkinter import Button, Toplevel
from timer import CountdownApp
from horary import HoraryTimer
from settings import SettingsWindow
from info import InfoWindow


def Timer(time_limit):
    try:
        root_e = Toplevel()  # Create Top-Level window
        app = CountdownApp(root_e, time_limit)  # Instantiate Timer App
        root_e.mainloop()
    except Exception as e:
        traceback.print_exc()  # Print exception traceback

def Horary():
    try:
        root_e = Toplevel()  # Create Top-Level window
        app = HoraryTimer(root_e)  # Instantiate Horary Timer App
        root_e.mainloop()
    except Exception as e:
        traceback.print_exc()  # Print the exception traceback

def Open_settings():
    try:
        root_e = Toplevel()  # Create Top-Level window
        app = SettingsWindow(root_e)  # Instantiate Settings Window
        root_e.mainloop()
    except Exception as e:
        traceback.print_exc()  # Print the exception traceback

def Open_info():
    try:
        root_e = Toplevel()  # Top-Level window
        app = InfoWindow(root_e)  # Instantiate Info Window
        root_e.mainloop()
    except Exception as e:
        traceback.print_exc()  # Print the exception traceback

def create_default_config():
    if not os.path.exists("config.ini"):
        with open("config.ini", "w") as configfile:
            configfile.write("[Settings]\nkey=n\n")

def main():

    # Call config.ini creation function
    create_default_config()


    # Timers and durations (Seconds)
    times = {"CM_Rosso": 150, "CM_Berthe": 90}

    # Styles
    c1 = "#222831"
    c2 = "#31363F"
    c3 = "#76ABAE"
    ct = "WHITE"
    cbt = "BLACK"

    # Main Window parameters
    window = Tk()
    window.title("ElsTimer")
    window.geometry("500x500")
    window.minsize(500, 500)
    window.config(background=c1)

    # Main Frame
    frame = Frame(window, bg=c1)

    label_title = Label(frame, text="ElsTimer", font=("Arial", 40), bg=c1, foreground=ct)
    label_title.pack()

    # Check if the script is run with administrative privileges
    # Show warning if not
    if not ctypes.windll.shell32.IsUserAnAdmin():
        label_perm = Label(frame, text="Warning /!\ Run tool as admin to enable overlay capability", font=("Arial", 10), bg=c1, foreground=ct)
        label_perm.pack()


    # Buttons
    # Timer buttons are set in their own for loop
    button_data = [
        {"text": "Info", "command": Open_info},
    {"text": "Settings", "command": Open_settings}
    ]
    
    # Menu Buttons loop and parameters
    for buttons in button_data:
        button = Button(
            frame,
            text=buttons["text"],
            font=("Arial"),
            border=0,
            bg=c3,
            foreground=cbt,
            padx=3,
            pady=4,
            command=buttons["command"]
        )
        button.pack(pady=10, fill=X)

    # Celestia Timer Button parameters
    button_cl = Button(
        frame,
        text=f"Open Celestia/Horary Timer",
        font=("Arial"),
        border=0,
        bg=c3,
        foreground=cbt,
        padx=3,
        pady=4,
        command=Horary)

    button_cl.pack(pady=10, fill=X)

    # Custom Timers loop and parameters
    for timer_name, time_limit in times.items():
        button = Button(
            frame,
            text=f"Open {timer_name} Timer",
            font=("Arial"),
            border=0,
            bg=c3,
            foreground=cbt,
            padx=3,
            pady=4,
            command=lambda time_limit=time_limit: Timer(time_limit))

        button.pack(pady=10, fill=X)

    # Render Frame
    frame.pack(expand=YES)

    window.mainloop()


if __name__ == "__main__":
        main()