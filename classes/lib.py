import time, dns.resolver 

class Lib:
	config_id	= -1001328058005

	def __init__(self, app):
		self.app = app

	async def turn_on(self, app):
		self.bot = await app.get_me()

		txt = f'**Turned on bot:**'
		txt+= f'\n`User:     {self.bot.first_name}`'
		txt+= f'\n`Username: @{self.bot.username}`'
		txt+= f'\n`User ID:  {self.bot.id}`'
		txt+= f'\n`Time:     {time.strftime("%y/%m/%d %H:%M:%S", time.localtime())}`'
		txt+= f'\n`IP:       {self.find_ip()}`'

		self.username = self.bot.username
		await app.send_message(self.config_id, txt)

	@staticmethod
	def find_ip():
		resolver = dns.resolver.Resolver(configure=False)
		resolver.nameservers = ["208.67.222.222", "208.67.220.220"]
		return resolver.query('myip.opendns.com')[0]