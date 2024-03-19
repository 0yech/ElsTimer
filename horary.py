import tkinter as tk
import keyboard
import configparser


class HoraryTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("")
        self.master.geometry("150x80")
        self.master.attributes('-alpha', 0.8)  # Set transparency level
        self.master.overrideredirect(True)  # Remove window decorations
        self.master.attributes('-topmost', 1)  # Window stays on top of other windows (doesn't apply in fullscreen)


        self.frame = tk.Frame(self.master, bg="SystemButtonFace", width=150, height=80)
        self.frame.pack_propagate(False)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.frame, text="", font=("Helvetica", 20), bg="SystemButtonFace", fg="white")
        self.label.pack(pady=20, fill=tk.BOTH, expand=True)

        self.time_left = 0
        self.countdown_id = None  # store the ID of the countdown after it starts

        # Bind the mouse events for moving the window
        self.master.bind("<B1-Motion>", self.drag)
        self.master.bind("<ButtonPress-1>", self.start_move)
        self.master.bind("<ButtonRelease-1>", self.stop_move)

        # Set focus to the window to ensure keyboard events are captured
        self.master.focus_force()

        config = configparser.ConfigParser()
        config.read("config.ini")
        self.key = config.get("Settings", "key", fallback="n")

        # Start listening for the "n" key globally
        keyboard.on_press_key(self.key, self.restart_countdown)

    def restart_countdown(self, event):
        self.time_left = 0  # Reset the time
        self.update_countdown()

    def update_countdown(self):
        minutes, seconds = divmod(self.time_left, 60)
        time_str = f"{minutes:02}:{seconds:02}"
        self.label.config(text=time_str)

        # Change background color based on time elapsed
        if self.time_left < 20:
            bg_color = "dark blue"
            text_color = "white"  # White text color for dark blue background
        elif self.time_left < 40:
            bg_color = "purple"
            text_color = "white"  # White text color for purple background
        elif self.time_left < 55:
            bg_color = "yellow"
            text_color = "black"  # Black text color for yellow background
        else:
            bg_color = "light blue"
            text_color = "black"  # White text color for light blue background

        self.master.config(bg=bg_color)
        self.frame.config(bg=bg_color)
        self.label.config(bg=bg_color, fg=text_color)  # Set text color based on background color

        self.time_left += 1

        # Restart the timer after 1 minute
        if self.time_left >= 60:
            self.time_left = 0

        # kill the previous timer
        if self.countdown_id:
            self.master.after_cancel(self.countdown_id)

        self.countdown_id = self.master.after(1000, self.update_countdown)

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
        self.master.geometry(f"150x80+{x}+{y}")

if __name__ == "__main__":
        root = tk.Tk()
        app = HoraryTimer(root)
        root.mainloop()