import logging

from setting import LOG_FILENAME
from ui.app import UI

logging.basicConfig(
    filename=LOG_FILENAME,
    
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG,
)
logger=logging.getLogger(__name__)



if __name__ == "__main__":
    ui=UI()
    ui.run()
