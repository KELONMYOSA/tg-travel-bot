from utils.dao import get_providers


def run(bot):
    @bot.message_handler(commands=["sources"])
    async def sources(message):
        providers = get_providers()
        sources_text = "Список источников:\n"
        for provider in providers:
            sources_text += f"\n-️ <a href='{provider.url}'>{provider.name}</a>"

        await bot.delete_message(message.chat.id, message.message_id)
        await bot.send_message(
            message.chat.id,
            sources_text,
            parse_mode="HTML",
            disable_web_page_preview=True
        )
