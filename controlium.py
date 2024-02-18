import os
import time
import telebot
import requests
import threading
import subprocess
from plyer import notification

pid = os.getpid()

notification.notify(
    title="Controlium",
    message=f'''Program running in the background
Process ID: {pid}''',
    app_icon=None,
    timeout=5,)

def telegram_alert(send):
    bot_token = "YOUR BOT TOEKN"
    my_chatID = "CHAT ID"
    send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + my_chatID + "&parse_mode=Markdown&text=" + send

    response = requests.get(send_text)
    return response.json()

def win_notification(message):
    msg = message.text
    notification.notify(
        title="Controlium Notification",
        message=msg,
        app_icon=None,
        timeout=5,)


bot = telebot.TeleBot("YOUR BOT TOKEN")
@bot.message_handler(func=lambda message: True)

def command_engine(message):
    
    if message.text.lower() == "stop":
        bot.reply_to(message, "System Stopped")
        subprocess.run(["taskkill", "/F", "/PID", str(pid)])

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

    elif message.text.lower() == "alert":
        bot.reply_to(message, "Enter notification messeage")
        bot.register_next_step_handler(message, win_notification)
    

    else:
        bot.reply_to(message, "Invalid Command")





bot.polling()
