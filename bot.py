from flask import Flask, request
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import logging
import os
import asyncio

# ===== Настройки =====
TOKEN = "8038703445:AAHq-7WaSpel99M6sKiXWwz7mugCsv7jw64"
ADMIN_ID = 7574702101
WEBHOOK_PATH = f"/{TOKEN}"
WEBHOOK_URL = f"https://husenov-tg-bot.onrender.com{WEBHOOK_PATH}"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# ===== Flask =====
app = Flask(__name__)

@app.route("/")
def home():
    return "Бот работает!"

# ===== Вебхук =====
@app.route(WEBHOOK_PATH, methods=["POST"])
def webhook():
    update = types.Update(**request.json)
    asyncio.run(dp.process_update(update))
    return "OK"

# ===== Кнопки =====
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(KeyboardButton("💎 Алмаз Харидан"))
main_menu.add(KeyboardButton("⚙ Настройка"))

back_menu = ReplyKeyboardMarkup(resize_keyboard=True)
back_menu.add(KeyboardButton("⬅️ Ба Кафо"))
back_menu.add(KeyboardButton("🏠 Меню"))

def get_diamond_inline():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("💎 100 — 10 🇹🇯", callback_data="100💎"),
        InlineKeyboardButton("💎 200 — 20 🇹🇯", callback_data="200💎"),
        InlineKeyboardButton("💎 300 — 30 🇹🇯", callback_data="300💎"),
        InlineKeyboardButton("💎 400 — 40 🇹🇯", callback_data="400💎"),
        InlineKeyboardButton("💎 500 — 50 🇹🇯", callback_data="500💎"),
        InlineKeyboardButton("💎 1000 — 100 🇹🇯", callback_data="1000💎"),
        InlineKeyboardButton("💎 2000 — 200 🇹🇯", callback_data="2000💎")
    )
    return kb

phone_inline = InlineKeyboardMarkup(row_width=3)
phone_inline.add(
    InlineKeyboardButton("📱 Самсунг", callback_data="phone_samsung"),
    InlineKeyboardButton("📱 Редми", callback_data="phone_redmi"),
    InlineKeyboardButton("📱 Айфон", callback_data="phone_iphone"),
    InlineKeyboardButton("📱 Хуавей", callback_data="phone_huawei"),
    InlineKeyboardButton("📱 Поко", callback_data="phone_poco"),
    InlineKeyboardButton("📱 ЗТЕ", callback_data="phone_zte")
)

buy_premium_inline = InlineKeyboardMarkup(row_width=1)
buy_premium_inline.add(
    InlineKeyboardButton("🎁 Buy The Premium 💎 Settings ⚙ 20 🇹🇯", callback_data="buy_premium"),
    InlineKeyboardButton("⬅️ Назад", callback_data="back_phone")
)

# ===== Handlers =====
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(
        "🎄 Хуш Омадед Ба Боти FF - HUSANOV! 🎄\n"
        "Барои Алмаз Харидан ё Настройка ⚙ Free Fire Лутфан Чизи Мехостагиатонро Интихоб Кунед!🎁",
        reply_markup=main_menu
    )

@dp.message_handler()
async def main_handler(message: types.Message):
    text = message.text
    if text == "💎 Алмаз Харидан":
        await message.answer("Выберите количество алмазов:", reply_markup=get_diamond_inline())
    elif text == "⚙ Настройка":
        await message.answer("Намуди ⚙ Телефонатонро 📱 Интихоб Кунед!", reply_markup=phone_inline)
    elif text == "⬅️ Ба Кафо":
        await message.answer("Барои Давом Лутфан Чизи Мехостагиатонро Интихоб Кунед!", reply_markup=main_menu)
    elif text == "🏠 Меню":
        await message.answer("Меню", reply_markup=main_menu)
    else:
        await message.answer("Выберите действие!", reply_markup=main_menu)

