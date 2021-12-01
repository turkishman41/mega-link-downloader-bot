import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import pyrogram
from pyrogram import Client, filters
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import os
import shutil
import subprocess

from database.blacklist import check_blacklist
from database.userchats import add_chat

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from mega import Mega

mega = Mega()

email = Config.Mega_email
password = Config.Mega_password
speed = "0"
# It is really not imprtant for you to enter your mega email or password in config variables!

if email != "None" and password != "None":
    try:
        m = mega.login(email, password) # Logging into mega.py 
        logging_in_megacmd = subprocess.run(["mega-login", email, password]) # Logging into MEGAcmd (Helps to bypass quota limits if you use a pro/business account)
        speedlimit_in_megacmd = subprocess.run(["mega-speedlimit", speed]) # Setting the download speed limit to unlimited in MEGAcmd 😉
    except Exception as e:
        logger.info(e)
        m = mega.login()
else:
    m = mega.login() # Here we make an anonymous, temporary account for mega.py!
    speedlimit_in_megacmd = subprocess.run(["mega-speedlimit", speed])

@Client.on_message(filters.command("mega_ini") & filters.user(int(Config.OWNER_ID)))
async def log_to_megatools(client, message):
    fuser = message.from_user.id
    if check_blacklist(fuser):
        await message.reply_text("Üzgünüm! Siz Yasaqlısınız!!")
        return
    add_chat(fuser)
    cred_location = Config.CREDENTIALS_LOCATION + "/mega.ini"
    megatools_credentials = message.reply_to_message
    if message.reply_to_message:
        await client.download_media(
            message=megatools_credentials,
            file_name=cred_location
        )
        # Using your mega.nz credentials for logging into megatools when downloading links with megatools (Helps to bypass quota limits if you use a pro/business account)
        await message.reply_text(f"<b>`mega.nz` kimlik bilgiləriniz başarıyla Qeyd edildi!✅</b>\n\nProfesyonel/Biznes mega hesabının kimlik bilgilərini sağladıysanız, dosyaları herhangi bir kota sorunu olmadan indirəbiləcəksiniz!")
    else:
        await message.reply_text("<b>Öncə https://github.com/turkishman41/mega-link-downloader-bot/blob/main/README.md ünvanından oxuyun</b>\n\nSonra `mega.ini` adlı fayl yaradın Readme-də qeyd olunan təlimatlar kimi və mənə göndərin. <b>Sonra ona cavab olaraq göndərin<code>/mega_ini</code></b>", disable_web_page_preview=True)
