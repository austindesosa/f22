import os, glob, time
from moviepy.editor import *
from mutagen.mp3 import MP3
from gtts import gTTS
import filer

def name_mp3(mp4, ext='mp3'):
    s = mp4.split('.')[0]
    s += '.' + ext
    return s

def to_mp3(mp4, mp3=None):
    x = VideoFileClip(mp4)
    if not mp3:
        mp3 = name_mp3(mp4)
    x.audio.write_audiofile(mp3)
    return mp3

def play(mp3):
    a = MP3(mp3)
    os.system(mp3)
    time.sleep(a.info.length)

def playlist(el):
    for x in el:
        play(x)

def play_mp3s(k):
    x = glob.glob(str(k) + "*.mp3")
    playlist(x)
    return x

def to_voice(txt, mp3=None, language='en'):
    x = filer.read(txt)
    y = gTTS(text=x, lang=language)
    if not mp3:
        mp3=name_mp3(txt, ext='mp3')
    y.save(mp3)
    return mp3
    