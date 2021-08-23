import speech_recognition as sr
import webbrowser
import os
import subprocess
from threading import Thread as thread
from time import sleep
import winapps
import sys

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
r = sr.Recognizer()

important_commands_code = "111"

def open_program(rs):
	path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
	#print(os.listdir(path))
	for file in os.listdir(path):
		if os.path.isdir(file):
			open_program(file)
		elif rs.replace("open ", "") in file.lower():
			print(os.path.join(path, file))
			thread(target = lambda a : os.system(f'"{os.path.join(path, file)}"'), args = (10, )).start()
			break

def main():
	while True:
		check = True
		with sr.Microphone() as source:
			print("Say something!")
			audio = r.listen(source)

		try:
			rs = r.recognize_google(audio).lower()
			print(rs)

			if "close yourself" in rs:
				sys.exit()
			if "shut down" in rs and important_commands_code in rs:
				os.system("shutdown /s /t 1")
			if "find" in rs or "search for" in rs:
				request = rs.replace("find", "").replace("search for", "").replace(" ", "+")
				thread(target = lambda a : webbrowser.get(chrome_path).open(f"http://www.google.com/search?q={request}"), args = (10, )).start()
				check = False
			if "translate" in rs:
				request = rs.replace("translate", "").replace(" ", "+")
				thread(target = lambda a : webbrowser.get(chrome_path).open(f"http://www.google.com/search?q={request}"), args = (10, )).start()
				check = False
			if "open" in rs:
				if "youtube" in rs:
					thread(target = lambda a : webbrowser.get(chrome_path).open("www.youtube.com/"), args = (10, )).start()
					check = False
				if "chrome" in rs:
					thread(target = lambda a : webbrowser.get(chrome_path).open("www.google.com"), args = (10, )).start()
					check = False
				if "steam" in rs:
					thread(target = lambda a : os.system('"C://Program Files (x86)//Steam//Steam.exe"'), args = (10, )).start()
					check = False
				if "discord" in rs:
					thread(target = lambda a : os.system('"C://Users//DANPRAV//AppData//Local//Discord//Update.exe --processStart Discord.exe"'), args = (10, )).start()
					check = False
				if "spotify" in rs:
					thread(target = lambda a : os.system('"C://Users//DANPRAV//AppData//Roaming//Spotify//Spotify.exe"'), args = (10, )).start()
					check = False
				if check:
					open_program(rs)

			
		except sr.UnknownValueError:
			print("Could not understand audio")
		except sr.RequestError as e:
			print(e)


if __name__ == "__main__":
    main()
















# for app in winapps.search_installed(rs):
			# 	print(app)
			# 	thread(target = lambda a : os.system(fr'"{str(app.install_location)}//{app.name}.exe"'), args = (10, )).start()