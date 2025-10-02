import asyncio
import logging
from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = '8196826964:AAEvCpkPFrwwoFoeNrvjOdND25s7lVJJ1Js'
CHANNEL_USERNAME = "@ZOBME_team"
CHANNEL_INVITE_LINK = "https://t.me/ZOMBE_Team"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()

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
🎮 <b>ПРИВЕТ, {user_name}! ДОБРО ПОЖАЛОВАТЬ В ZOMBE TEAM! 🔥</b>

Мы - легендарная команда, которая 8 лет подряд не проходит на TI, 
но от этого стала только сильнее духом! 💪

<b>Используй кнопки ниже чтобы узнать о нас больше:</b>

• 🎮 <b>Состав команды</b> - наши звездные игроки
• 🏆 <b>TI 2026</b> - наш великий путь
• 📹 <b>Наш контент</b> - видео и стримы
• 📊 <b>Статистика</b> - наши "успехи"

<b>Или переходи напрямую на наши платформы!</b>

<i>P.S. Дiма до сих пор не уверен на какой позиции играет...</i> 😂
    """
    
    await bot.send_message(
        chat_id=chat_id,
        text=welcome_text,
        reply_markup=main_keyboard,
        parse_mode=ParseMode.HTML
    )

# ========== КОМАНДЫ ========== #

@dp.message(CommandStart())
async def start_command(message: Message):
    """Команда /start"""
    user = message.from_user
    logger.info(f"🎯 Новый пользователь: {user.full_name}")
    await send_welcome_message(message.chat.id, user.first_name)

@dp.message(Command("help"))
async def help_command(message: Message):
    """Команда /help - список всех команд"""
    
    help_text = """
🛠 <b>ДОСТУПНЫЕ КОМАНДЫ ZOMBE TEAM:</b>

<b>Основные команды:</b>
/start - Главное меню
/help - Эта справка
/team - Состав нашей легендарной команды
/ti - Наш путь к The International 2026
/content - Наш контент на всех платформах
/stats - Наша "впечатляющая" статистика

<b>Быстрые команды:</b>
/streams - Ближайшие стримы
/matches - Последние матчи
/goals - Наши цели на сезон

<b>Используй кнопки в меню для быстрого доступа!</b> 🎯
    """
    
    await message.answer(help_text, parse_mode=ParseMode.HTML)

@dp.message(Command("team"))
async def team_command(message: Message):
    """Команда /team - состав команды"""
    
    team_text = """
🎮 <b>ZOMBE TEAM - СОСТАВ ЛЕГЕНД</b>

<b>Наши звезды, которые почти прошли на TI:</b>

• 🔥 <b>Миша Хохлорез (2 позиция)</b>
  Фармит как бог, дерется как демон!
  <i>"Я не фармлю, я инвестирую в победу!"</i>

• 🎯 <b>Стiс (4 позиция)</b>
  Роуминг-машина, ноумер ван по патикам!
  <i>"Вижу врага - значит, он уже мертв!"</i>

• 💎 <b>DOMINIC (5 позиция)</b>
  Бывший про-игрок Aurora Gaming!
  <i>"Из про-сцены в легенды ZOBME!"</i>

• 🌟 <b>Величайший Максос (3 позиция)</b>
  Гордость Великих Лук, мета-брейкер!
  <i>"Я не играю в мету, я создаю её!"</i>

• ❓ <b>Дiма (1 позиция, но это не точно)</b>
  Темная лошадка команды!
  <i>"Иногда керри, иногда фидер - всегда сюрприз!"</i>

<b>Наша философия:</b>
"Мы не проигрываем - мы собираем опыт для TI 2026!" 🏆
    """
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🏆 Узнать про TI", callback_data="ti_info"),
                InlineKeyboardButton(text="📹 Наш контент", callback_data="content")
            ],
            [
                InlineKeyboardButton(text="🔙 Главное меню", callback_data="main_menu")
            ]
        ]
    )
    
    await message.answer(team_text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

@dp.message(Command("ti"))
async def ti_command(message: Message):
    """Команда /ti - история TI"""
    
    ti_text = """
🏆 <b>ИСТОРИЯ НАШИХ ВЕЛИКИХ БИТВ ЗА TI</b>

📅 <b>Наш путь к славе (пока не очень успешный):</b>

• <b>TI 2018:</b> "В следующий раз точно пройдем!"
• <b>TI 2019:</b> "Мета не та была..."
• <b>TI 2020:</b> "Пандемия помешала!"
• <b>TI 2021:</b> "Судьи были необъективны!"
• <b>TI 2022:</b> "Нас задидосили!"
• <b>TI 2023:</b> "Компьютер сломался в квалификациях!"
• <b>TI 2024:</b> "Патч вышел неудачный!"
• <b>TI 2025:</b> "Мы уже почти прошли, но..."

