import logging
import functools


logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
file_handler = logging.FileHandler("error.log")
logger.addHandler(file_handler)

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(message)s")


def log(func):
    @functools.wraps(func)
    def wrapper(*args):
        try:
            result = func(*args)
            return result
        except Exception:
            logging.debug("User Password is NOT OK")
            logger.exception(__name__)

        finally:
            result = func(*args)
            if result == True:
                logging.debug("User Password is ok")

    return wrapper
