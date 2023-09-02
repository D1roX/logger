import logging
import threading
import time

from logger import Logger


def logger_test():
    log = Logger(only_error=True)
    log.loger(60, 'test system log')
    log.loger(70, 'test init log')
    log.loger(80, 'test diagnost log')
    log.loger(10, 'test debug log')
    log.loger(20, 'test info log')
    log.loger(30, 'test warning log')
    log.loger(40, 'test error log')
    log.loger(50, 'test critical log')

    log.system('test system log')
    log.init('test init log')
    log.diagnost('test diagnost log')
    log.info('test info log')
    log.debug('test debug log')
    log.warning('test warning log')
    log.error('test error log')
    log.critical('test critical log')

    log.loger(60, 'test error system log', True)
    log.loger(70, 'test error init log', True)
    log.loger(80, 'test error diagnost log', True)
    log.loger(10, 'test error debug log', True)
    log.loger(20, 'test error info log', True)
    log.loger(30, 'test error warning log', True)
    log.loger(40, 'test error warning log')
    log.loger(50, 'test error warning log', True)

    log.system('test error system log', True)
    log.init('test error init log', True)
    log.diagnost('test error diagnost log', True)
    log.info('test error info log', True)
    log.debug('test error debug log', True)
    log.warning('test error warning log', True)
    log.error('test error error log')
    log.critical('test error critical log')


def logger_name_test():
    log = Logger('logger_name_test')
    log.info('test loger name')


if __name__ == '__main__':
    logger_test()
    logger_name_test()

