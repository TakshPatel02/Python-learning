# Advanced WhatsApp Message Sender with some validations

import pywhatkit as kit
import pyautogui 
import datetime
import time

def schedule_whatsapp_message(number, message, send_time):
    current_time = datetime.datetime.now()
    send_time = datetime.datetime.strptime(send_time, "%Y-%m-%d %H:%M")

    if send_time <= current_time:
        print("Send time must be in the future.")
        return
    
    wait_time = (send_time - current_time).total_seconds()
    print(f"Message scheduled to be sent in {wait_time} seconds.")

    kit.sendwhatmsg(number, message, send_time.hour, send_time.minute)
    print("Message scheduled successfully!")

if __name__ == "__main__":
    number = input("Enter the phone number with country code: ")
    message = input("Enter your message: ")
    send_time = input("Enter the send time (YYYY-MM-DD HH:MM): ")

    schedule_whatsapp_message(number , message , send_time)

    time.sleep(15)
    pyautogui.press('enter')

# After running the script, ensure to keep the browser window open for the message to be sent. and we have to wait for some time before the message is sent.
