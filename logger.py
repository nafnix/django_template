import sys

from loguru import logger


LOG_FORMAT = (
    "<level>{level: <8}</level> | "
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
)
# logger = logging.getLogger("website.error")

logger.remove()
logger.add(sys.stdout, format=LOG_FORMAT)

