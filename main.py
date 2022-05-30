from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
import config, time, subprocess, time, datetime


print("Hi! This is TELEGRAM APP - TIME. If you have not entered the data, then enter your data in the config.py file for further work. If you have any questions or error - write me. \n \n Author: https://github.com/UW935\n TELEGRAM: @uw935. \n \n")

session_name = 'session'
ApiId = config.api_id
ApiHash = config.api_hash

cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'

with TelegramClient(session_name, config.api_id, config.api_hash) as client:
	sec = 0
	hour = 0
	mint = 0

	while True:
		proc = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE)
		proc_output = [line.decode().rstrip() for line in proc.stdout if line.rstrip()]

		if proc_output[2] == 'Discord' or 'Python':
			outp = proc_output[3]
		else:
			outp = proc_output[2]

		sec += 1
		time.sleep(1)

		if sec == 60:
			mint += 1

		elif sec == 3600:
			hour += 1
			a = 0

		profile_bio = f"🎮 | Now playing in {outp} | {hour}:{mint}:{sec}"

		client(UpdateProfileRequest(about=profile_bio))
		time.sleep(30)

		sec = sec + 30

