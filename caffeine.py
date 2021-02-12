# caffeine.py
import pyautogui
from time import sleep, time
from datetime import timedelta
import subprocess


def main():
    print("Caffeine running\nBreak with Ctrl+C\n")
    Dt = timedelta(minutes=3, seconds=59)
    print("Wait interval is", Dt)
    t0 = time()
    while True:
        # Print time running
        time_running = timedelta(seconds=round(time() - t0))
        print(f"\rTime running: {time_running}", end='')
       sleep(Dt.total_seconds())

        # Press Shift to stay awake
        pyautogui.press("shift")

        # Ping network to keep VPN alive
        s = subprocess.run(["ping", "solon.prd"], capture_output=True)
        if s.returncode:
            print("\nPing solon.prd failed.\n")


if __name__ == "__main__":
    # Als er iets mis gaat, wil ik het kunnen zien
    try:
        main()
    finally:
        input("\n\nPress any key to quit...\n")
