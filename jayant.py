#For printing Large Jayant
import pyfiglet

#For Converting Language
import googletrans

#For Getting human voice
import speech_recognition

#For text to speech
import gtts

#For Playing Sound
import playsound

#Declare Some Global Variable
input_lang="hi"
output_lang="en"
name=1
developer="Jayant"

#Use Exception Handling
try:

    #Use Pyfiglet module for printing name
    pri=pyfiglet.figlet_format('Jayant')
    print(pri)

    
    print(f"Developer:'{developer}'")
    print('Welcome To Voice Translator')
    print('\n')

    #Create while loop Continue working 
    while True:

        print("Choose 1:For Continue")
        print("Choose 0:For Exit")

        #Taking Input Form User
        choose=int(input("Enter Your Choice:"))

        #Use if condition for code is run or not
        if choose==1:

            #For Getting voice of Human or User and compulsary to use (with)
            recognizer=speech_recognition.Recognizer()
            with speech_recognition.Microphone() as source:
                print("Speak Now")
                voice=recognizer.listen(source)
                text=recognizer.recognize_google(voice,language=input_lang)
                print(text)

            #Use googletrans module for converting Language
            translator=googletrans.Translator()
            translation=translator.translate(text,dest=output_lang)
            print(translation.text)

            #Converting text to audio
            convert_audio=gtts.gTTS(translation.text,lang=output_lang)
            convert_audio.save(f'one{name}.mp4')

            #For playing Audio
            playsound.playsound(f'one{name}.mp4')

            #take name and increment it because compulsary to change file convert audio file
            name+=1

        # Use elif For Exit the while loop or program
        elif choose==0:
            break

        # else use if user press wrong Number
        else:
            print("\nPlease Choose Valid Number\n")

#Use Except if try block is not executed,then work except block
except:
    print("\nCode is Not Correct\n")
