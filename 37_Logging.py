import logging

#logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.DEBUG, filename='example.log')
logging.basicConfig(format='%(asctime)s   %(levelname)s:%(message)s', datefmt='%m%d%Y %I:%M:%S %p', level=logging.DEBUG, filename='example.log')

logging.debug('This message will be ignored')
logging.info('This should be logged')
logging.warning('And this, too')