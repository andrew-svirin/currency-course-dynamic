# Files and directories declarations.

from pathlib import Path

__cache_dir__ = 'cache'
__course_file__ = 'course.json'


def get_project_dir() -> Path:
    return Path(__file__).parent.parent.parent


def get_cache_dir() -> Path:
    return get_project_dir().joinpath(__cache_dir__)


def get_course_file() -> Path:
    return get_cache_dir().joinpath(__course_file__)
