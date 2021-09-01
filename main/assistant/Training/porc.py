import pvporcupine
import pyaudio
import struct
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume',1.0)
lss = sr.Recognizer()
handle = pvporcupine.create(keywords=['computer'])


def get_next_audio_frame():
    pa = pyaudio.PyAudio()
    audio_stream = pa.open(rate=handle.sample_rate, channels=1, format=pyaudio.paInt16, input=True,
                           frames_per_buffer=handle.frame_length, input_device_index=None)
    pcm = audio_stream.read(handle.frame_length)
    pcm = struct.unpack_from("h" * handle.frame_length, pcm)
    return pcm


while True:
    pcm = get_next_audio_frame()
    keyword_index = handle.process(pcm)
    if keyword_index == 0:

        print("listening")
        break
engine.say("listening")
engine.runAndWait()
with sr.Microphone() as source:
    print("listening...")
    voice = lss.listen(source)
    command = lss.recognize_google(voice)
    command.lower()
print (command)