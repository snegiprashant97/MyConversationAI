from utility.openai.RequestHandler import RequestHandler

if __name__ == "__main__":
    obj = RequestHandler()
    obj.get_prompt_from_user()
    obj.play_response_as_a_speech()
    transcript = obj.get_response_as_a_transcript()
    print(transcript)