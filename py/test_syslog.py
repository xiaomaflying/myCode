from logging import getLogger, StreamHandler, Formatter, DEBUG
from logging.handlers import SysLogHandler 


def create_logger(logger_name):

    logger = getLogger(logger_name)
    logger.setLevel(DEBUG)

    if logger.handlers:
        return logger

    handler = SysLogHandler( facility=SysLogHandler.LOG_LOCAL2)
    #handler = StreamHandler()
    handler.setLevel(DEBUG)
    logger.addHandler(handler)

    return logger


def main():
    logger = create_logger('abc_test')
    logger.info(open('ab.txt', 'r').read())
#    logger.debug("Feb 25 14:09:07 1 app 2003-10-11T22:14:15.003Z mymachine.example.com su - ID47 - BOM'su root' failed for lonvick on /dev/pts/8")
#    logger.debug('Feb 25 14:09:07 webserver syslogd[12]  sdkjfskf: sdfkrestart')
#    logger.info('mozart|this is critical')

if __name__ == '__main__':
    main()
