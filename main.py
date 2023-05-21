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
DEF_FORMAT = "480"
from dotenv import load_dotenv
load_dotenv()
os.makedirs("./downloads", exist_ok=True)
API_ID = 952608
API_HASH = "8d8d0ad8e3d4bcd54420190f57da78ad"
BOT_TOKEN = "6055835688:AAFm4IavDpFO1H8jaXocUzk_nTcj13Gp8pY"
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
 editable = await m.reply_text("**Hi BOSS I'm Alive Send /down download and for classplus send /cpd  for /dhurina for /vision**")


          

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

    editable = await m.reply_text("**Enter Batch** 🥎")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text

    await m.reply_text("**Enter Resolution Quality**🥊")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text

    raw_text6 = "no"
    thumb = "no"

    if raw_text == '0':
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(arg, len(links)):

            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/","").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*","").replace("download",".pdf").replace(".","").strip()
            if ".pdf" in url or "pdf" in name1:
                name = f"{str(count).zfill(3)}) {name1.replace('pdf', '')}.pdf"
                r = requests.get(url, allow_redirects=True)
                if r.status_code != 200:
                    print("Error", name)
                    continue
                with open(name, "wb") as f:
                    f.write(r.content)
                    print("done: ", name)
                try:
                    await bot.send_document(m.chat.id, name, file_name=name, caption=f'{name}')
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                count += 1
                os.remove(name) if os.path.exists(name) else None
                continue
                
            if "classplus" in url:
                ytf = None
                name = name1
                
            if "visionias" in url:
                url = get_va(url)
                name = name1
             

            if raw_text2 == "144":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '256x144' in out:
                    ytf = f"{out['256x144']}"
                elif '320x180' in out:
                    ytf = out['320x180']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data1 in out:
                        ytf = out[data1]
            elif raw_text2 == "180":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '320x180' in out:
                    ytf = out['320x180']
                elif '426x240' in out:
                    ytf = out['426x240']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data2 in out:
                        ytf = out[data2]
            elif raw_text2 == "240":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '426x240' in out:
                    ytf = out['426x240']
                elif '426x234' in out:
                    ytf = out['426x234']
                elif '480x270' in out:
                    ytf = out['480x270']
                elif '480x272' in out:
                    ytf = out['480x272']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data3 in out:
                        ytf = out[data3]
            elif raw_text2 == "360":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '640x360' in out:
                    ytf = out['640x360']
                elif '638x360' in out:
                    ytf = out['638x360']
                elif '636x360' in out:
                    ytf = out['636x360']
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '638x358' in out:
                    ytf = out['638x358']
                elif '852x316' in out:
                    ytf = out['852x316']
                elif '850x480' in out:
                    ytf = out['850x480']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']
                elif '854x470' in out:
                    ytf = out['852x470']
                elif '1280x720' in out:
                    ytf = out['1280x720']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data4 in out:
                        ytf = out[data4]
            elif raw_text2 == "480":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']
                elif '854x470' in out:
                    ytf = out['854x470']
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '850x480' in out:
                    ytf = ['850x480']
                elif '960x540' in out:
                    ytf = out['960x540']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data5 in out:
                        ytf = out[data5]

            elif raw_text2 == "720":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '1280x720' in out:
                    ytf = out['1280x720']
                elif '1280x704' in out:
                    ytf = out['1280x704']
                elif '1280x474' in out:
                    ytf = out['1280x474']
                elif '1920x712' in out:
                    ytf = out['1920x712']
                elif '1920x1056' in out:
                    ytf = out['1920x1056']
                elif '854x480' in out:
                    ytf = out['854x480']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data6 in out:
                        ytf = out[data6]
            elif "player.vimeo" in url:
                if raw_text2 == '144':
                    ytf = 'http-240p'
                elif raw_text2 == "240":
                    ytf = 'http-240p'
                elif raw_text2 == '360':
                    ytf = 'http-360p'
                elif raw_text2 == '480':
                    ytf = 'http-540p'
                elif raw_text2 == '720':
                    ytf = 'http-720p'
                else:
                    ytf = 'http-360p'
            else:
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                for dataS in out:
                    ytf = out[dataS]

            try:
                if "unknown" in out:
                    res = "NA"
                else:
                    res = list(out.keys())[list(out.values()).index(ytf)]

                name = f'{str(count).zfill(3)}) {name1} {res}'
            except Exception:
                res = "NA"

          
            if "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'
            if "youtu" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={int(raw_text2)}]+bestaudio" --no-keep-video --remux-video mkv "{url}"'
            elif "classplusapp" in url:
            	headers = {'Host': 'api.classplusapp.com', 'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6ODg5NjE4NDMsIm9yZ0lkIjoyNTUxLCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTY2NjMzMzY2NjU1OCIsIm5hbWUiOiJGZmZmZmZmIiwiZW1haWwiOiJsYWtlZm94NzA1QGxpZWJvZS5jb20iLCJpc0ZpcnN0TG9naW4iOnRydWUsImRlZmF1bHRMYW5ndWFnZSI6IkVOIiwiY291bnRyeUNvZGUiOiJJTiIsImlzSW50ZXJuYXRpb25hbCI6MCwiaXNEaXkiOmZhbHNlLCJsb2dpblZpYSI6Ik90cCIsImZpbmdlcnByaW50SWQiOiJiNjY3M2Y1YjQ2NmNiODZmZGFhZmJlZGZjNzRjZWYzNSIsImlhdCI6MTY4MTIzMjExNywiZXhwIjoxNjgxODM2OTE3fQ.r0klWJjEaA2jqpij_aSGXA7Mth2rd6LEsfRUhZT8a0byvsJd811FUiyH3TnIfTev', 'user-agent': 'Mobile-Android', 'app-version': '1.4.37.1', 'api-version': '18', 'device-id': '5d0d17ac8fhb3c9f51', 'device-details': '2848b866799971ca_2848b8667a33216c_SDK-30', 'accept-encoding': 'gzip'}
            	params = (('url', f'{url}'),)
            	response = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)
            	url = response.json()['url']
            	cmd = f'yt-dlp -o "{name}.%(ext)s" --no-keep-video --remux-video mkv "{url}"'
            elif "player.vimeo" in url:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif "m3u8" or "livestream" in url:
                if "classplus" in url:
                    cmd = f'yt-dlp --no-keep-video --no-check-certificate --remux-video mkv "{url}" -o "{name}.%(ext)s"'
                else:
                    cmd = f'yt-dlp -f "{ytf}" --no-check-certificate --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif ytf == "0" or "unknown" in out:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif ".pdf" or "download" in url:
                cmd = "pdf"
            else:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --no-check-certificate --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            print(cmd)
            try:
                Show = f"**Downloading:-**\n\n**Name :-** `{name}\nQuality - {raw_text2}`\n\n**Url :-** `{url}`"
                prog = await m.reply_text(Show)
                cc = f'{str(count).zfill(3)}**.** {name1} {res}\n**Batch :-** {raw_text0}'
                cc1 = f'{str(count).zfill(3)}**.** {name1} {res}.pdf\n**Batch :-** {raw_text0}'
                if cmd == "pdf" or ".pdf" in url or ".pdf" in name:
                    try:
                        ka = await helper.aio(url, name)
                        await prog.delete(True)
                        time.sleep(1)
                        reply = await m.reply_text(f"Uploading - ```{name}```")
                        time.sleep(1)
                        start_time = time.time()
                        await m.reply_document(
                            ka,
                            caption=
                            f'**Title »** {name1} {res}.pdf\n**Caption »** {raw_text0}\n**Index »** {str(count).zfill(3)}'
                        )
                        count += 1
                        # time.sleep(1)
                        await reply.delete(True)
                        time.sleep(1)
                        os.remove(ka)
                        time.sleep(3)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await helper.send_vid(bot, m, cc, filename, thumb, name,
                                          prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done")
    

   
@bot.on_message(filters.command(["cp"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("Send txt file**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

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

    editable = await m.reply_text(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text


    try:
        arg = int(raw_text)
    except:
        arg = 0
    
    
    editable = await m.reply_text("**Enter Title**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text
    
    await m.reply_text("**Enter resolution**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text

    editable4= await m.reply_text("Now send the **Thumb url**\nEg : ```https://telegra.ph/file/d9e24878bd4aba05049a1.jpg```\n\nor Send **no**")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"
        
    if raw_text =='0':
        count =1
    else:       
        count =int(raw_text)    

    
    try:
        for i in range(arg, len(links)):
            
            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@","").replace("*","").replace(".","").strip()
            
            if "classplus" in url:
                headers = {
                    'Host': 'api.classplusapp.com',
                    'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6ODg5NjE4NDMsIm9yZ0lkIjoyNTUxLCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTY2NjMzMzY2NjU1OCIsIm5hbWUiOiJGZmZmZmZmIiwiZW1haWwiOiJsYWtlZm94NzA1QGxpZWJvZS5jb20iLCJpc0ZpcnN0TG9naW4iOnRydWUsImRlZmF1bHRMYW5ndWFnZSI6IkVOIiwiY291bnRyeUNvZGUiOiJJTiIsImlzSW50ZXJuYXRpb25hbCI6MCwiaXNEaXkiOmZhbHNlLCJsb2dpblZpYSI6Ik90cCIsImZpbmdlcnByaW50SWQiOiJiNjY3M2Y1YjQ2NmNiODZmZGFhZmJlZGZjNzRjZWYzNSIsImlhdCI6MTY4MTIzMjExNywiZXhwIjoxNjgxODM2OTE3fQ.r0klWJjEaA2jqpij_aSGXA7Mth2rd6LEsfRUhZT8a0byvsJd811FUiyH3TnIfTev',
                    'user-agent': 'Mobile-Android',
                    'app-version': '1.4.37.1',
                    'api-version': '18',
                    'device-id': '5d0d17ac8b3c9f51',
                    'device-details': '2848b866799971ca_2848b8667a33216c_SDK-30',
                    'accept-encoding': 'gzip',
                }

                params = (
                    ('url', f'{url}'),
                )

                response = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)
                # print(response.json())
                a = response.json()['url']
                # print(a)


                headers1 = {
                    'User-Agent': 'ExoPlayerDemo/1.4.37.1 (Linux;Android 11) ExoPlayerLib/2.14.1',
                    'Accept-Encoding': 'gzip',
                    'Host': 'cdn.jwplayer.com',
                    'Connection': 'Keep-Alive',
                }


                response1 = requests.get(f'{a}', headers=headers1)

                url1 = (response1.text).split("\n")[2]
            else:
                url1 = url

                
            name = f'{str(count).zfill(3)}) {name1}'    
            Show = f"**Downloading:-**\n\n**Name :-** `{name}`\n\n**Url :-** `{url1}`"
            prog = await m.reply_text(Show)
            cc = f'**Title »** {name1}.mkv\n**Caption »** {raw_text0}\n**Index »** {str(count).zfill(3)}'
            if "pdf" in url:
                cmd = f'yt-dlp -o "{name}.pdf" "{url1}"'
            else:
                cmd = f'yt-dlp -o "{name}.mp4" --no-keep-video --no-check-certificate --remux-video mkv "{url1}"'
            try:
                download_cmd = f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
                os.system(download_cmd)
                

                if os.path.isfile(f"{name}.mkv"):
                    filename = f"{name}.mkv"
                elif os.path.isfile(f"{name}.mp4"):
                    filename = f"{name}.mp4"  
                elif os.path.isfile(f"{name}.pdf"):
                    filename = f"{name}.pdf"  
                subprocess.run(f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"', shell=True)
                await prog.delete (True)
                reply = await m.reply_text(f"Uploading - ```{name}```")
                try:
                    if thumb == "no":
                        thumbnail = f"{filename}.jpg"
                    else:
                        thumbnail = thumb
                except Exception as e:
                    await m.reply_text(str(e))

                dur = int(helper.duration(filename))

                start_time = time.time()
                if "pdf" in url1:
                    await m.reply_document(filename,caption=cc)
                else:
                    await m.reply_video(filename,supports_streaming=True,height=720,width=1280,caption=cc,duration=dur,thumb=thumbnail, progress=progress_bar,progress_args=(reply,start_time) )
                count+=1
                os.remove(filename)

                os.remove(f"{filename}.jpg")
                await reply.delete (True)
                time.sleep(1)
            except Exception as e:
                await m.reply_text(f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}` & `{url1}`")
                continue 
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done")      
    
    
    
    
bot.run()    





