import datetime
from speak import say
from spech_to_text import takecommand
from rapidfuzz import fuzz,process
from weather import Weather
from random import choice
import os
import webbrowser
from api_bot import ask_ai
import psutil
from NewsApi import get_top_headlines
import pyjokes
import requests

print("*"*100)
print("AI Desktop Assistant (Jarvis)".center(100))
print("*"*100)

def action_time():
    hour=datetime.datetime.now().strftime("%H")
    m=datetime.datetime.now().strftime("%M")
    print(f"Jarvis : Current time is {hour}:{m} ")
    say(f" Current time is {hour} {m} ") 

def action_date():
    mon=datetime.datetime.now().strftime("%B")
    day=datetime.datetime.now().strftime("%d")
    year=datetime.datetime.now().strftime("%Y")
    print(f"Jarvis : Today's Date is {mon} {day} {year}")
    say(f"Today's Date is {mon} {day} {year} ")

def action_name():
    w=["My name is jarvis","i am jarvis"]
    print(f"Jarvis : {choice(w)}") 
    say(f"{choice(w)}")

def action_weather():
    ans = Weather()
    details = f"Temperature of {ans[0]} is {ans[1]}degree celcius with {ans[2]}" 
    print(f"Jarvis : {ans[0]}: {ans[1]}°C {ans[2]}")
    say(details)

def action_thnk():
    w=choice(["welcome","your welcome","my pleasure"])
    print(f"Jarvis : {w}") 
    say(f"{w}")

def action_cam():
    os.system("start microsoft.windows.camera:")
    print("Jarvis : Camera opened")
    say("Camera opened")

def action_note():
    os.system("notepad")
    print("Jarvis : Notepad opened")
    say("Notepad opened")

def action_yt():
    url = 'https://youtube.com/'
    webbrowser.get().open(url)
    print("Jarvis : Youtube opened")
    say("Youtube opened")  

def action_google():
    url = 'https://google.com/'
    webbrowser.get().open(url)
    print("Jarvis : Google opened")
    say("Google opened")  

def action_music():
    webbrowser.open("https://gaana.com/")   
    print("Jarvis : Gaana.com is now ready for you, enjoy your music")
    say("Gaana.com is now ready for you, enjoy your music")   

def action_docs():
    path=r"C:\Users\Hp\OneDrive\Documents"
    os.startfile(path)
    print("Jarvis : Opening documents")
    say("Opening documents")

def action_fl_expl():
    os.startfile(os.path.expanduser("~"))
    print("Jarvis : Opening file explorer")
    say("Opening file explorer")

def action_battery():
    battery=psutil.sensors_battery()
    if battery is not None:
        per=battery.percent
        plugged=battery.power_plugged
        status="charging" if plugged else "not charging"
        print(f"Jarvis : Battery is at {per}% and it is {status}.")
        say(f"Battery is at {per}% and it is {status}.")
    else:
        print("Jarvis : Battery info not available.")
        say("Battery info not available.")
        return "Battery info not available."

def action_cpu():
    usage=psutil.cpu_percent(interval=1)
    print(f"Jarvis : Current CPU usage is {usage}")
    say(f"Current CPU usage is {usage}")

def action_RAM():
    mem=psutil.virtual_memory()
    used=mem.percent
    print(f"Jarvis : RAM usage is at {used}%")
    say(f"RAM usage is at {used}%")
    
def action_system():
    action_battery()
    action_cpu()
    action_RAM()

def action_code():
    os.system("code")
    print("Jarvis : Opening VScode")
    say("Opening VScode")

def action_terminal():
    os.system("start cmd")
    print("Jarvis : Opening terminal")
    say("Opening terminal")

def action_news():
    news=get_top_headlines()
    print(f"Jarvis : {news}")
    say(news)

def action_joke():
    joke=pyjokes.get_joke()
    print(f"Jarvis : {joke}")
    say(joke)

