# standard library imports
import os

# third party imports
from dotenv import load_dotenv

# local imports


load_dotenv()

API_KEY = os.getenv("API_KEY")
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
