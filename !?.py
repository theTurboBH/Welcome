from StrPy import StrPython
async def private(event):
	async for x in event.client.iter_dialogs():
		
		if x.is_user and not x.entity.bot:
			too = x.id
			msg = """
Welcome Yo Channel Programmers (Str Py)
It is in this channel : Sources, bots
to join : t.me/StrPython
-------------------------------------------
مرحباً بك في القناة البرمجيه (ستار بايثون)
يوجد في هذه القناة : ملفات سورسات، بوتات 🗽
للأنضمام : t.me/StrPython"""
			try:
				await event.send_message(too, msg)
			except BaseException:pass

private(event)