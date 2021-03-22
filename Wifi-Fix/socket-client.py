import socket
import time
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 80
status = " "
confirmation = " "
ask = " "


while True:
    try:
        sock.connect(("www.google.com", port))
        status = "online"
        if status == "online":
            print("You are currently online")
        break
    except OSError:
        status = "offline"
        if status == "offline":
            print("You are currently offline")
            ask = input("Would you like to run the program? (Yes/No):")
            if ask == "YES" or ask == "Yes" or ask == "yes":
                UserI = input("Would you like to restart you're computer? (Yes/No):")
                if UserI == "Yes" or UserI == "yes":
                    os.system("gnome-terminal -e 'sudo shutdown -r now'")
                elif UserI == "No" or UserI == "no":
                    UserI = input("Are you sure you want to close the program? Yes/No:")
                    if UserI == "Yes" or UserI == "yes" or UserI == "YES":
                        print("closing program")
                        time.sleep(5)
                        os.system("gnome-terminal -e 'sudo shutdown -r now'")
                        break
                    if UserI == "No" or UserI == "NO":
                        UserI = input("Would you like to restart you're computer? (Yes/No): ")
                        if UserI == "Yes" or UserI == "YES":
                            print("restarting your device")
            else:
                print("Please type Yes or No")
                UserI = input("Would you like to restart you're computer? (Yes/No): ")
                if UserI == "Yes" or UserI == "yes":
                     os.system("gnome-terminal -e 'sudo shutdown -r now'")
                elif UserI == "No" or UserI == "no":
                    print("closing program")
                    time.sleep(5)
                    break
