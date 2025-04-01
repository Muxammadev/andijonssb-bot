from aiogram.fsm.state import State, StatesGroup

class SendMessage(StatesGroup):
    fullname = State()
    location = State()
    number = State()
    text = State()
