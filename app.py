import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print("You said:", query)
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand.")
            return ""
        except sr.RequestError:
            speak("Service is down.")
            return ""

def calculate(expression):
    try:
        # Replace words with symbols
        expression = expression.replace("plus", "+").replace("minus", "-")
        expression = expression.replace("times", "").replace("multiplied by", "")
        expression = expression.replace("divided by", "/")
        result = eval(expression)
        return result
    except:
        return "Error"

# Main
speak("Say your calculation.")
query = get_audio()
if query:
    result = calculate(query)
    speak(f"The result is {result}")
