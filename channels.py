from chan import Channel
from funcs.odict import odict

alldeny = "-photo_(medium)+-curvy+-asphyxiation+-male_focus+-animated+-pregnant+-trap+-futanari+-body-horror+-guro+-yaoi+-abs+-muscular+-vore+-gigantic_breasts+-pokemon+"

deny = odict()
deny.char = f"{alldeny}-fellatio+-cum+-handjob+-sex+-clothed_sex+-penis+"
deny.lewd = f"{alldeny}-rating%3Asafe+"
deny.maid = alldeny

channels = (
	# 🦊 Themes
	Channel(-1001419557426,  1, f'{deny.char}greyscale+solo+1girl'), 										# 🦊 KuroShiro Sekai
	Channel(-1001292197663,  2, f'{deny.lewd}tentacle'), 																# 🦊 Tentacle Shop
	Channel(-1001306394316,  3, f'{deny.lewd}bdsm+-tentacle'), 													# 🦊 BDSM Castle
	Channel(-1001299479472,  4, f'{deny.lewd}{{exhibitionism+~+public}}'),							# 🦊 Exhibitionists Park
	
	Channel(-1001464474211,  7, f'{deny.lewd}{{sex_toy+~+dildo+~+vibrator}}'),					# 🦊 Sex Toys Department
	Channel(-1001268723500,  8, f'{deny.lewd}{{anal+~+vibrator_in_anus+~+anal_object_insertion}}'),# 🦊 Anal World
	Channel(-1001303621559,  9, f'{deny.maid}{{maid+~+maid_apron+~+maid_headdress}}'), 	# 🦊 Maid Mansion
	Channel(-1001341064178, 10, f'{deny.lewd}yuri'), 																		# 🦊 Yuri State

	# 🦊 Characters
	Channel(-1001170899702, 11, f'{deny.char}holo'), 																		# 🦊 Horo (Spice&Wolf)
	Channel(-1001225481381, 12, f'{deny.char}c.c.'), 																		# 🦊 C.C. (Code Geass)
	Channel(-1001210561500, 13, f'{deny.char}albedo_(overlord)'), 											# 🦊 Albedo (Overlord)
	Channel(-1001357421249, 14, f'{deny.char}zero_(zero_kara_hajimeru_mahou_no_sho)'),	# 🦊 Zero Kara Hajimeru Mahou no Sho
	Channel(-1001305843261, 15, f'{deny.char}yoko_littner'), 														# 🦊 Yoko (Tengen Toppa Gurren Lagann)
	Channel(-1001264811314, 16, f'{deny.char}shiina_mashiro'),													# 🦊 Mashiro (Sakura-sou no Pet na Kanojo)
	Channel(-1001180690168, 17, f'{deny.char}fkey'),																		# 🦊 @fkey123
	Channel(-1001375873369, 18, f'{deny.char}ia_(vocaloid)'),														# 🦊 IA Colourful
	Channel(-1001299485270, 19, f'{deny.char}{{grea_(shingeki_no_bahamut)+~+manaria_friends}}'),# 🦊 Grea (Shingeki no Bahamut)
	
	Channel(-1001398979215, 22, f'{deny.char}elaina_(majo_no_tabitabi)'), 							# 🦊 Elaina (Majo no Tabitabi)
	Channel(-1001224959410, 23, f'{deny.char}yuzuriha_inori'), 													# 🦊 Inori (Guilty Crown)
	Channel(-1001393185631, 24, f'{deny.char}pramanix_(arknights)'), 										# 🦊 Pramanix (Arknights)
	Channel(-1001450297428, 25, f'{deny.char}tohru_(maidragon)'), 											# 🦊 Tohru (Kobayashi-san Chi no Maidragon)
	Channel(-1001397826978, 26, f'{deny.char}{{gawr_gura+~+bloop_(gawr_gura)}}'),				# 🦊 Gawr Gura
	
	# 🦊 Anime
	Channel(-1001156479074, 33, f'{deny.char}{{tamaki_kotatsu+~+maki_oze+~+sister_cleaire}}'),# 🦊 Enen no Shouboutai
	Channel(-1001498572697, 34, f'{deny.char}fate_(series)'),														# 🦊 Fate Series
	Channel(-1001472087141, 35, f'{deny.char}one-punch_man+-raptora+-reptera'),					# 🦊 OnePunchMan
	Channel(-1001214700364, 36, f'{deny.char}monogatari_(series)'), 										# 🦊 Monogatari Series
	Channel(-1001431632000, 37, f'{deny.char}mushoku_tensei'), 													# 🦊 Реинкарнация безработного
	Channel(-1001305962472, 38, f'{deny.char}tensei_shitara_slime_datta_ken '), 				# 🦊 TenSura
	Channel(-1001212377345, 39, f'{deny.char}re%3Azero_kara_hajimeru_isekai_seikatsu '),# 🦊 Re:Zero
	Channel(-1001271806523, 40, f'{deny.char}steins%3Bgate'),														# 🦊 Steins;Gate
	Channel(-1001452419883, 41, f'{deny.char}go-toubun_no_hanayome'),										# 🦊 Go-toubun no Hanayome
	Channel(-1001341423528, 42, f'{deny.char}{{utawarerumono+~+utawareru_mono}}'),			# 🦊 Utawarerumono
	
	Channel(-1001150028201, 46, f'{deny.char}to_love-ru'),															# 🦊 To Love-Ru
	Channel(-1001275364036, 47, f'{deny.char}kono_subarashii_sekai_ni_shukufuku_wo%21'),# 🦊 KonoSuba
	Channel(-1001445769194, 48, f'{deny.char}no_game_no_life'), 												# 🦊 No Game, No Life
	Channel(-1001419152052, 49, f'{deny.char}sewayaki_kitsune_no_senko-san'), 					# 🦊 The Helpful Fox Senko-san
	# 🦊 Game
	Channel(-1001331456006, 51, f'{deny.char}arknights'), 															# 🦊 Arknights
	Channel(-1001194471974, 52, f'{deny.char}kantai_collection'), 											# 🦊 Kantai Collection
	Channel(-1001444542633, 53, f'{deny.char}genshin_impact'), 													# 🦊 Genshin Impact

	Channel(-1001347599255, 57, f'{deny.char}azur_lane'), 															# 🦊 Azur Lane
	Channel(-1001392234983, 58, f'{deny.char}touhou'), 																	# 🦊 Touhou	
	Channel(-1001282864009, 59, f'{deny.char}{{hololive ~ hololive_english}}'), 				# 🦊 Hololive	
)