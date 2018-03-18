# coding: utf8
import logging
import time
import datetime
from api.service import GameService as gs
import api.base_name as names
logging.basicConfig(filename='logger.log',
                    format='%(filename)-12s[LINE:%(lineno)d] %(levelname)-8s %(message)s %(asctime)s',
                    level=logging.INFO)

#print(time.time())
def all_event(count):
    """
    Метод возвращает 10 событий, начиная с заданного номера
    :param count: int номер события, с которого начинать вывод
    :return: {names.ANSWER: names.SUCCESS, names.DATA: result}
    """
    try:
        sql = "SELECT Name, Description, Status, Date_start, Date_end FROM Event LIMIT 10 OFFSET {}".format(count)
        if isinstance(count, int) and count >= 0:
            result = gs.SqlQuery(sql)
            #print(result)
        else:
            logging.error(names.ERROR_EXECUTE_DATABASE)
            return {names.ANSWER: names.ERROR}
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}


def current_event(count):
    """
    Метод возвращает 10 событий, начиная с заданного номера и если они еще не начались
    :param count: int номер события, с которого начинать вывод
    :return: {names.ANSWER: names.SUCCESS, names.DATA: result}
    """
    sql = "SELECT Name, Description, Status, Date_start, Date_end " \
          "FROM Event WHERE Date_start < {} LIMIT 10 OFFSET {}".format(time.time(), count)
    try:
        if isinstance(count, int) and count >= 0:
            result = gs.SqlQuery(sql)
        else:
            logging.error(names.ERROR_EXECUTE_DATABASE)
            return {names.ANSWER: names.ERROR}
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}


def end_event(count):
    """
    Метод возвращает 10 событий, начиная с заданного номера и если они закончились
    :param count: int номер события, с которого начинать вывод
    :return: {names.ANSWER: names.SUCCESS, names.DATA: result}
    """
    sql = "SELECT Name, Description, Status, Date_start, Date_end " \
          "FROM Event WHERE Date_end > {} LIMIT 10 OFFSET {}".format(datetime.datetime.now().strftime('%d.%m.%Y'), count)
    print(sql)
    try:
        if isinstance(count, int) and count >= 0:
            result = gs.SqlQuery(sql)
        else:
            logging.error(names.ERROR_EXECUTE_DATABASE)
            return {names.ANSWER: names.ERROR}
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}

def find_event(alf, count):

    """
    Метод возвращает 10 событий, начиная с заданного номера и если они закончились
    :param alf: str Символы, которые встречаются в названии события
    :param count: int номер события, с которого начинать вывод
    :return: {names.ANSWER: names.SUCCESS, names.DATA: result}
    """
    sql = "SELECT id_event, Name, Description, Status, Date_start, Date_end " \
          "FROM Event WHERE Name LIKE '%{}%' ORDER BY id_event LIMIT 10 OFFSET {}".format(alf, count)
    #print(sql)
    try:
        if isinstance(count, int) and count >= 0:
            result = gs.SqlQuery(sql)
            #print(result)
        else:
            logging.error(names.ERROR_EXECUTE_DATABASE)
            return {names.ANSWER: names.ERROR}
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}


def page_event(count):  # Пустышка
    sql = "SELECT Name, Description, Status, Date_start, Date_end FROM Event"
    try:
        if isinstance(count, int) and count >= 0:
            result = gs.SqlQuery(sql)
        else:
            logging.error(names.ERROR_EXECUTE_DATABASE)
            return {names.ANSWER: names.ERROR}
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}


def filter_by_status(count, status):
    """
    Метод возвращает 10 событий, начиная с заданного номера и если они закончились
    :param count: int номер события, с которого начинать вывод
    :param status: int Признак завершенного или активного события
    :return: {names.ANSWER: names.SUCCESS, names.DATA: result}
    """
    sql = "SELECT Name, Description, Date_start, Date_end FROM Event where status='{}' LIMIT 10 OFFSET {}".format(status, count)
    try:
        if isinstance(count, int) and count >= 0:
            result = gs.SqlQuery(sql)
        else:
            logging.error(names.ERROR_EXECUTE_DATABASE)
            return {names.ANSWER: names.ERROR}
    except:
        logging.error(names.ERROR_EXECUTE_DATABASE)
        return {names.ANSWER: names.ERROR}
    return {names.ANSWER: names.SUCCESS, names.DATA: result}
