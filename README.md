# Chicken for Windows

Hello hi welcome! Chicken For Windows is a small project that I did on my free time! It's a bit of a desktop assistant, it can open apps for you and open web pages too. As it's powered by Gemini, you can ask it anything really!

## Requirements

Everything's in the requirement.txt, you can pip install all of these!

## The code

What I do here is that I use Gemini as my ai model and prompt it to answer in a specific way, you can check it all out no problem! i'll update this readme when I have time! Note that you should use your own gemini key in .env, you can create one here[https://aistudio.google.com/app/apikey].

.env
```
GEMINI_KEY_API=put_your_key_here
```

## The exe

I used pyinstall to create an executable:
C:/Users/{username}/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0/LocalCache/local-packages/Python311/Scripts/pyinstaller --onefile --noconsole --icon=icone.ico CFW.py
