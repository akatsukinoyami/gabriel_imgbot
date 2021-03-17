from pyrogram.errors import FloodWait, WebpageCurlFailed, MediaEmpty
from funcs.gelbooru import Gelbooru
import time, traceback, asyncio

class Channel:
	def __init__(self, chan_id, minutes, tags):
		self.chan_id	= chan_id
		self.minutes	= minutes
		self.tags 		= tags
		self.title		= ''
		self.link			= ''

	async def renamer(self, app):
		chat = await app.get_chat(int(self.chan_id))
		self.title= chat.title
		self.link = f'<a href=\"{chat.invite_link}\">{chat.title}</a>'
		
	async def check_and_send(self, app, session):
		sended = False
		if int(self.minutes) == int(time.strftime('%M')): 
			if not self.title: 
				await self.renamer(app)
			while not sended:
				sended = await self.sender(app, session)
		return sended

	async def sender(self, app, session):
		try:
			url, caption = None, None
			url, caption = await Gelbooru().gelbooru(session, self.tags, self.link)
			return await app.send_photo(chat_id=int(self.chan_id), photo=url, caption=caption)
		except (WebpageCurlFailed, MediaEmpty, FloodWait) as e:
			if e.x is not None: await asyncio.sleep(e.x)
			return False
		except:
			return await app.send_message(-1001328058005, await self.format_error(url, caption))

	async def format_error(self, url, caption):
		txt = '**Bot: ** __@gabriel_imgbot__'
		txt+= f'\n**Chan:** __{self.link}__'
		txt+= f'\n**Img URL:** <a href=\"{url}\">Link</a>' if url is not None else ''
		txt+= f'\n**Caption:** {caption}' if caption is not None else ''
		txt+= f'\n**Taceback:**\n__{str(traceback.format_exc())}__'
		return txt
	
	async def make(self, app, msg):
		if not self.title: 
			await self.renamer(app)

		await asyncio.sleep(5)
		return await msg.edit_text(f"{msg.text.html}\n{self.link}")