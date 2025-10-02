import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


BOT_TOKEN = '8245543069:AAFQMMk6KM-H6lYHG7M94iLzPAWXNuIIuqk'
CHANNEL_LINK = "https://t.me/ZOMBE_Team"


# Инициализация бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ========== КОНФИГУРАЦИЯ ========== #
LINKS = {
    'youtube': "https://youtube.com/@ZOMBE",
    'twitch': "https://twitch.tv/ZOMBE", 
    'tiktok': "https://tiktok.com/@ZOMBE",
    'channel': CHANNEL_LINK
}

# Словарь текстов для удобства управления и избежания дублирования
TEXTS = {
    'welcome': """
🎮 <b>ПРИВЕТ, {name}! ДОБРО ПОЖАЛОВАТЬ В ZOMBE TEAM! 🔥</b>

Мы - легендарная команда, которая 8 лет подряд не проходит на TI, 
но от этого стала только сильнее духом! 💪

<b>Используй кнопки ниже чтобы узнать о нас больше:</b>

• 🎮 <b>Состав команды</b> - наши звездные игроки
• 🏆 <b>TI 2026</b> - наш великий путь
• 📹 <b>Наш контент</b> - видео и стримы
• 📊 <b>Статистика</b> - наши "успехи"
• 📖 <b>Наша история</b> - как мы начинали

<b>Или переходи напрямую на наши платформы!</b>

<i>P.S. Дiма до сих пор не уверен на какой позиции играет...</i> 😂
    """,
    'team': """
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
  <i>"Из про-сцены в легенды ZOMBE!"</i>

• 🌟 <b>Величайший Максос (3 позиция)</b>
  Гордость Великих Лук, мета-брейкер!
  <i>"Я не играю в мету, я создаю её!"</i>

• ❓ <b>Дiма (1 позиция, но это не точно)</b>
  Темная лошадка команды!
  <i>"Иногда керри, иногда фидер - всегда сюрприз!"</i>

<b>Наша философия:</b>
"Мы не проигрываем - мы собираем опыт для TI 2026!" 🏆
    """,
    'bio': """
📖 <b>ИСТОРИЯ ZOMBE TEAM - ОТ НУЛЯ ДО ЛЕГЕНДЫ! 🚀</b>

<b>📅 2017 - Начало пути:</b>
Всё началось в интернет-кафе "Квант" в Великих Луках, где Величайший Максос играл на стареньком компьютере. К нему подсел парень с ником "Хохлорез" и сказал: "Бро, давай соберем команду!"

<b>🔥 2018 - Первый состав:</b>
Мы собрали первых 5 человек:
- Максос (оффлейн из В.Лук)
- Миша (керри с амбициями)  
- Стiс (роумер с улиц Киева)
- Дiма (загадочный тип из Москвы)
- DOMINIC (бывший про-игрок в поисках себя)

<b>💀 2019-2021 - Эра поражений:</b>
• 2019: Проиграли 50 матчей подряд
• 2020: Научились говорить "гг вп" не расстраиваясь
• 2021: Дiма впервые купил БКБ (и сразу умер)

<b>🌟 2022 - Переломный момент:</b>
DOMINIC, уставший от про-сцены, присоединился к нам на постоянной основе. С его приходом мы наконец-то выиграли 3 игры подряд!

<b>🎯 2023-2025 - Путь к славе:</b>
Создали YouTube канал, начали стримить на Twitch, завоевали 47 подписчиков в TikTok! Наши фейлы стали мемами, а неудачи - нашей фишкой!

<b>🚀 2026 - НАШ ГОД!</b>
8 лет упорных тренировок, тысячи проигранных матчей и несломленный дух привели нас к TI 2026!

<b>Наша миссия:</b> Доказать, что главное - не победа, а то, как ты проигрываешь! 😎

<i>"Мы не идеальны, но мы - ZOMBE!"</i> 💪
    """,
    'ti': """
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
    """,
    'content': """
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
    """,
    'stats': """
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
    """,
    'streams': """
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
    """,
    'help': """
🛠 <b>ДОСТУПНЫЕ КОМАНДЫ ZOMBE TEAM:</b>

<b>Основные команды:</b>
/start - Главное меню
/help - Эта справка
/team - Состав нашей легендарной команды
/ti - Наш путь к The International 2026
/content - Наш контент на всех платформах
/stats - Наша "впечатляющая" статистика
/bio - Наша история

<b>Быстрые команды:</b>
/streams - Ближайшие стримы

<b>Используй кнопки в меню для быстрого доступа!</b> 🎯
    """
}

# Функция для создания клавиатур (для переиспользования и эффективности)
def create_main_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 Состав команды", callback_data="team"),
         InlineKeyboardButton(text="🏆 TI 2026", callback_data="ti_info")],
        [InlineKeyboardButton(text="📹 Наш контент", callback_data="content"),
         InlineKeyboardButton(text="📊 Статистика", callback_data="stats")],
        [InlineKeyboardButton(text="📖 Наша история", callback_data="bio")],
        [InlineKeyboardButton(text="🎥 YouTube", url=LINKS['youtube']),
         InlineKeyboardButton(text="🔴 Twitch", url=LINKS['twitch'])],
        [InlineKeyboardButton(text="⚡️ TikTok", url=LINKS['tiktok']),
         InlineKeyboardButton(text="📢 Наш канал", url=LINKS['channel'])]
    ])

