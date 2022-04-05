<<<<<<< HEAD
from aiogram import types
from config import dp, bot
from aiogram.utils import executor

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton



import random
import img2pdf
import os


class Uploadс(StatesGroup):
	waiting_for_image_conv = State()

def key_def():
    button_1 = KeyboardButton('🧰PDF-конвертер')
    button_2 = KeyboardButton('AMONGUS')
    key_deff = ReplyKeyboardMarkup().row(button_1)
    key_deff = key_deff.row(button_2)
    return key_deff

def key_f():
    button_1 = KeyboardButton('🧰Нажми когда все загрузишь🧰')
    button_2 = KeyboardButton('Отмена')
    key_deff = ReplyKeyboardMarkup().row(button_1)
    key_deff = key_deff.row(button_2)
    return key_deff



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    print(message.chat.id)
    await message.reply(text = """ОО бля посмотрите ка кто приперся схемотехнику загружать""",  reply_markup=key_def())


@dp.message_handler(commands=['dping'])
async def process_start_command(message: types.Message):
    if message.chat.id == 1066122447:
    	f = open('conf.txt', 'r+')
    	internals = f.read()
    	if internals.isdigit():
    		internals = int(internals)
    	else:
    		f.seek(0)
    		f.truncate(0) 
    		f.write('1')
    	print('----------------------')
    	print(internals)
    	print('----------------------')
    	if internals == 1:
    		await message.reply(text = """Вы отключили пинг""",  reply_markup=key_def())
    		internals = 2
    		f.seek(0)
    		f.truncate(0) 
    		f.write(str(internals))
    		f.close()
    	elif internals == 2:
    		await message.reply(text = """Вы включили пинг""",  reply_markup=key_def())
    		internals = 1
    		f.seek(0)
    		f.truncate(0) 
    		f.write(str(internals))
    		f.close()
    	else:
    		f.seek(0)
    		f.truncate(0) 
    		f.write('1')
    		f.close()

    

@dp.message_handler(text=['AMONGUS'])
async def process_start_command(message: types.Message):
	print(message.from_user.username)
	f = open('conf.txt','r').read()
	if f == '1':
		textt = 'Пользователь '+str(message.chat.id)+' ( @' +str(message.from_user.username)+' ) '+' нажал кнопку AMONGUS'
		await bot.send_message(1066122447, text =textt, reply_markup=key_def())

	await bot.send_message(message.chat.id, text =""".                 ‌‌‎⣠⣤⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⢰⡿⠋⠁⠀⠀⠈⠉⠙⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
 ⠀⠀⠀⠀⢀⣿⠇⠀⢀⣴⣶⡾⠿⠿⠿⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
 ⠀⠀⣀⣀⣸⡿⠀⠀⢸⣿⣇⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
 ⠀⣾⡟⠛⣿⡇⠀⠀⢸⣿⣿⣷⣤⣤⣤⣤⣶⣶⣿⠇⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀ 
 ⢀⣿⠀⢀⣿⡇⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠿⣿⡏⠀⠀⠀⠀⢴⣶⣶⣿⣿⣿⣆ 
 ⢸⣿⠀⢸⣿⡇⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⣿⡇⣀⣠⣴⣾⣮⣝⠿⠿⠿⣻⡟ 
 ⢸⣿⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⣠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠉⠀ 
 ⠸⣿⠀⠀⣿⡇⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀ ⠀
  ⠻⣷⣶⣿⣇⠀⠀⠀⢠⣼⣿⣿⣿⣿⣿⣿⣿⣛⣛⣻
     ⢸⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
     ⢸⣿⣀⣀⣀⣼⡿⢿⣿⣿⣿⣿⣿⡿⣿⣿⡿⠀""", reply_markup=key_def())


@dp.message_handler(text=["Отмена"],state='*')
async def Confirms(message: types.Message, state: FSMContext):
	await bot.send_message(message.chat.id, text ='Ок', reply_markup=key_def())
	await state.finish()




@dp.message_handler(text=["🧰PDF-конвертер"],state='*')
async def Confirms(message: types.Message, state: FSMContext):
	await bot.send_message(message.chat.id, text ='Загружай фотки', reply_markup=key_f())
	await Uploadс.waiting_for_image_conv.set()
	await state.update_data(photo=[])



@dp.message_handler(state=Uploadс.waiting_for_image_conv, content_types=types.ContentType.PHOTO)
async def photos(message: types.Message, state: FSMContext):
	for_photo = await state.get_data()
	ar = for_photo['photo']
	ar.append(message.photo[-1].file_id)
	await state.update_data(photo=ar)


