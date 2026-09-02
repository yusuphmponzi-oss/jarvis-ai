# Jarvis AI Setup Guide

## System Requirements

### Windows
- Python 3.8 or higher
- PyAudio (may require Visual C++ Build Tools)
- Microphone and speakers

### macOS
- Python 3.8 or higher
- Xcode Command Line Tools
- Microphone and speakers

### Linux
- Python 3.8 or higher
- ALSA sound utilities
- Microphone and speakers

## Step-by-Step Installation

### 1. Install Python
Download from https://www.python.org/downloads/

### 2. Clone Repository
```bash
git clone https://github.com/yusuphmponzi-oss/jarvis-ai.git
cd jarvis-ai
```

### 3. Create Virtual Environment
```bash
python -m venv venv
```

Activate it:
- **Windows**: `venv\Scripts\activate`
- **macOS/Linux**: `source venv/bin/activate`

### 4. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Test Your Microphone
```bash
python
>>> import speech_recognition as sr
>>> r = sr.Recognizer()
>>> with sr.Microphone() as source:
...     print("Say something!")
...     audio = r.listen(source)
...     print("Recognizing...")
...     print(r.recognize_google(audio))
```

### 6. Run Jarvis
```bash
python jarvis.py
```

## Troubleshooting

### PyAudio Installation Issues
**Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

**macOS:**
```bash
brew install portaudio
pip install pyaudio
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install python3-dev portaudio19-dev
pip install pyaudio
```

### Microphone Not Detected
- Check system sound settings
- Try running as administrator (Windows)
- Test microphone with other applications first

### Google Speech Recognition Not Working
- Check internet connection
- Verify firewall settings allow Python
- Try restarting the application

## Customization

### Change Owner Name
Edit `config.py`:
```python
OWNER_NAME = "Your Name"
```

### Adjust Voice Settings
```python
VOICE_RATE = 150  # Increase for faster speech
VOICE_VOLUME = 0.9  # Adjust volume (0.0 to 1.0)
```

### Add Custom Tasks
Edit `jarvis.py` and add to `process_command()` method.

## Running on Startup

### Windows
1. Create a batch file `run_jarvis.bat`:
```batch
@echo off
cd /d "C:\path\to\jarvis-ai"
venv\Scripts\python.exe jarvis.py
```
2. Add to Task Scheduler

### macOS/Linux
1. Create a shell script `run_jarvis.sh`:
```bash
#!/bin/bash
cd /path/to/jarvis-ai
source venv/bin/activate
python jarvis.py
```
2. Add to crontab with `@reboot`

## Support

For issues, please open a GitHub issue in the repository.
