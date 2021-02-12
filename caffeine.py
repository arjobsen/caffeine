import pyautogui
import time
import sys

pyautogui.FAILSAFE = False

# Get interval (seconds) from CLI argument
if len(sys.argv) > 1:
    interval = float(sys.argv[1])
else:
    interval = 60
print("Interval set:", str(interval), "sec")

i = 0
print("Break with Ctrl+C")
while True:
    #pyautogui.moveTo(100, 100, duration=1)
    #pyautogui.moveRel(0, 50, duration=1)
    #pyautogui.press('volumeup')
    time.sleep(1)
    #pyautogui.press('volumedown')
    pyautogui.press('shift')
    time.sleep(interval)
    i -= -1
    print("\r" + str(i), end='')
