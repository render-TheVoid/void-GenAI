import os
import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
from youtubesearchpython import VideosSearch
import pyjokes
import pyautogui as pyAutoGUI
import google.generativeai as genAI

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

genAI.configure(api_key="#-------YOUR API KEY--------#")
model = genAI.GenerativeModel("gemini-1.5-flash")

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def wishme():
    hourNow = int(datetime.datetime.now().hour)
    if hourNow>0 and hourNow<12:
        print("Hey! Good Morning. I'm void. Please tell me how I may assist you?")
        speak("Hey! Good Morning. I'm void. Please tell me how I may assist you?")
    elif hourNow>12 and hourNow<15:
        print("Hey! Good Afternoon. I'm void. Please tell me how I may assist you?")
        speak("Hey! Good Afternoon. I'm void. Please tell me how I may assist you?")
    else:
        print("Hey! Good Evening. I'm void. Please tell me how I may assist you?")
        speak("Hey! Good Evening. I'm void. Please tell me how I may assist you?")

def take_instructions():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Let me see...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")

    except Exception as exp:
        print(exp)
        print("Unable to listen properly. Say Again. ")
        return "none"

    return query
#For YouTube search
def searchyoutube(query):
    search = VideosSearch(query, limit=1)
    result = search.result()['result'][0]
    video_url = result['link']
    webbrowser.open(video_url)

