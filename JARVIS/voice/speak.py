import pyttsx3 

# For converting text to speech
def speak(text):
    engine = pyttsx3.init(driverName='sapi5', debug=True)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) 
    engine.setProperty('rate', 200)
    engine.say(text)
    engine.runAndWait()