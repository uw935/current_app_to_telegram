from telethon.sync import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.account import UpdateProfileRequest
import time, subprocess, time, datetime, appsettings


print("Author: https://github.com/uw935/ \nTelegram: @uw935.\n")
print("Please, use CTRL+C to exit\n\n")

API_ID   = int(input("Enter you API ID: "))
API_HASH = str(input("Enter you API HASH: "))


with TelegramClient('session', API_ID, API_HASH) as client:
	bionow = str(client(GetFullUserRequest(client.get_me().username)).about)

	print(f"\nSuccessful connected as {client.get_me().username}")

	sec  = 00
	mint = 00
	hour = 00

	while True:

		try:
			proc = subprocess.Popen('powershell "gps | where {$_.MainWindowTitle } | select Description', shell=False, stdout = subprocess.PIPE)
			proc_output = [line.decode().rstrip() for line in proc.stdout if line.rstrip()]
			outp = proc_output[2]

			if proc_output[2] == 'Discord' or 'Python':
				outp = proc_output[3]
			
			for x in appsettings.app:
				if x in outp.lower():
					delt = appsettings.app[x]

			if delt:
				delt = delt
			else:
				delt = 'playing'

			if sec >= 60:
				mint += 1
				sec = 0

			elif sec >= 3600:
				hour += 1
				sec = 00

			client(UpdateProfileRequest(about = f"🎮 | Now {delt} in {outp} | {hour}:{mint}:{sec}"))
			time.sleep(15)

			sec += 15

		except:
			client(UpdateProfileRequest(about = bionow))
			client.disconnect()
			



