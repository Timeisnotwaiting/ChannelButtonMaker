from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
import asyncio

ID = 10763476

HASH = "e7d6d5493a896264a09d04fda7a30f9d"

TOKEN = "5938959685:AAFPeHQSOxbdoBHmDj-2YDIVZHQZcL8mDqg"

Yashvi = Client(":CBM:", api_id=ID, api_hash=HASH, bot_token=TOKEN)

markup = IKM(
         [
         [
         IKB("Channel ✨💭", url="t.me/SpoiledCommunity"),
         IKB("Group ✨💭", url="t.me/Spoiled_Community")
         ]
         ]
         )

txt = """

𝗛𝗼𝗹𝗮 𝗰𝗼𝘀𝗺𝗼 𝗲𝘀𝘁𝗮𝘀!!

𝗪𝗲 𝗰𝗿𝗲𝗮𝘁𝗲𝗱 𝗮 𝗻𝗲𝘄 𝗽𝗳𝗽 𝗰𝗵𝗮𝗻𝗻𝗲𝗹
𝗛𝗲𝗿𝗲 𝘆𝗼𝘂 𝗰𝗮𝗻 𝗴𝗲𝘁 𝗮𝘄𝗲𝘀𝗼𝗺𝗲 𝗽𝗳𝗽𝘀, 𝘄𝗮𝗹𝗹𝗽𝗮𝗽𝗲𝗿𝘀 𝗳𝗼𝗿 𝗽𝗰 𝗻𝗱 𝗮𝗹𝗹

𝗝𝗼𝗶𝗻 𝗼𝘂𝗿 𝘀𝘁𝗶𝗰𝗸𝗲𝗿 𝗰𝗵𝗮𝗻𝗻𝗲𝗹
𝗡𝗱 𝗰𝗵𝗮𝘁𝘁𝗶𝗻𝗴 𝗴𝗿𝗼𝘂𝗽 𝘁𝗼𝗼👀

"""

async def yashu():
    await Yashvi.send_message(5754821527, text=txt, reply_markup=markup)

async def alpha():
    await Yashvi.start()
    await print("bot started !")
    await yashu()
    await print("post sent !")
    await idle()

asyncio.run(alpha())
