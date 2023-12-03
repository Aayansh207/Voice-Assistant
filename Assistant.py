import pyttsx3
import pyperclip as pc
import random
import speech_recognition as sr
import datetime
import wikipedia
import pyautogui
from googletrans import Translator 
import time
import webbrowser
import speedtest
import os
import pyjokes
import requests
import pywhatkit

engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def talk_listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("You said:", query, "\n")
        return str(query)
    except sr.UnknownValueError:
        print("You were not audible. Please try by typing.")
        speak("You were not audible. Please try by typing.")
        r.pause_threshold = 1
        query = input("")
        return str(query)

def wikipedia_search(name):
    try:
        results = wikipedia.summary(name, sentences = 5)
        speak("According to Wikipedia")
        print(results)
        speak(results)
        speak("these were all the results from wikipedia")
    except:
        messuif="We were unable to find "+name+"in wikipedia please retry"
        print(messuif)
        speak(messuif)

def natural_calculator():
    clear()
    while True:   
        print("1-Sum")
        print("2-difference")
        print("3-product")
        print("4-quotient")
        print("5-table teller")
        print("6-Square")
        print("7-power")
        print("8-square root")
        print("9-cube root")
        print("10-Factorial")
        print("11-Fibonacci series")
        a=int(input("please select one of them \n",))
        if(a==1):
            b=int(input("enter the first no."))
            c=int(input("enter the second no."))
            print(b,"+",c,"=",b+c)
        elif(a==2):
            e=int(input("enter the first no."))
            f=int(input("enter the second no."))
            g=e-f
            print(e ,"-",f,"=",g)
        elif(a==3):
            h=int(input("enter the first no."))
            i=int(input("enter the second no."))
            j=h*i
            print(h,"*",i,"=",j)
        elif(a==4):
            k=int(input("enter the first no."))
            l=int(input("enter the second no."))
            m=k/l
            print(k,"/",l,"=",m)
        elif(a==5):
            n=int(input("enter the number of which you want the table"))
            o=int(input("enter the number till where do you want the table"))
            p=1
            while p<=o:
                print(str(n) + ' * ' + str(p) + ' = '+str(n*p))
                p=p+1
        elif(a==6):
            q=int(input("enter the number you want to know the square"))
            r=q*q
            print('the square of',q,'is =',r)
        elif(a==7):
            s=int(input("enter the no. you want to know the square of"))
            t=int(input("enter the the no. of power"))
            u=t*(s*s)
            print("the answer is",u)
        elif(a==8):
            w=int(input("Enter the no. of which you want the square root"))
            x=0
            while x**2 < w:
                x=x+1
                print("the square root of " + str(w) + " is equal to: " + str(x))
        elif(a==9):
            y=int(input("Enter the no. of which you want the cube root"))
            z=0
            while z**3 < y:
                z=z+1
            print("the cube root of " + str(y) + " is equal to: " + str(z))
        elif(a==10):
            za=int(input("Enter the number"))
            zb=1
            for i in range(1,za+1):
                zb=zb*i
            print("the factorial of a number is= ", zb)
        elif(a==11):
            fg=int(input("Enter the level upto which you want to know the fibonacci series"))
            zd=0
            ze=1
            for zf in range(1,fg+1):
                zg=zd+ze
                print(zg)
                zd=ze
                ze=zg
        else:
            print("please select a valid choise")
        Var1=input("To re run press ENTER to exit Type-E")
        if Var1!=" ":
            break

def voicenoter():
    clear()
    print("Speak what you want to type")
    speak("Speak What you want to type")
    stra=talk_listen().capitalize()
    sp="Your note is "+stra
    print(sp)
    speak(sp)
    print("Your text has been copied to your clipboard")
    speak("Your text has been copied to your clipboard")
    pc.copy(stra)

def search_google(search_name):
    search_name=search_name.replace("search","")
    search_name=search_name.replace("google","")
    search_name=search_name.replace("on","")
    search_name=search_name.replace("search about the movie","")
    search_name=search_name.replace("web series","")
    gofir='https://www.google.com/search?q='
    golin=gofir+search_name
    webbrowser.open(golin)
    speak("these are all your results")
    exit()

