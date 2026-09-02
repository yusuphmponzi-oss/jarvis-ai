import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import sys
import psutil
from config import *

class JarvisAI:
    def __init__(self):
        """Initialize Jarvis AI Voice Assistant"""
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', VOICE_RATE)
        self.engine.setProperty('volume', VOICE_VOLUME)
        self.listening = True
        
    def speak(self, text):
        """Convert text to speech"""
        print(f"Jarvis: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listen to microphone input and convert to text"""
        try:
            with sr.Microphone() as source:
                print("\n[Listening...]")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(
                    source,
                    timeout=MIC_TIMEOUT,
                    phrase_time_limit=MIC_PHRASE_TIME_LIMIT
                )
            
            text = self.recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text.lower()
        
        except sr.UnknownValueError:
            self.speak("Sorry sir, I did not understand that. Please repeat.")
            return None
        except sr.RequestError as e:
            self.speak(f"Could not request results; {e}")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def get_time(self):
        """Get current time"""
        now = datetime.datetime.now()
        return now.strftime("%I:%M %p")
    
    def get_date(self):
        """Get current date"""
        today = datetime.date.today()
        return today.strftime("%A, %B %d, %Y")
    
    def get_system_info(self):
        """Get system information"""
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        info = f"CPU usage is at {cpu_percent} percent. Memory usage is {memory.percent} percent."
        return info
    
    def open_browser(self, query=None):
        """Open browser and optionally search"""
        if query:
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)
            self.speak(f"Opening search results for {query}")
        else:
            webbrowser.open("https://www.google.com")
            self.speak("Opening Google")
    
    def shutdown(self):
        """Shutdown the computer"""
        self.speak(f"Shutting down the system, sir.")
        os.system("shutdown /s /t 1")  # Windows
        # For Linux/Mac: os.system("shutdown -h now")
    
    def restart(self):
        """Restart the computer"""
        self.speak(f"Restarting the system, sir.")
        os.system("shutdown /r /t 1")  # Windows
        # For Linux/Mac: os.system("shutdown -r now")
    
    def greet(self):
        """Greet the owner"""
        import random
        greeting = random.choice(GREETINGS)
        self.speak(greeting)
    
    def process_command(self, command):
        """Process voice commands"""
        if not command:
            return True
        
        # Check for exit commands
        if any(word in command for word in ["exit", "quit", "goodbye", "bye"]):
            self.speak(f"Goodbye, {OWNER_NAME}. It has been a pleasure serving you.")
            return False
        
        # Check for owner name mentions
        if any(title in command for title in OWNER_TITLES):
            self.speak(f"Yes, {OWNER_NAME}? At your service.")
            return True
        
        # Time command
        if "time" in command:
            time_str = self.get_time()
            self.speak(f"The current time is {time_str}, sir.")
        
        # Date command
        elif "date" in command:
            date_str = self.get_date()
            self.speak(f"Today is {date_str}, sir.")
        
        # System info command
        elif "system" in command or "performance" in command:
            info = self.get_system_info()
            self.speak(info)
        
        # Browser commands
        elif "open" in command and "browser" in command:
            self.open_browser()
        elif "search" in command:
            # Extract search query
            search_query = command.replace("search", "").replace("for", "").strip()
            if search_query:
                self.open_browser(search_query)
            else:
                self.speak("What would you like me to search for, sir?")
        
        # System commands
        elif "shutdown" in command:
            self.speak("Are you sure you want to shutdown? Please confirm.")
            confirm = self.listen()
            if confirm and any(word in confirm for word in ["yes", "confirm", "shutdown"]):
                self.shutdown()
        
        elif "restart" in command:
            self.speak("Are you sure you want to restart? Please confirm.")
            confirm = self.listen()
            if confirm and any(word in confirm for word in ["yes", "confirm", "restart"]):
                self.restart()
        
        # Available tasks
        elif "help" in command or "available tasks" in command or "what can you do" in command:
            tasks = ", ".join(AVAILABLE_TASKS)
            self.speak(f"I can help you with: {tasks}. What would you like me to do?")
        
        else:
            self.speak("I'm not sure how to help with that, sir. Please try again or ask what I can do.")
        
        return True
    
    def run(self):
        """Main loop for Jarvis AI"""
        print("="*50)
        print("JARVIS AI - Voice Assistant")
        print(f"Owner: {OWNER_NAME}")
        print("="*50)
        
        self.greet()
        
        while self.listening:
            command = self.listen()
            if command:
                should_continue = self.process_command(command)
                if not should_continue:
                    self.listening = False

if __name__ == "__main__":
    jarvis = JarvisAI()
    try:
        jarvis.run()
    except KeyboardInterrupt:
        print("\nShutting down Jarvis...")
        sys.exit(0)
