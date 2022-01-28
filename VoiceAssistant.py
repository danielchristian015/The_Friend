import webbrowser
from datetime import time
from time import ctime
import time
import speech_recognition as speech_recognition
import os
import playsound


import random
from gtts import gTTS


recognition = speech_recognition.Recognizer()

def assistant(audio_input):

    if 'search' in audio_input:
        search = record_audio('what do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        voiceRespond('Here is what I found for' + search)
        voiceRespond('if you want to make any further searches, please say the keyword: search. Otherwise I\'ll help you with something else')
    if 'look for a video' in audio_input:
        search = record_audio('what kind of video?')
        url = 'https://youtube.com/search?q=' + search
        webbrowser.get().open(url)
        voiceRespond('Here is what I fond for' + search)
        voiceRespond('what else can I do for you please? If you would like to make further internet searches, please say the keyword: search')
    if 'my school website' in audio_input:
        #search = record_audio('opening U N G\'s website')
        url = 'https://ung.edu'
        webbrowser.get().open(url)
        voiceRespond('opening U N G website')
        voiceRespond('what else can I do for you please?')
    if 'what class is this project for' in audio_input:
         voiceRespond('This is for the senior project class C S C I 49 50')
    if 'what is the best football team' in audio_input:
         voiceRespond('Obvious answer! GO DAWGS!')
    if 'what is your name' in audio_input:
        voiceRespond('Like I said my name is the assistant. I would like to assist you. I may not be as smart as a human but I can do my part')

        count =1
    if 'thank you' in audio_input:
         voiceRespond('You are welcome.Is there anything else I can do for you?')
    if 'who programmed you' in audio_input:
         voiceRespond('Daniel, a student in C S C I 49 50 at the University of North Georgia implemented my design, so here am I')
    if 'what is the tuition at your school' in audio_input:
        url = 'https://ung.edu/cost-aid/tuition/tuition-and-fee-estimator.php'
        webbrowser.get().open(url)
        voiceRespond('Here is some information about the tuition at the University of North Georgia. You can use the estimator to estimate your tuition fees')
    if 'what is your name' in audio_input and count==2:
         voiceRespond('Like I said my name is the assistant. I would like to assist you. I may not be as smart as a human but I can do my part')
         count = 2
    if 'what is your name' in audio_input and count==3:
         voiceRespond('This is the 3rd time you\'re asking me my name. It\'s beginning to get annoying')
         count=3
    if 'what is your name' in audio_input:
         count = count +1
    if 'exit' in audio_input:
        exit()


def voiceRespond(audio_string=None):
    t = gTTS(text=audio_string, lang='en')
    recognition = random.randint(1,10000000)
    audio_file = 'audio-' +str(recognition) + '.mp3'
    t.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)



def record_audio(Quesiton = False):

    with speech_recognition.Microphone() as source:
        count = 0
        if Quesiton:
            voiceRespond(Quesiton)
        audio = recognition.listen(source)
        #audio_input = r.recognize_google(audio)
        audio_input = ''
        try:
            audio_input = recognition.recognize_google(audio)
        except speech_recognition.UnknownValueError:

            if(count<2):
                voiceRespond('I\'m not sure I understand')
                count = count + 1
            if(count==10):
                voiceRespond('I\'m not sure I understand. You can say the keyword: search if you want to make an internet search ')
                count = 2
            if (count > 11):
                voiceRespond('I didn\'t hear you. Could you repeat please?')
                count = 0
        except speech_recognition.RequestError:
            voiceRespond('Sorry')
        return audio_input





time.sleep(1)


voiceRespond('Hello my name is the assistant, I am your friend. How can I help you today ?')

while(1):
 audio_input = record_audio()
 assistant(audio_input)





