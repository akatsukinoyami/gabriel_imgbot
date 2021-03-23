from pyrogram.errors	import FloodWait, WebpageCurlFailed, MediaEmpty, MediaCaptionTooLong as errors
from engines.gelbooru	import Gelbooru
from engines.rule34		import Rule34
from engines.danbooru	import Danbooru
import time, traceback, asyncio, random, time

class Channel:
	def __init__(self, chan_id, gelbooru, rule34, danbooru):
		self.chan_id	= chan_id

		self.gelbooru	= Gelbooru(gelbooru)
		self.rule34		= Rule34(rule34 if rule34 else gelbooru)
		self.danbooru	= Danbooru(danbooru if danbooru else gelbooru)
		
	async def check_and_send(self, app, session):
		start_time = time.time()
					
		self.app		 = app
		self.session = session
		await self.namer()

		sended = 0
		while not sended:
			sended = await self.sender()

		end_time = time.time()
		return 85 - (int(end_time) - int(start_time))

	async def namer(self):
		chat = await self.app.get_chat(int(self.chan_id))

		self.title= chat.title
		self.link = f'<a href=\"{chat.invite_link}\">{chat.title}</a>'

	async def sender(self):
		media = {}
		try:
			img_engine	= await self.select_engine()
			media 			= await img_engine.run(self)
			return await self.app.send_photo(chat_id=int(self.chan_id), **media)

		except errors as e:
			if e.x is not None: await asyncio.sleep(e.x)
			return False

		except:
			return await self.app.send_message(-1001328058005, await self.format_error(media))

	async def select_engine(self):
		q = random.randint(1, 100)
		print(q)
		if q>90: 		return self.rule34
		elif q>55: 	return self.danbooru
		else:				return self.gelbooru

	async def format_error(self, media):
		
		txt = '**Bot: ** __@gabriel_imgbot__'
		txt+= f'\n**Chan:** __{self.link}__'

		if media:
			txt+= f'\n**Img URL:** <a href=\"{media["photo"]}\">Link</a>'
			txt+= f'\n**Caption:** {media["caption"]}' 

		txt+= f'\n**Taceback:**\n__{str(traceback.format_exc())}__'
		return txt
	
	async def make(self, app, msg):
		await self.renamer(app)

		await asyncio.sleep(5)
		return await msg.edit_text(f"{msg.text.html}\n{self.link}")