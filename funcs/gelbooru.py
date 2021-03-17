from os import getenv as env
from funcs.odict import odict

class Gelbooru:		
	async def gelbooru(self, client, tags, link_chan):
		self.client 	= client
		self.tags			= tags
		self.link_chan= link_chan
		self.link_gb	= f'https://gelbooru.com/index.php?page=dapi&q=index&json=1&api_key={env("GB_API_ID")}&user_id={env("GB_USER_ID")}'

		await self.fetch_link()
		url = self.img['file_url']

		await self.find_tags()
		await self.format_caption()
	
		return url, self.caption

	async def aio_request(self, link):
		async with self.client.request('GET', link) as response:
			response.raise_for_status()
			return await response.json()

	async def fetch_link(self):
		link_search = f"{self.link_gb}&s=post&limit=1&tags={self.tags}+sort%3arandom"

		json = await self.aio_request(link_search)

		self.img = json[0]

	async def find_tags(self):
		link_tags = f"{self.link_gb}&s=tag&names={self.img['tags'].replace(' ','+')}"
		json = await self.aio_request(link_tags)

		info = odict(char	= [], title	= [])

		for tag in json:
			if   tag['type'] == 'copyright': info.title.append(tag['tag'].replace('_',' ').title())
			elif tag['type'] == 'character': info.char.append(tag['tag'].replace('_',' ').title().split('(')[0])

		self.info = info

	async def format_caption(self):
		caption = self.link_chan
		caption+= ' <a href=\"https://t.me/joinchat/JHtZAaRg1G03Zjc0\">Universe</a>'		

		caption+= await self.format("\n**Title{}:**", self.info.title)
		caption+= await self.format("\n**Character{}:**", self.info.char)

		caption+=f'\n**ID:** {self.img["id"]}'

		self.caption = caption

	async def format(self, name, somelist):
		if somelist:
			if len(somelist) == 1:	return f"{name.format('' )} {somelist[0]}"
			else:										return f"{name.format('s')} {', '.join(set(somelist))}"
		else:											return ''

	