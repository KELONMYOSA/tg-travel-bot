from models.dictionaries import topic2domain


def run(bot):
    @bot.message_handler(commands=["expo", "party", "standup"])
    async def get_events_by_topic(message):
        domain = topic2domain[message.text[1:]]

        await bot.delete_message(message.chat.id, message.message_id)
