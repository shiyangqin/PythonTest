# -*- coding: utf-8 -*-
import logging
import os
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler


LEVELS = {
    'NOSET': logging.NOTSET,
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
}


def get_logger(name: str, file_path: str, file_name: str, log_level="info", file_handler="time") -> logging.Logger:
    """获取循环日志记录器
    :param name:日志记录器名称，请保证name值唯一
    :param file_path:日志存放路径，例："/var/log/antiy"
    :param file_name:日志文件名，统一以 .log结尾，例： "asset.log"
    :param log_level:日志打印等级
    :param file_handler:文件句柄类型
    :return:logger对象
    """
    log_level = log_level.upper()
    file_handler = file_handler.lower()
    assert isinstance(name, str), "日志记录器名称必须是str"
    assert file_name.endswith(".log"), "文件名需要以 .log 结尾"
    assert log_level in LEVELS.keys(), "日志等级错误"
    assert file_handler in ("rotate", "time"), "文件句柄类型错误"

    # 创建文件夹
    if not (os.path.exists(file_path) and os.path.isdir(file_path)):
        os.makedirs(file_path)
    file_name = os.path.join(file_path, file_name)

    # 创建logger对象并设置日志记录等级
    logger = logging.getLogger(name)
    logger.handlers = []
    logger.setLevel(LEVELS[log_level])

    # 设置日志格式
    formatter = logging.Formatter("%(asctime)s %(name)s %(lineno)s %(levelname)s %(message)s")

    # 设置FileHandler
    if file_handler == 'rotate':
        file_handler = RotatingFileHandler(
            filename=file_name, maxBytes=1024 * 1024 * 200, backupCount=2, encoding='utf-8')
    else:
        file_handler = TimedRotatingFileHandler(
            filename=file_name, when='midnight', backupCount=7, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # 设置StreamHandler
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger


if __name__ == '__main__':
    logger_1 = get_logger("test_1", file_path='./logs', file_name='1.log')
    logger_1.info('this is test 1')
    logger_2 = get_logger("test_2", file_path='./logs', file_name='2.log')
    logger_2.info('this is test 2')

    # 当name再次为1时，获取的是logger_1对象，同时会更新对象属性
    # 导致接下来logger_1和logger_3都是输出到3.log中，logger_2正常使用
    # 为了避免影响，请保证name值唯一
    logger_3 = get_logger("test_1", file_path='./logs', file_name='3.log')
    logger_1.info('this is test 31')
    logger_2.info('this is test 32')
    logger_3.info('this is test 33')
