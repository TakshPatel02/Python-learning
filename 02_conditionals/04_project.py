# your're building a smart thermostat alert system:
# if the device_status is "active"
#     and temperature > 35 -> warn:"high temperature alert!"
#     else :"temperature normal"
# if device is off -> "device is offline"

device_status = "active"
temperature = 30

if device_status == "active":
    if temperature > 35:
        print("high temperature alert!")
    else:
        print("temperature normal")    
else:
    print("device is offline")    


# we can do this  below also if we have to much in the if block and do not want to complicate it then we write pass in the if block and write the else block normally , and after doing the else block we can write the if block code normally , pass is  used to avoid the error of empty if block
# if device_status == "active":
    # pass
# else:
    # print("device is offline")   