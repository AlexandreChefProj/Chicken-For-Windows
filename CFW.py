import tkinter as tk
import pyttsx3
import speech_recognition as sr
from PIL import Image, ImageTk
import os
from gtts import gTTS
import pygame
import io
import random
import webbrowser
from ai import feed_ai



# ----------------------------  SPEAK
engine = pyttsx3.init()
def speak(text):
    # generate speech using gTTS
    tts = gTTS(text)
    
    # convert the speech to a byte stream
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    # initialize pygame mixer and play the byte stream
    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()









# ----------------------------  LISTEN
def listen_for_command():
    recognizer = sr.Recognizer()
    
    mic_list = sr.Microphone.list_microphone_names()
    mic_index = 0
    print(f"debug: Listening for command using {mic_list[mic_index]} from {mic_list}")
    try:
        with sr.Microphone() as source:
            print("Calibrating microphone...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            speak("I'm ready!")
            audio = recognizer.listen(source)

            # audio save
            with open("recorded_audio.wav", "wb") as f:
                f.write(audio.get_wav_data())

            print("Recognizing...")
            text = recognizer.recognize_google(audio, language="fr-FR")
            text = text.lower()
            return text

    except sr.UnknownValueError:
        speak("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        speak(f"Could not request results from Google Speech Recognition service; {e}")
        return None




def writefile(file,text):
    with open(file, "w") as file:
            file.write(text)

def readfile(file):
    with open(file, "r") as file:
        return file.read()


# ----------------------------  COMMANDE HANDLER
def launch_program(ai_input):
    lines = ai_input.splitlines()

    command = lines[0] if len(lines) > 0 else None
    line = lines[1] if len(lines) > 1 else None
    pref = lines[2] if len(lines) > 2 else None
    text = "\n".join(lines[3:]) if len(lines) > 3 else None
    if command != 'none':
        print(command)
        if "cmd" in command:
            os.system(line)
        elif "web" in command:
            webbrowser.open(line)
    if pref != 'none' :
        newpref = readfile("pref.txt")+ f"\n{pref}"
        writefile('pref.txt', newpref)
    speak(text)










#  ----------------------------  ONCLICK
def on_click(event=None):
    command = listen_for_command()
    if command:
        ai_output=feed_ai(command)
        print(ai_output)
        launch_program(ai_output)







#  ----------------------------  WINDOW
def create_bot_window():
    root = tk.Tk()
    root.title("Screen Bot")
    root.geometry("200x200")
    root.attributes("-topmost", True)
    root.overrideredirect(1)  # window decoration off
    root.wm_attributes("-transparentcolor", "white")
    root.bind("<Control-q>", lambda e: root.destroy())

    # image handle click
    if is_shiny == 1:
        img = Image.open("torchic1.png").resize((200, 200))
    else:
        img = Image.open("torchic2.png").resize((200, 200))
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo, bg="white")
    label.image = photo
    label.pack()
    label.bind("<Double-1>", on_click)


    # drag window
    def start_drag(event):
        root.x = event.x
        root.y = event.y

    def drag(event):
        x = root.winfo_x() + (event.x - root.x)
        y = root.winfo_y() + (event.y - root.y)
        root.geometry(f"+{x}+{y}")

    label.bind("<Button-1>", start_drag)
    label.bind("<B1-Motion>", drag)

    root.mainloop()






#  ----------------------------  START
speak("Hello, I am chicken for Windows.")
is_shiny=0
if random.randrange(0, 172) == 9:
    is_shiny=1

create_bot_window()

