import speech_recognition
from playsound import playsound
from gtts import gTTS

vd={"apple":"a fruit","potato":"a vegetable"}

def voicedict():
    voice=speech_recognition.Recognizer()#creating voice recognizer
    #now setting microphone as the source of voice....
    with speech_recognition.Microphone() as source:
        print("Speak the Word ......")
        voiceword=voice.listen(source)#using the listen function to listen voice through Microphone using recognizer.
        flag=0
        
        try:
            textword=voice.recognize_google(voiceword,language="en-us")#now converting the speech recognized in text in english language using recognize_google( ) function with recognizer(voice).
            for key in vd:
                if key==textword.lower():
                    flag=1
                    tts=gTTS(vd[key],lang="en-us")#now converting the value of key from text to speech using gTTS function..
                    tts.save("value.mp3")#now saving the file using save( ).
                    print(textword.lower())
                    playsound("value.mp3")#and now playing the sound file using playsound( ) function.
                    print(vd[key])
                    break
            if(flag==0):
                print("this word is not defined in dictionary")
        except:
            print("try again.....")
        
if __name__=="__main__":
    voicedict()

