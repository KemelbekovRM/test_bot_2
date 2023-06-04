# написать на айограм эхо бота который будет получать два числа,
# спрашивать что с ними делать через меню и присылать ответ

# Обновление: петуханский бот спрашивае как тебя зовут, ты отвечаешь, он спрашивает ты петух?
# и выпадает только одна кнопка с ответом да. Ты нажимаешь и он говорит что ты рустам петух твой ид такой то
# Можешь две кнопки сделать конечно, но так как ты петух у тебя на это еще неделя уйдет



#import aiogram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

executor.start_polling(dp, skip_updates=True)
