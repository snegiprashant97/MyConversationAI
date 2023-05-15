from utility.openai.RequestHandler import RequestHandler

if __name__ == "__main__":
    obj = RequestHandler()
    response = ''

    # Holding a Full conversation
    while True:
        obj.get_prompt_from_user(response)
        obj.play_response_as_a_speech()
        response = obj.get_response_as_a_transcript()
        print(response)
