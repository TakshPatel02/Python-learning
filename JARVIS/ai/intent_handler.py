from voice.speak import speak
from system.open_apps import open_apps
from system.close_apps import close_apps
from ai.gemini import generate_response , is_question

# For handling user intents
def handle_intent(text):
    if text:
        if "open" in text.lower():
            speak(f"Opening {text.split('open' , 1)[1].strip()}")
            open_apps(text)
        elif "jarvis who are you" in text.lower():
            speak("I am Jarvis , Personal AI assistant created by Taksh Patel.")
        elif "close" in text.lower():
            speak(f"Closing {text.split('close' , 1)[1].strip()}")
            close_apps(text.split('close' , 1)[1].strip())
        elif is_question(text.lower()):
            response = generate_response(text)
            speak(response)
            print(response)
        else:
            print({text})
    else:
        pass