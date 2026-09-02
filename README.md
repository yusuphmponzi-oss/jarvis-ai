# Jarvis AI - Voice Assistant

**A sophisticated voice assistant that recognizes Dr. Yusuph Mponzi as its owner and performs automated tasks.**

## Features

✨ **Voice Recognition & Response**
- Listens to voice commands using Google's Speech Recognition API
- Responds with natural speech output
- Understands commands even with variations

👤 **Owner Recognition**
- Recognizes Dr. Yusuph Mponzi as the owner
- Personalized greetings and responses
- Respectful titles and forms of address

🤖 **Task Automation**
- **Time**: Get current time
- **Date**: Get current date
- **Weather**: Check weather (expandable)
- **Browser**: Open Google or search the web
- **System Info**: Check CPU and memory usage
- **Shutdown/Restart**: Control system power
- **Help**: List available tasks

## Installation

### Prerequisites
- Python 3.8+
- Microphone for voice input
- Internet connection (for speech recognition and web browsing)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yusuphmponzi-oss/jarvis-ai.git
cd jarvis-ai
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Start Jarvis:
```bash
python jarvis.py
```

### Example Commands

- "What time is it?"
- "Tell me the date"
- "Doctor Mponzi, how are you?"
- "Search for Python tutorials"
- "Open browser"
- "What's my system performance?"
- "Help"
- "Goodbye"

## Configuration

Edit `config.py` to customize:
- Owner name and titles
- Voice rate and volume
- Microphone timeout settings
- Greetings and available tasks

## Roadmap

- [ ] Weather API integration
- [ ] Calendar and reminders
- [ ] Email management
- [ ] Smart home integration
- [ ] Machine learning for personalization
- [ ] Multi-language support
- [ ] Mobile app companion

## Technologies Used

- **SpeechRecognition**: Google API for voice recognition
- **pyttsx3**: Text-to-speech conversion
- **PyAudio**: Microphone input handling
- **psutil**: System monitoring

## License

MIT License - Feel free to use and modify

## Author

Built with ❤️ for Dr. Yusuph Mponzi
