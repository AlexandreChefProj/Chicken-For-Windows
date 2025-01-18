import tkinter as tk
import pyttsx3
import speech_recognition as sr
import subprocess
from PIL import Image, ImageTk
import os

username = os.getlogin()


# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for a command (with a 5-second time limit)
def listen_for_command():
    recognizer = sr.Recognizer()
    
    # List all available microphones
    mic_list = sr.Microphone.list_microphone_names()
    mic_index = 0  # You can change this index if you want to select a different microphone

    # Print the name of the microphone being used
    print(f"Listening for command using {mic_list[mic_index]} from {mic_list}")
    
    # Start listening for a command from the selected microphone
    with sr.Microphone(device_index=mic_index) as source:
        recognizer.adjust_for_ambient_noise(source)
        
        print("Listening...")

        # Listen for a maximum of 5 seconds
        try:
            speak("I'm listening!")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio)
            print(f"Raw command received: {command}")  # Print the exact recognized text
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            speak("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            print("Could not request results, check your internet connection.")
            speak("Could not request results, check your internet connection.")
            return None
        except sr.WaitTimeoutError:
            print("Listening timed out, please try again.")
            speak("Listening timed out, please try again.")
            return None

# Function to launch a program based on the command
def launch_program(command):
    if command:
        if "start" in command or "lance" in command:
            if "start" in command:
                program_name = command.replace("start", "").strip()
                print(f"Attempting to start: {program_name}")
            else:
                program_name = command.replace("lance", "").strip()
                print(f"Attempting to start: {program_name}")

            # Example: launch a program based on the command
            if program_name == "notepad":
                subprocess.run("notepad")  # Launch Notepad
                speak("Starting Notepad.")
            elif program_name == "":
                speak("I only heard start.")
            elif program_name == "calculator":
                subprocess.run("calc")  # Launch Calculator
                speak("Starting Calculator.")
            elif program_name == "chrome":
                subprocess.run("C:/Program Files/Google/Chrome/Application/chrome.exe")  # Launch Chrome
                speak("Starting Google Chrome.")
            elif program_name == "firefox":
                subprocess.run("C:/Program Files/Mozilla Firefox/firefox.exe")  # Launch Firefox
                speak("Starting Mozilla Firefox.")
            elif program_name == "steam":
                subprocess.run("C:/Program Files (x86)/Steam/steam.exe")  # Launch Steam
                speak("Starting Steam.")
            elif program_name == "vscode" or program_name == "vs code" or program_name == "code" or program_name == "vs":
                subprocess.run(f"fC:/Users/{username}/AppData/Local/Programs/Microsoft VS Code/Code.exe")  # Launch VS Code
                speak("Starting Visual Studio Code.")
            elif program_name == "discord" or program_name == "disc":
                subprocess.run(f'C:/Users/{username}/AppData/Local/Discord/Update.exe --processStart "Discord.exe"')  # Launch Discord
                speak("Starting Discord.")
            elif program_name == "vlc":
                subprocess.run("C:/Program Files/VideoLAN/VLC/vlc.exe")  # Launch VLC Media Player
                speak("Starting VLC Media Player.")
            elif program_name == "spotify":
                subprocess.run(f"C:/Users/{username}/AppData/Roaming/Spotify/Spotify.exe")  # Launch Spotify
                speak("Starting Spotify.")
            elif program_name == "teams":
                subprocess.run(f"C:/Users/{username}/AppData/Local/Microsoft/Teams/current/Teams.exe")  # Launch Microsoft Teams
                speak("Starting Microsoft Teams.")
            elif program_name == "word":
                subprocess.run("C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE")  # Launch Microsoft Word
                speak("Starting Microsoft Word.")
            elif program_name == "photoshop":
                subprocess.run("C:/Program Files/Adobe/Adobe Photoshop <version>/Photoshop.exe")  # Launch Photoshop
                speak("Starting Adobe Photoshop.")
            elif program_name == "cmd" or program_name == "cm":
                subprocess.run("cmd.exe")  # Launch Command Prompt
                speak("Starting Command Prompt.")
            elif program_name == "explorer":
                subprocess.run("explorer.exe")  # Launch File Explorer
                speak("Opening File Explorer.")
            

            else:
                speak(f"Sorry, I don't know how to start {program_name}.")
        else:
            speak("Please say 'Start' followed by the program name.")
    else:
        print("No command recognized.")

# Function to handle click event
def on_click(event=None):
    command = listen_for_command()
    if command:
        launch_program(command)

# Create main bot window
def create_bot_window():
    root = tk.Tk()
    root.title("Screen Bot")
    root.geometry("200x200")
    root.attributes("-topmost", True)
    root.overrideredirect(1)  # Remove window decorations
    root.wm_attributes("-transparentcolor", "white")
    root.bind("<Control-q>", lambda e: root.destroy())

    # Load and display character image
    img = Image.open("torchic1.png").resize((200, 200))
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo, bg="white")
    label.image = photo
    label.pack()
    label.bind("<Double-1>", on_click)

    # Drag window functionality
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

# Run the bot
speak("Hello, I am chiken for Windows.")
create_bot_window()

