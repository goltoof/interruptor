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

INTERVAL = 10000  # 10 seconds for testing

def show_popup():
    message_config = random.choice(MESSAGES)
    
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.lift()
    ws, hs = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(f"{ws}x{hs}+0+0")

    # Create canvas for semi-transparent background
    canvas = tk.Canvas(root, width=ws, height=hs, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # Draw a semi-transparent rectangle (simulate alpha using a dark gray)
    # Tkinter doesn't support true per-widget alpha, so we fake it with color
    canvas.create_rectangle(0, 0, ws, hs, fill="#000000", stipple="gray50")  # ~50% opaque

    # Place fully opaque message
    label = tk.Label(
        root,
        text=message_config["text"],
        bg="#000000",  # background matches canvas color
        fg="white",
        font=("Segoe UI", 48),
        wraplength=ws - 100,
        justify="center"
    )
    label.place(relx=0.5, rely=0.4, anchor="center")

    # Buttons
    button_frame = tk.Frame(root, bg="#000000")
    button_frame.place(relx=0.5, rely=0.7, anchor="center")

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
            bg="#444444",  # solid dark gray
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
