import datetime
import smtplib
import pyttsx3          #pip install pyttsx3
import speech_recognition as sr        #pip install speechRecognition
import wikipedia                      #pip install wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)  # 1 for girl's voice and 0 for boy's voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak(" I am chitti a Robot, Speed 1 terahertz, memory 1 zeta byte.")


def takeCommand():
    # It takes microphone input from the user and returns string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.......")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
       # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('bagrianju2002@gmail.com','amrud')
    server.sendmail('bagrianju2002@gmail.com',to, content)
    server.close()



if __name__ == '__main__':
    #speak("Anju is very good girl") #  here we already given the content which we want to listen from javris.
    wishMe()
    while True:
   # if 1:
        query = takeCommand().lower()
    #logic for execute tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'play music' in query:
            music_dir= 'D:\\music_dir'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, The time is {strTime}")

        elif 'open code' in query:
            codePath="C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

   #     elif 'send email to anju' in query:
      #      try:

     #           speak("What should i say?")
     #           content = takeCommand()
     #           to = "bagrianju2002@gmail.com"
     #           sendEmail(to, content)
     #           speak("Email has been send!")
     #       except Exception as e:
      #          print(e)
       #         speak("sorry my sister i am not able to send your mail at this moment")
#if 'quit jarvis' in query:
   # quit()