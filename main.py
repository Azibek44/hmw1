from aiogram import Bot, Dispatcher,types,executor
import config

bot =Bot(config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands= ['start','go'])
async def start(message:types.Message):
    await message.answer(f'Здраствуйте {message.from_user.full_name},{message.from_user.username}')

@dp.message_handler(commands=['help'])
async def start(message:types.Message):
    await message.reply("Вот мои команды:") 

@dp.message_handler(text=['Привет'])
async def start(message:types.Message):
    await message.answer("Привет")  

@dp.message_handler(commands=['about'])
async def about(message:types.Message):
    await message.answer("Привет")      

@dp.message_handler()
async def not_found(message:types.Message):
    await message.answer(f"{message.from_user.as_json()}")   
    await message.answer(f"Фамилия{message.from_user.last_name}\nИмя: {message.from_user.last_name}\nUsername {message.from_user.username}")       
    await message.answer_photo("data:image/jpeg;base64,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")
    await message.answer_location(0,0)
    # with open ()

@dp.message_handler()
async def not_found(message:types.Message):
    await message.answer("Ваша команда не распознана, введите /help")



executor.start_polling(dp)