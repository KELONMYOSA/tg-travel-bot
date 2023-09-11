def run(bot):
    @bot.message_handler(func=lambda message: message.text not in ["/start", "/expo", "/party", "/standup"])
    async def echo_all(message):
        await bot.delete_message(message.chat.id, message.message_id)
        await bot.send_message(
            message.chat.id,
            "Я пока таких команд не знаю"
        )
