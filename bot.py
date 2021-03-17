from os import getenv as env
from pyrogram	import Client
from channels import channels
import asyncio, aiohttp, time

app = Client('gabriel_imgbot', env('API_ID'), env('API_HASH'), bot_token=env('TG_TOKEN'))

async def main():
	async with app:
		async with aiohttp.ClientSession() as session:
			msg = await app.send_message(-1001328058005, '**Bot:** __@gabriel_imgbot__\n Started work.')
			while True:
				for chan in channels:
					await chan.check_and_send(app, session)
					#msg = await chan.make(app, msg)
				await asyncio.sleep(58)

app.run(main())
