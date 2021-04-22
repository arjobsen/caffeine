# caffeine.py
def main():
    from time import sleep
    from datetime import datetime, timedelta
    import pyautogui
    import requests
    import traceback


    print(r"""
                __  __      _            
      ___ __ _ / _|/ _| ___(_)_ __   ___ 
     / __/ _` | |_| |_ / _ \ | '_ \ / _ \
    | (_| (_| |  _|  _|  __/ | | | |  __/
     \___\__,_|_| |_|  \___|_|_| |_|\___|
    
    """)
    print("Gestart op", datetime.now().strftime("%H:%M"))
    Dt = timedelta(minutes=0, seconds=59)
    print("Klikt op [shift] met interval", Dt)
    print("\nStop met Ctrl+C\n")
    while True:
        # Press a button to stay awake
        pyautogui.press("shift")

        # Ping network to keep VPN alive - not tested
        try:
            requests.get("https://google.com")
        except:
            pass

        # Wacht
        sleep(Dt.total_seconds())


if __name__ == "__main__":
    # Als er iets mis gaat, wil ik het kunnen zien
    try:
        main()
    except Exception:
        # Doe dit niet voor KeyboardInterrupt
        print("Error. Maak aub een screenshot van onderstaande foutmelding\n")
        traceback.print_exc()
    finally:
        input("\n\nPress any key to quit...\n")
