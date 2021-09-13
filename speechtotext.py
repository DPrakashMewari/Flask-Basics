import flask
from flask import Flask
import speech_recognition as sr

app = Flask(__name__)


@app.route("/")
def speech_audio():
    speech = sr.Recognizer()
    with sr.Microphone() as src:
        print("Let try To Speek")
        audio = speech.listen(src)
    # This engine will convert your audio to txt
    try:
        text = speech.recognize_google(audio)
        return text
    except Exception as e:
        print(f"Sorry that exception {e} occur")


if __name__ == "__main__":
    app.run()
