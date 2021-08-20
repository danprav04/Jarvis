import speech_recognition as sr
import webbrowser
import os
import subprocess
from threading import Thread as thread
from time import sleep
import winapps

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
r = sr.Recognizer()

for app in winapps.list_installed():
    print(app)
    print("# " * 100)

while True:
	with sr.Microphone() as source:
		print("Say something!")
		audio = r.listen(source)

	try:
		rs = r.recognize_google(audio).lower()
		print(rs)

		if "chrome" in rs:
			thread(target = lambda a : webbrowser.get(chrome_path).open("www.google.com"), args = (10, )).start()
		if "steam" in rs:
			thread(target = lambda a : os.system('"C://Program Files (x86)//Steam//Steam.exe"'), args = (10, )).start()
		if "discord" in rs:
			thread(target = lambda a : os.system('"C://Users//DANPRAV//AppData//Local//Discord//Update.exe --processStart Discord.exe"'), args = (10, )).start()
		if "spotify" in rs:
			thread(target = lambda a : os.system('"C://Users//DANPRAV//AppData//Roaming//Spotify//Spotify.exe"'), args = (10, )).start()
			



	except sr.UnknownValueError:
		print("Could not understand audio")
	except sr.RequestError as e:
		print(" {0}".format(e))

