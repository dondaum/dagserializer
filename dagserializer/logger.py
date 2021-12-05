import logging
import time
from logging import Logger

from dagserializer import flags

logger: Logger = logging.getLogger('dummy')


def init_logger() -> None:
    """
    Function that set the logging level and config for the py package
    and changes the logging level for 3rd pip packages
    """
    global logger
    logging.basicConfig(
        format="[%(asctime)s-%(name)s-%(levelname)s-%(filename)s] %(message)s"
    )
    logging.Formatter.converter = time.gmtime
    log = logging.getLogger("dagserializer")
    log.setLevel(getattr(logging, flags.LOGGING_LEVEL))
    logger = log
