import pyttsx3
import speech_recognition as sr

class VoiceEngine:
    """Handles voice recognition and text-to-speech functionality"""
    
    def __init__(self, voice_speed=150, voice_volume=1.0):
        """Initialize voice engine with speech recognition and TTS"""
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', voice_speed)
        self.engine.setProperty('volume', voice_volume)
        
        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 4000  # Adjust sensitivity
    
    def speak(self, text):
        """Convert text to speech and play it"""
        print(f"J.A.R.V.I.S: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self, timeout=5, phrase_time_limit=10):
        """Listen for voice input and return recognized text"""
        try:
            print("Listening...")
            with sr.Microphone() as source:
                # Reduce background noise
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                
                # Capture audio
                audio = self.recognizer.listen(
                    source, 
                    timeout=timeout, 
                    phrase_time_limit=phrase_time_limit
                )
            
            # Recognize speech using Google Speech Recognition
            print("Processing...")
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        
        except sr.UnknownValueError:
            self.speak("Sorry, I could not understand that. Please try again.")
            return None
        
        except sr.RequestError as e:
            self.speak(f"Error with the speech recognition service: {e}")
            return None
        
        except sr.WaitTimeoutError:
            self.speak("I did not hear anything. Please try again.")
            return None
    
    def set_voice_properties(self, speed=None, volume=None):
        """Update voice properties"""
        if speed:
            self.engine.setProperty('rate', speed)
        if volume:
            self.engine.setProperty('volume', volume)
