import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os 
import random
import smtplib
import pyjokes
import pywhatkit

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',150)
def speak(audio) :
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("HEY! GOOD MORNING!")
    elif hour>=12 and hour<18 :
        speak("HEY! GOOD AFTERNOON!")
    else :
        speak("HEY! GOOD EVENING!")
    
    speak("THIS IS MICHAL SCOFIELD,HOW CAN I HELP YOU?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en')
        print(f"User said {query}\n")

    except Exception as e :
        print(e)
        print("SORRY! CAN YOU REPEAT AGAIN?")
        return "NONE"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email @gmail.com', 'your password')
    server.sendmail('your email @gmail.com', to, content)
    server.close()

def whatsapp_auto(no,message) :
    hour=int(datetime.datetime.now().strftime('%H'))
    min2=int(datetime.datetime.now().strftime('%M'))+2        
    pywhatkit.sendwhatmsg("+91 {}".format(no),message,hour,min2)
    return "DONE"

if __name__=="__main__" :
    wishme()
    while True:
        
        query = takeCommand().lower() #Converting user query into lower case

        #if wikipedia found in the query
        if 'wikipedia' in query:   
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            currentTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f" the current time is {currentTime}")

        elif 'github' in query :
            webbrowser.open("https://github.com/Navodayavarmak")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com/users/16497231/k-navodaya-varma")

        elif ' code' in query:
            codePath = "C:\\Users\\NAVODAYA VARMA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'play music' in query:
            music_dir = 'C:\\Users\\NAVODAYA VARMA\\Desktop\\audio'
            songs = os.listdir(music_dir)
            ran_song = random.choice(songs)
            print(songs)    
            os.startfile(os.path.join(music_dir,ran_song))

        elif 'email to me' in query:
            try:
                speak("What should I send ?")
                content = takeCommand()
                to = "navodayavarma1234@gmail.com"    
                sendEmail(to, content)
                print(content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend varma . I am not able to send your email")

        elif 'whatsapp' or "automatate whatsapp" in query:
            try:
                speak("To Who should I send ?")
                no = takeCommand()
                speak(" What should I send ?")                
                message = takeCommand()     
                whatsapp_auto(no,message)
                print(message)
                speak("YOUR MESSAGE WILL BE DELIVERED AFTER TWO MIN AUTOMATICALLY !")
            except Exception as e:
                print(e)
                speak("Sorry my friend varma . I am not able to send your email")

        elif "on YouTube"  or "in YT" in query :
            on_yt = takeCommand().replace("on YouTube"," ")
            speak(f"playing {on_yt} on Youtube!")
            pywhatkit.playonyt(on_yt)

        elif 'joke' or 'tell me a joke' or 'say joke' in query:
            speak(pyjokes.get_joke())

        elif 'exit' or 'bye' or 'see you later' in query :
            speak('THANK YOU! FOR YOUR TIME BY SCOFIELD')
            exit()