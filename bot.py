from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

TOKEN = "8038703445:AAHq-7WaSpel99M6sKiXWwz7mugCsv7jw64"
ADMIN_ID = 7574702101  # Айди админа
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# ===== Кнопки =====
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(KeyboardButton("💎 Алмаз Харидан"))
main_menu.add(KeyboardButton("⚙ Настройка"))

back_menu = ReplyKeyboardMarkup(resize_keyboard=True)
back_menu.add(KeyboardButton("⬅️ Ба Кафо"))
back_menu.add(KeyboardButton("🏠 Меню"))

# ===== Inline кнопки прайс-листа =====
def get_price_inline():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("💎100 — 10 🇹🇯s", callback_data="100💎"),
        InlineKeyboardButton("💎200 — 20 🇹🇯s", callback_data="200💎"),
        InlineKeyboardButton("💎300 — 30 🇹🇯s", callback_data="300💎"),
        InlineKeyboardButton("💎400 — 40 🇹🇯s", callback_data="400💎"),
        InlineKeyboardButton("💎500 — 50 🇹🇯s", callback_data="500💎"),
        InlineKeyboardButton("💎1000 — 100 🇹🇯s", callback_data="1000💎"),
        InlineKeyboardButton("💎2000 — 200 🇹🇯s", callback_data="2000💎"),
        InlineKeyboardButton("🗓️ Лайт — 10 🇹🇯s", callback_data="Ваучер Лайт"),
        InlineKeyboardButton("🗓️ Ҳафта — 15 🇹🇯s", callback_data="Ваучер Ҳафта"),
        InlineKeyboardButton("🗓️ Моҳ — 90 🇹🇯s", callback_data="Ваучер Моҳ"),
        InlineKeyboardButton("🎫 Буях Пропуск — 15 🇹🇯s", callback_data="Буях Пропуск")
    )
    return kb

# ===== Кнопки оплаты =====
pay_menu = InlineKeyboardMarkup(row_width=2)
pay_menu.add(
    InlineKeyboardButton("D/City 💳", url="http://pay.expresspay.tj/?A=9762000169349346&s=9.5&c=&f1=133"),
    InlineKeyboardButton("⬅️ Ба Кафо", callback_data="back")
)

# ===== /start =====
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(
        "╔════════════════════════════════════╗\n"
        "🎄 Хуш Омадед Ба Боти FF - HUSANOV! 🎄\n"
        "╚════════════════════════════════════╝\n\n"
        "Барои Алмаз Харидан ё Настройка ⚙ Free Fire Лутфан Чизи Мехостагиатонро Интихоб Кунед!🎁",
        reply_markup=main_menu
    )

# ===== Основной хэндлер сообщений =====
@dp.message_handler()
async def main_handler(message: types.Message):
    text = message.text

    if text == "💎 Алмаз Харидан":
        await message.answer("Барои Алмаз Харидори Кардан Айдии Худатон - Ро Ба Ман Фиристед!", reply_markup=back_menu)

    elif text == "⚙ Настройка":
        await message.answer("⚙ Настройка Free Fire: Функция позже", reply_markup=back_menu)

    elif text == "⬅️ Ба Кафо":
        await message.answer("Барои Давом Лутфан Чизи Мехостагиатонро Интихоб Кунед!🎁", reply_markup=main_menu)

    elif text == "🏠 Меню":
        await message.answer("Меню", reply_markup=main_menu)

    else:
        # Пользователь ввёл айди
        user_id = text
        price_list_msg = (
            "✨ Прайс Лист Алмазҳо 💎\n"
            "────────────────────\n"
            "💎100 — 10 🇹🇯\n"
            "💎200 — 20 🇹🇯\n"
            "💎300 — 30 🇹🇯\n"
            "💎400 — 40 🇹🇯\n"
            "💎500 — 50 🇹🇯\n"
            "💎1000 — 100 🇹🇯\n"
            "💎2000 — 200 🇹🇯\n"
            "🗓️ Лайт — 10 🇹🇯\n"
            "🗓️ Ҳафта — 15 🇹🇯\n"
            "🗓️ Моҳ — 90 🇹🇯\n"
            "🎫 Буях Пропуск — 15 🇹🇯\n"
            "────────────────────"
        )
        await message.answer(f"Айдии Шумо : {user_id}\n\n{price_list_msg}", reply_markup=get_price_inline())

# ===== Обработка выбора товара =====
@dp.callback_query_handler(lambda c: c.data != "back")
async def price_callback(callback_query: types.CallbackQuery):
    data = callback_query.data
    await bot.answer_callback_query(callback_query.id)

    # Сообщение оплаты с рамкой и эмодзи
    await bot.send_message(
        callback_query.from_user.id,
        f"╔═══════════════════════╗\n"
        f"🎁 Вы выбрали: {data}\n"
        f"╚═══════════════════════╝\n\n"
        f"Оплата Кардан!\nДар Хозира Замон Мо Танхо Душанбе Сити Дорем!\nБа Наздики Мо Дигар Кортхоро Дохил Мекунем!\n\nСкиньте чек после оплаты",
        reply_markup=pay_menu
    )

# ===== Кнопка "⬅️ Ба Кафо" =====
@dp.callback_query_handler(lambda c: c.data=="back")
async def back_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Барои Давом Лутфан Чизи Мехостагиатонро Интихоб Кунед!🎁", reply_markup=main_menu)

# ===== Обработка чеков и фото =====
@dp.message_handler(content_types=[types.ContentType.DOCUMENT, types.ContentType.PHOTO])
async def handle_receipt(message: types.Message):
    if message.content_type == "document":
        file_id = message.document.file_id
        await bot.send_document(ADMIN_ID, file_id)
    elif message.content_type == "photo":
        file_id = message.photo[-1].file_id
        await bot.send_photo(ADMIN_ID, file_id)

    # Сообщение пользователю с кнопкой "Чек!"
    await message.answer(
        "Спасибо за покупку! 💎\n"
        "Алмазҳо дар давоми 5-10 дақиқа ба шумо меоянд.\n"
        "Поддержка: @FF_HUSEINOV",
        reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton("Чек!", callback_data="check")
        )
    )

    # Уведомление админу с айди игрока
    info_msg = (
        f"🎉 Новый заказ!\n"
        f"Айди игрока: {message.from_user.id}\n"
        f"Отправил чек для получения алмазов."
    )
    await bot.send_message(ADMIN_ID, info_msg)

# ===== Запуск бота =====
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
