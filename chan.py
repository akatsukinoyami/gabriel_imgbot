from engines.gelbooru import gelbooru
import time

class Channel:
	def __init__(self, chan_id, minutes, gelbooru_tags):
		self.chan_id				= chan_id
		self.minutes				= minutes
		self.gelbooru_tags 	= gelbooru_tags
		self.title					= ''
		self.link						= ''

	async def check_and_send(self, app, session):
		diff = int(self.minutes) - int(time.strftime('%M'))

		try:
			if int(self.minutes) == int(time.strftime('%M')): 
				await self.sender(app, session)
				return True
			else:
				return False
		except:
			txt = '**Bot: ** __@gabriels_imgbot__'
			txt+= f'\n**Chan:** __{self.title}'
			txt+= f'\n**Taceback:**\n{str(traceback.format_exc())}'
			await app.send_message(-1001328058005, txt)
			await self.sender(app, session)

	async def sender(self, app, session):
		if not self.title: 
			await self.renamer(app)
			
		chat_id = int(self.chan_id)
		file_url, characters, titles = await gelbooru(session, self.gelbooru_tags)

		caption = await self.caption_formatter(characters, titles)
		
		await app.send_photo(chat_id=chat_id, photo=file_url, caption=caption)
		

	async def renamer(self, app):
		chat = await app.get_chat(int(self.chan_id))
		self.title= chat.title
		self.link = f'<a href=\"{chat.invite_link}\">{self.title}</a>'

	async def caption_formatter(self, characters, titles):
		caption = ''
		if titles:
			caption+= '\n**Titles:** '  
			caption+= ', '.join([title.replace('_',' ').title() for title in titles])
		if characters:
			caption+= '\n**Characters:** '  
			caption+= ', '.join([char.replace('_', ' ').title().split('(')[0] for char in characters])

		caption+= f'\n{self.link} '
		caption+= '<a href=\"https://t.me/joinchat/JHtZAaRg1G03Zjc0\">Universe</a>'

		return caption

