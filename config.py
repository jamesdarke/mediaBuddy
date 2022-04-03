import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5100929160:AAEFqRpUkquhne2ee8xGZObecT2nQNP5zMk")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "6515159"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "aa535109b4e3f0b33b9122b7829e32bb")

    # Authorized users to use this bot

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQCrlHLBx-zr7kB_ms6pTKnTwuUcpe22YolsT5Ni9lfa5gXzqjQ8jPtHDyk0m__O7g5b3pwCua2TKS1RUmWU5TQje0vyoWx-MjiWyNF0jGHqzm_aYLehiIIKMiC1rly2L4qLApxFa_gb4dpq4uVFAFpKvq3oQ7-cwjYrht69N9dq_iaiFJPzXyiXex20kTIerRvpcDirHQsyouC7O-s7FNj8K-AMKw_pta2X0-xQIBRHeKnyF_rGMgJ6meDXaEVU6ac7eDZb9dgPFgJVBfvsdrjhBwCdP06KEdnm7vTq0D_ju5uP5GRkbnVu5RzTkosS5MUtYuedqMNwfrZnkdzhryIjTLpIxwA")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
