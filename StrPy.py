import telethon
from telethon import events
from telethon.sync import functions
from telethon import TelegramClient
import telethon
import random
from random import choices
import time
from telethon.tl.functions.messages import GetPeerDialogsRequest
from telethon.sessions import StringSession
auction = []
band = []
auction.append("vipjz\n")
from config import *
StrPython.send_message("me","""
**لصيد ثلاثي بوت :** `حجز بوتات`
**لصيد رباعي بوت :** `حجز بوت`
**لصيد خماسي rm177 :** `حجز خماسيات-2`
**لصيد خماسي :** `حجز خماسيات`
**لصيد سداسي :**  `حجز سداسيات`
**لصيد ثلاثي :** `حجز ثلاثيات`
**لصيد vip : **`حجز خماسيات-3`
**للتجربه : **`حجز تيست`
""")


@StrPython.on(
events.NewMessage(
outgoing=True, pattern=r"حجز"))
async def StrPychecker(event):
        clicks = 1
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        
        type = str(msg[0])
      
        username = await rando(type)
        await event.reply(f"تم البدأ على النوع  - {type}")

        while True:
                clicks += 1
                try:
             	   await StrPython(GetPeerDialogsRequest(peers=[username]))
                except Exception as err:
                    if "No user has" in str(err):
                        try:
                        	await StrPython(functions.account.UpdateUsernameRequest(username=username))           
                        	await StrPython.send_file(event.chat_id, "https://t.me/jc_ksa/22",caption=f'''
Good evening, chief 🗽
⌯ User ⤷ @{username}
⌯ Save ⤷ Account
⌯ Clicks ⤷ {clicks}
⌯ Program the bot ⤷ @StrPython''')
                        except Exception as USFL:
                        	await StrPython.send_message(event.chat_id,f"User is error : @{username}")
                    else:
                        continue                    
                        
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    	await StrPython.send_message(event.chat_id,f"User is band 🥴 : {username}")
                    	band.append(username)
                    	
                except telethon.errors.rpcerrorlist.UsernameOccupiedError:
                    	time.sleep(1)
                    	
                except telethon.errors.rpcerrorlist.FloodWaitError as ses:
                    	await StrPython.send_message(event.chat.id,f"Flood & {ses.seconds}")
                    	
                    	break
                except telethon.errors.rpcerrorlist.UsernamePurchaseAvailableError: 
                    	
                    	auction.append(username+"\n")
                    	
              
                except Exception as Error:
                   await StrPython.send_message(event.chat.id,f"Error in the check : {Error}") 
                   break
                   
       
#  تخمط دليل فشلك 🤨
#تيم ستار بايثون 🗽

ban = open("band.txt","r").read().split()
band.append(ban)

abcd = "qwertyuiopassdfghjklzxcvbnm"
number = "1234567890"

async def rando(type):
	if type == "خماسيات-3":
		q = random.choices(abcd)
		w = random.choices(abcd)
		user = ["vip",q[0],w[0]]
		username = "".join(user)
		
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "خماسيات":
		q = random.choices(abcd)
		w = random.choices(abcd)
		user = [q[0],q[0],q[0],q[0],w[0]]
		username = "".join(user)
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "ثلاثيات":
		q = random.choices(abcd)
		w = random.choices(abcd)
		b = random.choices(abcd)
		user = [q[0],"_",b[0],"_",w[0]]
		username = "".join(user)
		
		
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "سداسيات":
		q = random.choices(abcd)
		w = random.choices(abcd)
		user = [q[0],q[0],q[0],w[0],w[0],w[0]]
		username = "".join(user)
		return username
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "تيست":
		q = random.choice(abcd)
		w = random.choice(abcd)
		user = [q[0],"b",q[0],"66",q[0],q[0],w[0]]
		username = "".join(user)
		
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "خماسيات-2":
		q = random.choice(abcd)
		w = random.choice(abcd)
		nu = random.choices(number)
		num = random.choices(number)
		user = [q[0],q[0],num[0],nu[0],nu[0]]
		username = "".join(user)
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "بوتات":
		q = random.choices(abcd)
		w = random.choices(abcd)
		b = random.choices(abcd)
		user = [q[0],w[0],b[0]]
		username = "".join(user)
		username = username+"bot"
		
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "بوت":
		q = random.choices(abcd)
		w = random.choices(abcd)
		b = random.choices(abcd)
		user = [q[0],b[0],"_",b[0]]
		username = "".join(user)
		username = username+"bot"
		
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
		     
print("Run")
StrPython.run_until_disconnected()