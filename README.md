# Controlium Engine

A Python-based remote system monitoring and control tool that lets you manage a Windows machine entirely through a **Telegram bot** — with activity logging, keystroke logging, screenshots, audio recording, app launching, and more.

---

## ✨ Features

- 📡 **Remote control** via Telegram bot commands
- 🖊️ **Keystroke logging** — logs every key press to a file
- 📋 **Activity logging** — tracks opened/closed windows and clipboard changes
- 🌐 **Network monitoring** — detects connected Wi-Fi networks
- 📸 **Screenshot capture** — takes and sends screenshots remotely
- 🎙️ **Audio recording** — records 10-second audio clips remotely
- 🔊 **Text-to-speech** — speaks text out loud on the target machine
- 💡 **System control** — shutdown, hibernate, sign out
- 🖥️ **App launcher** — open Notepad, Chrome, VS Code, Word, Excel, etc.
- 🪟 **Window management** — list, focus, and close windows remotely
- 🔑 **Wi-Fi password extraction** — retrieves saved Wi-Fi credentials
- 🕶️ **Incognito mode** — temporarily pauses all logging
- 🗑️ **Log management** — clear logs and temp files remotely

---

## 📁 Project Structure

```
Controlium-Engine/
├── Activity/           # Auto-created: activity logs & screenshots
├── Keystroke/          # Auto-created: keystroke logs
├── controlium.pyw      # Main script (runs without a console window)
└── LICENSE
```

---

## ⚙️ Requirements

**Python 3.x** + the following packages:

```
pytelegrambotapi
psutil
pyautogui
pyperclip
pynput
pygetwindow
plyer
pyttsx3
pygame
sounddevice
scipy
screen-brightness-control
winshell
requests
```

Install all at once:

```bash
pip install pytelegrambotapi psutil pyautogui pyperclip pynput pygetwindow plyer pyttsx3 pygame sounddevice scipy screen-brightness-control winshell requests
```

> ⚠️ Windows only. Some modules (`winshell`, `screen-brightness-control`) are Windows-specific.

---

## 🚀 Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/ashfaaqrifath/Controlium-Engine.git
   cd Controlium-Engine
   ```

2. Open `controlium.pyw` and fill in your credentials:
   ```python
   BOT_TOKEN = "YOUR BOT TOKEN"
   my_chatID = "YOUR CHAT ID"
   ```
   Get these from [@BotFather](https://t.me/botfather) and [@userinfobot](https://t.me/userinfobot) on Telegram.

3. Run the script:
   ```bash
   pythonw controlium.pyw
   ```
   > `.pyw` runs silently with no console window.

---

## 📟 Telegram Commands

### System Control
| Command | Action |
|---------|--------|
| `/stop` | Shut down the Controlium engine |
| `/shutdown` | Shutdown the PC (30s delay) |
| `/hibernate` | Hibernate the system |
| `/signout` | Sign out the current user |
| `/version` | Show current version |

### Logging & Monitoring
| Command | Action |
|---------|--------|
| `/log` | Send the activity log file |
| `/keylg` | Send the keystroke log file |
| `/sslog` | Send the last saved screenshot |
| `/incognito` | Pause all logging |
| `/incogoff` | Resume logging |
| `/clearlogs` | Delete all log files |
| `clean <Month>` | Delete logs for a specific month (e.g. `clean January`) |

### Screen & Media
| Command | Action |
|---------|--------|
| `/ss` | Take and send a screenshot |
| `/record` | Record 10s audio and send it |
| `audio <n>` | Play `Audio/audio<n>.mp3` on the machine |
| `/mute` | Stop audio playback |
| `volup <n>` | Increase volume by n steps |
| `voldown <n>` | Decrease volume by n steps |
| `brightness <n>` | Set screen brightness (0–100) |
| `/nobg` | Remove desktop wallpaper |

### App Launcher
| Command | Action |
|---------|--------|
| `/notepad` | Open Notepad |
| `/chrome` | Open Google Chrome |
| `/edge` | Open Microsoft Edge |
| `/vscode` | Open VS Code |
| `/word` | Open Microsoft Word |
| `/excel` | Open Microsoft Excel |
| `/powerpoint` | Open PowerPoint |
| `/files` | Open File Explorer |

### Window Management
| Command | Action |
|---------|--------|
| `/getfocus` | Get the currently focused window |
| `/getallwin` | List all open windows |
| `/closefocus` | Close the focused window |
| `/closeall` | Close all open windows |

### Input Simulation
| Command | Action |
|---------|--------|
| `/enter` | Simulate Enter key |
| `/undo` | Simulate Ctrl+Z |
| `/paste` | Simulate Ctrl+V |
| `/delete` | Simulate Delete key |
| `#<text>` | Type the given text on the machine |

### Misc
| Command | Action |
|---------|--------|
| `/alert` | Send a Windows notification popup |
| `/popup` | Show a warning message box |
| `> <text>` | Speak text aloud via TTS |
| `/time` | Speak the current time aloud |
| `wifi` | Extract and send saved Wi-Fi passwords |
| `search <query>` | Open a Google search on the machine |
| `/bin` | Empty the Recycle Bin |

---

## 🧵 How It Works

The engine spawns **6 threads** simultaneously on startup:

| Thread | Purpose |
|--------|---------|
| `keystroke_thread` | Logs every key press |
| `activity_thread` | Logs system info on startup |
| `network_thread` | Logs current Wi-Fi connection |
| `clipboard_thread` | Monitors clipboard for changes |
| `clear_logs_thread` | Auto-clears logs every 10 minutes |
| `telegram_bot_thread` | Listens for and executes Telegram commands |

---

## 🛠️ Tech Stack

- Python 3
- Telegram Bot API (`pytelegrambotapi`)
- `pynput` — keyboard listener
- `pyautogui` — screen control & input simulation
- `psutil` — system resource monitoring
- `pygetwindow` — window management
- `pyttsx3` — text-to-speech
- `sounddevice` / `scipy` — audio recording
- `pygame` — audio playback
- `winshell` — Windows shell utilities

---


# ⚠️DISCLAIMER
This software, Controlium Engine, is provided STRICTLY FOR EDUCATIONAL AND RESEARCH PURPOSES ONLY. It demonstrates concepts in system automation, remote administration, and monitoring techniques. The author does not endorse, condone, or encourage any illegal, unethical, or unauthorized use of this software, including but not limited to surveillance without consent, privacy invasion, or system compromise. Users are solely responsible for complying with all applicable laws and regulations in their jurisdiction and must obtain explicit, informed consent before deploying this software on any system. By using this software, you acknowledge that the author bears no responsibility or liability for any misuse, damages, or legal consequences arising from its use. Use responsibly and ethically.
