import pyautogui
import time
import tkinter as tk
from tkinter import messagebox

# Flag to control scrolling
is_scrolling = False

# Function to handle scrolling with delay
def auto_scroll(scroll_amount, interval, duration, delay_before_scroll):
    global is_scrolling
    is_scrolling = True  # Set flag to True when scrolling starts
    time.sleep(delay_before_scroll)  # Delay before scrolling starts
    
    start_time = time.time()

    while time.time() - start_time < duration:
        if not is_scrolling:  # Stop scrolling if the flag is set to False
            break
        pyautogui.scroll(scroll_amount)
        time.sleep(interval)

# Function to start the scroll when the button is clicked
def start_scroll():
    global is_scrolling
    if is_scrolling:
        messagebox.showinfo("Info", "Scrolling is already running.")
        return
    
    try:
        scroll_amount = int(scroll_amount_entry.get())
        interval = float(interval_entry.get())
        duration = float(duration_entry.get())
        delay = float(delay_entry.get())

        messagebox.showinfo("Scrolling", "Scroll will start after the delay.")
        auto_scroll(scroll_amount, interval, duration, delay)
        
        if is_scrolling:  # Only show if scrolling completes naturally
            messagebox.showinfo("Done", "Scrolling has finished.")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# Function to stop the scroll when the button is clicked or hotkey is pressed
def stop_scroll():
    global is_scrolling
    is_scrolling = False  # Set flag to False to stop scrolling
    messagebox.showinfo("Stopped", "Scrolling has been stopped.")

# Function to bind the 'S' key to stop the scroll
def on_key_press(event):
    if event.keysym == 'S':
        stop_scroll()

# Create the GUI window
window = tk.Tk()
window.title("Auto Scroll Script")

# Scroll amount input
tk.Label(window, text="Scroll Amount:").grid(row=0, column=0, padx=10, pady=5)
scroll_amount_entry = tk.Entry(window)
scroll_amount_entry.grid(row=0, column=1, padx=10, pady=5)

# Interval input
tk.Label(window, text="Interval (seconds):").grid(row=1, column=0, padx=10, pady=5)
interval_entry = tk.Entry(window)
interval_entry.grid(row=1, column=1, padx=10, pady=5)

# Duration input
tk.Label(window, text="Duration (seconds):").grid(row=2, column=0, padx=10, pady=5)
duration_entry = tk.Entry(window)
duration_entry.grid(row=2, column=1, padx=10, pady=5)

# Delay before scroll input
tk.Label(window, text="Delay Before Scroll (seconds):").grid(row=3, column=0, padx=10, pady=5)
delay_entry = tk.Entry(window)
delay_entry.grid(row=3, column=1, padx=10, pady=5)

# Start button to trigger the scroll
start_button = tk.Button(window, text="Start Scroll", command=start_scroll)
start_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Stop button to stop the scroll
stop_button = tk.Button(window, text="Stop Scroll", command=stop_scroll)
stop_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Bind the 'S' key to stop the scroll
window.bind('<KeyPress>', on_key_press)

# Run the GUI loop
window.mainloop()
