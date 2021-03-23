from os 					import getenv as env
from pyrogram			import Client
from channels 		import channels
from classes.lib	import Lib
import asyncio, aiohttp

app = Client('gabriel_imgbot', env('API_ID'), env('API_HASH'), bot_token=env('TG_TOKEN'))

def kprint(text):
	print(text, flush=True)
	return text

async def main():
	async with app:
		async with aiohttp.ClientSession() as session:
			Lib(app).turn_on()
			while True:
				for chan in channels:
					wait_time = await chan.check_and_send(app, session)
					await asyncio.sleep(wait_time)
				

app.run(main())
