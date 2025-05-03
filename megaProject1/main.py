import speech_recognition as sr
import pyttsx3
import os
from openai import OpenAI
import webbrowser
from dotenv import load_dotenv
from youtube_search import YoutubeSearch
import json
import requests
from time import sleep

load_dotenv()
engine = pyttsx3.init()


def ai(prompt):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.responses.create(
        model="gpt-4o",
        instructions="You are JARVIS. Respond concisely. Do only what you're told. No markdown, no extras.",
        input=prompt,
    )
    return response.output_text


def speak(text, rate=150):
    engine.say(text)
    engine.setProperty('rate', rate)
    engine.runAndWait()


def processCommand(c):
    print(c)
    prompt = f"""
    You are Jarvis. Match the user's intent to one of the following commands:
    - open_website: Open a website(link)
    - play_video: Play a YouTube video
    - get_news: Show current news
    - search_query: Google search
    - open_app: Open an app(actual exec file name: .exe)
    - something else: Handle by own(Use your mind and answer!)

    Respond in JSON with 'action' and 'value' keys.

    User request: {c}
    """

    response = json.loads(ai(prompt=prompt))  # {action:"",value:""}
    action = response.get("action")
    value = response.get("value")

    print(response)

    match action:
        case "open_website":
            webbrowser.open(value)
        case "play_video":
            youtubeId = json.loads(YoutubeSearch(value, max_results=1).to_json())[
                'videos'][0]['id']
            videoLink = f"https://www.youtube.com/watch?v={youtubeId}"
            webbrowser.open(videoLink)
        case "get_news":
            request = requests.get(
                f'https://newsapi.org/v2/top-headlines?country=us&apiKey={os.getenv("NEWS_API_KEY")}').text
            data = json.loads(request)
            news = [x['title'] for x in data['articles']]
            for index, title in enumerate(news):
                speak(f"{index+1}..... {title}", rate=125)
                sleep(1)
        case "search_query":
            webbrowser.open(value)
        case "open_app":
            os.startfile(value)
        case "something else":
            speak(value, rate=125)
        case _:
            speak("Unexpected Command", rate=125)


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while (True):
        try:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening!")
                audio = recognizer.listen(
                    source, timeout=5, phrase_time_limit=2)
                call = recognizer.recognize_google(audio)

                if (call.lower() == "jarvis"):
                    print("J.A.R.V.I.S Activated!")
                    speak("Ya!")
                    audio = recognizer.listen(
                        source, timeout=20, phrase_time_limit=10)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print(e)