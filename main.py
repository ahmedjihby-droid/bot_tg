from email import message

from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

import sqlite3

db = sqlite3.connect("users.db", check_same_thread=False)
db.execute(
    "CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY)"
)
db.commit()

app = Client(
    "bot",
    api_id=37089826,
    api_hash="b05f9535bd4e13be68b2ebea6fc95ba2",
    bot_token="8742768817:AAFOrGUzOzFIzgEdKhr-9zGa2TqzDFSWGd4"
)

@app.on_message(filters.command("start"))
async def start(client, message):
    db.execute(
    "INSERT OR IGNORE INTO users (user_id) VALUES (?)",
    (message.from_user.id,)
)
    db.commit()
    keyboard = ReplyKeyboardMarkup(
        [
            ["مهارات الحاسوب 👨‍💻"],
            ["البرمجة الهيكلية 🧰"],
            ["هياكل البيانات 📊"],
            ["انكليزي 📑"],
            ["عربي 🌆"],
            ["النضريه الاحتسابيه 📈"],
            ["البرمه الشيئية 💻"]
        ],
        resize_keyboard=True
    )


    

    await message.reply_text(
        "اختار شتو تريد من القائمه 👇",
        reply_markup=keyboard
    )
    # LEC 1: ملف مخزّن في تلغرام
@app.on_message(
    filters.private & filters.regex(r"^مهارات الحاسوب 👨‍💻$")
)
async def file_one(client, message):
    await message.reply_text(
        "اختار شتريد من مادة مهارات الحاسوب 📚",
        reply_markup=computer_options
    )
    
computer_options = ReplyKeyboardMarkup(
    [
        ["ملازم مهارات الحاسوب 👨‍💻"],
        ["رجوع"]
    ],
    resize_keyboard=True
)

@app.on_message(filters.private & filters.regex(r"^ملازم مهارات الحاسوب 👨‍💻$"))
async def file_one(client, message):
    await message.reply_text("بعده الدكتور ما دز اصبر اخي لا تستعجل")    
    await message.reply_text(
    "/start - للرجوع للقائمه",
    reply_markup=ReplyKeyboardRemove()
)       



    # LEC 2: ملف محلي مؤقتًا
@app.on_message(filters.private & filters.regex(r"^هياكل البيانات 📊$"))
async def file_two(client, message):
    await message.reply_document(
        "BQACAgIAAyEFAATIh5ZKAAMVatJX4fNnk6UsgDUbaoSOOvLsozMAAiy3AAJJW2FKwA7X3UrPFxEeBA"
    )
    await message.reply_text(
        "/start - للرجوع للقائمه",
        reply_markup=ReplyKeyboardRemove()
    )


@app.on_message(filters.private & filters.regex(r"^النضريه الاحتسابيه 📈$"))
async def file_three(client, message):
    await message.reply_document(
        "BQACAgIAAyEFAATIh5ZKAAMMatJOfFHL9jr0lHQb3Y1DzIuuWAcAAmSrAAKlpYFKKiNtXuZ6iOEeBA"
    )
    await message.reply_text(
        "/start - للرجوع للقائمه",
        reply_markup=ReplyKeyboardRemove()
    )

@app.on_message(filters.private & filters.regex(r"^البرمجة الهيكلية 🧰$"))
async def file_four(client, message):
    await message.reply_document("BQACAgIAAyEFAATIh5ZKAAMYatn47NhJ67xGiShwuND0dbgpl2EAArOfAAKG19BKRjvPkeKYoQIeBA")
    await message.reply_document("BQACAgIAAyEFAATIh5ZKAAMbatrrixOy3Z9TRCv_I9RJhQwUOc4AAr6jAALNJNlK4vMvIq4AAXT0HgQ")
    await message.reply_document("BQACAgIAAyEFAATIh5ZKAAMZatn4-tdH1bMNZI3K4VWPObu2G_oAArKfAAKG19BKvAMkq2kKJZAeBA")
    await message.reply_document("BQACAgIAAyEFAATIh5ZKAAMUatJRsjtWIHm242PGaf9FZzoMaUsAAueIAAJIVpFJ0SZQtcDHNKIeBA")
    await message.reply_text(
        "/start - للرجوع للقائمه",
        reply_markup=ReplyKeyboardRemove()
    )

@app.on_message(filters.private & filters.regex(r"^انكليزي 📑$"))
async def file_five(client, message):
    await message.reply_document("BQACAgIAAyEFAATIh5ZKAAMWatNeelJ7LpTOMn27hwAB2sKQ5s6KAALtrgACkGaZSjcqkx5tk3QSHgQ")
    await message.reply_document("BQACAgIAAyEFAATIh5ZKAAMXatNe1k3sw5P3bkO52AsCcjQb3ZoAAuutAAKa4plKOOD65A4p5dQeBA")
    await message.reply_text(
        "/start - للرجوع للقائمه",
        reply_markup=ReplyKeyboardRemove()
    )

@app.on_message(filters.private & filters.regex(r"^عربي 🌆$"))
async def file_six(client, message):
    await message.reply_text("ولك ماداز انتضر 🤨")
    await message.reply_text(
        "/start - للرجوع للقائمه",
        reply_markup=ReplyKeyboardRemove()
    )

@app.on_message(filters.private & filters.regex(r"^البرمه الشيئية 💻$"))
async def file_seven(client, message):
    await message.reply_text("انتضر بعده ما داز لا تلح😏")
    await message.reply_text(
        "/start - للرجوع للقائمه",
        reply_markup=ReplyKeyboardRemove()
    )


@app.on_message(
    filters.private & filters.regex(r"^رجوع$")
)
async def go_back(client, message):
    await start(client, message)

ADMIN_ID = [750076455,1481425288]  # حط Telegram ID مالك

@app.on_message(filters.private & filters.command("users")) 
async def show_users(client, message): 
    if message.from_user.id not in ADMIN_ID: 
        return
    users = db.execute( 
      "SELECT user_id FROM users"
    ).fetchall()

    await message.reply_text(
    f"👥 عدد المستخدمين: {len(users)}"
)

    if users:
      ids = "\n".join(str(user[0]) for user in users)
    for i in range(0, len(ids), 3500):
        await message.reply_text(
            "🆔 قائمة المستخدمين:\n" + ids[i:i + 3500]
        ) 

codes = { 
           "1001": "درجه الامتحام 20 من 100 يعني مزفتها ",
           "1002": "درجه الامتحان 50 من 100 يعني بيها مجال ",
           "1003": "حبيبي بطل احسلك درجتك 10 من 100",
           "1004": "عاشت ايدك درجتك 90 من 100",
           "1005": "45678",
                  }
@app.on_message(filters.private & filters.text) 
async def check_code(client, message): 
    code = message.text.strip()
    if code in codes:
     await message.reply_text(codes[code])


@app.on_message(filters.channel & filters.document)
async def get_file_id(client, message):
    print("وصل ملف من القناة")
    print("File name:", message.document.file_name)
    print("File ID:", message.document.file_id)

app.run()