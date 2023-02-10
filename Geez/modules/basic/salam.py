# if you can read this, this meant you use code from Geez | Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Geez and Ram doesn't care about credit
# at least we are know as well
# who Geez and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Geez | Ram Team
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from geezlibs.geez.helper.basic import edit_or_reply
from geezlibs.geez.helper.PyroHelpers import ReplyCheck
from Geez.modules.basic import add_command_help
from Geez import cmds

@Client.on_message(filters.command("p", cmds) & filters.me)
async def salamone(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Assalamualaikum...",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("pe", cmds) & filters.me)
async def salamdua(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Assalamualaikum Warahmatullahi Wabarakatuh",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("l", cmds) & filters.me)
async def jwbsalam(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Wa'alaikumsalam...",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("el", cmds) & filters.me)
async def jwbsalamlngkp(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Wa'alaikumsalam Warahmatullahi Wabarakatuh",
            reply_to_message_id=ReplyCheck(message),
        ),
    )



@Client.on_message(filters.command("ass", cmds) & filters.me)
async def salamarab(client: Client, message: Message):
    xx = await edit_or_reply(message, "Salam Dulu Gua..")
    await asyncio.sleep(2)
    await xx.edit("السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")


@Client.on_message(filters.command("vr", cmds) & filters.me)
async def salamarab(client: Client, message: Message):
    xx = await edit_or_reply(message, "**OOOO**")
    await asyncio.sleep(1.5)
    await xx.edit("**INI YANG VIRTUAL**")
    await asyncio.sleep(1.5)
    await xx.edit("**YANG KATANYA SAYANG BANGET**")
    await asyncio.sleep(1.5)
    await xx.edit("**TAPI TETEP AJA DI TINGGAL**")
    await asyncio.sleep(1.5)
    await xx.edit("**NI INGET**")
    await asyncio.sleep(1.5)
    await xx.edit("**TANGANNYA AJA GA BISA DI PEGANG**")
    await asyncio.sleep(1.5)
    await xx.edit("**APALAGI OMONGANNYA**")
    await asyncio.sleep(1.5)
    await xx.edit("**BHAHAHAHA**")
    await asyncio.sleep(1.5)
    await xx.edit("**KASIAN MANA MASIH MUDA**")

@Client.on_message(filters.command("mutu", cmd) & filters.me)
async def igehh(client: Client, message: Message):
    xx = await message.reply("**Mutualan IG Yuk!!**")
    await asyncio.sleep(2)
    await xx.edit(f"Nih IG Ku = [TEKAN](https://instagram.com/saya_wiki)", disable_web_page_preview=True)


@Client.on_message(filters.command("sfs", cmd) & filters.me)
async def channel(client: Client, message: Message):
    xx = await message.reply("**Yok SFS!!**")
    await asyncio.sleep(2)
    await xx.edit(f"Nih CH Ku = [TEKAN](https://t.me/chnlwiki)", disable_web_page_preview=True)


@Client.on_message(filters.command("gbn", cmds) & filters.me)
async def globalfake(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    user = await client.get_users(user_id)
    xx = await edit_or_reply(message, f"Memulai Proses Global Banned [{user.first_name}](tg://user?id={user.id})")
    await asyncio.sleep(3)
    await xx.edit("`Gbanning....`")
    await asyncio.sleep(5)
    await xx.edit(f"**\\\ Berhasil Gbanning //** \nFirst Name : [{user.first_name}](tg://user?id={user.id})\nReason : {reason}")

add_command_help(
    "salam",
    [
        [f"{cmds}p", "Assalamualaikum."],
        [f"{cmds}pe", "Assalamualaikum Warahmatullahi Wabarakatuh."],
        [f"{cmds}l", "Wa'alaikumsalam."],
        [f"{cmds}ass", "Assalamualaikum Bahas arab."],
        [f"{cmds}vr", "Ngatain bocah virtualan."],
    ]
)
