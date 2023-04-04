"""File with database utils."""
from config import SELECT_TOPIC
from psycopg2 import connect, Error
from os import getenv
from dotenv import load_dotenv

load_dotenv()


class DbHandler:
    """Class controls database requests."""

    connection = connect(
        dbname=getenv("PG_DBNAME"),
        user=getenv("PG_USER"),
        host=getenv("PG_HOST"),
        password=getenv("PG_PASSWORD"),
        port=getenv("PG_PORT"),
    )

    @classmethod
    def get_topics(cls) -> list:
        """Method gets topics from database.

        Returns:
            (list): list of topics from database.
        """
        with cls.connection.cursor() as cursor:
            cursor.execute(SELECT_TOPIC)
            try:
                return [topic[0] for topic in cursor.fetchall()]
            except Error:
                return []

    @classmethod
    def change_topic(cls, topics: list, method: str) -> None:
        """Method makes changes in database.

        Args:
            topics (list): list of topics.
            method (str): method for adding and deleting data from database.
        """
        with cls.connection.cursor() as cursor:
            for topic in topics:
                cursor.execute(method, (topic,))
            cls.connection.commit()
