import speech_recognition
from playsound import playsound
from gtts import gTTS

vd={"apple":"a fruit","potato":"a vegetable"}

def voicedict():
    voice=speech_recognition.Recognizer()#creating voice recognizer
    #now setting the source
    with speech_recognition.Microphone() as source:
        print("Speak the Word ......")
        voiceword=voice.listen(source)
        flag=0
        
        try:
            textword=voice.recognize_google(voiceword,language="en-us")
            for key in vd:
                if key==textword.lower():
                    flag=1
                    tts=gTTS(vd[key],lang="en-us")
                    tts.save("value.mp3")
                    print(textword.lower())
                    playsound("value.mp3")
                    print(vd[key])
                    break
            if(flag==0):
                print("this word is not defined in dictionary")
        except:
            print("try again.....")
        
if __name__=="__main__":
    voicedict()
