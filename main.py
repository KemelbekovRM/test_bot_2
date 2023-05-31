# написать на айограм эхо бота который будет получать два числа,
# спрашивать что с ними делать через меню и присылать ответ

#import aiogram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot (token='5969349861:AAFYdb1VjC5wnP7TBYKEhGkvL-4Q37ZN8WQ')
dp = Dispatcher(bot)

@dp.message_handlers()
async def echo(message: types.Message):
    await message.answer(message.text)

executor.start_polling(dp, skip_updates=True)
#print('Поставил ГИТ и втух, только не надо ныть ')