import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler_critical = logging.FileHandler('Critical.txt', 'w')
handler_critical.setLevel(logging.WARNING)

handler_info = logging.StreamHandler()
handler_info.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler_critical.setFormatter(formatter)
handler_info.setFormatter(formatter)

logger.addHandler(handler_info)
logger.addHandler(handler_critical)

logger.info('Information')
logger.warning('warning')
