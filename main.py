from logger import Logger


def logger_test():
    log = Logger()
    log.loger(0, 'test SYSTEM')
    log.loger(3, 'test INFO and ERROR', True)
    log.loger(2, 'test DIAGNOST')
    log.loger(1, 'test INIT')


if __name__ == '__main__':
    logger_test()

