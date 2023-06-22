from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def user_rkm():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="📃Menu")
    button2 = KeyboardButton(text="☎Kontakt")
    button3 = KeyboardButton(text="🌏Choyhona manzili")
    rkm.add(button, button2, button3)
    return rkm



def Menyu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="🥂Ichimliklar")
    button2 = KeyboardButton(text="🍡Shashliklar")
    button3 = KeyboardButton(text="🍽Ovqatlar")
    button4 = KeyboardButton(text="⏮ Back to home")
    rkm.add(button, button2, button3, button4)
    return rkm

def Ovqatlar():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="🍗Tovuq")
    button2 = KeyboardButton(text="🍖Quy jiz")
    button3 = KeyboardButton(text="🥩Qizilch")
    button4 = KeyboardButton(text="🍟Kartoshka fri")
    button5 = KeyboardButton(text="⏮ Back to menu")
    rkm.add(button, button2, button3, button4, button5)
    return rkm

def Ichimliklar():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="🍹Pepsi")
    button2 = KeyboardButton(text="🍹Cola")
    button3 = KeyboardButton(text="🍹Fanta")
    button4 = KeyboardButton(text="🍺Piva")
    button5 = KeyboardButton(text="⏮ Back to menyu")
    rkm.add(button, button2, button3, button4, button5)
    return rkm



def Pepsi():
    ikm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="0️⃣5️⃣ litr")
    button2 = KeyboardButton(text="1️⃣ litr")
    button3 = KeyboardButton(text="1️⃣.5️⃣ litr")
    button4 = KeyboardButton(text="2️⃣ litr")
    button5 = KeyboardButton(text="⏮ Back to ichimlik menu")
    ikm.add(button, button2, button3, button4, button5)
    return ikm


def Cola():
    ikm = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton(text="1 litr")
    button2 = KeyboardButton(text="1.5 litr")
    button3 = KeyboardButton(text="2 litr")
    button4 = KeyboardButton(text="⏮ Back to ichimlik menu")
    ikm.add(button1, button2, button3, button4)
    return ikm


def Fanta():
    ikm = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton(text="1litr")
    button2 = KeyboardButton(text="1.5litr")
    button3 = KeyboardButton(text="⏮ Back to ichimlik menu")
    ikm.add(button1, button2, button3)
    return ikm


def piva():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="🍺Razlivnoy")
    button2 = KeyboardButton(text="🍻Banishniy")
    button3 = KeyboardButton(text="🍾Butulishni")
    button4 = KeyboardButton(text="⏮ Back to menyu")
    rkm.add(button, button2, button3, button4)
    return rkm


def Razlivnoy():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="Filtr")
    button2 = KeyboardButton(text="Bezfiltr")
    button3 = KeyboardButton(text="⏮ Back to piva menu")
    rkm.add(button, button2, button3)
    return rkm

def Banishni():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="🍾Qibray")
    button2 = KeyboardButton(text="🍺Tuborg")
    button3 = KeyboardButton(text="⏮ Back to piva menu")
    rkm.add(button, button2, button3)
    return rkm

def butulishni():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="🍻Tuborg")
    button2 = KeyboardButton(text="⏮ Back to piva menu")
    rkm.add(button, button2)
    return rkm

def shashlik():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="🍢 Tovuq Shashlik")
    button2 = KeyboardButton(text="🍢 Kuskavoy Shashlik")
    button3 = KeyboardButton(text="🍢 G'ijduvon Shashlik")
    button4 = KeyboardButton(text="🍢 Kavkaz Shashlik")
    button5 = KeyboardButton(text="🍢 Katta G'jduvon Shashlik")
    button6 = KeyboardButton(text="⏮ Back to menyu")
    rkm.add(button, button2, button3, button4, button5, button6)
    return rkm


def zakaz_ber_ovqatlar():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="🛒Savatga qushish")
    button2 = KeyboardButton(text="⏮ Bekor qilish")
    rkm.add(button, button2)
    return rkm



def zakaz_ber_piva():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="🗑Savatga qushish")
    button2 = KeyboardButton(text="🔙 Bekor qilish")
    rkm.add(button, button2)
    return rkm

def zakaz_ber_pepsi():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="🗑 Savatga qushish")
    button2 = KeyboardButton(text="◀ Bekor qilish")
    rkm.add(button, button2)
    return rkm

def zakaz_ber_cola():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="🛒 Savatga qushish")
    button2 = KeyboardButton(text="⏪ Bekor qilish")
    rkm.add(button, button2)
    return rkm

def zakaz_ber_fanta():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="🛒 Savatga-qushish")
    buttton2 = KeyboardButton(text="⬅ Bekor qilish")
    rkm.add(button, buttton2)
    return rkm

def zakaz_ber_shashlik():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="🗑 Savatga-qushish")
    button2 = KeyboardButton(text="🔚 Bekor qilish")
    rkm.add(button, button2)
    return rkm
