def get_start_text(name: str) -> str:
    return (
        f'Привет, {name}!\nЯ создан, чтобы познакомить тебя со '
        f'способами взаимодействия пользователя '
        f'с ботами в Telegram.\n'
        f'Чтобы воспользоваться мной отправь одну из команд ниже:\n\n'
        f'/keyboard - знакомство с простой клавиатурой\n'
        f'/inlinekeyboard - знакомство с встроенной клавиатурой\n'
        f'/command - знакомство с командами\n'
        f'/file - работа с файлами\n'
    )


def get_keyboard_text_handler(button: str) -> str:
    return (
        f'Вы только что нажали на кнопку с текстом: {button}\n'
        f'Я специальный хендлер, который отслеживает эту фразу и отвечает на нее.\n'
        f'Вы также можете просто написать данный текст в чат и я вам отвечу.\n\n'
        f'Именно так работают простые кнопки.'
    )


command_tutorial_text = (
    'Команды - еще один замечательный способ взаимодействия с пользователем.\n'
    'Преимущество команд состоит в том, что:\n '
    '- позволяют быстро совершать какое либо действие'
    '- доступны глобально. Начните вводить / и Telegram подсветит список команд, '
    'которые создатель '
    'бота заложил для пользователей. Настраивается через @BotFather.'
    '- подсвечиваются и кликабельны в тексте.\n\n'
    'Для этого бота настроены следующие команды:\n'
    '/start - главное меню'
    '/keyboard - знакомство с простой клавиатурой\n'
    '/inlinekeyboard - знакомство с встроенной клавиатурой\n'
    '/command - знакомство с командами\n'
    '/file - работа с файлами\n'
)

help_text = (
    'В ботах часто используется команда /help, чтобы пользователь в любой '
    'момент мог понять, что делать и как решить свою проблему.'
)

keyboard_text = (
    'Далеко не все боты понимают естественный язык. Поэтому создатели Telegram '
    'добавили возможность отправлять '
    'вашему пользователю клавиатуру с заранее заданным набором кнопок.\n\n'
    'Это упрощает взаимодействия пользователя с ботом.\n'
    'Ниже представлен пример простой клавиатуры. На каждой клавише присутствует описание '
    'для чего она предназначена.\n\n'
    'Клавиатура в примере идет с флагами:\n'
    '- *resize_keyboard* - телеграм подгоняет размер кнопок;\n'
    '- *one_time_keyboard* - клавиатура скроется после нажатия или отправки сообщения в чат.\n\n'
    '[Доки на клавиатуру](https://core.telegram.org/bots#keyboards)\n'
    '[Описание ReplyKeyboardMarkup](https://core.telegram.org/bots/api/#replykeyboardmarkup)\n'
)

inline_text = (
    'Следующий вид клавиатуры, который предоставляет Telegram - Inline-клавиатуры.\n'
    'Они прикрепляются к конкретному сообщению и позволяют взаимодействовать с '
    'пользователем, без отправки дополнительных сообщений в чат.\n\n'
    '[Доки на Inline-клавиатура]'
    '(https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating)'
)


file_text = (
    'Телеграм предоставляет мощный API для работы с файлами. '
    'В мессенджер встроена поддержка более 20 типов файлов.\n'
    'Можно загрузить файл один раз и дальше работать с ним используя лишь один ID. '
    'Отправлять разным пользователям, публиковать в каналы.\n\n'
    'Кнопки ниже позволяют протестировать это функционал. При первой загрузке файла с диска '
    'он будет загружен. Далее мы кешируем его ID и продолжаем работать с ним используя его.'
)
