@echo off
setlocal
cd /d "%~dp0"
py -3 sliding_cat_desktop.py
if errorlevel 1 (
  python sliding_cat_desktop.py
)
