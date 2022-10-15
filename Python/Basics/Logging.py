import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%m/%d/%y %H:%M:%S')
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# creating custom logging
logger = logging.getLogger(__name__)
logger.info('logging message from logging.py') 

# creating handlers
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# levels
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

# format
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('This is a warning message')
logger.error('This is an error message')
