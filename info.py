import tkinter as tk


class InfoWindow:
    def __init__(self, master):
        # Info window parameters
        self.master = master
        self.master.config(background="#222831")
        self.master.geometry("420x220")
        self.master.minsize(420, 220)
        self.master.title("Info")

        # Render labels
        self.label1 = tk.Label(master, text="This tool was made to help with 12-7-3 spikes, 15-6-1 giant spikes and Celestia's Horary.", bg="#222831", fg="white", font=("Arial"), wraplength=380)
        self.label1.pack(pady=(20, 5))

        self.label2 = tk.Label(master, text="The tool must be run as admin to listen inputs on top of the game. It cannot be used while Elsword is in fullscreen.", bg="#222831", fg="white", font=("Arial"), wraplength=380)
        self.label2.pack(pady=(0, 20))

        self.label2 = tk.Label(master, text="Discord : Cheyo", bg="#222831", fg="white", font=("Arial"), wraplength=380)
        self.label2.pack(pady=(0, 20))

if __name__ == "__main__":
    root = tk.Tk()
    app = InfoWindow(root)
    root.mainloop()