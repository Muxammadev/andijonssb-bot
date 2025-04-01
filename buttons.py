from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

ibuilder = InlineKeyboardBuilder
builder = ReplyKeyboardBuilder
ibtn = InlineKeyboardButton
btn = KeyboardButton

institutions = [
    "Andijon viloyat ko'p tarmoqli tibbiyot markazi",
    "Respublika ixtisoslashtirilgan onkologiya va radiologiya ilmiy-amaliy tibbiyot markazi Andijon filiali",
    "Respublika ixtisoslashtirilgan dermatovenerologiya va kosmetologiya ilmiy-amaliy tibbiyot markazi Andijon viloyat hududiy filiali",
    "Andijon viloyat ftiziatriya va pulmonologiya markazi",
    "Respublika ixtisoslashtirilgan endokrinologiya ilmiy-amaliy tibbiyot markazi Andijon filiali",
    "Respublika ixtisoslashtirilgan ona va bola salomatligi ilmiy amaliy tibbiet markazi davlat muassasasining Andijon viloyati filiali",
    "Andijon viloyat OITSga qarshi kurash markazi",
    "Andijon viloyat ko‘p tarmoqli tibbiyot markazi",
    "Andijon viloyat yuqumli kasalliklar shifoxonasi",
    "Andijon viloyat oftalmologiya shifoxonasi",
    "Andijon viloyat bolalar ko‘p tarmoqli tibbiyot markazi",
    "Andijon viloyat psixonevrologiya dispanseri",
    "Viloyat ftiziatriya klinik shifoxonasi",
    "Viloyat ftiziatriya sanatoriysi",
    "RShTYoIM AF",
    "Viloyat qon quyish stansiyasi",
    "Andijon viloyat bolalar stomatologiya poliklinikasi",
    "Respublika sud tibbiy ekspertiza ilmiy amaliy markazi Andijon filiali",
    "Andijon viloyat bolalar sil kasaliklari sanatoriysi",
    "Andijon viloyat patologik anatomiya byurosi",
    "Respublika ixtisoslashtirilgan kardiologiya ilmiy-amaliy tibbiyot markazi Andijon filiali",
    "Respublika tez tibbiy yordam markazi Andijon viloyati filiali",
    "Respublika ixtisoslashtirilgan narkologiya ilmiy-amaliy tibbiyot markazi Andijon viloyat mintaqaviy filiali",
    "Xo‘jalik xisobidagi travmatologiya va ortopediya shifoxonasi",
    "Andijon shahar tibbiyot birlashmasi",
    "Qorasuv shaxar tibbiyot birlashmasi",
    "Andijon tuman tibbiyot birlashmasi",
    "Asaka tuman tibbiyot birlashmasi",
    "Oltinko‘l tumani tibbiyot birlashmasi",
    "Baliqchi tumani tibbiyot birlashmasi",
    "Bo‘ston tuman tibbiyot birlashmasi",
    "Jalaquduq tuman tibbiyot birlashmasi",
    "Izboskan tumani tibbiyot birlashmasi",
    "Marhamat tumani tibbiyot birlashmasi",
    "Ulug‘nor tuman tibbiet birlashmasi",
    "Paxtaobod tuman tibbiyot birlashmasi",
    "Xo‘jaobod tuman tibbiyot birlashmasi",
    "Qo‘rg‘ontepa tuman tibbiyot birlashmasi",
    "Shaxrixon tuman tibbiyot birlashmasi",
]


