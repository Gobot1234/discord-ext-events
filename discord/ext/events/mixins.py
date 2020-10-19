from typing import TYPE_CHECKING, Any

import discord

from .dispatcher import CustomEventDispatcher


class EventsMixin(discord.Client):
    dispatcher = CustomEventDispatcher()

    def dispatch(self, event: str, *args: Any, **kwargs: Any) -> None:
        super().dispatch(event, *args, **kwargs)  # type: ignore
        self.dispatcher.handle(self, event, *args, **kwargs)

    if TYPE_CHECKING:

        async def on_member_kick(self, member: discord.Member, entry: discord.AuditLogEntry):
            ...
