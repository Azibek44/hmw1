from aiogram import Bot, Dispatcher, types,executor
import config
import random
bot = Bot(config.token)
dp = Dispatcher(bot)
@dp.message_handler(text=[1,2,3])
async def start(msg:types.Message):
    await msg.answer("Zagadaute chislo ot 1 do 3")
    user = int(msg.text)
    rando = random.randint(1,3)
    if user == rando:
        await msg.reply(f"vy pobedili pravelinoe chislo {rando}")
    else:
        await msg.reply(f"ty loh pravelinoe chislo {rando}")
executor.start_polling(dp)