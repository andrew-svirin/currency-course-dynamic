# Prepare data for next plotting.

import json

from utils.filesystem import get_course_file


# Return list of 3 courses: [buy_course, sell_course, nbu_course]
def plot_historical_courses() -> list:
    f = open(get_course_file())
    return json.load(f)
