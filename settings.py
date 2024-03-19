import tkinter as tk
from tkinter import Button, Entry
import configparser


class SettingsWindow:
    def __init__(self, master):
        # Settings window parameters
        self.master = master
        self.master.config(background="#222831")
        self.master.geometry("300x150")
        self.master.minsize(300, 150)
        self.master.title("Settings")

        # Render labels/entry/button
        self.label = tk.Label(master, text="Bind Key:", bg="#222831", fg="white")
        self.label.pack(pady=10)

        self.entry = Entry(master, bg="#31363F", fg="white", width=15)
        self.entry.pack()

        self.button = Button(master, text="Save", command=self.save_and_close)
        self.button.pack(pady=10)

        self.load_key()

    def load_key(self):
        # Load binded key in config.ini
        try:
            config = configparser.ConfigParser()
            config.read("config.ini")
            if "Settings" in config and "key" in config["Settings"]:
                self.entry.insert(0, config["Settings"]["key"])
        except FileNotFoundError:
            # If the config file doesn't exist, create it using the default bind
            self.create_default_config()

    def save_and_close(self):
        self.save_key()
        self.master.destroy()  # Close the settings window

    def save_key(self):
        key = self.entry.get()
        config = configparser.ConfigParser()
        config["Settings"] = {"key": key}
        with open("config.ini", "w") as configfile:
            config.write(configfile)  # Save key in config.ini

    def create_default_config(self):
        config = configparser.ConfigParser()
        config["Settings"] = {"key": "n"}  # Set default key to 'n'
        with open("config.ini", "w") as configfile:
            config.write(configfile)

if __name__ == "__main__":
    root = tk.Tk()
    app = SettingsWindow(root)
    root.mainloop()