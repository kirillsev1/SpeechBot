"""File manages database edition."""
from db_utils import DbHandler
from config import CSV_FILE, SIMPLE_TOPICS, MANAGE_MSG, DELETE_TOPIC, INSERT_TOPIC
import os
import csv


def read_csv() -> list:
    """Function gets topics from csv file.

    Returns:
        csv_topics (list): list of topics from csv file.
    """
    if not os.path.isfile(CSV_FILE):
        return None
    csv_topics = []
    with open(CSV_FILE, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\n')
        for text in csv_reader:
            csv_topics.append(text[0].strip())
    return csv_topics


# 1 - add topics from csv
# 2 - add topics yourself
# 3 - show topics
# 4 - delete topics
# 5 - end of work
def manage() -> None:
    """Function manages actions with database."""
    while True:
        match input(MANAGE_MSG):
            case "1":
                csv_data = read_csv()
                DbHandler.change_topic(csv_data if csv_data else SIMPLE_TOPICS, INSERT_TOPIC)
            case "2":
                try:
                    topics = [input(f"Topic {num}: ") for num in range(int(input("Number of moves: ")))]
                except ValueError:
                    continue
                DbHandler.change_topic(topics, INSERT_TOPIC)
            case "3":
                print("\n".join(DbHandler.get_topics()))
            case "4":
                try:
                    topics = [input(f"Topic {num}: ") for num in range(int(input("Number of moves: ")))]
                except ValueError:
                    continue
                DbHandler.change_topic(topics, DELETE_TOPIC)
            case "5":
                break


if __name__ == "__main__":
    manage()
