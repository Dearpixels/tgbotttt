import openai
from aiogram import Bot, types, executor, Dispatcher



token = '6237606983:AAEHGSjsy2QTmuyPwNyETbkd87pgdlUI8K0'
openai.api_key = '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' 

bot = Bot(token)
dp = Dispatcher(bot)

print('Start')

@dp.message_handler(commands=["start"], commands_prefix=".!/")
async def send(message: types.Message):   
    await message.reply("Привет. Меня зовут Асрор!\nНапиши мне что-нибудь, и я отвечу. напишите /help чтобы увидеть команды ")




@dp.message_handler(commands=["t"])
async def send(message: types.Message):
	await message.reply("Максим топ!")

@dp.message_handler(commands=["chat"])
async def qprocess_start_command(message: types.Message):
    await message.reply("Группа создателя это бота - https://t.me/Thejojolendss ")
    

@dp.message_handler(content_types=['text'], text=["кусь", "Кусь"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'😼 | {user_name} кусьнул(-а) {reply_user_name}', parse_mode='html')

@dp.message_handler(content_types=['text'], text=["обнять", "Обнять"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'🤗 | {user_name} обнял(-а) {reply_user_name}', parse_mode='html')

@dp.message_handler(content_types=['text'], text=["поцеловать", "Поцеловать"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'💋 | {user_name} поцеловал(-а) {reply_user_name}', parse_mode='html')
@dp.message_handler(content_types=['text'], text=["дать пять", "Дать пять"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'✋ | {user_name} дал(-а) пять {reply_user_name}', parse_mode='html')
@dp.message_handler(content_types=['text'], text=["подарить айфон", "Подарить айфон"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'📱 | {user_name} подарил(-а) айфон {reply_user_name}', parse_mode='html')
@dp.message_handler(content_types=['text'], text=["ударить", "Ударить"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'🤛 | {user_name} ударил(-а) {reply_user_name}', parse_mode='html')
@dp.message_handler(content_types=['text'], text=["заскамить", "Заскамить"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'👨‍💻 | {user_name} заскамил(-а) {reply_user_name}', parse_mode='html')
@dp.message_handler(content_types=['text'], text=["прижать", "Прижать"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'🤲 | {user_name} прижал(-а) {reply_user_name}', parse_mode='html')
@dp.message_handler(content_types=['text'], text=["укусить", "Укусить"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'😬 | {user_name} укусил(-а) {reply_user_name}', parse_mode='html')
@dp.message_handler(content_types=['text'], text=["взять за руку", "Взять за руку"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'🤝 | {user_name} взял(-а) за руку {reply_user_name}', parse_mode='html')
@dp.message_handler(content_types=['text'], text=["прижать", "Прижать"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'🤲 | {user_name} прижал(-а) {reply_user_name}', parse_mode='html')
@dp.message_handler(content_types=['text'], text=["похлопать", "Похлопать"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'👏 | {user_name} похлопал(-а) {reply_user_name}', parse_mode='html')
@dp.message_handler(content_types=['text'], text=["изнасиловать", "Изнасиловать"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'👉👌 | {user_name} изнасиловал(-а) {reply_user_name}', parse_mode='html')
@dp.message_handler(content_types=['text'], text=["пригласить на чай", "Пригласить на чай"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'☕️ | {user_name} пригласил(-а) на чай {reply_user_name}', parse_mode='html')
@dp.message_handler(content_types=['text'], text=["убить", "Убить"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'🔪 | {user_name} убил(-а) {reply_user_name}', parse_mode='html')
@dp.message_handler(content_types=['text'], text=["уебать", "Уебать"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'🤜 | {user_name} уебал(-а) {reply_user_name}', parse_mode='html')
@dp.message_handler(content_types=['text'], text=["украсть", "Украсть"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'💰 | {user_name} украл(-а) {reply_user_name}', parse_mode='html')

@dp.message_handler(content_types=['text'], text=["отсосать", "Отсосать"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'👅 | {user_name} отсосал(-а) у {reply_user_name}', parse_mode='html')

@dp.message_handler(content_types=['text'], text=["отлизать", "Отлизать"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'👅 | {user_name} отлизал(-а) {reply_user_name}', parse_mode='html')

@dp.message_handler(content_types=['text'], text=["выебать", "Выебать"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'🔞 | {user_name} выебал(-а) {reply_user_name}', parse_mode='html')

@dp.message_handler(content_types=['text'], text=["сжечь", "Сжечь"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'🔥 | {user_name} сжёг {reply_user_name}', parse_mode='html')

@dp.message_handler(content_types=['text'], text=["трахнуть", "Трахнуть"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   replyuser = reply.from_user
          	   await bot.send_message(message.chat.id, f'🔞 | {user_name} трахнул(-а) {reply_user_name}', parse_mode='html')        
@dp.message_handler(content_types=['text'], text=["послать", "Послать"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   await bot.send_message(message.chat.id, f'🙊 | {user_name} послал(-а) на *** {reply_user_name}', parse_mode='html')
          	   
@dp.message_handler(content_types=['text'], text=["напугать", "Напугать"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   await bot.send_message(message.chat.id, f'😱 | {user_name} напугал(-а) {reply_user_name}', parse_mode='html')            
          	     
@dp.message_handler(content_types=['text'], text=["напоить", "Напоить"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   await bot.send_message(message.chat.id, f'🍛 | {user_name} напоил(-а)  {reply_user_name}', parse_mode='html')
          	   
@dp.message_handler(content_types=['text'], text=["наказать", "Наказать"])
async def rp2(message):
          	reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
          	user_name = message.from_user.get_mention(as_html=True)
          	reply = message.reply_to_message
          	if reply:
          	   await bot.send_message(message.chat.id, f'👊 | {user_name} наказал(-а) {reply_user_name}', parse_mode='html')           
          	   


   
@dp.message_handler(commands=["help"])
async def process_start_command(message: types.Message):
    await message.reply("Все команды в боте /chat - Группа создателя")
    

   
@dp.message_handler(content_types=['text'])
async def send(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    await message.answer(response['choices'][0]['text'])


if __name__ == '__main__':
    # Executing local server
    from aiogram import executor
    exec = executor.start_polling(dp, skip_updates=True)
    exec.loop.run_forever()