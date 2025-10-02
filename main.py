import asyncio
import logging
import os
import sys
from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Получение токена из переменных окружения
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    logger.error("❌ BOT_TOKEN не найден! Установите переменную окружения.")
    sys.exit(1)

CHANNEL_USERNAME = "@ZOBME_team"
CHANNEL_INVITE_LINK = "https://t.me/ZOBME_team"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Основная клавиатура с командами
main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🎮 Состав команды", callback_data="team"),
            InlineKeyboardButton(text="🏆 TI 2026", callback_data="ti_info")
        ],
        [
            InlineKeyboardButton(text="📹 Наш контент", callback_data="content"),
            InlineKeyboardButton(text="📊 Статистика", callback_data="stats")
        ],
        [
            InlineKeyboardButton(text="🎥 YouTube", url="https://youtube.com/@ZOBME"),
            InlineKeyboardButton(text="🔴 Twitch", url="https://twitch.tv/ZOBME")
        ],
        [
            InlineKeyboardButton(text="⚡️ TikTok", url="https://tiktok.com/@ZOBME"),
            InlineKeyboardButton(text="📢 Наш канал", url=CHANNEL_INVITE_LINK)
        ]
    ]
)

async def send_welcome_message(chat_id: int, user_name: str):
    """Отправляет приветственное сообщение"""
    welcome_text = f"""
🎮 <b>ПРИВЕТ, {user_name}! ДОБРО ПОЖАЛОВАТЬ В ZOBME TEAM! 🔥</b>

Мы - легендарная команда, которая 8 лет подряд не проходит на TI! 

Используй кнопки ниже чтобы узнать о нас больше! 🎯
    """
    
    await bot.send_message(
        chat_id=chat_id,
        text=welcome_text,
        reply_markup=main_keyboard,
        parse_mode=ParseMode.HTML
    )

# Все обработчики команд остаются такими же как в предыдущем коде
@dp.message(CommandStart())
async def start_command(message: Message):
    user = message.from_user
    logger.info(f"🎯 Новый пользователь: {user.full_name}")
    await send_welcome_message(message.chat.id, user.first_name)

@dp.message(Command("help"))
async def help_command(message: Message):
    help_text = """
🛠 <b>ДОСТУПНЫЕ КОМАНДЫ:</b>
/start - Главное меню
/help - Справка
/team - Состав команды
/ti - Наш путь к TI
/content - Наш контент
/stats - Статистика
/streams - Стримы
    """
    await message.answer(help_text, parse_mode=ParseMode.HTML)

@dp.message(Command("team"))
async def team_command(message: Message):
    team_text = """
🎮 <b>ZOBME TEAM - СОСТАВ ЛЕГЕНД</b>
• 🔥 <b>Миша Хохлорез</b> - 1 позиция
• 🎯 <b>Стiс</b> - 4 позиция  
• 💎 <b>DOMINIC</b> - 5 позиция
• 🌟 <b>Величайший Максос</b> - 3 позиция
• ❓ <b>Дiма</b> - 1 позиция (но это не точно)
    """
    await message.answer(team_text, parse_mode=ParseMode.HTML)

# Добавьте остальные команды из предыдущего кода...

# Обработчики callback'ов
@dp.callback_query(F.data == "main_menu")
async def main_menu_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        text="🎮 <b>ГЛАВНОЕ МЕНЮ ZOBME TEAM</b>\n\nВыбери что тебя интересует:",
        reply_markup=main_keyboard,
        parse_mode=ParseMode.HTML
    )
    await callback.answer()

@dp.callback_query(F.data == "team")
async def team_handler(callback: CallbackQuery):
    team_text = "🎮 <b>Состав ZOBME Team</b>\n\nИспользуй /team для полной информации!"
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="🔙 Главное меню", callback_data="main_menu")]]
    )
    await callback.message.edit_text(text=team_text, reply_markup=keyboard, parse_mode=ParseMode.HTML)
    await callback.answer()

# Добавьте остальные обработчики callback'ов...

async def main():
    logger.info("🚀 ZOBME Bot запущен на хостинге!")
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    asyncio.run(main())