🎯 <b>TI 2026:</b> А вот это уже точно наш год! 
Готовьтесь, Dota-мир! ZOMBE едет на TI! 💪

<b>Наша подготовка:</b>
✅ Придумали новые оправдания
✅ Научились говорить "гг вп" после поражения
✅ Дiма определился с позицией (наверное)

<i>Стiс обещал перестать роумить на 1 уровне, если пройдем</i> 😂
    """
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🎮 Состав команды", callback_data="team"),
                InlineKeyboardButton(text="📊 Статистика", callback_data="stats")
            ],
            [
                InlineKeyboardButton(text="🔙 Главное меню", callback_data="main_menu")
            ]
        ]
    )
    
    await message.answer(ti_text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

@dp.message(Command("content"))
async def content_command(message: Message):
    """Команда /content - наш контент"""
    
    content_text = """
🎬 <b>КОНТЕНТ ZOMBE TEAM - СМЕХ И АДРЕНАЛИН! 🚀</b>

<b>📹 YouTube:</b>
🎥 "КАК ПРОИГРАТЬ 1000 ММР И УЛЫБАТЬСЯ"
🎥 "ТОП-10 НАШИХ ЛУЧШИХ ФЕДОВ"
🎥 "ДiMA: КЕРРИ ИЛИ ФИДЕР? РАССЛЕДОВАНИЕ"

<b>🔴 Twitch стримы:</b>
⏰ Каждый день с 19:00 МСК
💬 Живое общение с легендами
🎁 Раздачи предметов за подписку

<b>⚡️ TikTok:</b>
📱 Короткие нарезки лучших моментов
😂 Мемы и приколы от команды
🎮 Геймплей без цензуры!

<b>🎯 Эксклюзив для подписчиков:</b>
• Запись наших тренировок
• Разборы тактик (как надо было играть)
• Интервью с DOMINIC про Aurora Gaming

<b>Подписывайся на все платформы! Будет жарко! 🔥</b>
    """
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🎥 YouTube", url="https://youtube.com/@ZOBME"),
                InlineKeyboardButton(text="🔴 Twitch", url="https://twitch.tv/ZOBME")
            ],
            [
                InlineKeyboardButton(text="⚡️ TikTok", url="https://tiktok.com/@ZOBME"),
                InlineKeyboardButton(text="📢 Канал", url=CHANNEL_INVITE_LINK)
            ],
            [
                InlineKeyboardButton(text="🔙 Главное меню", callback_data="main_menu")
            ]
        ]
    )
    
    await message.answer(content_text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

@dp.message(Command("stats"))
async def stats_command(message: Message):
    """Команда /stats - наша статистика"""
    
    stats_text = """
📊 <b>СТАТИСТИКА ZOMBE TEAM - ЦИФРЫ НЕ ВРУТ! 📈</b>

<b>Общая статистика:</b>
• 🎯 Матчей сыграно: 2,547
• 🏆 Побед: 1,203 (47.2%)
• 💀 Поражений: 1,344 (52.8%)
• ⭐️ Лучшая серия побед: 3 игры!

<b>Персональная статистика:</b>
• 🔥 Миша Хохлорез: 552 GPM (в среднем)
• 🎯 Стiс: 23.7 патиков за матч
• 💎 DOMINIC: 87% вардов (покупает хотя бы)
• 🌟 Максос: 4.8 КДА на оффлейне
• ❓ Дiма: 50% winrate (на какой позиции?)

<b>Достижения сезона:</b>
✅ Не распались после 10 поражений подряд
✅ Нашли 5-го игрока (DOMINIC)
✅ Дiма наконец-то купил БКБ (один раз)
✅ Не зафейлили драфт (в последнем матче)

<b>Цель на сезон:</b>
Повысить винрейт до 50%! 🎯
    """
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🎮 Состав", callback_data="team"),
                InlineKeyboardButton(text="🏆 TI 2026", callback_data="ti_info")
            ],
            [
                InlineKeyboardButton(text="🔙 Главное меню", callback_data="main_menu")
            ]
        ]
    )
    
    await message.answer(stats_text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

@dp.message(Command("streams"))
async def streams_command(message: Message):
    """Команда /streams - ближайшие стримы"""
    
    streams_text = """
🔴 <b>БЛИЖАЙШИЕ СТРИМЫ ZOMBE TEAM</b>

<b>Расписание на неделю:</b>

📅 <b>Сегодня 20:00 МСК</b>
🎮 Рейтинговые игры с Мишей Хохлорезом
💬 Ответы на вопросы про 1 позицию

📅 <b>Завтра 19:00 МСК</b>  
🏆 Квалификации на очередной мини-турнир
🎯 Стiс покажет свой роуминг

