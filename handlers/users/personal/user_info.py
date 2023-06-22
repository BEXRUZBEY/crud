from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.default.menyu import Menyu, user_rkm, Ichimliklar, Pepsi, zakaz_ber_pepsi, Cola, zakaz_ber_cola, Fanta, \
    zakaz_ber_fanta, piva, zakaz_ber_piva, Razlivnoy, butulishni, Banishni
from loader import dp

@dp.message_handler(Text(equals="⏮ Back to menyu"))
async def Back (message: types.Message):
    await message.answer(text="<b>Tanlang</b>",
                         reply_markup=Menyu())

@dp.message_handler(Text(equals="📃Menu"))
async def get_info(message: types.Message):
    await message.answer(text="<b>Qaysi Amalni tanlaysiz</b>",
                         reply_markup=Menyu())


@dp.message_handler(Text(equals="☎Kontakt"))
async def kontaktlar (message: types.Message):
    await message.answer(text="<b>Shu Choyhonani egasi\nIsm: Azamat\nFamilya: Achilov\nTelefon raqam: 914607845</b>")

@dp.message_handler(Text(equals="⏮ Back to home"))
async def Back (message: types.Message):
    await message.answer(text="<b>Tanlang</b>",
                         reply_markup=user_rkm())

@dp.message_handler(Text(equals="🥂Ichimliklar"))
async def ichimlik (message: types.Message):
    await message.answer(text="<b>Qaysi bulimni tanlaysiz</b>",
                         reply_markup=Ichimliklar())


@dp.message_handler(Text(equals="🍹Pepsi"))
async def pepsi (message: types.Message):
    await message.answer(text="<b>Qaysi bulimni tanlaysiz</b>",
                         reply_markup=Pepsi())

@dp.message_handler(Text(equals="0️⃣5️⃣ litr"))
async def pepsi_litr_05 (message: types.Message):
        await message.answer_photo(photo="https://market.vseokoree.com/images/product/1577065376pepsi500.png")
        await message.answer_photo(photo="https://devel.prom.uz/upload/products/60/98/60988e6c799e5067b5232a3b98fe6397.jpg",
                                   caption="<b>Bu 0.5 litr pepsi\nNarhi: bepul</b>",
                                   reply_markup=zakaz_ber_pepsi())
@dp.message_handler(Text(equals="1️⃣ litr"))
async def pepsi_litr_1 (message: types.Message):
        await message.answer_photo(photo="https://babymarket.uz/wp-content/uploads/2020/05/pepsi-cola-1-l.jpg")
        await message.answer_photo(photo="https://cdn.yaponamama.uz/products/102_1626715995.png",
                                   caption="<b>Bu 1 litr pepsi\nNarhi: bepul</b>",
                                   reply_markup=zakaz_ber_pepsi())
@dp.message_handler(Text(equals="1️⃣.5️⃣ litr"))
async def pepsi_litr_1_5 (message: types.Message):
        await message.answer_photo(photo="https://babymarket.uz/wp-content/uploads/2020/05/pepsi-cola-15-l.jpg")
        await message.answer_photo(photo="https://web.lebazar.uz/resources/product/2023/4/18/medium_1684384583907101020102-00179.png",
                                   caption="<b>Bu 1.5 litr pepsi\nNarhi: bepul</b>",
                                    reply_markup=zakaz_ber_pepsi())
@dp.message_handler(Text(equals="2️⃣ litr"))
async def pepsi_litr_2 (message: types.Message):
        await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwwsk7Fg6vrYpPajmLYZtDUth7JN8aWbsvIA&usqp=CAU")
        await message.answer_photo(photo="https://jarpirogi.ru/wp-content/uploads/2019/05/12.jpg",
                                   caption="<b>Bu 2 litr pepsi\nNarhi: bepul</b>",
                                   reply_markup=zakaz_ber_pepsi())

@dp.message_handler(Text(equals="◀ Bekor qilish"))
async def bekor_qilish_pesi (message: types.Message):
    await message.answer(text="<b>Bekor qilindi</b>",
                         reply_markup=Pepsi())

@dp.message_handler(Text(equals="🍹Cola"))
async def cola (message: types.Message):
    await message.answer(text="<b>Qaysi bulimni tanlaysiz</b>",
                         reply_markup=Cola())

@dp.message_handler(Text(equals="1 litr"))
async def cola_litr_1 (message: types.Message):
    await message.answer_photo(photo="https://www.pngitem.com/pimgs/m/112-1122426_cocacola-png-free-download-tin-coca-cola-transparent.png")
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcQiHnFKNb3Bqu8AGG6ABks698vp4zQkd6wQ&usqp=CAU",
                               caption="<b>Bu 1 litr coca cola\nNarxi: bepul</b>",
                               reply_markup=zakaz_ber_cola())