@dp.callback_query_handler(lambda c: c.data.startswith("phone_"))
async def phone_callback(callback_query: types.CallbackQuery):
    data = callback_query.data
    await bot.answer_callback_query(callback_query.id)

    settings_text = ""
    if data == "phone_samsung":
        settings_text = "Обзор : 178\nКолимматор : 170\n2Х Прицел : 100\n4Х Прицел : 100\nСнайперский Прицел : 60\nСвободный Обзор : 10"
        await bot.send_message(callback_query.from_user.id, settings_text, reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ Назад", callback_data="back_phone")))
        return
    elif data == "phone_redmi":
        settings_text = ("Обзор : 170\nКолимматор : 100\n2Х Прицел : 65\n4Х Прицел : 60\nСнайперский Прицел : 60\nСвободный Обзор : 100\n"
                         "У Нас Ещё Есть Премиум Настройки Которые Стоят 10 🇹🇯\nЕсли Хотите Их Преобрести Нажмите На Кнопку Внизу!")
    elif data == "phone_iphone":
        settings_text = ("Обзор : 100\nКолимматор : 0\n2Х Прицел : 100\n4Х Прицел : 100\nСнайперский Прицел : 60\nСвободный Обзор : 0\n"
                         "У Нас Ещё Есть Премиум Настройки Которые Стоят 10 🇹🇯\nЕсли Хотите Их Преобрести Нажмите На Кнопку Внизу!")
    elif data == "phone_huawei":
        settings_text = ("Обзор : 170\nКолимматор : 170\n2Х Прицел : 200\n4Х Прицел : 200\nСнайперский Прицел : 20\nСвободный Обзор : 10\n"
                         "У Нас Ещё Есть Премиум Настройки Которые Стоят 10 🇹🇯\nЕсли Хотите Их Преобрести Нажмите На Кнопку Внизу!")
    elif data == "phone_poco":
        settings_text = ("Обзор : 180\nКолимматор : 180\n2Х Прицел : 107\n4Х Прицел : 105\nСнайперский Прицел : 10\nСвободный Обзор : 200\n"
                         "У Нас Ещё Есть Премиум Настройки Которые Стоят 10 🇹🇯\nЕсли Хотите Их Преобрести Нажмите На Кнопку Внизу!")
    elif data == "phone_zte":
        settings_text = ("Обзор : 100\nКолимматор : 100\n2Х Прицел : 100\n4Х Прицел : 100\nСнайперский Прицел : 60\nСвободный Обзор : 200\n"
                         "У Нас Ещё Есть Премиум Настройки Которые Стоят 10 🇹🇯\nЕсли Хотите Их Преобрести Нажмите На Кнопку Внизу!")

    await bot.send_message(callback_query.from_user.id, settings_text, reply_markup=buy_premium_inline)

@dp.callback_query_handler(lambda c: c.data in ["buy_premium", "back_phone"])
async def buy_or_back_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    if callback_query.data == "buy_premium":
        await bot.send_message(callback_query.from_user.id, "Напишите 🖋 Модель 🧩 Своего Телефона! 📱\nИ Скиньте Чек 🧾 После Оплаты 📪")
    elif callback_query.data == "back_phone":
        await bot.send_message(callback_query.from_user.id, "Намуди ⚙ Телефонатонро 📱 Интихоб Кунед!", reply_markup=phone_inline)

@dp.message_handler(content_types=[types.ContentType.DOCUMENT, types.ContentType.PHOTO])
async def handle_receipt(message: types.Message):
    if message.content_type == "document":
        file_id = message.document.file_id
        await bot.send_document(ADMIN_ID, file_id)
    elif message.content_type == "photo":
        file_id = message.photo[-1].file_id
        await bot.send_photo(ADMIN_ID, file_id)

    await message.answer(
        "Спасибо За Выбор 🗳 Наших Настроек! ⚙\n"
        "Скоро С Вами Свяжется 🔗 Наш Администратор! 👨‍✈️"
    )
    info_msg = (
        f"У Вас Заказ 🌆 Настроек! ⚙\n"
        f"Покупатель 🛒: @{message.from_user.username if message.from_user.username else message.from_user.id}"
    )
    await bot.send_message(ADMIN_ID, info_msg)

# ===== Установка вебхука при первом запросе =====
@app.before_first_request
def set_webhook():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.set_webhook(WEBHOOK_URL))

# ===== Запуск Flask =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
