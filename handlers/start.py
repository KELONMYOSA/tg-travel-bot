from utils.dao import log_action


def run(bot):
    @bot.message_handler(commands=["start"])
    async def start_bot(message):
        log_action(message.from_user.username, message.from_user.id, "start")
        await bot.delete_message(message.chat.id, message.message_id)
        await bot.send_message(
            message.chat.id,
            """
Приветствую!

С этого момента все мероприятия с тобой в удобном формате.

Мероприятия по тематикам:
🖼 Выставки - /expo
🎉 Вечеринки - /party
🤡 StandUp - /standup
            """
        )
