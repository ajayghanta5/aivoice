import AppOpener
import pip
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
from AppOpener import open, close



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)


    if 'open' in command:
        app = command.replace('open', '')
        talk('opening ' + app)
        AppOpener.open(app)
    elif 'close' in command:
        app = command.replace('close', '')
        talk('closing ' + app)
        AppOpener.close(app)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print(time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%d:%B %Y')
        talk('today date  is ' + date)
        print(date)
    elif 'are you single' in command:
        talk('Evadra nuvvu intha talented gaa vunav')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif'how r u' in command:
        talk('I am great thanks for asking')
        print("i'm great thanks for asking 😍")
    elif 'how are you' in command:
        talk('I am great thanks for asking')
        print("i'm great thanks for asking 😍")
    elif '' in command:
        web = command.replace('', '')
        talk('opening ' + web)
        webbrowser.open(web)

    else:
        talk('Please say the command again.')


while True:
    run_alexa()
