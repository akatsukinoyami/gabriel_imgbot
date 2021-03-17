from os import getenv as env
import traceback

async def fetch_link(client, tags, posts='1', random=True, api_id=env('GB_API_ID'), user_id=env('GB_USER_ID'), json=True):
	""" Return link to gelbooru.com with selected options. (posts=1, random=True, api_id=env GB_USER_ID, user_id=env GB_USER_ID, json=True for json, False for XML)"""
	
	random 	= '+sort%3arandom'	if random else ''
	json 		= '&json=1' 				if json		else ''
	tags		= f'&tags={tags}'
	posts		= f'&limit={str(posts)}'
	api_id	= f'&api_key={api_id}'
	user_id	=	f'&user_id={user_id}'

	link = f"https://gelbooru.com/index.php?page=dapi&s=post&q=index{posts}{json}{tags}{random}{api_id}{user_id}"

	async with client.request('GET', link) as response:
		response.raise_for_status()
		json =  await response.json()

	img				= json[0]

	return img

async def find_tags(client, tags):
	characters = []
	titles = []
	url = f"https://gelbooru.com/index.php?page=dapi&s=tag&q=index&json=1&names={tags.replace(' ','+')}"
	async with client.request('GET', url) as response:
		response.raise_for_status()
		json = await response.json()

	for tag in json:
		if tag['type'] == 'copyright': titles.append(tag['tag'])
		elif tag['type'] == 'character': characters.append(tag['tag'])

	return characters, titles

async def gelbooru(client, tags):
	img	= await fetch_link(client, tags)
	file_url	= img['file_url']
	characters, titles = await find_tags(client, img['tags'])
	
	return file_url, characters, titles

	