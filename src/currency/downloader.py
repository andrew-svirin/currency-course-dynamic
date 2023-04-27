# Downloading currency information.

from utils.filesystem import get_course_file
import urllib.request

__course_url__ = 'https://finance.i.ua/graph/avg_currency/?currency=840'


def download_historical_course() -> None:
    urllib.request.urlretrieve(__course_url__, get_course_file())
