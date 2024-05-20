# Playing Minecraft with Subway Surfers
- Link to the video demonstration: [[https://youtu.be/GARhnWDKDCA]](https://youtu.be/CUsOjA9R1mE)

## Prerequisites: 
- Download Python3 (Coding Language)
- Download [BlueStacks](https://www.bluestacks.com/download.html) (Android Emulator) 
- Download `main.py`
- Download and Extract [Android Debug Bridge](https://dl.google.com/android/repository/platform-tools-latest-windows.zip) (To Connect Code to the Andriod Emulator)

## Running the Code
1. Download Subway Surfers on BlueStacks
2. In BlueStacks Advanced Settings, turn on Android Debug Bridge 
    * ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png) **The message below this setting warns that outside code can connect to your Android Emulator. My code will be connecting to your Android Emulator. DO NOT RUN MY CODE IF THAT MAKES YOU UNCOMFORTABLE. PLEASE DO YOUR OWN RESEARCH BEFORE RUNNING MY CODE OR ANYONE ELSE'S CODE ON YOUR MACHINE** ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)
    * Always turn this setting off as soon as you're done playing (then turn it back on to play next time)
3. Add `main.py` to the folder where you extracted Android Debug Bridge
4. Run `main.py` (run `python3 main.py` on the command line)
    - If you need to change the keybinds, I've commented where you can change the keybinds in `main.py`. For example, change `'s'` to `'t'` if you'd like to make `t` the roll button.

## Troubleshooting
- Run `adb kill-server` then `adb start-server` to restart the server
- Run `adb connect 127.0.0.1:5555`
- Ensure you turned the Debug Bridge back on in the BlueStacks Advanced Settings
- Look at this more detailed, better made tutorial on running BlueStacks on your machine. If it works, my code should also work: https://github.com/Pbatch/ClashRoyaleBuildABot/wiki/Setup
