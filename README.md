# Sliding Cat Desktop

Sliding Cat Desktop is the non-browser version of Sliding Cat Cursor. It runs as
a small desktop overlay on Windows or macOS and shows a cutout sliding cat when
your mouse cursor moves downward.

This open-source GitHub build uses the cutout cat image from the original viral
photo. Please verify image rights before commercial redistribution.

This is separate from the Chrome extension. It works on the operating system
desktop, not just inside browser pages.

## Download

[sliding-cat-desktop-v0.1.2.zip](dist/sliding-cat-desktop-v0.1.2.zip)

## Run on Windows

1. Install Python 3 if needed: https://www.python.org/downloads/windows/
2. Unzip this folder.
3. Double-click `run-windows.bat`.
4. Move the mouse downward.

Press `Esc` while the cat window is focused, or close the terminal window, to
stop the app.

## Run on macOS

1. Install Python 3 if needed: https://www.python.org/downloads/macos/
2. Unzip this folder.
3. Open Terminal in the folder.
4. Run:

```bash
chmod +x run-macos.command
./run-macos.command
```

macOS may ask for accessibility or automation permission depending on system
settings.

## Developer Notes

The app uses only Python standard library modules and Tkinter. It polls the
global pointer position and moves a transparent always-on-top window near the
cursor when movement is downward.

No user data is collected, transmitted, or stored.

The desktop image assets use hard transparency to avoid green fringe artifacts
on transparent desktop windows.

## Make A Native App

For a true `.exe`, `.app`, or `.dmg`, package this app with PyInstaller on each
target OS.

Windows:

```powershell
py -3 -m pip install pyinstaller
py -3 -m PyInstaller --noconsole --name SlidingCatDesktop --add-data "assets;assets" sliding_cat_desktop.py
```

macOS:

```bash
python3 -m pip install pyinstaller
python3 -m PyInstaller --windowed --name SlidingCatDesktop --add-data "assets:assets" sliding_cat_desktop.py
```

The app is intentionally small and dependency-free so native packaging can be
done later without changing the source.