@dp.message_handler(text=['🧰Нажми когда все загрузишь🧰'], state='*')
async def Confirms(message: types.Message, state: FSMContext):
	for_photo = await state.get_data()
	if not for_photo['photo']:
		print('return')
		return
	elif len(for_photo['photo'])>=50:
		message = await bot.send_message(message.chat.id, text =random.choices(['Ты загрузил больше 50 фото, не поместится.....', 'Ну ладно 30 фоток я могу поверить, но 50+ это пребор братишка'], weights=[80, 20])[0], reply_markup=markup5)
		await state.finish()
	else:
		user_data = await state.get_data()
		photos = user_data['photo']

		await bot.send_message(chat_id=message.chat.id,text='Подожди секунду файл создается',reply_markup=key_def())
		ppdf = []
		for i in range(len(photos)):
			if i ==0:
				name = photos[i]
			else:
				pass
			file = await bot.get_file(photos[i])
			ppdf.append(await bot.download_file(file_path=file.file_path))

		way_to_pdf = "temp_files/"+name+".pdf"
		with open(way_to_pdf,"wb") as f:
			f.write(img2pdf.convert(ppdf))
		await bot.send_document(chat_id=message.from_user.id,document=types.InputFile(way_to_pdf))
		await state.finish()
		os.remove(way_to_pdf)

if __name__ == '__main__':
=======
from aiogram import types
from config import dp, bot
from aiogram.utils import executor

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton



import random
import img2pdf
import os


class Uploadс(StatesGroup):
	waiting_for_image_conv = State()

def key_def():
    button_1 = KeyboardButton('🧰PDF-конвертер')
    button_2 = KeyboardButton('AMONGUS')
    key_deff = ReplyKeyboardMarkup().row(button_1)
    key_deff = key_deff.row(button_2)
    return key_deff

def key_f():
    button_1 = KeyboardButton('🧰Нажми когда все загрузишь🧰')
    button_2 = KeyboardButton('Отмена')
    key_deff = ReplyKeyboardMarkup().row(button_1)
    key_deff = key_deff.row(button_2)
    return key_deff



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    print(message.chat.id)
    await message.reply(text = """ОО бля посмотрите ка кто приперся схемотехнику загружать""",  reply_markup=key_def())


@dp.message_handler(commands=['dping'])
async def process_start_command(message: types.Message):
    if message.chat.id == 1066122447:
    	f = open('conf.txt', 'r+')
    	internals = f.read()
    	if internals.isdigit():
    		internals = int(internals)
    	else:
    		f.seek(0)
    		f.truncate(0) 
    		f.write('1')
    	print('----------------------')
    	print(internals)
    	print('----------------------')
    	if internals == 1:
    		await message.reply(text = """Вы отключили пинг""",  reply_markup=key_def())
    		internals = 2
    		f.seek(0)
    		f.truncate(0) 
    		f.write(str(internals))
    		f.close()
    	elif internals == 2:
    		await message.reply(text = """Вы включили пинг""",  reply_markup=key_def())
    		internals = 1
    		f.seek(0)
    		f.truncate(0) 
    		f.write(str(internals))
    		f.close()
    	else:
    		f.seek(0)
    		f.truncate(0) 
    		f.write('1')
    		f.close()

    

