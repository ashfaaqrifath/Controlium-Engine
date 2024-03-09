import subprocess
import importlib

packages = ["psutil", "pyperclip", "telebot", "requests", "winshell", "webbrowser", "pyttsx3", "pygetwindow", "pynput", "plyer"]

for pkg in packages:
    if importlib.util.find_spec(pkg) is None:
        subprocess.check_call(["pip", "install", pkg])
        print("Installed packages")
    else:
        pass