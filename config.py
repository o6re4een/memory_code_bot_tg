from enum import Enum


db_file = "database.vdb"


class States(Enum):
    """
    Мы используем БД Vedis, в которой хранимые значения всегда строки,
    поэтому и тут будем использовать тоже строки (str)
    """
    S_START = "0"  # Начало нового диалога
    S_ENTER_LOGPAS='1'
    S_ENTER_LAST_AND_NAME = "2"
    S_ENTER_AGE = "3"
    S_ENTER_BIRTHPLACE = "4"
    S_ENTER_PROF = "5"
    S_ENTER_FREETIME = "6"
    S_ENTER_HOBBY = "7"
    S_ENTER_RELIGION = "8"
    S_ENTER_VALUES = "9"
    S_ENTER_GOODREL = "10"
    S_ENTER_PERSANALITY = "11"
    S_ENTER_SPECIALMOMENTS = "12"
