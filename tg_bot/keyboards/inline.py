from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

days_scroll = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<<", callback_data="scroll_previous_day"),
            InlineKeyboardButton(text=">>", callback_data="scroll_next_day")
        ],
        [
            InlineKeyboardButton(text="Переключить неделю", callback_data="change_week")
        ]
    ]
)
