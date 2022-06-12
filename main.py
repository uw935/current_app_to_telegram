from telethon.sync import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.account import UpdateProfileRequest
import time, subprocess, time, datetime, appsettings


print("Author: https://github.com/uw935/ \nTelegram: @uw935.\n")
print("Please, use CTRL+C to exit\n\n")

API_ID   = int(input("Enter you API ID: "))
API_HASH = str(input("Enter you API HASH: "))

def telegApp():
	print("\nYou select: current app to telegram")
	print("Program started. Use CTRL+C to exit\n\n\n\n")

	sec  = 00
	mint = 00
	hour = 00

	while True:
			try:
				proc = subprocess.Popen('powershell "gps | where {$_.MainWindowTitle } | select Description', shell=False, stdout = subprocess.PIPE)
				proc_output = [line.decode().rstrip() for line in proc.stdout if line.rstrip()]
				
				outp = proc_output[2]

				if proc_output[2] == '-----------':
					print("No app found")
					break

				if proc_output[2] == 'Discord' or 'Python':
					try:
						outp = proc_output[3]
					except:
						outp = proc_output[2]
				
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
				break

def telegTime():
	print("\nYou select: current time to telegram\n")
	print("Program started. Use CTRL+C to exit\n\n\n\n")

	while True:
		try:
			today = datetime.datetime.today()

			client(UpdateProfileRequest(about = "🕓 | Current local time: " + today.strftime("%H:%M:%S")))
			time.sleep(15)

		except:
			client(UpdateProfileRequest(about = bionow))
			break

with TelegramClient('session', API_ID, API_HASH) as client:
	bionow = str(client(GetFullUserRequest(client.get_me().username)).about)

	print(f"\nSuccessfully connected as {client.get_me().username}")

	while True:
		print("\nMENU: \n\n[1] - current time to telegram\n[2] - current app to telegram\n[3] - exit\n\n")
		action = int(input("Just send number. Select an action from the menu: "))

		if action == 1:
			telegTime()
				
		elif action == 2:
			telegApp()

		elif action == 3:
			client(UpdateProfileRequest(about = bionow))
			client.disconnect()
			break

		else:
			print("\nUnknown command")






