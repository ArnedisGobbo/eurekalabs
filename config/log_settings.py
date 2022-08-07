# -*- coding: utf-8 -*-

import logging
import datetime as dt

LOG_FILE_PATH = './logs/EurekaLabs.log'
LOG_ENABLED = True
UNIT_ID = 'EurekaLabsAPI'


class ASCFilter(logging.Filter):
    """Injects micro seconds info to log. """

    converter = dt.datetime.fromtimestamp

    def __init__(self, unitid=None):
        super(ASCFilter, self).__init__()
        self.unitid = unitid

    def filter(self, record):
        ct = self.converter(record.created)
        record.microsecs = ct.microsecond
        record.unitid = self.unitid
        return True


def fill_logging_dict(level, log_path, unitid):
    """
    :param level: A string 'INFO', 'DEBUG', 'WARNING' or 'CRITICAL'
    :param log_path: path to log file
    :param unitid: The UnitId
    :return: A dict with the logging configuration.
    """

    dicti = {
        "version": 1,
        "disable_existing_loggers": False,
        'filters': {
            'ascfilter': {
                '()': ASCFilter,
                'unitid': unitid
            }
        },
        "formatters": {
            "info": {
                "format": "%(asctime)s.%(microsecs)06d - %(unitid)s - "
                          "%(levelname)s - L3 - %(message)s",
                "datefmt": "%Y-%m-%dT%H:%M:%S"
            },
            "info_time": {
                "format": "%(message)60s"
            }
        },
        "handlers": {
            "info_file_handler": {
                "class": "logging.FileHandler",
                "level": level,
                "formatter": "info",
                "filename": log_path,
                "encoding": "utf8",
                "mode": "a",
                "filters": ["ascfilter"]
            }
        },
        "root": {
            "level": level,
            "handlers": ["info_file_handler"]
        }
    }

    return dicti
