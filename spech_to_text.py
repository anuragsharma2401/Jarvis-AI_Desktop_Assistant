import speech_recognition as sr 

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold=0.5
        try :
            audio=r.listen(source)
            query=r.recognize_google(audio,language="en-in")
            print(f"User : {query}")
            return query
        except sr.WaitTimeoutError:
            print("No Speech Detected")
            return ""
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return 'No internet connect please turn on you internet'