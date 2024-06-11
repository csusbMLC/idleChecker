from pynput import keyboard, mouse
from datetime import datetime, timedelta
import threading
import os
import tkinter as tk
from tkinter import messagebox

idle_threshold = timedelta(seconds=5)  # Set the idle threshold to 5 minutes
warning_threshold = timedelta(seconds=4)  # Set the warning threshold to 4 minutes
last_activity_time = datetime.now()
warning_shown = False

def on_activity():
    global last_activity_time, warning_shown
    last_activity_time = datetime.now()
    warning_shown = False  # Reset the warning flag on activity

def on_press(key):
    on_activity()

def on_move(x, y):
    on_activity()

def on_click(x, y, button, pressed):
    on_activity()

def show_warning_popup():
    def popup():
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        messagebox.showwarning("Inactivity Warning", "You will be logged out in 1 minute due to inactivity.")
        root.destroy()
    
    popup_thread = threading.Thread(target=popup)
    popup_thread.start()

def log_out_user():
    # For Windows, use the shutdown command with the /l flag to log out
    if os.name == 'nt':
        os.system('shutdown /l')
    # For Linux, use the logout command (this may vary depending on the environment)
    elif os.name == 'posix':
        os.system('pkill -KILL -u $USER')
    else:
        print("Logout command not supported on this OS")

def check_idle():
    global last_activity_time, warning_shown
    while True:
        idle_time = datetime.now() - last_activity_time
        if idle_time > idle_threshold:
            print("User is idle, logging out...")
            log_out_user()
            break  # Exit the loop after logging out
        elif idle_time > warning_threshold and not warning_shown:
            print("User is idle, showing warning...")
            warning_shown = True
            show_warning_popup()
        else:
            print("User is active")
        threading.Event().wait(1)  # Check every 10 seconds

keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click)

keyboard_listener.start()
mouse_listener.start()

idle_checker = threading.Thread(target=check_idle)
idle_checker.daemon = True  # Allow thread to exit when main program exits
idle_checker.start()

keyboard_listener.join()
mouse_listener.join()

