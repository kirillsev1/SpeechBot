"""File with functions for processing audios."""
from ffmpeg.asyncio import FFmpeg
import speech_recognition as speech
from db_utils import DbHandler
from config import LANGUAGE, NO_DATA
import nltk
from nltk.corpus import stopwords

recognizer = speech.Recognizer()


def recognise(filename: str) -> str:
    """Function transforms audio to text.

    Args:
        filename (str): path to audio file.

    Returns:
        text (str): text from voice.
    """
    with speech.AudioFile(filename) as source:
        audio_text = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_text, language=LANGUAGE)
        except speech.UnknownValueError:
            return NO_DATA
        return text


async def run_ffmpeg(input_path: str, output_path: str) -> None:
    """Function transforms ogg file to wav.

    Args:
        input_path (str): path for .ogg file.
        output_path (str): path for .wav file.
    """
    ffmpeg = (FFmpeg().input(input_path).output(output_path))
    await ffmpeg.execute()


def choose_topic(text: str) -> str:
    """Function analyses text from voice and chooses one topic.

    Args:
        text (str): text from voice.

    Returns:
        matching_topic (str): chosen topic.
    """
    tokens = nltk.word_tokenize(text)
    tags = nltk.pos_tag(tokens)

    nouns = [word for word, pos in tags if pos.startswith('NN') and word not in stopwords.words("russian")]

    matching_topic = NO_DATA
    max_count = 0

    for topic in DbHandler.get_topics():
        count = sum([1 for noun in nouns if noun.lower() in topic.lower()])
        if count > max_count:
            matching_topic = topic
            max_count = count
    return matching_topic
