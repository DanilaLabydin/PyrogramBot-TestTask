import loguru
import os

from dotenv import load_dotenv
from configparser import ConfigParser


LOGGER = loguru.logger


if os.path.isfile(".env"):
    load_dotenv()
else:
    raise Exception("No .env file found")


API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
if not all([API_ID, API_HASH]):
    raise Exception("Not all env variables are present")


def postgres_config(filename="database.ini", section="postgresql"):
    parser = ConfigParser()

    parser.read(filename)

    db_config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_config[param[0]] = param[1]
    else:
        raise Exception(f"Section {section} not found in the {filename} file")

    return db_config
