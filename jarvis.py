
#########################     Made By MRxO1    ############################################
#   #   #   #   #   #   #   #   #   # Guys We Can Add Many More Amazing Features In This Assistant...
#   #   #   #   #   #   #   #   #   # You Can Chat With Jarvis Just Like Shown In Iron Man Movie, It Is Your Own Personal Jarvis!

import pyttsx3
import speech_recognition as sr
import datetime
import requests
import wikipedia
import webbrowser
import random
import pprint
import os
import subprocess

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set up Jarvis-like voice
def setup_jarvis_voice():
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'male' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 150)  # Speed up for a sharper voice
    engine.setProperty('volume', 1)  # Max volume

# Function to speak text
def jarvis_speak(text):
    setup_jarvis_voice()
    engine.say(text)
    engine.runAndWait()

# Function to take voice input
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print("Could not understand audio, please say that again.")
        return None
    return query.lower()

# Function to tell the current time
def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    jarvis_speak(f"The current time is {current_time}")

# Function to tell the current date
def tell_date():
    today = datetime.datetime.now()
    jarvis_speak(f"Today is {today.strftime('%A')}, {today.strftime('%d %B %Y')}")

# Function to fetch weather information
def fetch_weather(city):
    api_key = ""  # Replace with your WeatherAPI key
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(url)
    weather_data = response.json()
    
    if "current" in weather_data:
        temperature = weather_data['current']['temp_c']
        feels_like = weather_data['current']['feelslike_c']
        description = weather_data['current']['condition']['text']
        
        weather_info = f"The temperature in {city} is {temperature}°C, feels like {feels_like}°C, with {description}."
        jarvis_speak(weather_info)
        print(f"City: {city}\nDescription: {description}\nTemperature: {temperature}°C\nFeels like: {feels_like}°C")
        
        return {
            "city": city,
            "description": description,
            "temperature": temperature,
            "feels_like": feels_like
        }
    else:
        error_message = "I could not retrieve the weather information."
        jarvis_speak(error_message)
        return {"error": error_message}

