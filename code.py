from pynput.mouse import Listener
import threading
import time
import pyautogui

# Global variables
mouse_pressed = False
vibration_triggered = False

def on_mouse_press(x, y, button, pressed):
    global mouse_pressed
    mouse_pressed = True

def on_mouse_release(x, y, button, pressed):
    global mouse_pressed, vibration_triggered
    if mouse_pressed and not vibration_triggered:
        mouse_pressed = False
        threading.Timer(10, trigger_vibration).start()

def trigger_vibration():
    global mouse_pressed, vibration_triggered
    if mouse_pressed:
        vibration_triggered = True
        pyautogui.moveTo(0, 0, duration=0.1)  # Move the mouse to the top-left corner
        pyautogui.moveTo(1, 0, duration=0.1)  # Move the mouse slightly to the right
        time.sleep(0.1)  # Pause for a short moment
        pyautogui.moveTo(0, 0, duration=0.1)  # Move the mouse back to the top-left corner
        vibration_triggered = False

# Start mouse listener
with Listener(on_press=on_mouse_press, on_release=on_mouse_release) as listener:
    listener.join()
