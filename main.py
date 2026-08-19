import telebot
import random

# ТОКЕН ОТ BOTFATHER (вставь свой)
TOKEN = "8872204223:AAHb7qcfi1HSo-PfKHR7j0mlSaa6eT-LwtQ"
bot = telebot.TeleBot(TOKEN)

# ------------------------------------------
# 1. СПИСКИ ГЕРОЕВ
# ------------------------------------------
heroes = [
    "🏹 Мия", "🪓 Бальмонд", "⚔️ Сабер", "🧙 Алиса", "🎀 Нана", "🛡️ Тигрил", "🗡️ Алукард", "🗡️ Карина", "🦊 Акай",
    "💪 Франко", "🐉 Бэйн", "🎯 Бруно", "🔫 Клинт", "✨ Рафаэль", "❄️ Эйдора", "🐉 Зилонг", "🗡️ Фанни", "🏹 Лейла",
    "🛡️ Минотавр", "🛡️ Лолита", "🗡️ Хаябуса", "⚔️ Фрейя", "🔮 Горд", "🗡️ Наталья", "🧙 Кагура", "🥊 Чу", "🦊 Сан",
    "🤖 Альфа", "🩸 Руби", "🗡️ Ли Сун-Син", "🛡️ Москов", "🚗 Джонсон", "🔮 Циклоп", "🩺 Эстес", "🔥 Хильда",
    "❄️ Аврора", "🪓 Лапу-Лапу", "🔮 Вексана", "🐺 Роджер", "🦇 Кэрри", "🐗 Гатоткача", "🔮 Харли",
    "🔥 Иритель", "🐊 Грок", "🛡️ Аргус", "💃 Одетта", "⚔️ Ланселот", "🔫 Дигги", "🗡️ Хилос", "🛡️ Заск", "🧠 Хелкарт",
    "🎭 Фаша", "🏹 Лесли", "🤖 Кусака", "👼 Ангела", "🗡️ Госсен", "⚡ Валир", "🛡️ Мартис", "🛡️ Уранус", "🕵️‍♀️ Ханаби",
    "🌙 Чан'Э", "🛡️ Кайя", "🦇 Селена", "👹 Алдос", "🗡️ Клауд", "🌪️ Вэйл", "🧛 Леоморд", "🌑 Люнокс", "🐉 Ханзо",
    "🪨 Белерик", "💃 Кимми", "🔥 Тамуз", "❄️ Харит", "👑 Минситтар", "✨ Кадита", "🧙 Фарамис", "🗡️ Баданг",
    "🪄 Хуфра", "🏹 Грейнджер", "🪄 Гвиневра", "🔥 Эсмеральда", "🗡️ Тариэла", "🤖 Икс.Борг", "🗡️ Линг",
    "🪓 Дариус", "🌿 Лилия", "🛡️ Баксий", "💪 Маша", "🦊 Ванван", "🧙 Сильвана", "🛡️ Сесилион", "🧛 Кармилла",
    "🛡️ Атлас", "👥 Пополь и Купа", "⚡ Чонг", "🌑 Ло Ии", "⚔️ Бенедетта", "🪄 Халид", "🤖 Бартс", "🗡️ Броуди",
    "🪄 Ив", "✨ Матильда", "🐂 Пакито", "🦇 Глу", "💥 Беатрис", "🛡️ Фовиус", "🗡️ Натан", "🔥 Аулус", "🛡️ Эймон",
    "🔮 Валентина", "🪄 Эдит", "👶 Флорин", "🥋 Инь", "🔫 Мелисса", "🛡️ Ксавьер", "🌪️ Джулиан", "🗡️ Фредрин",
    "🎵 Джой", "🔮 Новария", "⚔️ Арлотт", "⚡ Иксия", "🛡️ Нолан", "🎪 Чичи", "🐱 Чип", "🔮 Чжусинь", "🗡️ Су Е",
    "🔥 Лукас", "🌊 Калеа", "⚔️ Цзэтянь", "🗡️ Обсидия", "🛡️ Сора", "🗡️ Марсель", "🦋 Хирара"
]

