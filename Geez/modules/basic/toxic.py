# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from geezlibs.geez.helper.basic import edit_or_reply
from geezlibs.geez.helper.PyroHelpers import ReplyCheck
from Geez.modules.basic import add_command_help
from Geez import cmds

@Client.on_message(filters.command("jamet", cmds) & filters.me)
async def ngejamet(client: Client, message: Message):
    user_id = await extract_user(message)
    xx = await edit_or_reply(message, "**WOII**")
    await asyncio.sleep(1.5)
    await xx.edit("**WOI NGENTOT**")
    await asyncio.sleep(1.5)
    await xx.edit("**CUMA MAU BILANG**")
    await asyncio.sleep(1.5)
    await xx.edit("**GAUSAH SO ASIK**")
    await asyncio.sleep(1.5)
    await xx.edit("**LO ITU JELEK?**")
    await asyncio.sleep(1.5)
    await xx.edit("**GAUSAH REPLY**")
    await asyncio.sleep(1.5)
    await xx.edit("**LO BUKAN LEVEL GUE**")
    await asyncio.sleep(1.5)
    await xx.edit("**KALO GA SENENG YA PC KONTOL**")
    await asyncio.sleep(1.5)
    await xx.edit("**BOCAH TOLOL**")
    await asyncio.sleep(1.5)
    await xx.edit("**MENTAL PENGEMIS**")
    await asyncio.sleep(1.5)
    await xx.edit("**LEMBEK NGENTOT🥵**")


@Client.on_message(filters.command("gbn", cmds) & filters.me)
async def globalfake(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    user = await client.get_users(user_id)
    xx = await edit_or_reply(message, f"Memulai Proses Global Banned [{user.first_name}](tg://user?id={user.id})")
    await asyncio.sleep(3)
    await xx.edit("`Gbanning....`")
    await asyncio.sleep(5)
    await xx.edit(f"**\\\ Berhasil Gbanning //** \nFirst Name : [{user.first_name}](tg://user?id={user.id})\nReason : {reason}")
    

@Client.on_message(filters.command("gmt", cmds) & filters.me)
async def fakegmute(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    user = await client.get_users(user_id)

    xx = await edit_or_reply(message, f"Memulai Proses Global mute [{user.first_name}](tg://user?id={user.id})")
    await asyncio.sleep(3)
    await xx.edit("`Memulai Proses Global mute....`")
    await asyncio.sleep(5)
    await xx.edit(f"**\\\ Berhasil Gmute //** \nFirst Name : [{user.first_name}](tg://user?id={user.id})\nReason : {reason}")
    

@Client.on_message(filters.command("ywc", cmds) & filters.me)
async def ywc(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "ok Kontol Sama - Sama",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("pp", cmds) & filters.me)
async def toxicpp(client: Client, message: Message):
    user_id = await extract_user(message)
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "PASANG PP DULU GOBLOK,BIAR ORANG-ORANG PADA TAU BETAPA HINA NYA MUKA LU 😆",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("dp", cmds) & filters.me)
async def toxicdp(client: Client, message: Message):
    user_id = await extract_user(message)
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "MUKA LU HINA, GAUSAH SOK KERAS YA ANJENGG!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("so", cmds) & filters.me)
async def toxicso(client: Client, message: Message):
    user_id = await extract_user(message)
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "GAUSAH SOKAB SAMA GUA GOBLOK, LU BABU GA LEVEL!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("nb", cmds) & filters.me)
async def toxicnb(client: Client, message: Message):
    user_id = await extract_user(message)
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "MAEN BOT MULU ALAY NGENTOTT, KESANNYA NORAK GOBLOK!!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("met", cmds) & filters.me)
async def toxicmet(client: Client, message: Message):
    user_id = await extract_user(message)
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "NAMANYA JUGA JAMET CAPER SANA SINI BUAT CARI NAMA",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("war", cmds) & filters.me)
async def toxicwer(client: Client, message: Message):
    user_id = await extract_user(message)
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "WAR WAR PALAK BAPAK KAU WAR, SOK KERAS BANGET GOBLOK, DI TONGKRONGAN JADI BABU, DI TELE SOK JAGOAN.",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("wartai", cmds) & filters.me)
async def toxicwartai(client: Client, message: Message):
    user_id = await extract_user(message)
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "WAR WAR TAI ANJING, KETRIGGER MINTA SHARELOK LU KIRA MAU COD-AN GOBLOK, BACOTAN LU AJA KGA ADA KERAS KERASNYA GOBLOK",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("kismin", cmds) & filters.me)
async def toxickismin(client: Client, message: Message):
    user_id = await extract_user(message)
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "CUIHHHH, MAKAN AJA MASIH NGEMIS LO GOBLOK, JANGAN SO NINGGI YA KONTOL GA KEREN LU KEK GITU GOBLOK!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("ded", cmds) & filters.me)
async def toxicded(client: Client, message: Message):
    user_id = await extract_user(message)
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "MATI AJA LU GOBLOK, GAGUNA LU HIDUP DI BUMI",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("sokab", cmds) & filters.me)
async def toxicsokab(client: Client, message: Message):
    user_id = await extract_user(message)
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "SOKAB BET LU GOBLOK, KAGA ADA ISTILAH NYA BAWAHAN TEMENAN AMA BOS!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("gembel", cmds) & filters.me)
async def toxicgembel(client: Client, message: Message):
    user_id = await extract_user(message)
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "MUKA BAPAK LU KEK KELAPA SAWIT ANJING, GA USAH NGATAIN ORANG, MUKA LU AJA KEK GEMBEL TEXAS GOBLOK!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("cuih", cmds) & filters.me)
async def toxiccuih(client: Client, message: Message):
    user_id = await extract_user(message)
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "GAK KEREN LO KEK BEGITU GOBLOK, KELUARGA LU BAWA SINI GUA LUDAHIN SATU-SATU. CUIHH!!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("dih", cmds) & filters.me)
async def toxicdih(client: Client, message: Message):
    user_id = await extract_user(message)
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "DIHHH NAJISS ANAK HARAM LO GOBLOK, JANGAN BELAGU DIMARI KAGA KEREN LU KEK BGITU TOLOL!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("gcs", cmds) & filters.me)
async def toxicgcs(client: Client, message: Message):
    user_id = await extract_user(message)
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "GC SAMPAH KAYA GINI, BUBARIN AJA GOBLOK!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("skb", cmds) & filters.me)
async def toxicskb(client: Client, message: Message):
    user_id = await extract_user(message)
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "EMANG KITA KENAL? KAGA GOBLOK SOKAB BANGET LU GOBLOK",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("virtual", cmds) & filters.me)
async def toxicvirtual(client: Client, message: Message):
    user_id = await extract_user(message)
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
