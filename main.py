from voice_engine import VoiceEngine
from task_automation import TaskAutomation
from system_control import SystemControl
from browser_control import BrowserControl
from config import USERNAME, VOICE_SPEED, VOICE_VOLUME
from datetime import datetime
import platform

class JARVIS:
    """Main J.A.R.V.I.S Assistant - Windows Only"""
    
    def __init__(self):
        """Initialize J.A.R.V.I.S"""
        # Check if running on Windows
        if platform.system() != "Windows":
            raise Exception("This application is designed for Windows only!")
        
        self.voice = VoiceEngine(VOICE_SPEED, VOICE_VOLUME)
        self.tasks = TaskAutomation()
        self.running = True
    
    def greet(self):
        """Greet the user"""
        hour = datetime.now().hour
        if hour < 12:
            greeting = f"Good morning, {USERNAME}! I'm J.A.R.V.I.S. How can I help you?"
        elif hour < 18:
            greeting = f"Good afternoon, {USERNAME}! I'm J.A.R.V.I.S. What can I do for you?"
        else:
            greeting = f"Good evening, {USERNAME}! I'm J.A.R.V.I.S. What do you need?"
        
        self.voice.speak(greeting)
    
    def process_command(self, command):
        """Process voice commands"""
        if not command:
            return
        
        command = command.lower().strip()
        
        # Greeting commands
        if any(word in command for word in ['hello', 'hi', 'hey']):
            self.voice.speak(f"Hello {USERNAME}! How can I assist you?")
        
        # Search commands
        elif 'search' in command or 'google' in command:
            query = command.replace('search', '').replace('google', '').replace('for', '').strip()
            result = BrowserControl.search_google(query)
            self.voice.speak(result)
        
        elif 'youtube' in command:
            query = command.replace('youtube', '').replace('search', '').replace('for', '').strip()
            result = BrowserControl.search_youtube(query)
            self.voice.speak(result)
        
        elif 'wikipedia' in command:
            query = command.replace('wikipedia', '').replace('search', '').replace('for', '').strip()
            result = BrowserControl.search_wikipedia(query)
            self.voice.speak(result)
        
        # Website commands
        elif 'open' in command and 'website' in command:
            website = command.replace('open', '').replace('website', '').strip()
            result = BrowserControl.open_website(website)
            self.voice.speak(result)
        
        elif any(site in command for site in BrowserControl.WEBSITES.keys()):
            for site in BrowserControl.WEBSITES.keys():
                if site in command:
                    result = BrowserControl.open_website(site)
                    self.voice.speak(result)
                    break
        
        # App control commands
        elif 'open' in command or 'launch' in command or 'start' in command:
            for app in BrowserControl.list_available_apps():
                if app in command:
                    result = BrowserControl.open_app(app)
                    self.voice.speak(result)
                    return
        
        # Task commands
        elif 'create task' in command or 'add task' in command or 'new task' in command:
            self.voice.speak("What is the task?")
            task_name = self.voice.listen()
            if task_name:
                self.tasks.add_task(task_name)
                self.voice.speak(f"Task {task_name} created successfully")
        
        elif 'list tasks' in command or 'show tasks' in command or 'my tasks' in command:
            tasks = self.tasks.get_tasks()
            if tasks:
                task_list = ". ".join([f"{i+1}. {task['name']}" for i, task in enumerate(tasks)])
                self.voice.speak(f"Your tasks are: {task_list}")
            else:
                self.voice.speak("You have no tasks")
        
        elif 'complete task' in command or 'finish task' in command:
            self.voice.speak("Which task number?")
            response = self.voice.listen()
            if response:
                try:
                    task_num = int(response.split()[0]) - 1
                    self.tasks.complete_task(task_num)
                    self.voice.speak("Task marked as complete")
                except:
                    self.voice.speak("Could not complete task")
        
        elif 'set reminder' in command:
            self.voice.speak("What should I remind you about?")
            reminder_text = self.voice.listen()
            if reminder_text:
                self.voice.speak("In how many seconds?")
                try:
                    seconds = int(self.voice.listen())
                    self.tasks.set_reminder(reminder_text, seconds)
                    self.voice.speak(f"Reminder set for {seconds} seconds")
                except:
                    self.voice.speak("Could not set reminder")
        
        # System commands
        elif 'cpu usage' in command:
            result = SystemControl.get_cpu_usage()
            self.voice.speak(result)
        
        elif 'memory' in command or 'ram' in command:
            result = SystemControl.get_memory_usage()
            self.voice.speak(result)
        
        elif 'disk' in command:
            result = SystemControl.get_disk_usage()
            self.voice.speak(result)
        
        elif 'battery' in command:
            result = SystemControl.get_battery_status()
            self.voice.speak(result)
        
        elif 'system info' in command or 'system information' in command:
            info = SystemControl.get_system_info()
            info_text = SystemControl.format_system_info(info)
            self.voice.speak(info_text)
        
        # Time and date
        elif 'time' in command or 'what time' in command:
            current_time = datetime.now().strftime('%I:%M %p')
            self.voice.speak(f"The current time is {current_time}")
        
        elif 'date' in command or 'what date' in command:
            current_date = datetime.now().strftime('%A, %B %d, %Y')
            self.voice.speak(f"Today is {current_date}")
        
        # Exit commands
        elif any(word in command for word in ['goodbye', 'bye', 'exit', 'quit', 'stop']):
            self.voice.speak(f"Goodbye {USERNAME}! Have a great day!")
            self.running = False
        
        else:
            self.voice.speak("I did not understand that. Please try again.")
    
    def run(self):
        """Main loop for J.A.R.V.I.S"""
        print("=" * 50)
        print("J.A.R.V.I.S - Windows Voice Assistant")
        print("=" * 50)
        print(f"Platform: {platform.system()}")
        print("Status: Ready")
        print("=" * 50)
        
        self.greet()
        
        while self.running:
            try:
                print("\nListening for commands...")
                command = self.voice.listen()
                
                if command:
                    print(f"Processing: {command}")
                    self.process_command(command)
                
            except KeyboardInterrupt:
                print("\nShutting down...")
                self.voice.speak("Shutting down. Goodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
                self.voice.speak("An error occurred. Please try again.")

if __name__ == "__main__":
    try:
        assistant = JARVIS()
        assistant.run()
    except Exception as e:
        print(f"Failed to start J.A.R.V.I.S: {e}")
        print("Make sure you are running this on Windows!")
