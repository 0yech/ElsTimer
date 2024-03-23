import tkinter as tk
import keyboard
import configparser


class CountdownApp:
    def __init__(self, master, time_limit):
        self.master = master
        self.master.title("")
        self.master.geometry("150x80")
        self.master.attributes('-alpha', 0.8)  # Set transparency level
        self.master.overrideredirect(True)  # Remove window decorations
        self.master.attributes('-topmost', 1)  # Window stays on top of other windows (doesn't apply in fullscreen)

        self.label = tk.Label(self.master, text="", font=("Helvetica", 20))
        self.label.pack(pady=20)

        self.time_limit = time_limit
        self.time_left = 0
        self.countdown_id = None  # To store the ID of the countdown after it starts

        # Bind the mouse events for moving the window
        self.master.bind("<B1-Motion>", self.drag)
        self.master.bind("<ButtonPress-1>", self.start_move)
        self.master.bind("<ButtonRelease-1>", self.stop_move)

        # Set focus to the window to ensure keyboard events are captured
        self.master.focus_force()

        config = configparser.ConfigParser()
        config.read("config.ini")
        self.key = config.get("Settings", "key", fallback="n")

        # Start listening for the configured key globally
        self.start_keyboard_listener()

        # Periodically check keyboard listener status
        self.check_keyboard_listener()

        # Initial display update
        self.update_display()

    def start_keyboard_listener(self):
        keyboard.on_press_key(self.key, self.restart_countdown)

    def stop_keyboard_listener(self):
        keyboard.unhook_all()

    def restart_countdown(self, event):
        # Cancel the existing countdown if it's running
        if self.countdown_id is not None:
            self.master.after_cancel(self.countdown_id)

        # Reset time left to the original time limit
        self.time_left = self.time_limit
        self.update_countdown()

    def update_countdown(self):
        if self.time_left > 0:
            minutes, seconds = divmod(self.time_left, 60)
            time_str = f"{minutes:02}:{seconds:02}"
            self.label.config(text=time_str)
            self.time_left -= 1
            self.countdown_id = self.master.after(1000, self.update_countdown)
        else:
            self.label.config(text="Spikes !")

    def update_display(self):
        if self.time_left > 0:
            minutes, seconds = divmod(self.time_left, 60)
            time_str = f"{minutes:02}:{seconds:02}"
            self.label.config(text=time_str)
        else:
            self.label.config(text="")

        self.master.after(1000, self.update_display)

    def check_keyboard_listener(self):
        # Checks every 5 secs if kb is still listening for inputs
	# Fixes timer not listening to inputs after some time
        if not keyboard.is_hooked(self.key):
            # Restart listener
            self.stop_keyboard_listener()
            self.start_keyboard_listener()

        # Time next check (5sec)
        self.master.after(5000, self.check_keyboard_listener)

    # Window movement
    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def drag(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.master.winfo_x() + deltax
        y = self.master.winfo_y() + deltay
        self.master.geometry(f"+{x}+{y}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownApp(root, 150)  # Change the time limit as needed
    root.mainloop()