📅 <b>Среда 21:00 МСК</b>
💎 DOMINIC обучает саппорт-игре
📚 Разбор вард-позиций от экс-про

<b>Специальные стримы:</b>
⭐️ Четверг - стрим с загадочным Дiмой
🌟 Пятница - Величайший Максос ломает мету

<b>Не пропусти! Будет эпично! 🚀</b>
    """
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🔴 Twitch", url="https://twitch.tv/ZOBME"),
                InlineKeyboardButton(text="📹 YouTube", url="https://youtube.com/@ZOBME")
            ],
            [
                InlineKeyboardButton(text="🔙 Главное меню", callback_data="main_menu")
            ]
        ]
    )
    
    await message.answer(streams_text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

# ========== ОБРАБОТЧИКИ КНОПОК ========== #

@dp.callback_query(F.data == "main_menu")
async def main_menu_handler(callback: CallbackQuery):
    """Обработчик кнопки 'Главное меню'"""
    await callback.message.edit_text(
        text="🎮 <b>ГЛАВНОЕ МЕНЮ ZOBME TEAM</b>\n\nВыбери что тебя интересует:",
        reply_markup=main_keyboard,
        parse_mode=ParseMode.HTML
    )
    await callback.answer()

@dp.callback_query(F.data == "team")
async def team_handler(callback: CallbackQuery):
    """Обработчик кнопки 'Состав команды'"""
    team_text = """
🎮 <b>ZOMBE TEAM - СОСТАВ ЛЕГЕНД</b>

• 🔥 <b>Миша Хохлорез</b> - 2 позиция
• 🎯 <b>Стiс</b> - 4 позиция  
• 💎 <b>DOMINIC</b> - 5 позиция (экс Aurora)
• 🌟 <b>Величайший Максос</b> - 3 позиция
• ❓ <b>Дiма</b> - 1 позиция (но это не точно)

Используй команду /team для полной информации!
    """
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🏆 TI 2026", callback_data="ti_info"),
                InlineKeyboardButton(text="📹 Контент", callback_data="content")
            ],
            [
                InlineKeyboardButton(text="🔙 Главное меню", callback_data="main_menu")
            ]
        ]
    )
    
    await callback.message.edit_text(
        text=team_text,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML
    )
    await callback.answer()

@dp.callback_query(F.data == "ti_info")
async def ti_handler(callback: CallbackQuery):
    """Обработчик кнопки 'TI 2026'"""
    ti_text = "🏆 <b>TI 2026 - НАША ЦЕЛЬ!</b>\n\nИспользуй команду /ti чтобы узнать всю историю наших попыток!"
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🎮 Состав", callback_data="team"),
                InlineKeyboardButton(text="📊 Статистика", callback_data="stats")
            ],
            [
                InlineKeyboardButton(text="🔙 Главное меню", callback_data="main_menu")
            ]
        ]
    )
    
    await callback.message.edit_text(
        text=ti_text,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML
    )
    await callback.answer()

@dp.callback_query(F.data == "content")
async def content_handler(callback: CallbackQuery):
    """Обработчик кнопки 'Наш контент'"""
    content_text = "📹 <b>НАШ КОНТЕНТ</b>\n\nИспользуй команду /content чтобы увидеть все наши платформы и расписание!"
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🎥 YouTube", url="https://youtube.com/@ZOBME"),
                InlineKeyboardButton(text="🔴 Twitch", url="https://twitch.tv/ZOBME")
            ],
            [
                InlineKeyboardButton(text="⚡️ TikTok", url="https://tiktok.com/@ZOBME")
            ],
            [
                InlineKeyboardButton(text="🔙 Главное меню", callback_data="main_menu")
            ]
        ]
    )
    
    await callback.message.edit_text(
        text=content_text,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML
    )
    await callback.answer()

@dp.callback_query(F.data == "stats")
async def stats_handler(callback: CallbackQuery):
    """Обработчик кнопки 'Статистика'"""
    stats_text = "📊 <b>СТАТИСТИКА</b>\n\nИспользуй команду /stats чтобы увидеть наши впечатляющие цифры!"
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🎮 Состав", callback_data="team"),
                InlineKeyboardButton(text="🏆 TI 2026", callback_data="ti_info")
            ],
            [
                InlineKeyboardButton(text="🔙 Главное меню", callback_data="main_menu")
            ]
        ]
    )
    
    await callback.message.edit_text(
        text=stats_text,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML
    )
    await callback.answer()

async def main():
    logger.info("🚀 Бот ZOMBE Team запущен с командами и кнопками!")
    logger.info("📝 Доступные команды: /start, /help, /team, /ti, /content, /stats, /streams")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())