# написать на айограм эхо бота который будет получать два числа,
# спрашивать что с ними делать через меню и присылать ответ

# Обновление: петуханский бот спрашивае как тебя зовут, ты отвечаешь, он спрашивает ты петух?
# и выпадает только одна кнопка с ответом да. Ты нажимаешь и он говорит что ты рустам петух твой ид такой то
# Можешь две кнопки сделать конечно, но так как ты петух у тебя на это еще неделя уйдет
# получать ответ пользователя и сохранять


#import aiogram
from aiogram.dispatcher import FSMContext
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN
from keyboard import button_privet

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=MemoryStorage())

class MyState(StatesGroup):
    wait_answer = State()
    hello_answer = State()
    echo_answer = State()



#функция старт
@dp.message_handler(commands=['Start'])
async def commanda_start(message: types.Message,  state: FSMContext):
    await message.reply("Салям уалейкум,\n как тебя зовут?", reply_markup=kb.greet_kb)
    await MyState.hello_answer.set()

@dp.message_handler(state=MyState.hello_answer)    #функция улавливает сообщения
async def echo_message(message: types.Message, state: FSMContext):             # функция принимает сообщение которое уловила
        print(message.text)
        await state.update_data(otvet=message.text)
        await message.answer('Ты разве не Джафар?')   #перед сообщением всегда пишется await
        await MyState.wait_answer.set()

@dp.message_handler(state=MyState.wait_answer)    # попадает если установлен статус
async def answer_message(message: types.Message, state: FSMContext):             # функция принимает сообщение которое уловила
        data_state = await state.get_data()     #переменная получает сосотяние
        print(data_state)
        await message.answer(f'Ну ладно, тебя зовут {data_state["otvet"]}')   #перед сообщением всегда пишется await
        await MyState.echo_answer.set()

@dp.message_handler(state=MyState.echo_answer)
async def answer_message(message: types.Message, state: FSMContext):
    data_state = await state.get_data()  # переменная получает сосотяние
    print(data_state)
    await message.answer(f'Хватит писать, я больше ничего не умею!')



# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)

executor.start_polling(dp, skip_updates=True)
