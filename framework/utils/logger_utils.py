import logging


class LoggerUtils:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            logger = logging.getLogger()
            file_handler = logging.FileHandler('general.log', mode='w')
            formatter = logging.Formatter('%(asctime)s - %(levelname)s:%(message)s', datefmt='%d/%m/%Y %H:%M:%S')
            logger.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            file_handler.setLevel(logging.DEBUG)
            logger.addHandler(file_handler)
            cls._instance = logger
        return cls._instance
