import pywhatkit as kit

number = input("Enter the phone number with country code: ")
message = input("Enter your message: ")
hours = int(input("Enter the hour (24-hour format): "))
minutes = int(input("Enter the minutes: "))

kit.sendwhatmsg(number, message, hours, minutes)

print("Message scheduled successfully!")