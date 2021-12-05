import speech_recognition as sr
from gtts import gTTS
import os
import pyglet
import time
from transformers import pipeline
from translate import Translator

#Niezrozumienie
def unrecognized():
    text='Nie rozumiem, powtórz proszę.'
    language = 'pl'
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save('text.mp3')
    music = pyglet.media.load('text.mp3', streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove('text.mp3')

#Nagrywanie tekstu
def record_voice():
    r=sr.Recognizer()
    mic = sr.Microphone()
    print('start')
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10)
    print('koniec')
    return str(r.recognize_google(audio, language='pl-PL'))

def speaker(moj_tekst):
    speech=gTTS(text=moj_tekst,lang='pl', slow = False)
    speech.save('moja_mowa.mp3')
    music = pyglet.media.load('moja_mowa.mp3', streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove('moja_mowa.mp3')

def yes_no(tekst):
    translator = Translator(to_lang='en', from_lang='pl')
    translation = str(translator.translate(tekst))
    print(tekst)
    classifier = pipeline('zero-shot-classification')

    wynik=classifier(
        translation,
        candidate_labels = ['yes','no'],  
    )
    TLUMACZ = {'yes':True,
                'no':False}
    scores = wynik['scores']
    labele = wynik['labels']
    res = dict(zip(labele,scores))
    max_key = max(res, key=res.get)
    return TLUMACZ[max_key]

def asking(text,topic_function):
    speaker(text)
    while True:
        wynik = topic_function()
        while True:
            try:
                yn = record_voice()
                break
            except:
                unrecognized()
        wartosc_bool = yes_no(yn)
        if wartosc_bool:
            break
        else:
            speaker(text)
    return wynik

