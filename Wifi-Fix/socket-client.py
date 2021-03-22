import socket
import time
import os
from datetime import datetime


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 80
status = " "
confirmation = " "
while True:
    try:
        sock.connect(("google.com", port))
        status = "online"
        if status == "online":
            print("You are currently online")
        break
    except:
        status = "offline"
        if status == "offline":
            print("You are currently offline")
            UserI = input("Would you like to restart you're computer? (Yes/No): ")
            if UserI == "Yes" or UserI == "yes":
                confirmation = input("Are you sure? (It will close all you're application currently opened) Yes/No: ")
                if confirmation == "Yes" or confirmatiom == "YES":
                    print("downloading Internet tools")
                    os.system("gnome-terminal -e 'sudo apt-get install -y net-tools'")
                    print("Restarting your device")
                    time.sleep(5)
                    os.system("gnome-terminal -e 'sudo shutdown -r now'")
            elif UserI == "No" or UserI == "no":
                UserI = input("Are you sure you want to close the program? Yes/No:")
                if UserI == "Yes" or UserI == "yes" or UserI == "YES":
                    print("closing program")
                    time.sleep(5)
                    break
                if UserI == "No" or UserI == "NO":
                    UserI = input("Would you like to restart you're computer? (Yes/No): ")
                    if UserI == "Yes" or UserI == "YES":
                        print("restarting your device")
            else:
                print("Please type Yes or No")
                UserI = input("Would you like to restart you're computer? (Yes/No): ")
                if UserI == "Yes" or UserI == "yes":
                    confirmation = input(
                        "Are you sure? (It will close all you're application currently opened) Yes/No: ")
                    if confirmation == "Yes" or confirmatiom == "YES":
                        print("Restarting your device")
                        time.sleep(5)
                        os.system("gnome-terminal -e 'sudo shutdown -r now'")
                    elif UserI == "No" or UserI == "no":
                        print("closing program")
                        time.sleep(5)
                        break

        sleep.time(10)
        if status == "offline":
            UserI = input("Would you like to disable/enable your internet? Yes/No")
            if UserI == "YES" or UserI == "Yes" or UserI == "yes":
                print("disabling/enabling internet")
                time.sleep(5)
                os.system("gnome-terminal -e 'sudo ifconfig wlp2s0 down'")
                time.sleep(2)
                os.system("gnome-terminal -e 'sudo ifconfig wlp2s0 up'")




while True:
    time.sleep(30)
    timenow = now.strftime("%H:%M:%S")
    try:
        sock.connect(("google.com", port))
        status = "online"
        if status == "online":
            print('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
