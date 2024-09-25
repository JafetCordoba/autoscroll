import pyautogui
import time

def auto_scroll(scroll_amount, interval, duration, delay_before_scroll):
    """
    Automatically scrolls the active window after a delay.
    
    Parameters:
    scroll_amount: Number of clicks to scroll (positive for up, negative for down).
    interval: Time in seconds between each scroll.
    duration: Total duration to keep scrolling in seconds.
    delay_before_scroll: Time in seconds to wait before starting the scroll.
    """
    print(f"Waiting {delay_before_scroll} seconds before starting the scroll...")
    time.sleep(delay_before_scroll)  # Delay before scrolling starts
    
    start_time = time.time()
    print("Starting scroll...")

    while time.time() - start_time < duration:
        pyautogui.scroll(scroll_amount)
        time.sleep(interval)

# Example usage: Scroll down by 5 "clicks" every 0.5 seconds for 10 seconds after a 10-second delay.
auto_scroll(scroll_amount=-5, interval=0.5, duration=10, delay_before_scroll=10)
