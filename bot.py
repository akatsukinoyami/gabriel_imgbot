from os import getenv as env
from pyrogram	import Client
from channels import channels
import asyncio, aiohttp

app = Client('gabriel_imgbot', env('API_ID'), env('API_HASH'), bot_token=env('TG_TOKEN'))

async def main():
	async with app:
		async with aiohttp.ClientSession() as session:
			while True:
				for chan in channels:
					await chan.check_and_send(app, session)
				await asyncio.sleep(60)

			
app.run(main())
