from pyrogram.types		import InputMediaPhoto
from random 					import choice
from os import getenv as env

class Metabooru:		
	async def run(self, chan):
		print(type(self), flush=True)

		self.client 	= chan.session
		self.link_chan= chan.link

		img = await self.fetch_imgs()

		media = {	'photo' 	: img['file_url'],
							'caption' : await self.make_caption(img)}
							
		return media

	async def fetch_imgs(self):
		while True:
			try:
				json = await self.aio_request(self.link_search)

				for i in json:
					try:
						i['file_url']
					except:
						json.remove(i)
				
				return choice(json)
			except:
				asyncio.sleep(3)
		
	async def aio_request(self, link):
		async with self.client.request('GET', link) as response:
			response.raise_for_status()
			return await response.json()

	async def format_caption(self, img, titles, chars, booru):
		caption = self.link_chan
		caption+= ' <a href=\"https://t.me/joinchat/JHtZAaRg1G03Zjc0\">Universe</a>'		

		caption+= await self.format("\n**Title{}:**", titles)
		caption+= await self.format("\n**Character{}:**", chars)

		caption+=f'\n**{booru} ID:** {img["id"]}'

		return caption

	async def format(self, name, somelist):
		if somelist:
			if len(somelist) == 1:	return f"{name.format('' )} {somelist[0]}"
			else:										return f"{name.format('s')} {', '.join(set(somelist))}"
		else:											return ''