if __name__ == "__main__":
    wishme()
    while True:
        query = take_instructions().lower()
        #For wikipedia search
        if 'wikipedia' in query:
            speak("Let me search the Wikipedia...")
            query = query.replace("wikipedia", "")
            searchResults = wikipedia.summary(query, sentences=2)
            print(f"As per the wikipedia,  {searchResults}")
            speak("As per the Wikipedia, ")
            speak(searchResults)

        #Opening Websites
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            print("\nOpening Youtube!")
            speak("Opening Youtube!")

        elif "open google" in query:
            webbrowser.open("google.com")
            print("\nOpening Google!")
            speak("Opening Google!")

        elif "open linkedin" in query:
            webbrowser.open("linkedin.com")
            print("\nOpening LinkedIn!")
            speak("Opening LinkedIn!")

        elif "open github" in query:
            webbrowser.open("github.com")
            print("\nOpening Github!")
            speak("Opening Github!")

        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")
            print("\nOpening Stack Overflow!")
            speak("Opening Stack Overflow!")

        elif "open instagram" in query:
            webbrowser.open("Instagram.com")
            print("\nOpening Instagram!")
            speak("Opening Instagram!")

        elif "open whatsapp" in query:
            webbrowser.open("web.whatsapp.com")
            print("\nOpening Whatsapp!")
            speak("Opening Whatsapp!")

        elif "open amazon" in query:
            webbrowser.open("amazon.in")
            print("\nOpening Amazon!")
            speak("Opening Amazon!")

        elif "open geekforgeeks" in query:
            webbrowser.open("geekforgeeks.com")
            print("\nOpening GeekForGeeks!")
            speak("Opening GeekForGeeks!")

        elif "open w3 schools" in query:
            webbrowser.open("w3schools.com")
            print("\nOpening W3 Schools")
            speak("Opening W3 Schools!")

        elif "open twitter" in query or "open x" in query:
            webbrowser.open("x.com")
            print("\nOpening X!")
            speak("Opening X!")

        elif "open chatgpt" in query:
            webbrowser.open("chat.openai.com")
            print("\nOpening ChatGPT!")
            speak("Opening ChatGPT!")

        elif "open reddit" in query:
            webbrowser.open("reddit.com")
            print("\nOpening Reddit!")
            speak("Opening Reddit!")

        elif "open amazon" in query:
            webbrowser.open("amazon.in")
            print("\nOpening Amazon!")
            speak("Opening Amazon!")

        elif "open microsoft" in query:
            webbrowser.open("microsoft.com")
            print("\nOpening MicroSoft!")
            speak("Opening MicroSoft!")

        elif "open pinterest" in query:
            webbrowser.open("pinterest.com")
            print("\nOpening Pinterest!")
            speak("Opening Pinterest!")

        elif "open duck duck go" in query:
            webbrowser.open("duckduckgo.com")
            print("\nOpening Duck Duck Go!")
            speak("Opening Duck Duck Go!")

        elif "open weather" in query:
            webbrowser.open("weather.com")
            print("\nOpening Weather!")
            speak("Opening Weather!")

        elif "open quora" in query:
            webbrowser.open("quora.com")
            print("\nOpening Quora!")
            speak("Opening Quora!")

        elif "open telegram" in query:
            webbrowser.open("web.telegram.org")
            print("\nOpening Telegram!")
            speak("Opening Telegram!")

        elif "open zoom" in query:
            webbrowser.open("zoom.com")
            print("\nOpening Zoom!")
            speak("Opening Zoom!")

        elif "stop" in query:
            print("\nBye! Catch You Later.")
            speak("Bye! Catch You Later.")
            break

        elif "the time" in query:
            theTime = datetime.datetime.now().strftime("%H : %M : %S")
            print(theTime)
            time = "It is" + theTime
            speak(time)

        elif "open" in query and "code" in query:
            pathFile = "C:\\Users\\risha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            print("Opening VS Code!")
            os.startfile(pathFile)
            print("\nBye! Catch You Later.")
            speak("Enjoy! Catch You Later. Bye")
            break

        elif "open" in query and "photoshop" in query:
            pathFile = "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"
            print("Opening Adobe Photoshop!")
            os.startfile(pathFile)
            print("\nBye Bye! Catch You Later.")
            speak("Enjoy! Catch You Later. Bye Bye")
            break

        elif "open" in query and "notepad" in query:
            pathFile = "C:\\Windows\\notepad.exe"
            print("Opening Notepad!")
            os.startfile(pathFile)
            print("\nBye Bye! Catch You Later.")
            speak("Enjoy! Catch You Later. Bye Bye")
            break

        elif "open" in query and "filmora" in query:
            pathFile = "C:\\Users\\risha\\AppData\\Local\\Wondershare\\Wondershare Filmora\\Wondershare Filmora Launcher.exe"
            print("Opening Filmora!")
            os.startfile(pathFile)
            print("\nBye Bye! Catch You Later.")
            speak("Enjoy! Catch You Later. Bye Bye")
            break

        elif "open" in query and "after effects" in query:
            pathFile = "C:\\Program Files\\Adobe\\Adobe After Effects 2021\\Support Files\\AfterFX.exe"
            print("Opening After Effects!")
            os.startfile(pathFile)
            print("\nBye Bye! Catch You Later.")
            speak("Enjoy! Catch You Later. Bye Bye")
            break

        elif "open" in query and "media player" in query:
            pathFile = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            print("Opening Media Player!")
            os.startfile(pathFile)
            print("\nBye Bye! Catch You Later.")
            speak("Enjoy! Catch You Later. Bye Bye")
            break

        elif "open" in query and "chrome" in query:
            pathFile = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            print("Opening Chrome!")
            os.startfile(pathFile)
            print("\nBye Bye! Catch You Later.")
            speak("Enjoy! Catch You Later. Bye Bye")
            break

        elif "open" in query and "media encoder" in query:
            pathFile = "C:\\Program Files\\Adobe\\Adobe Media Encoder 2021\\Adobe Media Encoder.exe"
            print("Opening Adobe Media Encoder!")
            os.startfile(pathFile)
            print("\nBye Bye! Catch You Later.")
            speak("Enjoy! Catch You Later. Bye Bye")
            break

        elif "open" in query and "audacity" in query:
            pathFile = "C:\\Program Files\\Audacity\\Audacity.exe"
            print("Opening Audacity!")
            os.startfile(pathFile)
            print("\nBye Bye! Catch You Later.")
            speak("Enjoy! Catch You Later. Bye Bye")
            break

        elif "open" in query and "github desktop" in query:
            pathFile = "C:\\Users\\risha\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
            print("Opening Github Desktop!")
            os.startfile(pathFile)
            print("\nBye Bye! Catch You Later.")
            speak("Enjoy! Catch You Later. Bye Bye")
            break

        elif "open" in query and "7 zip" in query:
            pathFile = "C:\\Program Files\\7-Zip\\7zFM.exe"
            print("Opening 7 Zip File Manager!")
            os.startfile(pathFile)
            print("\nBye Bye! Catch You Later.")
            speak("Enjoy! Catch You Later. Bye Bye")
            break

        elif "open" in query and "excel" in query:
            pathFile = "C:\\Program Files (x86)\\Microsoft Office\\Office12\\EXCEL.exe"
            print("Opening Microsoft Excel!")
            os.startfile(pathFile)
            print("\nBye Bye! Catch You Later.")
            speak("Enjoy! Catch You Later. Bye Bye")
            break

        elif "open" in query and "word" in query:
            pathFile = "C:\\Program Files (x86)\\Microsoft Office\\Office12\\WINWORD.exe"
            print("Opening Microsoft Word!")
            os.startfile(pathFile)
            print("\nBye Bye! Catch You Later.")
            speak("Enjoy! Catch You Later. Bye Bye")
            break

        elif "open" in query and "powerpoint" in query:
            pathFile = "C:\\Program Files (x86)\\Microsoft Office\\Office12\\POWERPNT.exe"
            print("Opening Microsoft PowerPoint!")
            os.startfile(pathFile)
            print("\nBye Bye! Catch You Later.")
            speak("Enjoy! Catch You Later. Bye Bye")
            break

        elif "open" in query and "powerpoint" in query:
            pathFile = "C:\\Program Files (x86)\\Microsoft Office\\Office12\\POWERPNT.exe"
            print("Opening Microsoft PowerPoint!")
            os.startfile(pathFile)
            print("\nBye Bye! Catch You Later.")
            speak("Enjoy! Catch You Later. Bye Bye")
            break

        elif "open" in query and "explorer" in query:
            pathFile = "C:\\Windows\\Explorer.exe"
            print("Opening Explorer!")
            os.startfile(pathFile)
            print("\nBye Bye! Catch You Later.")
            speak("Enjoy! Catch You Later. Bye Bye")
            break

        elif "open" in query and "paint" in query:
            pathFile = "C:\\Program Files\\WindowsApps\\Microsoft.Paint_11.2410.38.0_x64__8wekyb3d8bbwe\\PaintApp.exe"
            print("Opening Explorer!")
            os.startfile(pathFile)
            print("\nBye Bye! Catch You Later.")
            speak("Enjoy! Catch You Later. Bye Bye")
            break

        elif "play" and "on youtube" in query:
            query = query.replace("on youtube", "")
            query = query.replace("play", "").capitalize()
            print(f"Looking for {query}!")
            searchyoutube(query)
            query = f"Looking for {query}!"
            speak(query)
            break

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif "text" in query:
            query = query.replace("text", "")
            print(f"Writing: {query}")
            pyAutoGUI.typewrite(query)

        elif "explain" in query:
            query = query.replace("explain", "")
            response = model.generate_content(query)
            print(response.text)
            speak(response.text)

        elif "take a screenshot" in query:
            print("Took a screenshot!")
            speak("Took a screenshot!")
            image = pyAutoGUI.screenshot("screenshot.jpg")

        else:
            response = model.generate_content(query)
            print(response.text)
            speak(response.text) 