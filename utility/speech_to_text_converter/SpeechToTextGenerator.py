import speech_recognition as sr

from configuration.config import Configuration

class SpeechToTextGenerator:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.text = None

    def listen_for_speech(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
                print("Speak...")
                speech = self.recognizer.listen(source, phrase_time_limit=3)
                self.__convert_to_text(speech)
        except Exception as e:
            print(e.__str__())

    def __convert_to_text(self, speech):
        text = self.recognizer.recognize_google(speech)
        self.text = text.lower()

    def get_text(self):
        return self.text
