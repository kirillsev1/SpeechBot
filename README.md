# About:
## This is a Telegram bot writen on python. After starting SpeechBot he will send greeting message. Then user can send his/her voice to chat. The first thing which this bot will do is scanning and returning text from voice message. Then he will analyse users sentences and send the most suitable topic.

# How to start
    git clone https://github.com/kirillsev1/SpeechBot.git

    python3.10 -m venv ./venv

    . ./venv/bin/activate

    pip install -r requirements.txt

# Docker container
    docker run -d --name speech -p 5666:5432 \
        -v $HOME/postgresql/speech_db:/var/lib/postgresql/speech_db \
        -e POSTGRES_PASSWORD=12345678 \
        -e POSTGRES_USER=speech_user \
        -e POSTGRES_DB=speech_db \
        postgres

### Now run ddl file for creating and filling database

    cd init_db
    
    psql -p 5666 -h 127.0.0.1 -U speech_user speech_db -f init_db.ddl

### Fill the .env file
### Now move to project directory
### Run command:
    python3 main.py

# Postgres database
## Tables: 
    topic fields:
        id uuid primary key not null default uuid_generate_v4(),
        name text

# .env
    HOST - host for http server

    PORT - port for http server

    PG_DBNAME - database name

    PG_HOST - database host

    PG_PORT - database port

    PG_USER - database user

    PG_PASSWORD - database password

    TOKEN - Telegramm bot token