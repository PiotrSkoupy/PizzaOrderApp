import pyaudio
import wave
import speech_recognition as sr

CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5

for i in range (1,3):
    WAVE_OUTPUT_FILENAME = f'Plik1_ZUM{i}.wav'
    NAME_TO_NOTE=f'Plik1_ZUM{i}'

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    r=sr.Recognizer() 
    harvard = sr.AudioFile(WAVE_OUTPUT_FILENAME)
    with harvard as source:
        audio = r.record(source)
    text_do_zapisu=str(r.recognize_google(audio, language='pl-PL'))
    with open('text.txt', 'a', encoding='utf-8') as f:
        f.write(NAME_TO_NOTE+' '+text_do_zapisu+'\n')