class Inline:
    @staticmethod
    def hospitals_menu(page: int = 1):
        if page == 2:
            return ibuilder(markup=[
                [
                    ibtn(text="1️⃣", callback_data="hospital_11"),
                    ibtn(text="2️⃣", callback_data="hospital_12"),
                    ibtn(text="3️⃣", callback_data="hospital_13"),
                    ibtn(text="4️⃣", callback_data="hospital_14"),
                    ibtn(text="5️⃣", callback_data="hospital_15"),
                ],
                [
                    ibtn(text="6️⃣", callback_data="hospital_16"),
                    ibtn(text="7️⃣", callback_data="hospital_17"),
                    ibtn(text="8️⃣", callback_data="hospital_18"),
                    ibtn(text="9️⃣", callback_data="hospital_19"),
                    ibtn(text="🔟", callback_data="hospital_20"),
                ],
                [
                    ibtn(text="⬅️", callback_data="page_1"),
                    ibtn(text="❌", callback_data="main_menu"),
                    ibtn(text="➡️", callback_data="page_3"),
                ]
            ]).as_markup()
        elif page == 3:
            return ibuilder(markup=[
                [
                    ibtn(text="1️⃣", callback_data="hospital_21"),
                    ibtn(text="2️⃣", callback_data="hospital_22"),
                    ibtn(text="3️⃣", callback_data="hospital_23"),
                    ibtn(text="4️⃣", callback_data="hospital_24"),
                    ibtn(text="5️⃣", callback_data="hospital_25"),
                ],
                [
                    ibtn(text="6️⃣", callback_data="hospital_26"),
                    ibtn(text="7️⃣", callback_data="hospital_27"),
                    ibtn(text="8️⃣", callback_data="hospital_28"),
                    ibtn(text="9️⃣", callback_data="hospital_29"),
                    ibtn(text="🔟", callback_data="hospital_30"),
                ],
                [
                    ibtn(text="⬅️", callback_data="page_2"),
                    ibtn(text="❌", callback_data="main_menu"),
                    ibtn(text="➡️", callback_data="page_4"),
                ]
            ]).as_markup()
        elif page == 4:
            return ibuilder(markup=[
                [
                    ibtn(text="1️⃣", callback_data="hospital_31"),
                    ibtn(text="2️⃣", callback_data="hospital_32"),
                    ibtn(text="3️⃣", callback_data="hospital_33"),
                    ibtn(text="4️⃣", callback_data="hospital_34"),
                    ibtn(text="5️⃣", callback_data="hospital_35"),
                ],
                [
                    ibtn(text="6️⃣", callback_data="hospital_36"),
                    ibtn(text="7️⃣", callback_data="hospital_37"),
                    ibtn(text="8️⃣", callback_data="hospital_38"),
                    ibtn(text="9️⃣", callback_data="hospital_39"),
                    ibtn(text="🔟", callback_data="hospital_40"),
                ],
                [
                    ibtn(text="⬅️", callback_data="page_3"),
                    ibtn(text="❌", callback_data="main_menu"),
                    ibtn(text="➡️", callback_data="page_0"),
                ]
            ]).as_markup()
        else:
            return ibuilder(markup=[
                [
                    ibtn(text="1️⃣", callback_data="hospital_1"),
                    ibtn(text="2️⃣", callback_data="hospital_2"),
                    ibtn(text="3️⃣", callback_data="hospital_3"),
                    ibtn(text="4️⃣", callback_data="hospital_4"),
                    ibtn(text="5️⃣", callback_data="hospital_5"),
                ],
                [
                    ibtn(text="6️⃣", callback_data="hospital_6"),
                    ibtn(text="7️⃣", callback_data="hospital_7"),
                    ibtn(text="8️⃣", callback_data="hospital_8"),
                    ibtn(text="9️⃣", callback_data="hospital_9"),
                    ibtn(text="🔟", callback_data="hospital_10"),
                ],
                [
                    ibtn(text="⬅️", callback_data="page_0"),
                    ibtn(text="❌", callback_data="main_menu"),
                    ibtn(text="➡️", callback_data="page_2"),
                ]
            ]).as_markup()


class Reply:
    @staticmethod
    def main_menu():
        return builder(markup=[
            [
                btn(text="🏥 Tibbiyot muassasalari manzillari")
            ],
            [
                btn(text="📞 Ishonch telefoni"),
                btn(text="🏢 Boshqarma haqida"),
            ],
            [
                btn(text="📝 Murojaat yuborish"),
            ]
        ]).as_markup(resize_keyboard=True)

    @staticmethod
    def back_menu():
        return builder(markup=[
            [
                btn(text="◀️ Orqaga")
            ]
        ]).as_markup(resize_keyboard=True)
