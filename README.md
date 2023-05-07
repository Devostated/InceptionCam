# Inception-Cam
An HLAE tool to create inception cam transitions.

# Usage
* Record and save the first campath.
* Use the ingame command `getpos` at the position where you want the campath to happen.
* Drag and drop the saved campath onto the InceptionCam.exe
* Enter your `getpos` value 
   - Format examples:
      - `setpos -2160.120361 644.429016 12535.342773;setang 0.000000 -157.500000 0.000000`
      - `setpos -2160.120361 644.429016 12535.342773`
      - `-2160.120361 644.429016 12535.342773`
* Load campath


# Example
https://user-images.githubusercontent.com/30211694/236698283-f6287fd1-6eeb-4d46-a0a0-5bc67fdb2768.mp4

Inspired by [Ganymede by Gmzorz](https://youtu.be/OKpI_Ea48Wo) using his [documentation](http://gmzorz.com/inception).

# Build
Build it using PyInstaller
```
pyinstaller.exe --onefile --windowed --add-data="images/HLAELauncher.ico;images" --noconsole --icon=images/HLAELauncher.ico inception.py
```

# Requirements
```
PySimpleGUI
PyInstaller
```