def create_back_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Главное меню", callback_data="main_menu")]
    ])

def create_content_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎥 YouTube", url=LINKS['youtube']),
         InlineKeyboardButton(text="🔴 Twitch", url=LINKS['twitch'])],
        [InlineKeyboardButton(text="⚡️ TikTok", url=LINKS['tiktok'])],
        [InlineKeyboardButton(text="🔙 Главное меню", callback_data="main_menu")]
    ])

def create_streams_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔴 Twitch", url=LINKS['twitch']),
         InlineKeyboardButton(text="🎥 YouTube", url=LINKS['youtube'])],
        [InlineKeyboardButton(text="🔙 Главное меню", callback_data="main_menu")]
    ])

# Универсальная функция для отправки/редактирования сообщений (снижает дублирование кода)
async def send_or_edit_text(obj, text_key: str, reply_markup=None, user_name: str = None, parse_mode=ParseMode.HTML):
    text = TEXTS[text_key]
    if user_name and "{name}" in text:
        text = text.format(name=user_name)
    if isinstance(obj, Message):
        await obj.answer(text, reply_markup=reply_markup, parse_mode=parse_mode)
    elif isinstance(obj, CallbackQuery):
        await obj.message.edit_text(text, reply_markup=reply_markup, parse_mode=parse_mode)
        await obj.answer()
    else:
        logger.error("Неизвестный тип объекта для отправки текста")

# ========== ОБРАБОТЧИКИ КОМАНД ========== #
@dp.message(CommandStart())
async def start_command(message: Message):
    """Команда /start"""
    user = message.from_user
    logger.info(f"🎯 Новый пользователь: {user.full_name}")
    await send_or_edit_text(message, 'welcome', create_main_keyboard(), user.first_name)

@dp.message(Command("help"))
async def help_command(message: Message):
    """Команда /help"""
    await send_or_edit_text(message, 'help')

@dp.message(Command("team"))
async def team_command(message: Message):
    """Команда /team"""
    await send_or_edit_text(message, 'team', create_back_keyboard())

@dp.message(Command("ti"))
async def ti_command(message: Message):
    """Команда /ti"""
    await send_or_edit_text(message, 'ti', create_back_keyboard())

@dp.message(Command("content"))
async def content_command(message: Message):
    """Команда /content"""
    await send_or_edit_text(message, 'content', create_content_keyboard())

@dp.message(Command("stats"))
async def stats_command(message: Message):
    """Команда /stats"""
    await send_or_edit_text(message, 'stats', create_back_keyboard())

@dp.message(Command("streams"))
async def streams_command(message: Message):
    """Команда /streams"""
    await send_or_edit_text(message, 'streams', create_streams_keyboard())

@dp.message(Command("bio"))
async def bio_command(message: Message):
    """Команда /bio"""
    await send_or_edit_text(message, 'bio', create_back_keyboard())

# Обработчик неизвестных сообщений (для лучшего UX)
@dp.message()
async def unknown_message(message: Message):
    """Обработчик неизвестных команд/сообщений"""
    await message.answer("❓ Неизвестная команда. Используйте /help для списка доступных команд.", parse_mode=ParseMode.HTML)

# ========== ОБРАБОТЧИКИ КНОПОК ========== #
@dp.callback_query(F.data == "main_menu")
async def main_menu_handler(callback: CallbackQuery):
    """Обработчик кнопки 'Главное меню'"""
    await send_or_edit_text(callback, 'welcome', create_main_keyboard(), callback.from_user.first_name)

@dp.callback_query(F.data == "team")
async def team_handler(callback: CallbackQuery):
    """Обработчик кнопки 'Состав команды'"""
    await send_or_edit_text(callback, 'team', create_back_keyboard())

@dp.callback_query(F.data == "ti_info")
async def ti_handler(callback: CallbackQuery):
    """Обработчик кнопки 'TI 2026'"""
    await send_or_edit_text(callback, 'ti', create_back_keyboard())

@dp.callback_query(F.data == "content")
async def content_handler(callback: CallbackQuery):
    """Обработчик кнопки 'Наш контент'"""
    await send_or_edit_text(callback, 'content', create_content_keyboard())

@dp.callback_query(F.data == "stats")
async def stats_handler(callback: CallbackQuery):
    """Обработчик кнопки 'Статистика'"""
    await send_or_edit_text(callback, 'stats', create_back_keyboard())

@dp.callback_query(F.data == "bio")
async def bio_handler(callback: CallbackQuery):
    """Обработчик кнопки 'Наша история'"""
    await send_or_edit_text(callback, 'bio', create_back_keyboard())

# Обработчик неизвестных callback (для robustness)
@dp.callback_query()
async def unknown_callback(callback: CallbackQuery):
    """Обработчик неизвестных callback"""
    await callback.answer("❓ Неизвестная кнопка. Вернитесь в главное меню с помощью /start.", show_alert=True)

# ========== ЗАПУСК ========== #
async def main():
    if not BOT_TOKEN:
        logger.error("❌ BOT_TOKEN не установлен!")
        return
    logger.info("🚀 Бот ZOMBE Team запущен с командами и кнопками!")
    logger.info("📝 Доступные команды: /start, /help, /team, /ti, /content, /stats, /streams, /bio")
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"❌ Ошибка при запуске: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