@dp.message_handler(Text(equals="1.5 litr"))
async def cola_litr_1_5 (message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrS5mxWzc9soKtv3QFTpRpAJtALycX_vva7w&usqp=CAU")
    await message.answer_photo(photo="https://niholjoja.uz/wa-data/public/shop/products/59/00/59/images/73/73.970.png",
                               caption="<b>Bu 1.5 litr coca cola\nNarxi: bepul</b>",
                               reply_markup=zakaz_ber_cola())

@dp.message_handler(Text(equals="2 litr"))
async def cola_litr_2 (message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRApvya4wK7PVtB2rcqytMFV-j6M1NBIIXX6w&usqp=CAU")
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSsPzPKTqC6Lk5PGLyzQC5e1isktRPBleXKA&usqp=CAU",
                               caption="<b>Bu 2 litr coca cola\nNarxi: bepul</b>",
                               reply_markup=zakaz_ber_cola())

@dp.message_handler(Text(equals="⏪ Bekor qilish"))
async def bekor_qilish_cola (message: types.Message):
    await message.answer(text="<b>Bekor qilindi</b>",
                         reply_markup=Cola())


@dp.message_handler(Text(equals="🍹Fanta"))
async def fanta (message: types.Message):
    await message.answer(text="<b>Qaysi bulimni tanlaysiz</b>",
                         reply_markup=Fanta())


@dp.message_handler(Text(equals="1litr"))
async def fanta_litr_1 (message: types.Message):
    await message.answer_photo(photo="https://arbuz.kz/image/s3/arbuz-kz-products/20801-napitok_fanta_1_l.jpg?w=1100&h=1100&_c=1684214221")
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnKfj5g5blEwV_oNRqiEPoRGGHvMyjudD-ow&usqp=CAU",
                               caption="<b>Bu 1 litr Fanta\nNarxi: bepul</b>",
                               reply_markup=zakaz_ber_fanta())


@dp.message_handler(Text(equals="1.5litr"))
async def fanta_litr_1_5 (message: types.Message):
    await message.answer_photo(photo="https://turnerprice.gumlet.io/media/catalog/product/cache/266be06552e40de495ca8a0ecf632bea/5/d/5d08e420b87e97e6f3c4258ca85987de.jpg")
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwYHlmvIoGaPlq-M7QDzhaw_Tv3-Bbxi2amw&usqp=CAU",
                               caption="<b>Bu 1.5 litr Fanta\nNarxi: bepul</b>",
                               reply_markup=zakaz_ber_fanta())

@dp.message_handler(Text(equals="⬅ Bekor qilish"))
async def bekor_qilish_fanta (message: types.Message):
    await message.answer(text="<b>Bekor qilindi</b>",
                         reply_markup=Fanta())

@dp.message_handler(Text(equals="🔙 Bekor qilish"))
async def bekor_qilish_piva (message: types.Message):
    await message.answer(text="<b>Bekor qilindi</b>",
                         reply_markup=piva())


@dp.message_handler(Text(equals="🍺Piva"))
async def piva_menyu (message: types.Message):
    await message.answer(text="<b>Qaysi bulimni tanlaysiz</b>",
                         reply_markup=piva())

@dp.message_handler(Text(equals="🍺Razlivnoy"))
async def piva_razlivnoy (message: types.Message):
    await message.answer(text="<b>Qaysi amalni tanlaysiz</b>",
                         reply_markup=Razlivnoy())


@dp.message_handler(Text(equals="Filtr"))
async def filtr(message: types.Message):
    await message.answer_photo(photo="https://foni.club/uploads/posts/2023-02/1675565238_foni-club-p-fon-pivo-krasivii-6.jpg")
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0FjMULufzoDm3rJJG4MH1qZneWfmOZKh-eg&usqp=CAU",
                               caption="<b>Bu piva razlivnoy filtri\nNarxi: bepul</b>",
                               reply_markup=zakaz_ber_piva())


@dp.message_handler(Text(equals="Bezfiltr"))
async def bezfiltr (message:types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_PYgPyO-gufGNSoCwZCglyzXCCNxqH9wPWQ&usqp=CAU")
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCOtMR1N9ttCodd9QQFQS86uYtBZCOU3eULQ&usqp=CAU",
                               caption="<b>Bu piva razlivnoy bezfiltr\nNarxi: bepul</b>",
                               reply_markup=zakaz_ber_piva())


@dp.message_handler(Text(equals="🍻Banishniy"))
async def banishni (message: types.Message):
    await message.answer(text="Qaysi bulimbi tanlaysiz",
                         reply_markup=Banishni())

@dp.message_handler(Text(equals="🍾Qibray"))
async def qibray (message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTN6wmOj849hfRGUbWylaRjqaasplLRtkqsOw&usqp=CAU",
                               caption="<b>Bu qibray banishni\nNarxi: bepul</b>",
                               reply_markup=zakaz_ber_piva())

@dp.message_handler(Text(equals="🍺Tuborg"))
async def Tuborg (message: types.Message):
    await message.answer_photo(photo="https://alcomarket.md/media/images/items/0006/th2/items-5793-1000.png",
                               caption="<b>Bu tuborg banishni\nNarxi: bepul</b>",
                               reply_markup=zakaz_ber_piva())


@dp.message_handler(Text(equals="🍾Butulishni"))
async def butilishnik (message: types.Message):
    await message.answer(text="<b>Qaysi amailni tanlaysiz</b>",
                         reply_markup=butulishni())


@dp.message_handler(Text(equals="🍻Tuborg"))
async def tuborg (message: types.Message):
    await message.answer_photo(photo="https://content1.rozetka.com.ua/goods/images/big/269756806.jpg",
                               caption="<b>Bu butulishni tuborg\nNarxi: bepul</b>",
                               reply_markup=zakaz_ber_piva())





@dp.message_handler(Text(equals="⏮ Back to piva menu"))
async def Back (message: types.Message):
    await message.answer(text="<b>Tanlang</b>",
                         reply_markup=piva())





@dp.message_handler(Text(equals="Back to menu"))
async def Back (message: types.Message):
    await message.answer(text="<b>Tanlang</b>",
                         reply_markup=Menyu())