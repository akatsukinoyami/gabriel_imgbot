from os import getenv as env
from engines.metabooru import Metabooru
from random import choice

class Danbooru(Metabooru):

	exclude_tags = {'safe' : "-rating%3Aexplicit+",
									'male' : "-male_focus+"}

	def __init__(self, tags):
		if type(tags) is str:	
			self.tags = f'&tags={tags.format(**self.exclude_tags)}'
		else:									
			self.tags = f'&tags={choice([tag.format(**self.exclude_tags) for tag in tags])}'

		self.link_search = f"https://danbooru.donmai.us/posts.json?format=json&random=1&limit=9{self.tags}"

	async def make_caption(self, img):
		split = lambda somestr: [x.replace('_',' ').title() for x in somestr.split(' ')]

		titles = split(img['tag_string_copyright'])
		chars = split(img['tag_string_character'])
		return await self.format_caption(img, titles, chars, "Danbooru")