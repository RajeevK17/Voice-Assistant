from gtts import gTTS
import datetime
from datetime import date
import speech_recognition as sr
import wikipedia
import requests
import sys
import webbrowser
import os
import time
import pywhatkit
import pyqrcode

def speak(audio):
    speech = gTTS(text=audio, lang='en', slow=False)
    speech.save('speech.mp3')
    os.system('mpg321 -q speech.mp3')

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('\nListening...')
        speak('Listening')
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print('Recognizing...')
        speak('Recognizing')
        query = r.recognize_google(audio, language="en-IN")
        print(f"User said : {query}")

    except:
        speak("Say that again please...")
        return "None"

    return query

def sara():
    speak("I'm sara an assistant to help you with a variety of tasks. Made by Rajeev.")

def my_name():
    speak("I'm Sara.")

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir. I'm Sara your personal assistant. How may I help you?")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir. I'm Sara your personal assistant. How may I help you?")

    else:
        speak("Good Evening Sir. I'm Sara your personal assistant. How may I help you?")


def say_date():
    today_date = str(date.today())
    speak(f'Today is {today_date}')

def say_time():
    str_time = datetime.datetime.now().strftime('%H:%M:%S')
    speak(f"Sir, the time is {str_time}")

def search_wikipedia(query):
    query = query.replace('wikipedia', '')
    speak('Searching Wikipedia...')
    try:
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(f'According to wikipedia {results}')
        
    except:
        speak('Please provide more brief input!')

def open_youtube():
    webbrowser.open('https://www.youtube.com')

def open_google():
    webbrowser.open('https://www.google.com')

def open_facebook():
    webbrowser.open('https://www.facebook.com')

def open_stackoverflow():
    webbrowser.open('https://www.stackoverflow.com')

def open_instagram():
    webbrowser.open('https://www.instagram.com')

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    print('Your IP address :', ip_address['ip'])
    speak('Sir, your ip address is')
    speak(ip_address['ip'])

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    print(res['joke'])
    speak(res['joke'])

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    print('Advice :', res['slip']['advice'])
    speak(res['slip']['advice'])

def news_reader():
    try:
        print("\nTop 10 headlines as of now...")
        url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=YourAPIKey"
        r = requests.get(url)
        result = r.json()
        speak('Here are the top 10 headlines as of now. Listen carefully.')

        i = 0
        while i<10:
            print("\n",result['articles'][i]['title'],"\n")
            speak(result['articles'][i]['title'])
            i+=1

    except:
        speak("Please check your internet connection.")

def get_weather_report():
    try:
        speak('Please say the city name')

        query = take_command().lower()
        speak('Working on it')
        
        city = query
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YourAPIKey&units=metric"
        result = requests.get(url).json()

        weather = result['weather'][0]['main']
        temperature = str(result['main']['temp'])

        speak(f"It's {weather} in {city}")
        speak(f'Temperature is {temperature} degree celsius')
        time.sleep(5)
    except:
        speak(f'Cannot find city named {city}')
        time.sleep(5)


def search_on_google(query):
    query = query.replace('search', '')
    try:
        pywhatkit.search(query)

    except:
        speak('Unable to connect to the internet.')

def take_note():
    speak('What should i write in note')

    note = take_command().lower()
    with open('/home/rajeev/sara_note.txt', 'at') as f:
        f.write(f'[{datetime.datetime.now()}] - {note}\n')

    speak('Your note has been saved successfully in home directory.')

def create_directory():
    speak('What should i name directory?')
    directory = take_command().lower()
    directory = directory.capitalize()

    path = f'/home/rajeev/{directory}'
    
    if os.path.isdir(path) == True:
        speak(f'Directory {directory} already exists in your home directory.')

    else:
        os.mkdir(f'/home/rajeev/{directory}')
        speak(f'Directory {directory} has been created successfully in your home directory.')

def delete_directory():
    speak('Please say directory name')
    directory = take_command().lower()
    directory = directory.capitalize()

    path = f'/home/rajeev/{directory}'

    if os.path.isdir(path) == False:
        speak(f'There is no directory named {directory} in your home directory')
    
    else:
        os.rmdir(path)
        speak(f'Directory {directory} has been deleted successfully from your home directory')

def open_text_editor():
    speak('Opening text editor')
    os.system('gedit')

def qr_generator():
    speak('Sure Sir. Enter some details on the terminal')

    txt = str(input("\nEnter text to display: "))
    file_name = str(input("Enter file name [Default extension is .png]: "))
    file_path = str(input("Enter file path: "))
    path = file_path + '/' + file_name

    url = pyqrcode.create(txt)
    url.svg(path, scale=8)
    url.png(path, scale=6)
    speak('QR code has been created successfully')

def run():
    wish_me()

    while True:
        query = take_command().lower()
        if 'goodbye' in query:
            speak('Goodbye Sir. Have a good day.')
            sys.exit()

        elif 'the time' in query:
            say_time()
            time.sleep(5)

        elif 'wikipedia' in query:
            try: 
                search_wikipedia(query)
                time.sleep(5)
            except:
                speak('Please check your internet connection.')
                time.sleep(5)

        elif 'open youtube' in query:
            speak('Opening youtube')
            open_youtube()
            time.sleep(5)

        elif 'open google' in query:
            speak('Opening google')
            open_google()
            time.sleep(5)

        elif 'open facebook' in query:
            speak('Opening facebook')
            open_facebook()
            time.sleep(5)
        
        elif 'open stack overflow' in query:
            speak('Opening stackoverflow')
            open_stackoverflow()
            time.sleep(5)
        
        elif 'open instagram' in query:
            speak('Opening instagram')
            open_instagram()
            time.sleep(5)

        elif 'the headlines' in query:
            news_reader()
            time.sleep(5)

        elif 'advice' in query:
            get_random_advice()
            time.sleep(5)

        elif 'a joke' in query:
            get_random_joke()
            time.sleep(5)

        elif 'who are you' in query:
            sara()
            time.sleep(5)

        elif 'your name' in query:
            my_name()
            time.sleep(5)

        elif 'search' in query:
            speak('Searching')
            search_on_google(query)
            time.sleep(5)

        elif 'date' in query:
            say_date()
            time.sleep(5)

        elif 'my ip' in query:
            find_my_ip()
            time.sleep(5)

        elif 'weather' in query:
            get_weather_report()
            time.sleep(5)

        elif 'create a directory' in query or 'create directory' in query:
            create_directory()
            time.sleep(5)

        elif 'open text editor' in query:
            open_text_editor()
            time.sleep(5)

        elif 'delete a directory' in query or 'delete directory' in query:
            delete_directory()
            time.sleep(5)

        elif 'write a note' in query or 'write note' in query or 'take a note' in query:
            take_note()
            time.sleep(5)

        elif 'create qr code' in query or 'create quick response code' in query:
            qr_generator()
            time.sleep(5)
