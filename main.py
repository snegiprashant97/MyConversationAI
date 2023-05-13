from utility.text_to_speech_converter.TextToSpeechGenerator import TextToSpeechGenerator

if __name__ == "__main__":
    text = "My name is Prashant. (And i am not a terrorist)"
    converted_obj = TextToSpeechGenerator(text)
    converted_obj.play_speech()
