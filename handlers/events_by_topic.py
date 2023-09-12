from telebot.types import CallbackQuery

from models.dictionaries import topic2domain, topic2pre_speech
from models.event_message import EventMessage
from models.pagination_keyboard import PaginationKeyboard
from utils.dao import get_event_ids_by_domain_name, get_events_by_ids


def run(bot):
    @bot.message_handler(commands=["expo", "party", "standup"])
    async def get_events_by_topic(message):
        await bot.delete_message(message.chat.id, message.message_id - 1)

        domain = topic2domain[message.text[1:]]
        pre_speech = topic2pre_speech[message.text[1:]]

        event_ids = get_event_ids_by_domain_name(domain)
        events = get_events_by_ids(event_ids)

        await bot.delete_message(message.chat.id, message.message_id)

        if not events:
            await bot.send_message(
                message.chat.id,
                "Мероприятия не найдены!"
            )
        else:
            event_message = EventMessage(events)
            await bot.send_message(
                message.chat.id,
                pre_speech + "\n\n" + event_message.get_message_text(0),
                parse_mode="HTML",
                disable_web_page_preview=True,
                reply_markup=event_message.create_keyboard(f"EventsByTopic/{domain}")
            )

    @bot.callback_query_handler(func=lambda call: call.data.startswith("EventsByTopic"))
    async def events_by_topic_pagination(call: CallbackQuery):
        await bot.answer_callback_query(call.id)

        topic = call.data.split("|")[0].split("/")[1]
        domain = topic2domain[topic]
        pre_speech = topic2pre_speech[topic]

        event_ids = get_event_ids_by_domain_name(domain)
        events = get_events_by_ids(event_ids)

        event_message = EventMessage(events)
        page = PaginationKeyboard.get_current_page_from_callback(call.data)

        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(
            call.message.chat.id,
            pre_speech + "\n\n" + event_message.get_message_text(page),
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=event_message.change_keyboard_page(call.data)
        )
