import pyautogui
import time

def auto_scroll(scroll_amount, interval, duration):
    """
    Automatically scrolls the active window.
    
    Parameters:
    scroll_amount: Number of clicks to scroll (positive for up, negative for down).
    interval: Time in seconds between each scroll.
    duration: Total duration to keep scrolling in seconds.
    """
    start_time = time.time()

    while time.time() - start_time < duration:
        pyautogui.scroll(scroll_amount)
        time.sleep(interval)
        # Adjust for desired behavior, e.g., clicking a window or focusing on it

# Example usage: Scroll down by 5 "clicks" every 0.5 seconds for 10 seconds.
auto_scroll(-5, 0.5, 10)
