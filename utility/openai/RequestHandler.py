import json
import requests

from configuration.config import Configuration
from utility.speech_to_text_converter.SpeechToTextGenerator import SpeechToTextGenerator
from utility.text_to_speech_converter.TextToSpeechGenerator import TextToSpeechGenerator


class RequestHandler:

    def __init__(self):
        self.response = None
        self.prompt = None
        self.temperature = 0.2
        self.response_message = None

    def get_prompt_from_user(self):
        speech_obj = SpeechToTextGenerator()
        speech_obj.listen_for_speech()
        prompt = speech_obj.get_text()
        self.__send_prompt(prompt)

    def __send_prompt(self, prompt):
        self.prompt = prompt
        self.__send_request_to_openai_model()

    def play_response_as_a_speech(self):
        if self.response_message is not None:
            converted_obj = TextToSpeechGenerator(self.response_message)
            converted_obj.play_speech()

    def get_response_as_a_transcript(self):
        if self.response_message is not None:
            return self.response_message

    def __send_request_to_openai_model(self):
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {Configuration.OPENAI_API_KEY}"
        }
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": self.prompt}],
            "temperature": self.temperature
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        self.response = response.json()
        self.response_message = self.response.get('choices')[0].get("message").get("content")
