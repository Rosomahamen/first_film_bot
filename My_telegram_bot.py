from telegram.ext import Application, MessageHandler, filters, CommandHandler

a = {
    "Форсаж":["2001","Боєвик","Роб_Коен","США","100_грн"],
    "Втеча з Шоушенка":["1994","Драма","Френк_Дарабонт","США","90_грн"],
    "Форрест Гамп":["1994","Драма","Роберт_Земекис","США","70_грн"],
    "1+1":["2011","Драма","Олів'є_Накаш","Франція","80_грн"],
    "Назад в майбутнє":["1985","Пригоди","Роберт_Земекис","США","90_грн"],
    "Матриця":["1999","Фантастика","Лана_Вачовскі","США","60_грн"],
    "Бійцівський клуб":["1999","Драма","Девід_Фінчер","США", "100_грн"],
    "Час":["2011","Фантастика","Ендрю_Ніккол","США","70_грн"],
    "Тіні забутих предків":["1964","Драма","Сергій_Паранджанов","Україна","60_грн"],
    "Вежа":["2022","Тріллер","Скотт_Манн","Великобританія","90_грн"]

}


async def start_and_help(update, context):
    string_in = update.message.text
    if string_in == "/start":
        string_out = "Привіт! Це фільм-бот. Напиши /help для детальній інформації."
    elif string_in == '/help':
        string_out = 'Доступні команди /start, /help, /catalog, /search, /add'
    await update.message.reply_text(string_out)


async def catalog(update, context):
    global a
    result = ""
    string_in = update.message.text
    if string_in == "/search":
        string_out = "Для пошуку використовуй ці команди: /name , /year , /janre , /director , /country , /price"
    elif string_in == "/catalog":
        for key, value in a.items():
            result += f"{key}: {', '.join(value)}\n"
        string_out = result
    await update.message.reply_text(string_out)




async def name(update, context):
    global a
    string_in = update.message.text
    if string_in == "/name":
        string_out = "напишіть команду і через двокрапку та пробіл назву(/name : назва)"
        await update.message.reply_text(string_out)
    else:
        c = string_in.split(' : ')
        if c[1] in a:  
            string_out = f"{c[1]}: {', '.join(a.get(c[1]))}"
        else:
            string_out = None
    await update.message.reply_text(string_out)


async def year(update, context):
    global a
    string_in = update.message.text
    if string_in == "/year":
        string_out = "напишіть команду і через пробіл рік"
        await update.message.reply_text(string_out)
    else:
        c = string_in.split(' ')
        b = c[1]
        matching_movies = [] 
        for key, value in a.items():
            if value[0] == b:
                l = []
                l.append(key)
                l.append(", ".join(value))
                matching_movies.append(": ".join(l))
        if matching_movies:
            string_out = "\n".join(matching_movies)
        else:
            string_out = "Фільм не знайдено"
        await update.message.reply_text(string_out)


async def janre(update, context):
    global a
    string_in = update.message.text
    if string_in == "/janre":
        string_out = "напишіть команду і через пробіл рік"
        await update.message.reply_text(string_out)
    else:
        c = string_in.split(' ')
        b = c[1]
        matching_movies = [] 
        for key, value in a.items():
            if value[1] == b:
                l = []
                l.append(key)
                l.append(", ".join(value))
                matching_movies.append(": ".join(l))
        if matching_movies:
            string_out = "\n".join(matching_movies)
        else:
            string_out = "Фільм не знайдено"
        await update.message.reply_text(string_out)


async def director(update, context):
    global a
    string_in = update.message.text
    if string_in == "/director":
        string_out = "напишіть команду і через пробіл режисера типу так: Роб_Коен"
        await update.message.reply_text(string_out)
    else:
        c = string_in.split(' ')
        b = c[1]
        m = [] 
        for key, value in a.items():
            if value[2] == b:
                l = []
                l.append(key)
                l.append(", ".join(value))
                m.append(": ".join(l))
        if m:
                string_out = "\n".join(m)
        else:
            string_out = "Фільм не знайдено"
        await update.message.reply_text(string_out)



async def country(update, context):
    global a
    string_in = update.message.text
    if string_in == "/country":
        string_out = "напишіть команду і через пробіл країну"
        await update.message.reply_text(string_out)
    else:
        c = string_in.split(' ')
        b = c[1]
        m = [] 
        for key, value in a.items():
            if value[3] == b:
                l = []
                l.append(key)
                l.append(", ".join(value))
                m.append(": ".join(l))
        if m:
                string_out = "\n".join(m)
        else:
            string_out = "Фільм не знайдено"
        await update.message.reply_text(string_out)


async def price(update, context):
    global a
    string_in = update.message.text
    if string_in == "/price":
        string_out = "напишіть команду і через пробіл ціну типу так: 100_грн"
        await update.message.reply_text(string_out)
    else:
        c = string_in.split(' ')
        b = c[1]
        m = [] 
        for key, value in a.items():
            if value[4] == b:
                l = []
                l.append(key)
                l.append(", ".join(value))
                m.append(": ".join(l))
        if m:
                string_out = "\n".join(m)
        else:
            string_out = "Фільм не знайдено"
        await update.message.reply_text(string_out)




async def add(update, context):
    global a
    string_in = update.message.text
    if string_in == "/add":
        string_out = "Фільм потрібно добавляти так: /add : Назва фільму : рік, жанр, режисер(Так:Роб_Коен), країна, ціна(Так:100_грн)"
        await update.message.reply_text(string_out)
    else:   
        c = string_in.split(' : ')
        c[2].strip()
        n = c[2].split(', ')
        if  len(n) == 5 :
            a[c[1]] = n
            string_out = "Фільм успішно добавлено"
        else:
            string_out = "Не правильно добавлено"
        await update.message.reply_text(string_out)




application = Application.builder().token("6059473394:AAEU5UtzdJWzwYa6Xb3_jgll1BvcXkj9BdQ").build()


application.add_handler(CommandHandler("search",catalog))
application.add_handler(CommandHandler("name", name))
application.add_handler(CommandHandler("year", year))
application.add_handler(CommandHandler("janre", janre))
application.add_handler(CommandHandler("director", director))
application.add_handler(CommandHandler("country", country))
application.add_handler(CommandHandler("price", price))
application.add_handler(CommandHandler("add", add))
application.add_handler(CommandHandler("catalog", catalog))





application.add_handler(MessageHandler(filters.TEXT, start_and_help))
