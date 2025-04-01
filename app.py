import asyncio
from handlers import r
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config import BOT_TOKEN, CHANNEL_ID
from middlewares import CheckSubscriptionMiddleware
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties


default = DefaultBotProperties(parse_mode=ParseMode.HTML)
bot = Bot(token=BOT_TOKEN, default=default)
dp = Dispatcher(storage=MemoryStorage())


async def main():
    dp.message.middleware(CheckSubscriptionMiddleware(channel_id=CHANNEL_ID))
    dp.include_router(router=r)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())