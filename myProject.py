import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listener = sr.Recognizer()
# this engine will talk to me. init -> initialize
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# voice=""
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        print("Entering try")
        # r=sr.Recognizer()
        # r.energy_threshold=4000
        # print(r)
        with sr.Microphone() as source:
            print("listening")
            text = "Hello This is your virtual assistant friday. How can I help you?"
            print(text)
            engine.say(text)
            engine.runAndWait()

            print("I am Listening......")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'friday' in command:
                command = command.replace('friday', '')
                print(command)
                engine.say(command)
                engine.runAndWait()
    except:
        print("Error")
        command = ''
        pass
    return command

def run_friday(): 
    command = take_command().lower()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is' + time)
        print('Current time is' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

run_friday()
