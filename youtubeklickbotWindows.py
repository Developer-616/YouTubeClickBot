
import webbrowser
import time
import os

url = input("Enter the YouTube URL: ")
refresh = input("Enter the refresh time in seconds: ")
count = input("How many views do you want? ")

def openURL():
    # Close the currently open browser tabs/windows before opening a new one
    if os.name == 'nt':  # For Windows
        os.system("taskkill /IM msedge.exe /F")
   

    # Open the new URL
    webbrowser.open(url)
    time.sleep(int(refresh))

    for i in range(int(count)):
        print("Webpage has been viewed")
        openURL()

openURL()