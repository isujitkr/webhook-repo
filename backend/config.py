import logging
from dotenv import load_dotenv

load_dotenv()

def setup_logging():
    logging.getLogger("werkzeug").setLevel(logging.ERROR)
