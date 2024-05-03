import speech_recognition as sr
import win32com.client
import datetime
import openai
import datetime
import random
import numpy as np
import replicate
import sys
import os
import replicate
# setting up the Api token in the local environment valriables.
os.environ["REPLICATE_API_TOKEN"] = "r8_aNuK8miFKFg9kYkcw1z1SYNmJnmNVzo4RanS6"
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred"
        
# This function uses llama model to make respond        
def chat(query):
    char=""
    output = replicate.run(
    "meta/llama-2-70b-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1",
    input={"prompt":query,"max_new_tokens":50}
    )
    for item in output:
        char+=item
    print(char)
    speak(char)

#This function uses to speak out the response
def speak(text):
    speaker=win32com.client.Dispatch("SAPI.spvoice")
    speaker.speak(text)

#main
while True:
    print("Listening...")
    query = takeCommand()
    if "the time now" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speak(f"The time is {hour} {min}")
    elif "Quit".lower() in query.lower():
        print("Quit")
        sys.exit(0)
    elif "Some Error Occurred" in query:
        continue
    else:
        
        print("Chatting...")
        chat(query)