# Function to search Google
def google_search(query):
    jarvis_speak(f"Searching Google for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

# Function to search Wikipedia
def wikipedia_search(query):
    try:
        jarvis_speak(f"Searching Wikipedia for {query}")
        summary = wikipedia.summary(query, sentences=2)
        jarvis_speak(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        jarvis_speak("There were too many results for this query. Please be more specific.")
    except wikipedia.exceptions.PageError:
        jarvis_speak("I'm sorry, I couldn't find any results for that query.")
        print("Page Error: No page found for this query.")
    except Exception as e:
        jarvis_speak("An error occurred while searching Wikipedia.")
        print(f"Unexpected error: {e}")

# Function to search YouTube
def youtube_search(query):
    jarvis_speak(f"Searching YouTube for {query}")
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

# Function to tell a random joke
def get_random_jokes():
    try:
        headers = {'Accept': 'application/json'}
        response = requests.get("https://icanhazdadjoke.com/", headers=headers)
        response.raise_for_status()  # Check if the request was successful
        joke_data = response.json()
        joke = joke_data.get("joke", "I couldn't fetch a joke at the moment.")
        
        jarvis_speak(joke)
        print(joke)
        return joke  # Return joke if you want to print or use it elsewhere 
    except requests.exceptions.RequestException as e:
        error_message = "I couldn't fetch a joke at the moment. Please try again later."
        jarvis_speak(error_message)
        print(f"Error fetching joke: {e}")
        return error_message

# Function to give random advice
def get_random_advice():
    try:
        response = requests.get("https://api.adviceslip.com/advice")
        response.raise_for_status()  # Ensure we catch any HTTP errors
        advice_data = response.json()
        advice = advice_data['slip']['advice']  # Extracting the advice from the JSON response
        return advice
    except requests.exceptions.RequestException as e:
        print(f"Error fetching advice: {e}")
        return "Sorry, I couldn't fetch advice at the moment."


# Function to fetch news headlines
def fetch_news():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey="  # Replace with your News API key
    response = requests.get(url)
    news_data = response.json()
    
    if news_data["status"] == "ok":
        articles = news_data["articles"][:5]  # Get top 5 news
        jarvis_speak("Here are the top news headlines:")
        for article in articles:
            jarvis_speak(article["title"])
    else:
        jarvis_speak("I could not retrieve the news at the moment.")

# Conversitional AI Using xAI Grok

from openai import OpenAI
import json


def grok_conversation(prompt):
    try:
        MODEL_NAME = "grok-beta"
        XAI_API_KEY = "API_KEY"

        client = OpenAI(
            api_key="",
            base_url="https://api.x.ai/v1",
        )

        messages = [
            {"role": "system", "content": "You are a highly intelligent AI assistant named Jarvis, just like Tony Stark's personal assistant. You're cool, calm, and always ready with a quick wit or a snarky remark. You give smart suggestions, crack jokes, and always keep it classy — just like Tony would want."},
            {"role": "user", "content": prompt}
        ]

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages = messages,
        )
        print(response)
        print(response.choices[0].message.content)
        return response.choices[0].message.content
  
    except Exception as e:
        return f"General error: {e}"

# Function to handle conversation with Grok AI
def handle_grok_conversation():
    jarvis_speak("What would you like to talk about")
    while True:
        user_input = take_command()
        if user_input:
            if "exit" in user_input or "stop" in user_input:
                jarvis_speak("Goodbye! Exiting the chat now.")
                break

            ai_response = grok_conversation(user_input)
            jarvis_speak(ai_response)  
            
        else:
            jarvis_speak("I didn't catch that. Could you please repeat?")

# Offline  

#Give the path of your application here
paths = {
    'discord': "",
    'telegram': "",
}

def open_telegram():
    os.startfile(paths["telegram"])

def close_telegram():
    os.system('taskkill /f /im Telegram.exe')  

def open_discord():
    os.startfile(paths['discord'])

def close_discord():
    os.system('taskkill /f /im Discord.exe')

def open_cmd():
    os.system('start cmd')

def close_cmd():
    os.system('taskkill /f /im cmd.exe')

# Function to Control the Volume of the System

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL

def get_volume_control():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    return interface.QueryInterface(IAudioEndpointVolume)

# Function to increase volume
def volume_up(step=0.1):
    try:
        volume = get_volume_control()
        current_volume = volume.GetMasterVolumeLevelScalar()
        new_volume = min(1.0, current_volume + step)  # Ensure it doesn't go above 1.0
        volume.SetMasterVolumeLevelScalar(new_volume, None)
        jarvis_speak(f"Volume increased to {int(new_volume * 100)}%.")
    except Exception as e:
        jarvis_speak("I couldn't adjust the volume.")
        print(f"Error: {e}")

# Function to decrease volume
def volume_down(step=0.1):
    try:
        volume = get_volume_control()
        current_volume = volume.GetMasterVolumeLevelScalar()
        new_volume = max(0.0, current_volume - step)  # Ensure it doesn't go below 0.0
        volume.SetMasterVolumeLevelScalar(new_volume, None)
        jarvis_speak(f"Volume decreased to {int(new_volume * 100)}%.")
    except Exception as e:
        jarvis_speak("I couldn't adjust the volume.")
        print(f"Error: {e}")

#Function to Control Screen Brightness

import screen_brightness_control as sbc

# Function to increase brightness
def brightness_up(step=10):
    try:
        current_brightness = sbc.get_brightness(display=0)[0] 
        new_brightness = min(100, current_brightness + step)  # Ensure it doesn't exceed 100
        sbc.set_brightness(new_brightness, display=0)  
        jarvis_speak(f"Brightness increased to {new_brightness} percent.")
    except Exception as e:
        jarvis_speak("I couldn't adjust the brightness.")
        print(f"Error: {e}")

# Function to decrease brightness
def brightness_down(step=10):
    try:
        current_brightness = sbc.get_brightness(display=0)[0]  
        new_brightness = max(0, current_brightness - step)  # Ensure it doesn't go below 0
        sbc.set_brightness(new_brightness, display=0) 
        jarvis_speak(f"Brightness decreased to {new_brightness} percent.")
    except Exception as e:
        jarvis_speak("I couldn't adjust the brightness.")
        print(f"Error: {e}")

# Main function to run the assistant
def run_jarvis():
    jarvis_speak("Welcome Back Sir, All system for gaming will be prepared in a few minutes, so grab a cup of coffee and have a good day .")
    while True:
        query = take_command()

        if query:
            if "time" in query:
                tell_time()
            elif "date" in query:
                tell_date()

            elif 'open discord' in query:
               open_discord()

            elif 'close discord'in query:
                close_discord()
            
            elif 'open telegram' in query:
                open_telegram()
            
            elif 'close telegram' in query:
                close_telegram()

            elif 'open command prompt' in query or 'open cmd' in query:
                open_cmd()

            elif ' close command prompt' in query or 'close cmd' in query:
                close_cmd()

            elif "volume up" in query:
                volume_up()
    
            elif "volume down" in query:
                volume_down()

            elif "brightness up" in query:
                brightness_up()

            elif "brightness down" in query:
                brightness_down()

            elif "chat" in query or "conversation" in query:
                handle_grok_conversation()
            
            elif "weather" in query:
                 jarvis_speak("Which city's weather would you like to search for?")
                 city = take_command()
                 if city:
                    weather_info = fetch_weather(city)
                    if "error" not in weather_info:
                        jarvis_speak(f"For your convenience, I am printing it on the screen.")
                    else:
                        jarvis_speak(weather_info["error"])

            elif "google" in query:
                jarvis_speak("What would you like to search on Google?")
                search_query = take_command()
                if search_query:
                    google_search(search_query)

            elif "wikipedia" in query:
                jarvis_speak("What would you like to search on Wikipedia?")
                search_query = take_command()
                if search_query:
                    wikipedia_search(search_query)

            elif "youtube" in query:
                jarvis_speak("What would you like to search on YouTube?")
                search_query = take_command()
                if search_query:
                    youtube_search(search_query)

            elif "advice" in query:
                jarvis_speak("Here's an advice for you, sir")
                advice = get_random_advice()
                jarvis_speak(advice)  
                jarvis_speak("For your convenience, I am printing it on the screen, sir.")
                print(advice)  

            elif 'joke' in query:
                jarvis_speak("Hope you like this one sir")
                joke = get_random_jokes()
                jarvis_speak(joke)
                jarvis_speak("For your convenience, I am printing it on the screen sir.")
                pprint.pprint(joke)

            elif "news" in query:
                fetch_news()

            elif "exit" in query or "stop" in query:
                jarvis_speak("Goodbye, sir.")
                break
            else:
                jarvis_speak("I'm sorry, I did not understand the command.")



# wake up voice detectation

import pvporcupine
import pyaudio
import struct
import speech_recognition as sr

# add your real access key which you will get from Picovoice 
access_key = ""

# Initialize Porcupine with the access key and the wake word
porcupine = pvporcupine.create(access_key=access_key, keywords=["terminator", "jarvis"])  # Change wake words as desired

pa = pyaudio.PyAudio()
audio_stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)

def listen_for_wake_word():
    print("Listening for wake word...")

    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        keyword_index = porcupine.process(pcm)
        if keyword_index >= 0:
            print("Wake word detected!")
            execute_command()
            break

def execute_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"Command received: {command}")
    except sr.UnknownValueError:
        print("Could not understand the command.")
    except sr.RequestError as e:
        print(f"Error with the service; {e}")

try:
    listen_for_wake_word()
except KeyboardInterrupt:
    print("Program terminated.")
finally:
    audio_stream.stop_stream()
    audio_stream.close()
    pa.terminate()
    porcupine.delete()


# Run the Jarvis 
run_jarvis()