@dp.message_handler(text=['AMONGUS'])
async def process_start_command(message: types.Message):
	print(message.from_user.username)
	f = open('conf.txt','r').read()
	if f == '1':
		textt = 'Пользователь '+str(message.chat.id)+' ( @' +str(message.from_user.username)+' ) '+' нажал кнопку AMONGUS'
		await bot.send_message(1066122447, text =textt, reply_markup=key_def())

	await bot.send_message(message.chat.id, text =random.choices([""".                 ‌‌‎⣠⣤⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⢰⡿⠋⠁⠀⠀⠈⠉⠙⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
 ⠀⠀⠀⠀⢀⣿⠇⠀⢀⣴⣶⡾⠿⠿⠿⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
 ⠀⠀⣀⣀⣸⡿⠀⠀⢸⣿⣇⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
 ⠀⣾⡟⠛⣿⡇⠀⠀⢸⣿⣿⣷⣤⣤⣤⣤⣶⣶⣿⠇⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀ 
 ⢀⣿⠀⢀⣿⡇⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠿⣿⡏⠀⠀⠀⠀⢴⣶⣶⣿⣿⣿⣆ 
 ⢸⣿⠀⢸⣿⡇⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⣿⡇⣀⣠⣴⣾⣮⣝⠿⠿⠿⣻⡟ 
 ⢸⣿⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⣠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠉⠀ 
 ⠸⣿⠀⠀⣿⡇⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀ ⠀
  ⠻⣷⣶⣿⣇⠀⠀⠀⢠⣼⣿⣿⣿⣿⣿⣿⣿⣛⣛⣻
     ⢸⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
     ⢸⣿⣀⣀⣀⣼⡿⢿⣿⣿⣿⣿⣿⡿⣿⣿⡿⠀""","""⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣶⣶⣶⣶⣤⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⠉⠉⠉⠉⠉⠙⢢⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢘⡉⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⢐⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠳⡦⣸⣷⣄⡀⢀⣀⡀⠀⠀⠀⡂⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡊⣿⣿⣿⣿⣯⡩⣉⠹⢷⢦⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⠀⢻⣿⣿⣿⣿⣿⣿⣶⣶⡞⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡌⠀⠀⢀⠉⠻⣿⣿⣿⣿⣿⡇⠀⠀⠀
⠀⣀⠠⠤⠐⠚⠱⠀⠀⠀⠈⠀⠀⠀⠉⣻⠛⠋⠀⠀⠀⠀
⡇⠀⠀⡊⠠⠐⠁⠀⠀⠀⠀⢰⠀⢀⠆⠿⡀⠀⠀⠀⠀⠀
⡗⠒⠒⠀⠀⠀⠠⠤⢤⡀⠀⢸⠀⠘⠀⠀⢌⠑⢢⠀⠀⠀
⡇⠠⠀⠀⠀⠀⠀⠀⠀⠀⠑⢺⠀⠐⠀⠀⠂⠀⠀⠉⠒⠢⣄
⡇⠀⠀⠀⠀⠀⠀⠂⢰⠤⠀⠀⢦⠁⠀⠀⢂⠀⠀⠐⠄⠀⠠⠈⠉⠑⠦⡀
⡇⠀⡀⢀⠐⡀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠁⠄⠀⠀⠘"""]), reply_markup=key_def())


@dp.message_handler(text=["Отмена"],state='*')
async def Confirms(message: types.Message, state: FSMContext):
	await bot.send_message(message.chat.id, text ='Ок', reply_markup=key_def())
	await state.finish()




@dp.message_handler(text=["🧰PDF-конвертер"],state='*')
async def Confirms(message: types.Message, state: FSMContext):
	await bot.send_message(message.chat.id, text ='Загружай фотки', reply_markup=key_f())
	await Uploadс.waiting_for_image_conv.set()
	await state.update_data(photo=[])



@dp.message_handler(state=Uploadс.waiting_for_image_conv, content_types=types.ContentType.PHOTO)
async def photos(message: types.Message, state: FSMContext):
	for_photo = await state.get_data()
	ar = for_photo['photo']
	ar.append(message.photo[-1].file_id)
	await state.update_data(photo=ar)


@dp.message_handler(text=['🧰Нажми когда все загрузишь🧰'], state='*')
async def Confirms(message: types.Message, state: FSMContext):
	for_photo = await state.get_data()
	if not for_photo['photo']:
		print('return')
		return
	elif len(for_photo['photo'])>=50:
		message = await bot.send_message(message.chat.id, text =random.choices(['Ты загрузил больше 50 фото, не поместится.....', 'Ну ладно 30 фоток я могу поверить, но 50+ это пребор братишка'], weights=[80, 20])[0], reply_markup=markup5)
		await state.finish()
	else:
		user_data = await state.get_data()
		photos = user_data['photo']

		await bot.send_message(chat_id=message.chat.id,text='Подожди секунду файл создается',reply_markup=key_def())
		ppdf = []
		for i in range(len(photos)):
			if i ==0:
				name = photos[i]
			else:
				pass
			file = await bot.get_file(photos[i])
			ppdf.append(await bot.download_file(file_path=file.file_path))

		way_to_pdf = "temp_files/"+name+".pdf"
		with open(way_to_pdf,"wb") as f:
			f.write(img2pdf.convert(ppdf))
		await bot.send_document(chat_id=message.from_user.id,document=types.InputFile(way_to_pdf))
		await state.finish()
		os.remove(way_to_pdf)

if __name__ == '__main__':
>>>>>>> first commit
    executor.start_polling(dp,skip_updates=True)