def dictionary(query):
    query=query.replace("for","")
    query=query.replace("dictionary","")
    query=query.replace("in","")
    query=query.replace("on","")
    query=query.replace(" a ","")
    query=query.replace("search","")
    query=query.replace("the word","")
    query=query.replace("what is the meaning of","")
    query=query.replace("what is the meang of","")
    query=query.replace("please tell the meaning of ","")
    print("Searching!!!")
    speak("Searching dictionary")
    dict_fir="https://www.wolframalpha.com/input/?i="
    dict_link=dict_fir+query
    webbrowser.open(dict_link)
    speak("these are all your results")
    clear()
    exit()

def search_amazon(search_name2):
    search_name2=search_name2.replace("search","")
    search_name2=search_name2.replace("on amazon","")
    search_name2=search_name2.replace("for","")
    amfir="https://www.amazon.in/s?k="
    amlas="&ref=nb_sb_noss_2"
    amlink=amfir+search_name2+amlas
    webbrowser.open(amlink)
    speak("these are all your results")
    exit()

def search_flipkart(search_name3):
    search_name3=search_name3.replace("search","")
    search_name3=search_name3.replace("on","")
    search_name3=search_name3.replace("flipkart","")
    item1="searching"+search_name3
    print(item1)
    speak(item1)
    fkfir="https://www.flipkart.com/search?q="
    fklas="&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    fklink=fkfir+search_name3+fklas
    webbrowser.open(fklink)
    speak("these are all your results")
    exit()

def search_youtube(search_name4):
    search_name4=search_name4.replace("search","",)
    search_name4=search_name4.replace("youtube","",)
    search_name4=search_name4.replace("play","",)
    search_name4=search_name4.replace("song","",)
    search_name4=search_name4.replace("on","")
    search_name4=search_name4.replace("for","")
    print("Searching")
    speak("Searching")
    First=("https://www.youtube.com/results?search_query=")
    link=First+search_name4
    webbrowser.open(link)
    speak("these are all your results")
    exit()

def dowhat():
    whatcanyoudo=["I can search for you on Wikipedia",
                  "I can search words in dictionary",
                  "I can search on youtube",
                  "I can search on Amazon and flipkart",
                  "I can open websites",
                  "I can tell the time",
                  "I can talk with you",
                  "I can start calculator",
                  "You can tell me if you are bored",
                  "I can tell you jokes",
                  "I can tell you the weather ",
                  "I can tell you the news"
                  "I can play songs"]
    print(whatcanyoudo[0])            
    print(whatcanyoudo[1])
    print(whatcanyoudo[2])
    print(whatcanyoudo[3])
    print(whatcanyoudo[4])
    print(whatcanyoudo[5])
    print(whatcanyoudo[6])
    print(whatcanyoudo[7])
    print(whatcanyoudo[8])
    print(whatcanyoudo[9])
    print(whatcanyoudo[10])
    print(whatcanyoudo[11])            
    print(whatcanyoudo[12])            
    speak(whatcanyoudo[0])            
    speak(whatcanyoudo[1])
    speak(whatcanyoudo[2])
    speak(whatcanyoudo[3])
    speak(whatcanyoudo[4])
    speak(whatcanyoudo[5])
    speak(whatcanyoudo[6])
    speak(whatcanyoudo[7])
    speak(whatcanyoudo[8])
    speak(whatcanyoudo[9])
    speak(whatcanyoudo[10])
    speak(whatcanyoudo[11])
    speak(whatcanyoudo[12])

def appopener(path1):
    searchpath='"'+path1+'"'
    os.startfile(searchpath)
    exit()

def clear():
    os.system('cls')
    
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)
 
