import webview
import subprocess
import sys
import time
import ctypes
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

process = subprocess.Popen([
    sys.executable,
    "-m",
    "streamlit",
    "run",
    "main.py",
    "--server.headless", "true",
    "--server.runOnSave", "false"  # disable auto-reloader
])
time.sleep(2)

webview.create_window("AgroBoard [Client]", "http://localhost:8080",resizable=True, maximized=True, min_size=(screen_width, screen_height))
webview.start(icon="/logo.png",)

process.terminate()
sys.exit()
