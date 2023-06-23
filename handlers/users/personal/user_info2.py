from aiogram.dispatcher.filters import Text
from aiogram import types

from keyboards.default.menyu import Ovqatlar, shashlik, Menyu, Ichimliklar
from loader import dp


@dp.message_handler(Text(equals="🍽Ovqatlar"))
async def ovqatlar (message: types.Message):
    await message.answer(text="<b>Qanaqa ovqatlar tanlaysiz</b>",
                         reply_markup=Ovqatlar())

@dp.message_handler(Text(equals="🍗Tovuq"))
async def tovuq(message:types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFsnQd54mHYQ3KhLs27OZ8XivUwplaeA_irA&usqp=CAU",
                               caption="<b>Bu Tovuq \nNarxi: bepul</b>")


@dp.message_handler(Text(equals="🍖Quy jiz"))
async def quy_jiz (message: types.Message):
    await message.answer_photo(photo="https://dostavo4ka.uz/upload-file/2022/11/02/6301/750x750-bc5ba3c9-67f4-49e9-8bea-40d8b0624259.jpg",
                               caption="<b>Bu Quy Jiz\nNarxi: bepul</b>")


@dp.message_handler(Text(equals="🥩Qizilch"))
async def qizilch (message: types.Message):
    await message.answer_photo(photo="https://i.ytimg.com/vi/Vn5DtRHwZ3U/maxresdefault.jpg",
                               caption="<b>Bu qizilcha\nNarxi: bepul</b>")

@dp.message_handler(Text(equals="🍟Kartoshka fri"))
async def kartoshka_fri (message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTpLJs6v3tP1hEvqSDaj2smxNgaKlzEUsfkw&usqp=CAU",
                               caption="<b>Bu kartoshka fri\nNarxi: bepul</b>")

#
# @dp.message_handler(Text(equals="🛒Savatga s.Message):
#     await message.answer(text="<b>Yana nima ovqatlar qushmoqchisiz</b>",
#                          reply_markup=Ovqatlar())

@dp.message_handler(Text(equals="⏮ Bekor qilish"))
async def bekorqilish_ovqat (message: types.Message):
    await message.answer(text="<b>Bekor qilndi</b>",
                         reply_markup=Ovqatlar())

# @dp.message_handler(Text(equals="🗑Savatga s.Message):
#     await message.answer(text="<b>Yana nima piva savatga qushmoqchisiz</b>",
#                          reply_markup=piva())


@dp.message_handler(Text(equals="🌏Choyhona manzili"))
async def loc(message: types.Message):
    await message.answer_location(latitude=38.8080867, longitude=65.7851736)

@dp.message_handler(Text(equals="⏮ Back to menu"))
async def Back (message: types.Message):
    await message.answer(text="<b>Tanlang</b>",
                         reply_markup=Menyu())

@dp.message_handler(Text(equals="⏮ Back to ichimlik menu"))
async def Back (message: types.Message):
    await message.answer(text="<b>Tanlang</b>",
                         reply_markup=Ichimliklar())





@dp.message_handler(Text(equals="⏮ Back to menyu"))
async def Back (message: types.Message):
    await message.answer(text="<b>Tanlang</b>",
                         reply_markup=Menyu())

#
# @dp.message_handler(Text(equals="🗑Savatga s.Message):
#     await message.answer(text="<b>Yana nima piva savatga qushmoqchisiz</b>",
#                          reply_markup=piva())

# @dp.message_handler(Text(equals="🗑 Savatga : types.Message):
#     await message.answer(text="<b>Yana pepsi savatga qushmoqchimisiz</b>",
#                          reply_markup=Pepsi())
#
#
#
# @dp.message_handler(Text(equals="🛒 Savatga  types.Message):
#     await message.answer(text="<b>Yana cola savatga qushmoqchimisiz</b>",
#                          reply_markup=Cola())




# @dp.message_handler(Text(equals="🛒 Savatga-: types.Message):
#     await message.answer(text="<b>Yana fanta savatga qushmoqchimisiz</b>",
#                          reply_markup=Fanta())

@dp.message_handler(Text(equals="🍡Shashliklar"))
async def shashliklar(message: types.Message):
    await message.answer(text="<b>Qanaqa shashliklar tanlaysiz</b>",
                        reply_markup=shashlik())

# @dp.message_handler(Text(equals="🗑 Savatga-: types.Message):
#     await message.answer(text="<b>Yana Shashlik savatga qushmoqchimisiz</b>",
#                          reply_markup=shashlik())

@dp.message_handler(Text(equals="🍢 Tovuq Shashlik"))
async def tovuq_shashlik (message:types.Message):
    await message.answer_photo(photo="https://bazarplus.uz/wp-content/uploads/2023/01/tovuq-kichik.jpg",
                               caption="<b>Bu Tovuq Shashlik\nNarxi: bepul</b>")


@dp.message_handler(Text(equals="🍢 Kuskavoy Shashlik"))
async def Kuskavoy_shashlik (message: types.Message):
    await message.answer_photo(photo="https://img.povar.ru/mobile/4a/47/f6/fc/uzbekskii_shashlik-77241.jpg",
                               caption="<b>Bu Kuskavoy Shashlik\nNarhi: bepul</b>")

@dp.message_handler(Text(equals="🍢 G'ijduvon Shashlik"))
async def gijduvon_shashlik (message: types.Message):
    await message.answer_photo(photo="https://i.ytimg.com/vi/fAnr4ThhC1Q/mqdefault.jpg",
                               caption="<b>Bu G'ijduvon Shashlik\nNarhi: bepul</b>")

@dp.message_handler(Text(equals="🍢 Kavkaz Shashlik"))
async def kavkaz_shashlik (message: types.Message):
    await message.answer_photo(photo="https://live24.ru/wp-content/themes/yootheme/cache/d5/1593408320_annotacija-2020-06-29-082348-d590e1f3.png",
                               caption="<b>Bu Kavkaz Shashlik\nNarhi: bepul</b>")

@dp.message_handler(Text(equals="🍢 Katta G'jduvon Shashlik"))
async def katta_gijduvon_shashlik (message: types.Message):
    await message.answer_photo(photo="https://www.koolinar.ru/all_image/recipes/91/91160/recipe_5d8b972a-8cee-4f54-bf5a-966a4be03b4c_w450.jpg",
                               caption="<b>Bu Katta G'ijduvon Shashlik\nNarhi: bepul</b>")



@dp.message_handler(Text(equals="🔚 Bekor qilish"))
async def bekor_qilish_shashlik (message: types.Message):
    await message.answer(text="<b>Bekor qlindi</b>",
                         reply_markup=shashlik())
