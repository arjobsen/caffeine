# Caffeine
Voor slaperige computers.

## Download voor Windows
Download caffeine.exe [hier](www.google.com). Dubbelklik om uit te voeren.

## Ontwikkel
Clone deze repo en installeer de benodigde packages in een virtual environment.
```
git clone https://github.com/arjobsen/caffeine
python3 -m venv venv
source venv/bin/activate
pip install pyautogui requests pyinstaller
```

Voer uit met `python caffeine.py`.

Bouw de executables met `pyinstaller.exe --onefile caffeine.py`.