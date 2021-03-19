from os 				import getenv as env
from pyrogram		import Client
from channels 	import channels
import asyncio, aiohttp, time

app = Client('gabriel_imgbot', env('API_ID'), env('API_HASH'), bot_token=env('TG_TOKEN'))

def kprint(text):
	print(text, flush=True)
	return text

async def main():
	async with app:
		async with aiohttp.ClientSession() as session:
			msg = await app.send_message(-1001328058005, '**Bot:** __@gabriel_imgbot__\n Started work.\n')
			while True:
				for chan in channels:
					start_time = int(kprint(time.time()))

					await chan.check_and_send(app, session)

					end_time = int(kprint(time.time()))
					wait_time = kprint(85 - (end_time - start_time))
					await asyncio.sleep(wait_time)
				

app.run(main())
