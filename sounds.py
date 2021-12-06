import speech_recognition as sr
from gtts import gTTS
import os
import pyglet
import time
from transformers import pipeline
from translate import Translator

# Niezrozumienie
def unrecognized():
    text_input = "Nie rozumiem, powtórz proszę."
    language = "pl"
    speech = gTTS(text=text_input, lang=language, slow=False)
    speech.save("text.mp3")
    music = pyglet.media.load("text.mp3", streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove("text.mp3")


# Nagrywanie tekstu
def record_voice():
    r = sr.Recognizer()
    mic = sr.Microphone()
    print("start")
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10)
    print("end")
    return str(r.recognize_google(audio, language="pl-PL"))


def speaker(text_input):
    speech = gTTS(text=text_input, lang="pl", slow=False)
    speech.save("my_speech.mp3")
    music = pyglet.media.load("my_speech.mp3", streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove("my_speech.mp3")


def yes_no(text_input):
    translator = Translator(to_lang="en", from_lang="pl")
    translation = str(translator.translate(text_input))
    classifier = pipeline("zero-shot-classification")

    result = classifier(
        translation,
        candidate_labels=["yes", "no"],
    )
    translate = {"yes": True, "no": False}
    scores = result["scores"]
    labels = result["labels"]
    res = dict(zip(labels, scores))
    max_key = max(res, key=res.get)
    return translate[max_key]


def asking(text_input, topic_function):
    speaker(text_input)
    while True:
        result = topic_function()
        while True:
            try:
                decision = record_voice()
                break
            except:
                unrecognized()
        answer = yes_no(decision)
        if answer:
            break
        else:
            speaker(text_input)
    return result
