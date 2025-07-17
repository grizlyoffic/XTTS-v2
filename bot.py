import asyncio
from aiogram import Bot, Dispatcher, types
from xtts_wrapper import synthesize_text
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))  # Only you can interact

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def handle_dm(message: types.Message):
    if message.chat.type != 'private' or message.from_user.id != OWNER_ID:
        await message.reply("⛔ You are not authorized to use this bot.")
        return

    text = message.text
    voice_path = synthesize_text(text)
    with open(voice_path, 'rb') as audio:
        await message.reply_voice(audio)

if __name__ == '__main__':
    asyncio.run(dp.start_polling())