# ------------------------------------------
# 2. СПИСКИ ПРЕДМЕТОВ
# ------------------------------------------
items = [
    "👢 Сапоги воина", "👢 Ботинки демона", "👟 Сапоги-скороходы", "👢 Сапоги спешки", 
    "👢 Сапоги Заклинателя", "👢 Магические ботинки", "👢 Прочные Сапоги",
    "🗡️ Клинок отчаяния", "🌪️ Говорящий с ветром", "🦅 Злобный рык", "🔱 Трезубец", 
    "💥 Ярость берсерка", "🧛 Меч охотника на демонов", "🪄 Золотой посох", 
    "🧬 Коса коррозии", "💀 Удар охотника", "⚔️ Бесконечная битва", "🪓 Топор войны",
    "🗡️ Клинок семи морей", "☄️ Золотой метеор", "🌪️ Ветер природы", "🐉 Копье Великого дракона", 
    "☄️ Пронзающий небеса", "🔫 Губительный пулемет", "❄️ Зимняя корона", "🐾 Когти Хааса", 
    "⏳ Мимолетное время",
    "💎 Священный кристалл", "🩸 Кровавые крылья", "⚡ Жезл молний", "🔥 Пылающий жезл", 
    "✨ Божественный меч", "🧙 Палочка гения", "🔮 Концентрированная энергия", 
    "📿 Зачарованный талисман", "❄️ Жезл снежной королевы",
    "🪶 Райское перо", "🧚 Фонарь желаний", "💧 Фляга Оазиса", "🌀 Старлиумовая коса", "⌛ Часы судьбы",
    "🛡️ Щит Афины", "🛡️ Сияющая броня", "🛡️ Наплечник наказания", "💀 Бессмертие", 
    "🪨 Кираса грубой силы", "❄️ Господство льда", "🐍 Оракул", "🏛️ Древняя кираса", 
    "🪖 Защитный шлем", "🌊 Штормовой пояс", "🔥 Проклятый шлем", "🦇 Крылья королевы", 
    "🪡 Шипованная броня"
]

# ------------------------------------------
# 3. СПИСКИ ЭМБЛЕМ И ТАЛАНТОВ
# ------------------------------------------
emblems = [
    "Обычная эмблема", "Эмблема танка", "Эмблема убийцы", 
    "Эмблема мага", "Эмблема бойца", "Эмблема поддержки", "Эмблема стрелка"
]

talents = [
    "Трепет", "Проворность", "Опытный охотник", "Благословение природы", 
    "Боевой ключ", "Квантовый заряд", "Временное правление", "Нечестивая ярость",
    "Живучесть", "Стойкость", "Ударная волна", "Разрыв", "Мастер-убийца", 
    "Убийственный пир", "Вдохновение", "Охотник за скидками", 
    "Смертельное воспламенение", "Прочность", "Кровавое пиршество", "Отвага",
    "Ловкость", "Второе дыхание", "Фокус-метка", "Фатальность", 
    "Мастер оружий", "Точно в цель"
]

# ------------------------------------------
# 4. КОМАНДА ЗАПУСКА (/пиво)
# ------------------------------------------
@bot.message_handler(commands=['пиво'])
def start(message):
    remove_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Убираю старые кнопки...", reply_markup=remove_markup)

    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton("🎲 Герой", callback_data='hero')
    btn2 = telebot.types.InlineKeyboardButton("🛠 Сборка", callback_data='build')
    btn3 = telebot.types.InlineKeyboardButton("🔥 Полный рандом", callback_data='full_random')
    btn4 = telebot.types.InlineKeyboardButton("🎖️ Рандом эмблемы", callback_data='emblems')
    btn5 = telebot.types.InlineKeyboardButton("📖 Гайд на линию", callback_data='guide_menu')
    btn6 = telebot.types.InlineKeyboardButton("🦟 Убить комара", callback_data='kill_mosquito')
    btn7 = telebot.types.InlineKeyboardButton("🎰 Депнуть мать", callback_data='deposit_mom')
    
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5, btn6)
    markup.add(btn7)
    
    bot.send_message(message.chat.id, "Привет! Выбери режим рандома:", reply_markup=markup)

