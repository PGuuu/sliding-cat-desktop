import argparse
import os
import platform
import sys
import tkinter as tk
from pathlib import Path


APP_NAME = "Sliding Cat Desktop"
ASSET_DIR = Path(__file__).resolve().parent / "assets"


class SlidingCatApp:
    def __init__(self, sensitivity=3, offset_x=18, offset_y=16):
        self.sensitivity = sensitivity
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.last_x = None
        self.last_y = None
        self.visible = False
        self.hide_after_ticks = 0
        self.poll_ms = 16

        self.root = tk.Tk()
        self.root.title(APP_NAME)
        self.root.withdraw()
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)

        self.transparent_color = "#00ff01"
        self.bg_color = self._background_color()
        self.root.configure(bg=self.bg_color)
        self._set_transparency()

        self.right_img = tk.PhotoImage(file=str(ASSET_DIR / "cat-right-150.png"))
        self.left_img = tk.PhotoImage(file=str(ASSET_DIR / "cat-left-150.png"))
        self.label = tk.Label(
            self.root,
            image=self.right_img,
            bg=self.bg_color,
            borderwidth=0,
            highlightthickness=0,
        )
        self.label.pack()

        self.root.bind("<Escape>", lambda _event: self.quit())
        self.root.protocol("WM_DELETE_WINDOW", self.quit)

    def _background_color(self):
        if platform.system().lower() == "darwin":
            return "systemTransparent"
        return self.transparent_color

    def _set_transparency(self):
        system = platform.system().lower()
        try:
            if system == "windows":
                self.root.attributes("-transparentcolor", self.transparent_color)
            elif system == "darwin":
                self.root.attributes("-transparent", True)
            else:
                self.root.attributes("-alpha", 0.96)
        except tk.TclError:
            self.root.attributes("-alpha", 0.96)

    def pointer(self):
        return self.root.winfo_pointerx(), self.root.winfo_pointery()

    def show_cat(self, x, y, moving_left):
        self.label.configure(image=self.left_img if moving_left else self.right_img)

        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        img_w = self.left_img.width()
        img_h = self.left_img.height()
        win_x = max(0, min(screen_w - img_w, x + self.offset_x))
        win_y = max(0, min(screen_h - img_h, y + self.offset_y))

        self.root.geometry(f"{img_w}x{img_h}+{win_x}+{win_y}")
        if not self.visible:
            self.root.deiconify()
            self.visible = True
        self.hide_after_ticks = 8

    def hide_cat(self):
        if self.visible:
            self.root.withdraw()
            self.visible = False

    def tick(self):
        x, y = self.pointer()
        if self.last_x is None:
            self.last_x = x
            self.last_y = y
            self.root.after(self.poll_ms, self.tick)
            return

        dx = x - self.last_x
        dy = y - self.last_y
        self.last_x = x
        self.last_y = y

        if dy >= self.sensitivity:
            self.show_cat(x, y, dx < 0)
        elif dy < 0:
            self.hide_cat()
        elif self.hide_after_ticks > 0:
            self.hide_after_ticks -= 1
            if self.hide_after_ticks == 0:
                self.hide_cat()

        self.root.after(self.poll_ms, self.tick)

    def run(self):
        self.root.after(self.poll_ms, self.tick)
        self.root.mainloop()

    def quit(self):
        self.root.destroy()


def parse_args():
    parser = argparse.ArgumentParser(description=APP_NAME)
    parser.add_argument("--sensitivity", type=int, default=3, help="Downward pixels needed to show the cat.")
    return parser.parse_args()


def main():
    os.chdir(Path(__file__).resolve().parent)
    args = parse_args()
    app = SlidingCatApp(sensitivity=args.sensitivity)
    app.run()


if __name__ == "__main__":
    sys.exit(main())
