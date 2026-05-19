import pyttsx3
import speech_recognition as sr

class VoiceEngine:
    """
    Handles voice recognition and text-to-speech functionality using SpeechRecognition and sounddevice for microphone input.
    Note: PyAudio is not required; sounddevice is used for input compatibility.
    """
    
    def __init__(self, voice_speed=150, voice_volume=1.0):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', voice_speed)
        self.engine.setProperty('volume', voice_volume)
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 4000

    def speak(self, text):
        print(f"J.A.R.V.I.S: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self, timeout=5, phrase_time_limit=10):
        try:
            print("Listening...")
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(
                    source,
                    timeout=timeout,
                    phrase_time_limit=phrase_time_limit
                )
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
        except Exception as e:
            self.speak(f"Microphone error: {str(e)}. Ensure your microphone is properly set up and sounddevice is installed.")
            return None

    def set_voice_properties(self, speed=None, volume=None):
        if speed:
            self.engine.setProperty('rate', speed)
        if volume:
            self.engine.setProperty('volume', volume)
