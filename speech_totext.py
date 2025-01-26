import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Please Speak ...")
    audio = recognizer.listen(source, timeout=10, phrase_time_limit=20)
    text = recognizer.recognize_google(audio, language="en-US")
    print("You said: ", text)

