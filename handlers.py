from aiogram import Router, F
from states import SendMessage
from buttons import Inline, Reply
from config import PHOTO_URL, ADMIN_ID
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, LinkPreviewOptions

r = Router()

#COMMAND START
@r.message(CommandStart())
async def cmd_start(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer(text="Assalomu alaykum botga hush kelibsiz😇", reply_markup=Reply.main_menu())

@r.message(F.text == "◀️ Orqaga")
async def main_menu(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("🏠 Asosiy menyudasiz", reply_markup=Reply.main_menu())

# HOSPITALS MENU
@r.message(F.text == "🏥 Tibbiyot muassasalari manzillari")
async def hospitals_menu(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer(text=(
            "1. Andijon viloyat ko'p tarmoqli tibbiyot markazi\n"
            "2. Respublika ixtisoslashtirilgan onkologiya va radiologiya ilmiy-amaliy tibbiyot markazi Andijon filiali\n"
            "3. Respublika ixtisoslashtirilgan dermatovenerologiya va kosmetologiya ilmiy-amaliy tibbiyot markazi Andijon viloyat hududiy filiali\n"
            "4. Andijon viloyat ftiziatriya va pulmonologiya markazi\n"
            "5. Respublika ixtisoslashtirilgan endokrinologiya ilmiy-amaliy tibbiyot markazi Andijon filiali\n"
            "6. Respublika ixtisoslashtirilgan ona va bola salomatligi ilmiy amaliy tibbiet markazi davlat muassasasining Andijon viloyati filiali\n"
            "7. Andijon viloyat OITSga qarshi kurash markazi\n"
            "8. Andijon viloyat ko‘p tarmoqli tibbiyot markazi\n"
            "9. Andijon viloyat yuqumli kasalliklar shifoxonasi\n"
            "10. Andijon viloyat oftalmologiya shifoxonasi"
        ), reply_markup=Inline.hospitals_menu(page=1))

@r.callback_query(F.data.startswith("page_"))
async def pages_menu(call: CallbackQuery, state: FSMContext):
    await state.clear()
    if call.data == "page_1":
        await call.message.edit_text(text=(
            "1. Andijon viloyat ko‘p tarmoqli tibbiyot markazi\n"
            "2. Respublika ixtisoslashtirilgan onkologiya va radiologiya ilmiy-amaliy tibbiyot markazi Andijon filiali\n"
            "3. Respublika ixtisoslashtirilgan dermatovenerologiya va kosmetologiya ilmiy-amaliy tibbiyot markazi Andijon viloyat hududiy filiali\n"
            "4. Andijon viloyat ftiziatriya va pulmonologiya markazi\n"
            "5. Respublika ixtisoslashtirilgan endokrinologiya ilmiy-amaliy tibbiyot markazi Andijon filiali\n"
            "6. Respublika ixtisoslashtirilgan ona va bola salomatligi ilmiy amaliy tibbiet markazi davlat muassasasining Andijon viloyati filiali\n"
            "7. Andijon viloyat OITSga qarshi kurash markazi\n"
            "8. Andijon viloyat ko‘p tarmoqli tibbiyot markazi\n"
            "9. Andijon viloyat yuqumli kasalliklar shifoxonasi\n"
            "10. Andijon viloyat oftalmologiya shifoxonasi\n"
        ), reply_markup=Inline.hospitals_menu(page=1))
    elif call.data == "page_2":
        await call.message.edit_text(text=(
            "11. Andijon viloyat bolalar ko‘p tarmoqli tibbiyot markazi\n"
            "12. Andijon viloyat psixonevrologiya dispanseri\n"
            "13. Viloyat ftiziatriya klinik shifoxonasi\n"
            "14. Viloyat ftiziatriya sanatoriysi\n"
            "15. RShTYoIM AF\n"
            "16. Viloyat qon quyish stansiyasi\n"
            "17. Andijon viloyat bolalar stomatologiya poliklinikasi\n"
            "18. Respublika sud tibbiy ekspertiza ilmiy amaliy markazi Andijon filiali\n"
            "19. Andijon viloyat bolalar sil kasaliklari sanatoriysi\n"
            "20. Andijon viloyat patologik anatomiya byurosi\n"
        ), reply_markup=Inline.hospitals_menu(page=2))
    elif call.data == "page_3":
        await call.message.edit_text(text=(
            "21. Respublika ixtisoslashtirilgan kardiologiya ilmiy-amaliy tibbiyot markazi Andijon filiali\n"
            "22. Respublika tez tibbiy yordam markazi Andijon viloyati filiali\n"
            "23. Respublika ixtisoslashtirilgan narkologiya ilmiy-amaliy tibbiyot markazi Andijon viloyat mintaqaviy filiali\n"
            "24. Xo‘jalik xisobidagi travmatologiya va ortopediya shifoxonasi\n"
            "25. Andijon shahar tibbiyot birlashmasi\n"
            "26. Qorasuv shaxar tibbiyot birlashmasi\n"
            "27. Qorasuv shaxar tibbiyot birlashmasi\n"
            "28. Andijon tuman tibbiyot birlashmasi\n"
            "29. Asaka tuman tibbiyot birlashmasi\n"
            "30. Oltinko‘l tumani tibbiyot birlashmasi\n"
        ), reply_markup=Inline.hospitals_menu(page=3))
    elif call.data == "page_4":
        await call.message.edit_text(text=(
            "31. Baliqchi tumani tibbiyot birlashmasi\n"
            "32. Bo‘ston tuman tibbiyot birlashmasi\n"
            "33. Jalaquduq tuman tibbiyot birlashmasi\n"
            "34. Izboskan tumani tibbiyot birlashmasi\n"
            "35. Marhamat tumani tibbiyot birlashmasi\n"
            "36. Ulug‘nor tuman tibbiet birlashmasi\n"
            "37. Paxtaobod tuman tibbiyot birlashmasi\n"
            "38. Xo‘jaobod tuman tibbiyot birlashmasi\n"
            "39. Qo‘rg‘ontepa tuman tibbiyot birlashmasi\n"
            "40. Shaxrixon tuman tibbiyot birlashmasi\n"
        ), reply_markup=Inline.hospitals_menu(page=4))
    else:
        await call.answer(text="🤷‍♂️ Boshqa ma'lumot topilmadi", show_alert=True)


@r.callback_query(F.data.startswith("hospital_"))
async def hospital_locations_menu(call: CallbackQuery, state: FSMContext):
    await state.clear()
    if call.data == "hospital_1":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_2":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_3":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_4":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_5":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_6":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_7":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_8":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_9":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_10":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_11":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_12":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_13":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_14":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_15":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_16":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_17":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_18":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_19":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_20":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_21":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_22":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_23":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_24":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_25":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_26":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_27":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_28":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_29":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_30":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_31":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_32":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_33":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_34":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_35":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())


    elif call.data == "hospital_36":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_37":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_38":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_39":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())

    elif call.data == "hospital_40":
        await call.message.delete()
        latitude = 40.8108144105591
        longitude = 72.32388551151026
        await call.message.answer_location(latitude=latitude, longitude=longitude, reply_markup=Reply.main_menu())


# CONTACT MENU
@r.message(F.text == "📞 Ishonch telefoni")
async def contact_menu(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer(text="📞 Ishonch telefoni: 74-228-42-84")


# ABOUT
@r.message(F.text == "🏢 Boshqarma haqida")
async def contact_menu(msg: Message, state: FSMContext):
    await state.clear()
    latitude = 40.76377174774447
    longitude = 72.35885268851638
    await msg.answer_location(latitude=latitude, longitude=longitude)
    await msg.answer(text=f"<a href='{PHOTO_URL}'>📌</a> <b>Andijon viloyat sog‘liqni saqlash boshqarmasi (keyinchalik matnda Boshqarma) sog‘liqni saqlash bo‘yicha viloyat boshqaruvi hisoblanib, o‘z faoliyati bo‘yicha O‘zbekiston Respublikasi Sog‘liqni saqlash vazirligiga bo‘ysunadi. Boshqarma faoliyatini boshqa davlat idoralari, jumladan davlat muassasalari, Andijon viloyatining ijro etuvchi hokimiyat idoralari, shuningdek boshqa jamoatchilik tashkilotlari bilan birga olib boradi. Boshqarma faoliyati O‘zbekiston Respublikasi Sog‘liqni saqlash vazirligi buyruq va ko‘rsatmalari asosida yuritiladi</b>\n\n<b>Boshqarma tarkibida</b>\n🏥 25 ta viloyat davolash muassasalari hamda\n🏨 17 ta shahar va tuman tibbiyot birlashmalari mavjud", link_preview_options=LinkPreviewOptions(show_above_text=True, prefer_large_media=True), reply_markup=Reply.main_menu())


# SEND MESSAGE
@r.message(F.text == "📝 Murojaat yuborish")
async def contact_menu(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer(text="Iltimos to'liq ism familiyangiz kiriting. Masalan: Yuldashev Fahriddin Tojiddin o'g'li", reply_markup=Reply.back_menu())
    await state.set_state(SendMessage.fullname)


@r.message(SendMessage.fullname)
async def name_menu(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer(text=f"Yaxshi {msg.text}, endi esa manzilingizni yuboring. Masalan: Andijon shahar A.Xoji ko'chasi 138-uy", reply_markup=Reply.back_menu())
    await state.set_state(SendMessage.location)


@r.message(SendMessage.location)
async def number_menu(msg: Message, state: FSMContext):
    await state.update_data(location=msg.text)
    await msg.answer(text=f"Yaxshi endi esa telefon raqamingiz yuboring. Masalan: 99-000-00-00", reply_markup=Reply.back_menu())
    await state.set_state(SendMessage.number)


@r.message(SendMessage.number)
async def name_menu(msg: Message, state: FSMContext):
    await state.update_data(number=msg.text)
    await msg.answer(text=f"Yaxshi endi esa murojaatingizni yuboring.", reply_markup=Reply.back_menu())
    await state.set_state(SendMessage.text)


@r.message(SendMessage.text)
async def name_menu(msg: Message, state: FSMContext):
    user_data = await state.get_data()
    name = user_data["name"]
    number = user_data["number"]
    location = user_data["location"]

    await msg.bot.send_message(chat_id=ADMIN_ID, text=f"📝 <b>Yangi murojaat</b>\n\nIsmi: <a href='tg://user?id={msg.from_user.id}'>{name}</a>\nTelefon raqami: {number}\nJoylashuvi: {location}\nMurojaati: {msg.text}")
    await msg.answer(text=f"Murojatingiz qabul qilindi ✅", reply_markup=Reply.main_menu())
    await state.clear()



# BACK / CANCEL
@r.callback_query(F.data == "main_menu")
async def back_menu(call: CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await call.message.delete()
        await call.message.answer("🏠 Asosiy menyudasiz", reply_markup=Reply.main_menu())
    except Exception as e:
        await call.message.answer("🏠 Asosiy menyudasiz", reply_markup=Reply.main_menu())
        print(e)