def translator(phrase,den):
    try:
        den.lower()
        de='hi'
        if "hindi" in den:
            de="hi"
        elif 'afrikaans' in den:
            de="af"
        elif 'albanian' in den:
            de="sq"
        elif 'amharic' in den:
            de="am"
        elif 'arabic' in den:
            de="ar"
        elif 'armenium' in den:
            de="hy"
        elif 'azerbaijani' in den:
            de="az"
        elif 'basque' in den:
            de="eu"
        elif 'belarusian' in den:
            de="be"
        elif 'bengali' in den:
            de="bn"
        elif 'bosnian' in den:
            de="bs"
        elif 'bulgarian' in den:
            de="bg"
        elif 'catalan' in den:
            de="ca"
        elif 'cebuano' in den:
            de="ceb"
        elif 'chichewa' in den:
            de="ny"
        elif 'chinese' in den:
            de="zh-cn"
        elif 'corsican' in den:
            de="co"
        elif 'croatian' in den:
            de="hr"
        elif 'czech' in den:
            de="cs"
        elif 'danish' in den:
            de="da"
        elif 'dutch' in den:
            de="nl"
        elif 'english' in den:
            de="en"
        elif 'esperanto' in den:
            de="eo"
        elif 'estonian' in den:
            de="et"
        elif 'filipino' in den:
            de="tl"
        elif 'finnish' in den:
            de="fi"
        elif 'galician' in den:
            de="gl"
        elif 'georgian' in den:
            de="ka"
        elif 'german' in den:
            de="de"
        elif 'greek' in den:
            de="el"
        elif 'gujarati' in den:
            de="gu"
        elif 'haitian creole' in den:
            de="ht"
        elif 'hausa' in den:
            de="ha"
        elif 'hawaiian' in den:
            de="haw"
        elif 'hebrew' in den:
            de="iw"
        elif 'hmong' in den:
            de="hmn"
        elif 'hungarian' in den:
            de="hu"
        elif 'icelandic' in den:
            de="is"
        elif 'igbo' in den:
            de="ig"
        elif 'indonesian' in den:
            de="id"
        elif 'irish' in den:
            de="ga"
        elif 'italian' in den:
            de="it"
        elif 'japanese' in den:
            de="ja"
        elif 'javanese' in den:
            de="jw"
        elif 'kannada' in den:
            de="kn"
        elif 'kazakh' in den:
            de="kk"
        elif 'khmer' in den:
            de="km"
        elif 'korean' in den:
            de="ko"
        elif "kurdish" in den:
            de="ku"
        elif "lao" in den:
            de="lo"
        elif "latin" in den:
            de="la"
        elif "latvian" in den:
            de="lv"
        elif "lithuanian" in den:
            de="lt"
        elif "luxembourgish" in den:
            de="lb"
        elif "macedonian" in den:
            de="mk"
        elif "malagasy" in den:
            de="mg"
        elif "malay" in den:
            de="ms"
        elif "malyalam" in den:
            de="ml"
        elif "maltese" in den:
            de="mt"
        elif "maori" in den:
            de="mi"
        elif "marathi" in den:
            de="mr"
        elif "mangolian" in den:
            de="mn"
        elif "myanmar" in den:
            de="my"
        elif "napali" in den:
            de="ne"
        elif "norwegian" in den:
            de="no"
        elif "odia" in den:
            de="or"
        elif "pashto" in den:
            de="ps"
        elif "persian" in den:
            de="fa"
        elif "polish" in den:
            de="pl"
        elif "potuguese" in den:
            de="pt"
        elif "punjabi" in den:
            de="pa"
        elif "romanian" in den:
            de="ro"
        elif "russian" in den:
            de="ru"
        elif "spanish" in den:
            de="es"
        elif "tamil" in den:
            de="ta"
        elif "telugu" in den:
            de="te"
        elif "turkish" in den:
            de="tr"
        elif "vietnamese" in den:
            de="vi"
        elif "" in den:
            pass
        translater = Translator()
        answithusa=translater.translate(phrase,dest=de)
        print(answithusa)
    except Exception as e:
        print("Please choose a valid language and try again")
        speak("Please choose a valid language and try again")
        time.sleep(1)
    
    