# ------------------------------------------
# 5. ОБРАБОТЧИК НАЖАТИЙ КНОПОК
# ------------------------------------------
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'hero':
        hero = random.choice(heroes)
        bot.send_message(call.message.chat.id, f"⚔️ Твой случайный герой: *{hero}*", parse_mode='Markdown')
        
    elif call.data == 'build':
        selected_items = random.sample(items, 6)
        result = "🛠 Твоя безумная сборка:\n"
        for i, item in enumerate(selected_items, 1):
            result += f"{i}. {item}\n"
        bot.send_message(call.message.chat.id, result)
        
    elif call.data == 'full_random':
        hero = random.choice(heroes)
        selected_items = random.sample(items, 6)
        result = f"⚔️ Герой: *{hero}*\n\n🛠 Безумная сборка:\n"
        for i, item in enumerate(selected_items, 1):
            result += f"{i}. {item}\n"
        bot.send_message(call.message.chat.id, result)

    elif call.data == 'emblems':
        emblem = random.choice(emblems)
        random_talents = random.sample(talents, 3)
        result = f"🎖️ *Эмблема:* {emblem}\n\n🔮 *Таланты:*\n1. {random_talents[0]}\n2. {random_talents[1]}\n3. {random_talents[2]}"
        bot.send_message(call.message.chat.id, result, parse_mode='Markdown')

    elif call.data == 'guide_menu':
        markup = telebot.types.InlineKeyboardMarkup()
        btn_jungle = telebot.types.InlineKeyboardButton("🌲 Лес", callback_data='lane_jungle')
        btn_mid = telebot.types.InlineKeyboardButton("💠 Мид", callback_data='lane_mid')
        btn_gold = telebot.types.InlineKeyboardButton("💰 Голд", callback_data='lane_gold')
        btn_exp = telebot.types.InlineKeyboardButton("⚡ Эксп", callback_data='lane_exp')
        btn_roam = telebot.types.InlineKeyboardButton("👣 Роум", callback_data='lane_roam')
        markup.add(btn_jungle, btn_mid, btn_gold)
        markup.add(btn_exp, btn_roam)
        bot.send_message(call.message.chat.id, "🗺️ Выбери линию, по которой хочешь получить гайд:", reply_markup=markup)

    elif call.data == 'lane_jungle':
        bot.send_message(call.message.chat.id, "🌲 Вот видео-гайд по лесу (Джунгли):\nhttps://youtu.be/ZapDyO_eJKc?si=_CfThJycWPTIND8S")
    elif call.data == 'lane_mid':
        bot.send_message(call.message.chat.id, "💠 Вот видео-гайд по средней линии (Мид):\nhttps://youtu.be/jMexg8qyoXw?si=H2uQoP8UdgNjuUZ5")
    elif call.data == 'lane_gold':
        bot.send_message(call.message.chat.id, "💰 Вот видео-гайд по золотой линии (Голд):\nhttps://youtu.be/pJd7SDU2Y70?si=E7vkFZUMw7S-WVYG")
    elif call.data == 'lane_exp':
        bot.send_message(call.message.chat.id, "⚡ Вот видео-гайд по линии опыта (Эксп):\nhttps://youtu.be/Kp7d1e-lZAo?si=c2xuq7XiM3yvdwhM")
    elif call.data == 'lane_roam':
        bot.send_message(call.message.chat.id, "👣 Вот видео-гайд по линии поддержки (Роум):\nhttps://youtu.be/xwdRPVzHr4A?si=t3u_9XBJJxB8OXqt")

    # КОМАР
    elif call.data == 'kill_mosquito':
        bot.send_message(call.message.chat.id, "🦟💥 Вы убили комара!")

    # РУЛЕТКА КАЗИНО (ДЕПНУТЬ МАТЬ)
    elif call.data == 'deposit_mom':
        bot.send_message(call.message.chat.id, "🎰 Кручу-верчу, обмануть хочу...\n\nПоздравляю! Ты проебал мать в казик, иди нахуй! 😂")

    # Обязательная строчка для убирания "часиков" загрузки с нажатой кнопки
    bot.answer_callback_query(call.id)

# ------------------------------------------
# ЗАПУСК БОТА
# ------------------------------------------
print("Бот запущен...")
bot.polling(non_stop=True)
