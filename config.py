"""Configuration file."""
LANGUAGE = "ru_RU"

NO_DATA = "No data"
SEARCH_MSG = "Searching..."
HELLOW_MSG = """Hi there, I am SpeechBot.
I am here to echo you topics for you.
Just say anything nice and I'll send topic to you.
"""


SELECT_TOPIC = "select name from topic"
DELETE_TOPIC = "delete from topic where name=%s"
INSERT_TOPIC = "insert into topic(name) values (%s)"
FORMAT = '%(asctime)s - %(name)s:%(lineno)s - %(levelname)s - %(message)s'

TEMP_PATH = "temp/"
LOG_PATH = "logs/"
CSV_FILE = "test.csv"

SIMPLE_TOPICS = [
    "Искусственный интеллект и машинное обучение",
    "Разработка программного обеспечения и веб-разработка",
    "Базы данных и системы управления базами данных",
    "Кибербезопасность и защита информации",
    "Компьютерные сети и телекоммуникации",
    "Робототехника и автоматизация процессов",
    "Виртуализация и облачные технологии",
    "Блокчейн и криптовалюты",
    "Игровая разработка и развлекательная индустрия",
    "Электронная коммерция и интернет-маркетинг",
    "Мобильная разработка и приложения",
    "Научные вычисления и анализ данных",
    "Интернет вещей и умный дом",
    "Технологии распознавания и синтеза речи",
    "Работа с большими данными и аналитика",
]

MANAGE_MSG = """
# 1 - add topics from csv
# 2 - add topics yourself
# 3 - show topics
# 4 - delete topics
# 5 - end of work
Choose one: """
