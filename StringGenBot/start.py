from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""📟¦اهلا بـك عزيـزي 📬 
🖱 ¦ يـمكنك استـخـراج الـتـالـي 📥
📟 ¦ تيرمـكـس تليثون للحسـابـات 🥷
📡 ¦ تيرمـكـس تليثون للبوتــات 🎭
🎸 ¦ بايـروجـرام مـيوزك للحسابات 🥷
🔮 ¦ بايـروجـرام مـيوزك للبوتات 🎭
🔗 ¦ بايـروجـرام مـيوزك احدث اصدار 📀

- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس لتشغيل تلـيثون والبايروجرام لتشغيل سـورس اغــاني 
⎚¦تم انشاء البوت بواسطه المطور تربون  [ㅤ𓏺 ˛ َِ 𝐓𝐀𝐑𝐁𝐎𝐔𝞝𝐍.. 🧑‍💻 ˼ ](https://t.me/W_X_E1)""",

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="[{اضـعـط لـبـدا اسـتـخـراج الـكـود}] ", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("♥️️ قناه سورس تربون ❤️‍🔥 ️", url="https://t.me/ADXG25"),
                    InlineKeyboardButton(مــطـور الـبـوت ❤️‍🔥", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
