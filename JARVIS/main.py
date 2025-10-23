from ai.intent_handler import handle_intent
from voice.speak import speak
from voice.listen import listen

# Main loop of logic
speak("Hello! Master. How can I assist you today?")
while True:
    query = listen()
    if not query:
        continue
    query = str(query).lower()
    if "exit" in query or "stop" in query:
        speak("Stopping the listener. Goodbye!")
        break
    handle_intent(query)