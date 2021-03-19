from os import getenv as env
from engines.metabooru import Metabooru

class Rule34(Metabooru):		
	exclude_tags = {'safe' : "-rating%3Aexplicit+",}
	link_gb= f'https://gelbooru.com/index.php?page=dapi&q=index&json=1&api_key={env("GB_API_ID")}&user_id={env("GB_USER_ID")}'

	link_rl= f'https://rule34.xxx/index.php?page=dapi&s=post&q=index&json=1'

	def __init__(self, tags):
		deny_tags = "-photo_(medium)+-curvy+-asphyxiation+-fur+-video+-male_focus+-animated+-pregnant+-trap+-futanari+-body-horror+-guro+-yaoi+-abs+-muscular+-vore+-gigantic_breasts+-pokemon+-sonic_%28series%29+"

		tags = tags.format(**self.exclude_tags)
		self.link_search = f"{self.link_rl}&s=post&limit=9&tags={deny_tags}{tags}+sort%3arandom"

	async def find_tags(self, tags):
		link_tags = f"{self.link_gb}&s=tag&names={tags.replace(' ','+')}"
		json = await self.aio_request(link_tags)

		info = dict(title=[],char=[])

		for tag in json:
			if   tag['type'] == 'copyright': info['title'].append(tag['tag'].replace('_',' ').title())
			elif tag['type'] == 'character': info['char'].append(tag['tag'].replace('_',' ').title().split('(')[0])

		return info

	async def make_caption(self, img):
		info 	= await self.find_tags(img['tags'])
		return await self.format_caption(img, info['title'], info['char'], "Rule34")