import tkinter as tk
import pyttsx3
import speech_recognition as sr
from PIL import Image, ImageTk
import os
from gtts import gTTS
import pygame
import io
import random


# ----------------------------  GET USERNAME
username = os.getlogin()





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
            text = recognizer.recognize_google(audio, language="en-US")
            text = text.lower()
            return text

    except sr.UnknownValueError:
        speak("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        speak(f"Could not request results from Google Speech Recognition service; {e}")
        return None








# ----------------------------  COMMANDE HANDLER
def launch_program(command):
    if command:
        if "start" in command or "lance" in command or "open" in command:
            if "start" in command:
                program_name = command.replace("start", "").strip()
                print(f"Attempting to start: {program_name}")
            elif "lance" in command:
                program_name = command.replace("lance", "").strip()
                print(f"Attempting to start: {program_name}")
            else:
                program_name = command.replace("open", "").strip()
                print(f"Attempting to start: {program_name}")

            if program_name == "notepad":
                os.system("notepad")  # Launch Notepad
                speak("Starting Notepad.")
            elif program_name == "calculator":
                os.system("calc")  # Launch Calculator
                speak("Starting Calculator.")
            elif program_name == "chrome":
                os.system('"C:/Program Files/Google/Chrome/Application/chrome.exe"')  # Launch Chrome
                speak("Starting Google Chrome.")
            elif program_name == "firefox":
                os.system('"C:/Program Files/Mozilla Firefox/firefox.exe"')  # Launch Firefox
                speak("Starting Mozilla Firefox.")
            elif program_name == "steam":
                os.system('"C:/Program Files (x86)/Steam/steam.exe"')  # Launch Steam
                speak("Starting Steam.")
            elif program_name in ["vscode", "vs code", "code", "vs"]:
                os.system(rf"code")  # Launch VS Code
                speak("Starting Visual Studio Code.")
            elif program_name in ["discord", "disc"]:
                os.system(rf'C:/Users/{username}/AppData/Local/Discord/Update.exe --processStart "Discord.exe"')  # Launch Discord
                speak("Starting Discord.")
            elif program_name == "vlc":
                os.system('"C:/Program Files/VideoLAN/VLC/vlc.exe"')  # Launch VLC Media Player
                speak("Starting VLC Media Player.")
            elif program_name == "spotify":
                os.system(rf"C:/Users/{username}/AppData/Roaming/Spotify/Spotify.exe")  # Launch Spotify
                speak("Starting Spotify.")
            elif program_name == "teams":
                os.system(rf"C:/Users/{username}/AppData/Local/Microsoft/Teams/current/Teams.exe")  # Launch Microsoft Teams
                speak("Starting Microsoft Teams.")
            elif program_name == "word":
                os.system('"C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"')  # Launch Microsoft Word
                speak("Starting Microsoft Word.")
            elif program_name == "photoshop":
                os.system('"C:/Program Files/Adobe/Adobe Photoshop <version>/Photoshop.exe"')  # Launch Photoshop
                speak("Starting Adobe Photoshop.")
            elif program_name in ["cmd", "cm"]:
                os.system("cmd.exe")  # Launch Command Prompt
                speak("Starting Command Prompt.")
            elif program_name == "explorer":
                os.system("explorer.exe")  # Launch File Explorer
                speak("Opening File Explorer.")
            else:
                speak(f"Sorry, I don't know how to start {program_name}.")
        else:
            speak(f"I understood: {command}")










#  ----------------------------  ONCLICK
def on_click(event=None):
    command = listen_for_command()
    if command:
        launch_program(command)







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
speak("Hello, I am chiken for Windows.")
is_shiny=0
if random.randrange(0, 172) == 9:
    is_shiny=1

create_bot_window()

