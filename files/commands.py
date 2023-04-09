import pyttsx3
import speech_recognition as sr



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
      
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        query=query.lower()
        print(f"User said: {query}\n") 
    except Exception as e:
        print(e)
        print('Say that again please...')     
        return 'None'
    return query

def check_message(check,query):
    message_words=query.split()  
    if set(check).issubset(set(message_words)):
        return True
    else:
        return False
