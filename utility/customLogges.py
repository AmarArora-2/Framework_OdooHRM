import logging


def test_logging():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('framwork/logfile.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    logger.setLevel(logging.WARNING)
    logger.debug("A debug program")
    logger.info("Information statement")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")