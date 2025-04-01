from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable


class CheckSubscriptionMiddleware(BaseMiddleware):
    def __init__(self, channel_id: str):
        self.channel_id = channel_id
        super().__init__()

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        bot = data['bot']

        try:
            member = await bot.get_chat_member(
                chat_id=self.channel_id,
                user_id=event.from_user.id
            )

            if member.status in ["member", "administrator", "creator"]:
                return await handler(event, data)

            await event.answer(
                f"Iltimos, avval {self.channel_id} kanaliga a'zo bo'ling!"
            )
            return

        except Exception as e:
            await event.answer(
                f"Kechirasiz, a'zolikni tekshirishda xatolik yuz berdi: {e}"
            )
            return
