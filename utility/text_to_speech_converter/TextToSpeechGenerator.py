import os
from gtts import gTTS

from configuration.config import Configuration


class TextToSpeechGenerator:
    def __init__(self, text):
        self.text = text
        self.speech = None
        self.__convert_to_speech()

    def __convert_to_speech(self):
        """
        method uses gTTS library to convert text to speech using parameters to determine what speech to use.
        `tld` parameter is used to determine language accent.
        :return: None
        """
        self.speech = gTTS(text=self.text, lang='en', slow=False, tld='us')
        self.__save_speech_as_a_file()

    def __save_speech_as_a_file(self):
        self.speech.save(Configuration.SPEECH_SAVE_PATH + Configuration.SPEECH_FILE_NAME)

    def play_speech(self):
        """
        Plays the mp3 file generated in `__save_speech_as_a_file()` and then proceeds to delete it.
        :return: None
        """
        audio_file_path = f"{Configuration.SPEECH_SAVE_PATH}{Configuration.SPEECH_FILE_NAME}"
        # check if file exists
        if os.path.exists(audio_file_path):
            try:
                os.system(f"{Configuration.AUDIO_RUNNER} {audio_file_path}")
                # ALERT! MAKE SURE THE PATH POINTS TO MP3 FILE GENERATED
                os.remove(audio_file_path)
            except Exception as e:
                print(e.__str__())
        else:
            raise Exception("Unable to locate the speech file.")
