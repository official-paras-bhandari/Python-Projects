import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by paras")
    while True:
        x = input("Enter what do you want me to speak: ")
        if x == "q":
            break
        command = f'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\');"'
        os.system(command)
