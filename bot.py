# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot



from pyrogram import Client, filters
from Youtube.config import Config

# Create a Pyrogram client
app = Client(
    "my_bot",
    api_id=6666104129.API_ID, 
    api_hash=gZTTfaYU2B4.API_HASH, 
    bot_token=7321148061:AAEb8Rc9PzSLbVerQbkpywZ6OhmKFkw1wPc.BOT_TOKEN,
    plugins=dict(root="Youtube")
)



# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()
