import webbrowser
import os

# For opening various applications based on the app name
def open_apps(app_name):
    if "youtube" in app_name.lower():
        webbrowser.open("https://www.youtube.com")
    elif "google" in app_name.lower():
        webbrowser.open("https://www.google.com")
    elif "github" in app_name.lower():
        webbrowser.open("https://www.github.com")
    elif "chat gpt" in app_name.lower():
        webbrowser.open("https://chatgpt.com")
    elif "udemy" in app_name.lower():
        webbrowser.open("https://www.udemy.com")
    elif "notepad" in app_name.lower():
        os.startfile("notepad.exe")
    else:
        print("Application not recognized.")
