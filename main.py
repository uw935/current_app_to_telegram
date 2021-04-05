import os

os.system('pip install telethon')
os.system('pip install subprocess')
os.system('cls')

from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
import config, time, subprocess, time, datetime

print("Hi! This is TELEGRAM APP - TIME. If you have not entered the data, then enter your data in the config.py file for further work. If you have any questions or error - write me. \n \n Author: https://github.com/UW935\n TELEGRAM: @uw935. \n \n")

session_name = 'session'
ApiId = config.api_id
ApiHash = config.api_hash
a = 5

while a < 50:
	with TelegramClient(session_name, config.api_id, config.api_hash) as client:

		cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
		proc = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE)
		proc_output = [line.decode().rstrip() for line in proc.stdout if line.rstrip()]
		for i in range(3):
		 	print(proc_output[i])
 
		today = datetime.datetime.today()
		profile_bio = "🎮 | Plays now в" + proc_output[i] + " | " + today.strftime("%H:%M:%S")
		client(UpdateProfileRequest(about=profile_bio))
		time.sleep(30)

#говнокод))
