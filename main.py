from logger import Logger
import threading


def logger_test():
    log = Logger()
    logger_thread = threading.Thread(target=log.make_log, args=('bob',), daemon=True)
    log.loger(0, 'test SYSTEM')
    log.loger(3, 'test INFO and ERROR', True)
    log.loger(2, 'test DIAGNOST')
    log.loger(1, 'test INIT')


if __name__ == '__main__':
    logger_test()

