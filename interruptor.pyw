import tkinter as tk
import webbrowser
import random

MESSAGES = [
    {
        "text": "Are you using your time wisely?",
        "buttons": [
            {"label": "Dismiss", "action": "dismiss"},
            {"label": "Go to To-Do List", "action": "link", "url": "https://todoist.com"},
        ],
    },
    {
        "text": "Take a deep breath. Step back.",
        "buttons": [
            {"label": "OK", "action": "dismiss"}
        ],
    },
]

INTERVAL = 10000  # 10 seconds in milliseconds

def show_popup():
    message_config = random.choice(MESSAGES)
    
    root = tk.Tk()
    root.overrideredirect(True)
    root.configure(bg="black")  # background black
    root.attributes("-topmost", True)
    root.lift()  # bring window to front

    # Full screen
    ws, hs = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(f"{ws}x{hs}+0+0")

    # Message
    label = tk.Label(
        root,
        text=message_config["text"],
        bg="black",  # background black
        fg="white",  # text white
        font=("Segoe UI", 48),
        wraplength=ws - 100,
        justify="center"
    )
    label.pack(expand=True)

    # Buttons
    button_frame = tk.Frame(root, bg="black")  # frame background matches
    button_frame.pack(pady=50)

    def make_action(action, url=None):
        def inner():
            if action == "link" and url:
                webbrowser.open(url)
            root.destroy()
        return inner

    for b in message_config["buttons"]:
        btn = tk.Button(
            button_frame,
            text=b["label"],
            command=make_action(b["action"], b.get("url")),
            relief="flat",
            bg="#444444",  # dark gray button
            fg="white",
            padx=20,
            pady=10,
            font=("Segoe UI", 20)
        )
        btn.pack(side="left", padx=20)

    root.mainloop()

def schedule_next_popup():
    show_popup()
    root.after(INTERVAL, schedule_next_popup)

# Hidden root for scheduling
root = tk.Tk()
root.withdraw()
root.after(0, schedule_next_popup)
root.mainloop()
