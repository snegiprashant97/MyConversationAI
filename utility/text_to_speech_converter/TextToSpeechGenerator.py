import os
from gtts import gTTS

from configuration.config import Configuration


class TextToSpeechGenerator:
    def __init__(self, text):
        self.text = text
        self.speech = None
        self.__convert_to_speech()

    def __convert_to_speech(self):
        self.speech = gTTS(text=self.text, lang='en', slow=False, tld='us')
        self.__save_speech_as_a_file()

    def __save_speech_as_a_file(self):
        self.speech.save(Configuration.SPEECH_SAVE_PATH + Configuration.SPEECH_FILE_NAME)

    @staticmethod
    def play_speech():
        os.system(f"mpg321 {Configuration.SPEECH_SAVE_PATH}/{Configuration.SPEECH_FILE_NAME}")
