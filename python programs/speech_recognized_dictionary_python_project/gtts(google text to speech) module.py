from gtts import gTTS#importing google text to speech for converting the text to audio.
from playsound import playsound# importing playsound function from playsound module to play the specified audio file.
import speech_recognition#importing speech_recognition module to recognize the voice of the user.
def audio():
    tts=gTTS("chalo chaltein hai thik hai na hoooray.mp3",lang="hi")
    tts.save("hindi.mp3")#save function to save the file.
    playsound("hindi.mp3")
    
def audioarg(txt):#we cannot use 2 functions with same name
    tts=gTTS(txt,lang="en-us")
    tts.save("argumented audio.mp3")
    playsound("argumented audio.mp3")

def voicerecog():
    r=speech_recognition.Recognizer()#to recognize we create a recognizing variable.
    with speech_recognition.Microphone() as source:#and using Microphone( ) we set microphone as the source of the input of the voice or sound.
        print("Say Something ..... ")
        audio=r.listen(source)#using listen function we tell the source to recognize the voice.
        print(audio)

        try:
            print("converting....")
            auden=r.recognize_google(audio,language="en-us")# now converting the voice recognized to english-us language.
            print(auden)
        except Exception as e:
            print("unable to recognize.... try again....")
        
if __name__=="__main__":#using the main function we are calling the functions.
    audio()
    argument="hello , its me."
    audioarg(argument)
    voicerecog()
