from pyrogram.errors	import FloodWait, WebpageCurlFailed, MediaEmpty
from engines.gelbooru	import Gelbooru
from engines.danbooru	import Danbooru
from random 					import choice
import time, traceback, asyncio

class Channel:
	def __init__(self, chan_id, gelbooru, danbooru):
		self.chan_id	= chan_id
		self.gelbooru	= Gelbooru(gelbooru)
		self.danbooru = Danbooru(danbooru if danbooru else gelbooru)
		
	async def check_and_send(self, app, session):
		self.app		 = app
		self.session = session
		await self.namer()

		sended = 0
		while not sended:
			sended = await self.sender()

	async def namer(self):
		chat = await self.app.get_chat(int(self.chan_id))

		self.title= chat.title
		self.link = f'<a href=\"{chat.invite_link}\">{chat.title}</a>'

	async def sender(self):
		try:
			img_engine = choice((self.gelbooru, self.danbooru))
			media = await img_engine.run(self)
			return await self.app.send_photo(chat_id=int(self.chan_id), **media)

		except (WebpageCurlFailed, MediaEmpty, FloodWait) as e:
			if e.x is not None: await asyncio.sleep(e.x)
			return False

		except:
			return await self.app.send_message(-1001328058005, await self.format_error(media_group))

	async def format_error(self, media_group):
		
		txt = '**Bot: ** __@gabriel_imgbot__'
		txt+= f'\n**Chan:** __{self.link}__'

		if media_group:
			q = 0
			for i in media_group:
				q+=1
				txt+= f'\n**Img URL ({q}):** <a href=\"{i[0]}\">Link</a>'
				txt+= f'\n**Caption ({q}):** {i[1]}' 

		txt+= f'\n**Taceback:**\n__{str(traceback.format_exc())}__'
		return txt
	
	async def make(self, app, msg):
		await self.renamer(app)

		await asyncio.sleep(5)
		return await msg.edit_text(f"{msg.text.html}\n{self.link}")