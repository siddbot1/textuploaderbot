import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
from pyromod import listen
from pyrogram.types import Message
import tgcrypto
import pyrogram
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
from pyrogram.errors import FloodWait
import time
from pyrogram.types import User, Message
from p_bar import progress_bar
import subprocess
from subprocess import getstatusoutput
import logging
import os
import sys
from get_video_info import get_video_attributes, get_video_thumb
import re
from pyrogram import Client as bot
import threading


from dotenv import load_dotenv
load_dotenv()
os.makedirs("./downloads", exist_ok=True)
API_ID = 952608
API_HASH = "8d8d0ad8e3d4bcd54420190f57da78ad"
BOT_TOKEN = "6170442028:AAFjZE4YhF1JksQXKNsOuHhxmS2ayeZhuqE"

AUTH_USERS = 818269274
sudo_users = [818269274]
bot = Client(
    "bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)
async def exec(cmd):
  proc = await asyncio.create_subprocess_exec(*cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
  stdout, stderr = await proc.communicate()
  print(stdout.decode())
  return proc.returncode,stderr.decode()
  
  
  
  
@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
 editable = await m.reply_text("**HI Send /down or /cpd or /dhurina or /vision**")


          

@bot.on_message(filters.command(["cancel"]))
async def cancel(_, m):
    editable = await m.reply_text("Canceling All process Plz wait")
    global cancel
    cancel = True
    await editable.edit("cancled")
    return
@bot.on_message(filters.command("restart"))
async def restart_handler(_, m):
    await m.reply_text("Restarted!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)
    
    
    
    
    
    
@bot.on_message(filters.command(["cpd"]))
async def account_login(bot: Client, m: Message):
    
    editable = await m.reply_text("Send Classplus Links Text File")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/"

    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(
        f"Total **{len(links)}** Founded 🤷‍♂️\n\n Download Start From Which Link?.(Enter Line Number) \n\n If You Need To Download From First Then Enter Number 👉 **0**"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0

    editable = await m.reply_text("**Enter Tittle For Batch** 🥎")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text

    await m.reply_text("**Enter Resolution Quality**🥊\n\n Eg:- 720 or 480 or 360...without P")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    raw_text6 = "no"
    thumb = "no"
    res = "NA"
    format_filter = "filler"
    
    
    

    async def download_link(link, link_number, raw_text2, raw_text0):
       url = link[1]
       name1 = link[0].replace("\t", "").replace(":", "").replace("/","").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*","").replace("download",".pdf").replace(".","").strip()
       name = f'{str(link_number).zfill(3)}) {name1}'
    
       if "acecwply" in url:
           cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'
       else:
           cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --no-check-certificate --remux-video mkv "{url}" -o "{name}.%(ext)s"'
    
       print(cmd)
       output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
       eta = 0
    
       try:
           Show = f"**Downloading:-**\n\n**Name:** `{name}`\n**Quality:** **{raw_text2}p** (If It's Not Available, Automatically Download Best Quality)\n**URL:** `{url}`"
           prog = await m.reply_text(Show)
           cc = f'{str(link_number).zfill(3)}**.** {name1} {res}\n**Batch :-** {raw_text0}'
           cc1 = f'{str(link_number).zfill(3)}**.** {name1} {res}.pdf\n**Batch :-** {raw_text0}'

           if cmd == "pdf" or ".pdf" in url or ".pdf" in name:
               try:
                  time.sleep(0.5)
               except FloodWait as e:
                   await m.reply_text(str(e))
                   time.sleep(e.x)
                   return
           else:
               res_file = await helper.download_video(url, cmd, name)
               filename = res_file
               await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
               link_number += 1
               time.sleep(0.5)
       except Exception as e:
           await m.reply_text(
               f"**Downloading Failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`"
           )

    async def download_links(links, arg, raw_text2, raw_text0):
       if raw_text == '0':
           link_number = 1
       else:
           link_number = int(raw_text)
    
       threads = []
    
       for i in range(arg, len(links)):
           link = links[i]
           t = threading.Thread(target=download_link, args=(link, link_number, raw_text2, raw_text0))
           t.start()
           threads.append(t)
        
           link_number += 1
    
       for t in threads:
           t.join()

    # Call the function to start downloading links using threads
    
    asyncio.run(download_links(links, arg, raw_text2, raw_text0))
    await m.reply_text("Done")
    
    


    
    
bot.run()    
