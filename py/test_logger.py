from logging import getLogger, StreamHandler, Formatter, DEBUG
import sys

logger = getLogger('testlog')
stream = file('./testlog.log', 'w')
handler = StreamHandler(stream)
handler.setLevel(DEBUG)
handler.setFormatter(Formatter('%(name)-12s: %(levelname)-8s %(message)s'))
logger.addHandler(handler)
logger.setLevel(DEBUG)
logger.info('hello test')


