import pyttsx3

engine = pyttsx3.init()

text = "Hello! Welcome! i am your personal assistant"
engine.say(text)
engine.runAndWait()
