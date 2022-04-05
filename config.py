from aiogram import Bot, types
import logging
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token='5140865976:AAGo8DLrDeKpFdcHIAOnOsue5ho3fWmelWA')
dp = Dispatcher(bot,storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)