clear()
print("Assistant 2.0 in your service mister")
speak("Assistant 2 point o in your service mister")
while True:
    query = talk_listen().lower()
    if 'wikipedia' in query:
        print('Searching Wikipedia...')
        speak('Searching Wikipedia')
        query = query.replace("wikipedia", "")
        query = query.replace("search", "")
        query = query.replace("om", "")
        query = query.replace("for", "")

        wikipedia_search(query)
    elif "we are meeting after a long time" in query:
        print("No matter it's been how much time but our friendship will always be there")
        speak("No matter it's been how much time but our friendship will always be there")
    elif "search" in query and "google" in query:
        search_google(query)
    elif "what is a " in query or "movie" in query or "web series" in query:
        search_google(query)
    elif "search for" in query and "in dictionary" in query:
        dictionary(query)
    elif "in dictionary" in query:
            dictionary(query)
    elif "search for" in query and "on dictionary" in query:
        dictionary(query)
    elif "search" in query and "on dictionary" in query:
        dictionary(query)
    elif "search" in query and "in dictionary" in query:
        dictionary(query)
    elif "dictionary" in query or "in dictionary" in query or "on dictionary" in query or "what is the meaning of" in query or "please tell the meaning of " in query:
        dictionary(query)
    elif "open chrome" in query or "open google" in query:
        appopener("C:/Program Files/Google/Chrome/Application/chrome.exe")
    elif "open edge" in query or "open microsoft edge" in query:
        appopener("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
    elif "open whatsapp" in query or "open messages" in query:
        appopener("C:/Users/aayan/AppData/Local/WhatsApp/WhatsApp.exe")
    elif "open spotify" in query or "i want to listen some songs" in query:
        appopener("C:/Users/aayan/AppData/Roaming/Spotify/Spotify.exe")
    elif "open zoom" in query or "open zoom" in query:
        appopener("C:/Users/aayan/AppData/Roaming/Zoom/bin/Zoom.exe")
    elif "open code" in query or "I want to code" in query:
        appopener("C:/Users/aayan/AppData/Local/Programs/Microsoft VS Code/Code.exe")
    elif "open pdf opener" in query or "open acrobat" in query:
        appopener("C:/Program Files (x86)/Adobe/Acrobat Reader DC/Reader/AcroRd32.exe")
    elif "open gmail" in query:
        print("opening")
        speak("opening")
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        exit()
    elif "open amazon" in query:
        print("opening")
        speak("opening")
        webbrowser.open('https://www.amazon.in/')
        exit()
    elif "open flipkart" in query:
        print("Opening")
        speak("opening")
        webbrowser.open("https://www.flipkart.com/")
        exit()
    elif("amazon cart") in query or ("amazon card") in query:
        print("opening")
        speak('opening')
        webbrowser.open("https://www.amazon.in/gp/cart/view.html?ref_=nav_cart")
        exit()
    elif("filpkart cart") in query or ("flipkart card") in query:
        print("Opening")
        speak("opening")
        webbrowser.open("https://www.flipkart.com/viewcart?otracker=Cart_Icon_Click")
        exit()
    elif "search" in query and "on amazon" in query:
        search_amazon(query)
    elif "search" in query and "on flipkart" in query:
        search_flipkart(query)
    elif "what were you doing" in query:
        print("I was just waiting to talk to you")
        speak("I was just waiting to talk to you")
    elif 'open youtube' in  query:
        print("Opening Youtube")
        speak("Opening Youtube")
        webbrowser.open('www.youtube.com')
        exit()
    elif 'open google' in query:
        print("Opening Google")
        speak("opening google")
        webbrowser.open('www.google.com')
        exit()
    elif 'Meet' in query:
        print("Opening Google Meet")
        speak("opening google Meet")
        webbrowser.open('meet.google.com')
        exit()
    elif 'Classroom' in query:
        print("Opening Google classroom")
        speak("opening google classroom")
        webbrowser.open('meet.google.com')
        exit()
    
    elif 'how are you' in query:
        speak("I am fine, Thank you")
        speak("How are you, Sir")
    elif 'fine' in query or "good" in query:
        speak("It's good to know that your fine")
    elif 'exit' in query or 'bye' in query:
        speak("Thanks for giving me your time")
        clear()
        exit()
    elif 'open stackoverflow' in query:
        speak("Here you go to Stack Over flow. Happy coding")
        webbrowser.open("stackoverflow.com") 
        exit()
    elif "search"in query or 'youtube' in query:
        if "play" in query:
            query=query.replace("play","")
            pywhatkit.playonyt(query)
            exit()
        else:
            search_youtube(query)
    elif "play" in query:
        query=query.replace("play","")
        pywhatkit.playonyt(query)
        exit()
    elif "play the song" in query or "play song" in query:
        query=query.replace("play the song","")
        query=query.replace("play song","")
        pywhatkit.playonyt(query)
        exit()
    elif "I want to listen" in query:
        query=query.replace("I want to listen","")
        query=query.replace("the song","")
        pywhatkit.playonyt(query)
        exit()
    elif "who am i" in query:
        print("If you talk then definitely your human.")
        speak("If you talk then definitely your human.")
    elif "why you came to world" in query:
        print("Thanks to Aayansh. further It's a secret")
        speak("Thanks to Aayansh. further It's a secret")
    elif "who are you" in query:
        print("I am your virtual assistant created by Aayansh")
        speak("I am your virtual assistant created by Aayansh")
    elif 'reason for you' in query:
        print("I was created as a Major project made by Aayansh ")
        speak("I was created as a Major project made by Aayansh ")
    elif 'clear' in query:
        speak("Everything is getting cleared")
        clear()
    elif"hello" in query:
        Hello="Hello How can I help you sir"
        print(Hello)
        speak(Hello)
    elif "assistant" in query:
        print("Assistant 2 point o in your service Mister ")
        speak("Assistant 2 point o in your service Mister ")
    elif 'joke' in query:
        joke=(pyjokes.get_joke())
        print(joke)
        speak(joke)
    elif 'you are mad' in query:
        Ans1=["Let me tell you what little Alice said to the Mad Hatter, You are entirely bonkers. But I will tell you a secret. All the best people are.",
              "Sir I am really sorry to make you feel bad But I will take care from next time",
              "I think being mad is not bad till the time we are not doing bad" ]
        Ans1a= random.choice(Ans1)
        print(Ans1a)
        speak(Ans1a)
    elif "calculator" in query:
        natural_calculator()
    elif "calculate" in query:
        query=query.replace("calculate","")
        query=query.replace("+","%2B")
        query=query.replace("plus","%2B")
        gofir='https://www.google.com/search?q='
        golin=gofir+query
        webbrowser.open(golin)
        speak("This is your answer")
        clear()
        exit()
    elif "would you like to meet" in query:
        query=query.replace("would you like to meet","")
        print("Yes why not sir. I would be happy to meet him/her")
        speak("Yes why not sir. I would be happy to meet him or her")
        wihs="Assistant 2.o in your service"+query
        print(wihs)
        speak(wihs)
        print("It was nice to meet you")
        speak("It was nice to meet you")
    elif "weather" in query:
        webbrowser.open('https://www.google.com/search?q=weather&rlz=1C1CHBF_enIN958IN958&oq=weather&aqs=chrome..69i57j0i131i433i512j0i131i433i457i512j0i402l2j0i131i433i512j0i512j0i131i433i512l2j0i433i512.1540j1j7&sourceid=chrome&ie=UTF-8')
        exit()
    elif "news" in query:
        webbrowser.open('https://www.aajtak.in/')
        exit()
    elif "i am hungry" in query or "order something to eat" in query:
        print("You can order something")
        speak("You can order something")
        webbrowser.open('https://www.zomato.com/kanpur')
    elif "what do you eat" in query:
        print("I eat information and I give it to you")
        speak("I eat information and I give it to you")
    elif "do you go to washroom" in query:
        print("I do but aati nahi")
        speak("I do but aati nahi")
    elif "what can you do" in query:
        dowhat()    
    elif "What is your Family" in query:
        print("I am an virtual assistant and my family is python")     
        speak("I am an virtual assistant and my family is python")     
    elif "where do you live" in query:
        print("I live in the server")
        speak("I live in the server")
    elif "internet speed" in query:
        print("calculating...")
        st=speedtest.Speedtest()
        dl=st.download()
        up=st.upload()
        dlsp=dl*(0.00000001)
        ulsp=up*(0.00000001)
        print(f"Your download speed is{dlsp} mbps")
        print(f"Your upload speed is{ulsp} mbps")
    elif "make a note" in query:
        voicenoter()
        exit()
    elif "shutdown" in query:
        print("Do you wish to shutdown your computer? (yes / no): ")
        speak("Do you wish to shutdown your computer?")
        shutdown=talk_listen().lower()
        if shutdown == 'no':
            pass
        else:
            os.system("shutdown /s /t 1")
    elif "hotstar kholo" in query:
        webbrowser.open("hotstar.com")
        speak("jee bilkul ")
        exit()
    elif "open hotstar" in query:
        webbrowser.open("hotstar.com")
        speak("opening hotstar")
        exit()
    elif "volume up" in query or "increase the volume" in query:
        pyautogui.press("volumeup")
    elif "volume down" in query or "volume low" in query or "decrease the volume" in query:
        pyautogui.press("volumedown")
    elif "mute" in query:
        pyautogui.press("volumemute")
    elif "unmute" in query:
        pyautogui.press("volume mute")
    elif "ip address" in query:
        ip= requests.get("https://api.ipify.org").text
        print(f"Your I.P. address is {ip}")
        sp789="Your I.P. address is ",ip
        speak(sp789)
    elif"translate" in query or "translator" in query:
        print("Please tell the phrase that you want to translate")
        speak("Please tell the phrase that you want to translate")
        query=talk_listen()
        print("please type the destination language")
        speak("please type the destiantion language")
        asnh=input()
        translator(query,asnh)
        time.sleep(5)
        
    elif "bed" in query and "story" in query or "hindi" in query:
        bedtimestoryhindi=[
            "https://www.youtube.com/watch?v=BdSuoNSba88",
            "https://www.youtube.com/watch?v=brLJ7bj-UN4",
            "https://www.youtube.com/watch?v=_Qou_EJn7aA",
            "https://www.youtube.com/watch?v=7X4G75u926g",
            "https://www.youtube.com/watch?v=YDENkMfUw-Q",
            "https://www.youtube.com/watch?v=EqO_eXJo2RY",
            "https://www.youtube.com/watch?v=VgEFpaLDarU",
            "https://www.youtube.com/watch?v=hl37dhen8_0",]
        randlistlink=random.choice(bedtimestoryhindi)
        webbrowser.open(randlistlink)
        speak("Playing bed time story on youtube")
        exit() 
    elif "bed" in query and "story" in query and "english" in query:
        bedtimestoryeng=["",
            "https://www.youtube.com/watch?v=0t4bxC-4chs",
            "https://www.youtube.com/watch?v=F198bDkOJz8",
            "https://www.youtube.com/watch?v=bvRsScPoCuQ",
            "https://www.youtube.com/watch?v=LbGCKiei3ag",
            "https://www.youtube.com/watch?v=N7XdG0quoBc",
            "https://www.youtube.com/watch?v=zF7FID_RIeg",
            "https://www.youtube.com/watch?v=qAl2b_BaPe4",]
        randlistlinkeng=random.choice(bedtimestoryeng)
        webbrowser.open(randlistlinkeng)
        speak("Playing bed time story on youtube")
        exit() 
    elif "stories" in query:
        stories=["",
            "https://www.youtube.com/watch?v=0t4bxC-4chs",
            "https://www.youtube.com/watch?v=F198bDkOJz8",
            "https://www.youtube.com/watch?v=bvRsScPoCuQ",
            "https://www.youtube.com/watch?v=LbGCKiei3ag",
            "https://www.youtube.com/watch?v=N7XdG0quoBc",
            "https://www.youtube.com/watch?v=zF7FID_RIeg",
            "https://www.youtube.com/watch?v=qAl2b_BaPe4",
            "https://www.youtube.com/watch?v=BdSuoNSba88",
            "https://www.youtube.com/watch?v=brLJ7bj-UN4",
            "https://www.youtube.com/watch?v=_Qou_EJn7aA",
            "https://www.youtube.com/watch?v=7X4G75u926g",
            "https://www.youtube.com/watch?v=YDENkMfUw-Q",
            "https://www.youtube.com/watch?v=EqO_eXJo2RY",
            "https://www.youtube.com/watch?v=VgEFpaLDarU",
            "https://www.youtube.com/watch?v=hl37dhen8_0",]
        randlistlinkeng2=random.choice(stories)
        webbrowser.open(randlistlinkeng2)
        speak("Playing random story on youtube")
        exit()
        
    elif 'time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")   
        print(f"Sir, the time is {strTime}")
        speak(f"Sir, the time is {strTime}")
    elif "thank you" in query:
        speak("Sir please don't make me feel embarass")
        
    else:   
        gofir='https://www.google.com/search?q='
        golin=gofir+query
        webbrowser.open(golin)
        speak("Theese are the web results")
        clear()
        exit()
        