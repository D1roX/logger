import logging
import os
import threading


# уровни логирования
LOGGING_LEVELS = {
    0: 'SYSTEM',
    1: 'INIT',
    2: 'DIAGNOST',
    3: 'INFO',
}

# формат сообщения
MESSAGE_FORMAT = '%(asctime)s - %(name)s - %(message)s'


class Logger(logging.getLoggerClass()):
    """
    Класс логирования.
    """
    def __init__(self, name='logger'):
        super().__init__(name)

        # изменение имени файла логирования предыдущего запуска, если он существует
        if os.path.exists('_log.txt'):
            os.replace('_log.txt', '_old_log.txt')

        logging.basicConfig(filename='_log.txt', filemode='w', format=MESSAGE_FORMAT)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # для вывода логов в консоль расскоментировать строки ниже
        #
        # self.ch = logging.StreamHandler()
        # self.ch.setLevel(logging.DEBUG)
        # self.formatter = logging.Formatter(MESSAGE_FORMAT)
        # self.ch.setFormatter(self.formatter)
        # self.logger.addHandler(self.ch)

    def isEnabledFor(self, level_index):
        """
        Функция для проверки наличия переданного уровня логирования в словаре существующих.
        :param level_index: индекс уровня логирования.
        :return:
        True, если переданный индекс существует в словаре;
        False, если отсутствует.
        """
        if level_index in LOGGING_LEVELS.keys():
            return True
        else:
            return False

    def make_log(self, level_index=0, msg='', is_error=False):
        """
        Функция для записи сообщения с указанием уровня логирования и информацией о наличии ошибки.
        :param level_index: индекс уровеня логирования
        :param msg: сообщение
        :param is_error: наличие ошибки
        """
        level_name = '[NOTSET]'
        if self.isEnabledFor(level_index):
            level_name = f'[{LOGGING_LEVELS[level_index]}]'

        error = '[ERROR]' if is_error else ''
        msg = f'{error}{level_name} - {msg}'
        self.logger.log(10, msg)

    def loger(self, level_index=0, msg='', is_error=False):
        """
        Вызов функции для записи сообщения с указанием уровня логирования и информацией о наличии ошибки в отдельном
        потоке.
        :param level_index: индекс уровеня логирования
        :param msg: сообщение
        :param is_error: наличие ошибки
        """
        log_thread = threading.Thread(target=self.make_log, args=(level_index, msg, is_error))
        log_thread.start()

