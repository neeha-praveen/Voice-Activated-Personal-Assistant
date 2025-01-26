import speech_recognition as sr
import pyttsx3
import requests
import datetime

engine = pyttsx3.init()

def speakIntro(intro):
    engine.say(intro)
    print("Assistant: ",intro)
    engine.runAndWait()

def getWeather():
    city="bangalore"
    api_key="31895d271571d8b36da9d91f08d14d86"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        print(f"Assistant: weather in {city} is {weather} with a temperature of {temp} deg. C")
        engine.say(f"Assistant: weather in {city} is {weather} with a temperature of {temp} deg. C")
    else:
        print("Assistant: Sorry, I couldn't fetch the weather")
        engine.say("sorry, i couldn't fetch the weather")
    engine.runAndWait()

def getNews():
    api_key_news="2ba9d43f8beb4800b146b46e15b28911"
    news_url=f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key_news}"
    response=requests.get(news_url)
    if response.status_code == 200:
        articles = response.json().get("articles",[])
        headlines = [article['title'] for article in articles[:5]] # top 5
        print("Assistant: The top 10 headlines are: ")
        for i, headline in enumerate(headlines, start=1):
            print(f"{i}. {headline}")
            engine.say(headline)
            engine.runAndWait()

def getTime():
    time = datetime.datetime.now().strftime("%I:%M %p")
    print(time)
    engine.say(f"Assistant: it is {time} now")
    engine.runAndWait()

def end():
    print("Assistant: Bye!")
    engine.say("Bye!")
    engine.runAndWait()
    exit()

def processText(text):
    if "weather" in text:
        getWeather()
    elif "news" in text:
        getNews()
    elif "time" in text:
        getTime()
    elif "exit" in text or "quit" in text:
        end()
    else:
        print("Assistant: I don't know how to help you with that")
        engine.say("I don't know how to help you with that")

def main():
    speakIntro("Hello I'm Your Personal Assistant! How can i help you today?")

    while True:
        recognizer = sr.Recognizer()
    
        with sr.Microphone() as source:
            print("Please Speak ...")
            try:
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=20)
                text = recognizer.recognize_google(audio, language="en-US").lower()
                print("You: ", text)
                processText(text)
            except sr.UnknownValueError:
                print("Sorry, didn't get you")
                engine.say("Sorry, didn't get you")

if __name__ == "__main__":
    main()