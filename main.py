from utility.text_to_speech_converter.TextToSpeechGenerator import TextToSpeechGenerator
from utility.speech_to_text_converter.SpeechToTextGenerator import SpeechToTextGenerator

if __name__ == "__main__":
    # Test generate text
    speech_obj = SpeechToTextGenerator()
    speech_obj.listen_for_speech()
    text = speech_obj.get_text()
    print(text)

    # Test generate speech
    converted_obj = TextToSpeechGenerator(text)
    converted_obj.play_speech()