def action_quotes():
    try:
        res=requests.get("https://zenquotes.io/api/random")
        res.raise_for_status() 
        data = res.json()[0]
        quote=data['q']
        print(f"Jarvis : {quote}")
        say(quote)
    except:
        print("Jarvis : Sorry, I couldn't get a quote right now.")
        say("Sorry, I couldn't get a quote right now.")

def action_facts():
    try:
        res=requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        data=res.json()
        print(f"Jarvis : {data['text']}")
        say(data['text'])
    except:
        print("Jarvis : Sorry, I couldn't get a fact right now.")
        say("Sorry, I couldn't get a fact right now.")

intent_action={
    1:action_time,
    2:action_date,
    3:action_name,
    4:action_weather,
    5:action_music,
    6:action_thnk,
    7:action_cam,
    8:action_note,
    9:action_yt,
    10:action_google,
    11:action_docs,
    12:action_fl_expl,
    13:action_battery,
    14:action_cpu,
    15:action_RAM,
    16:action_system,
    17:action_code,
    18:action_terminal,
    19:action_news,
    20:action_joke,
    21:action_quotes,
    22:action_facts,
}

commands={
    "what is time":1,
    "time":1,
    "tell me the time":1,
    "current time":1,
    "time please":1,
    "what is date":2,
    "date":2,
    "tell me the date":2,
    "today date":2,
    "date please":2,
    "what is your name":3,
    "who are you":3,
    "your name":3,
    "what i call you":3,
    "tell me the name":3,
    "how may i address you":3,
    "weather":4,
    "what is weather":4,
    "tell me the weather":4,
    "weather today":4,
    "todays weather":4,
    "how is the weather":4,
    "music":5,
    "i want to listen music":5,
    "play songs":5,
    "play music":5,
    "songs":5,
    "thankyou":6,
    "thankyou very much":6,
    "open camera":7,
    "camera":7,
    "can you click my picture":7,
    "i wanna see myself":7,
    "open notepad":8,
    "notepad":8,
    "youtube":9,
    "open youtube":9,
    "open google":10,
    "google":10,
    "chrome":10,
    "open chrome":10,
    "open browser":10,
    "browser":10,
    "show me documents":11,
    "open documents":11,
    "documents":11,
    "open file explorer":12,
    "file explorer":12,
    "show me file explorer":12,
    "show me files":12,
    "battery":13,
    "battery status":13,
    "show battery usage":13,
    "show battery use":13,
    "show battery":13,
    "display battery":13,
    "display battery use":13,
    "how much battery left":13,
    "show cpu usage":14,
    "show cpu use":14,
    "show cpu":14,
    "display cpu":14,
    "display cpu use":14,
    "cpu level":14,
    "cpu status":14,
    "cpu":14,
    "ram":15,
    "ram status":15,
    "show ram usage":15,
    "show ram use":15,
    "show ram":15,
    "display ram":15,
    "display ram use":15,
    "system status":16,
    "system":16,
    "open vscode":17,
    "open terminal":18,
    "news":19,
    "tell me news":19,
    "tell me headlines":19,
    "whats new":19,
    "joke":20,
    "tell me joke":20,
    "entertain me":20,
    "quotes":21,
    "tell me quote":21,
    "facts":22,
    "tell me facts":22,
}



def detect_intent(query,threshold=70):
    best_score=0
    best_intent=None

    for phrase,intent in commands.items():
        score=fuzz.ratio(query,phrase)
        if score>best_score:
            best_score=score
            best_intent=intent

    if best_score>=threshold:
        return best_intent
    return None

while True:
    print("Listening......")
    query=takecommand().lower()
    # query=input("Enter your command: ")

    if query in commands:
        intent=commands[query]
    else:
        intent=detect_intent(query)

    if intent is not None:
        action= intent_action.get(intent)
        if action:
            action()
    elif query=="":
        pass
    elif query.strip():
        print("Jarvis : Calling chatbot api for : "+query)
        ans=ask_ai(query)
        print(f"Jarvis : {ans}")
        say(ans)   
    else:
        print("something went wrong...")
  