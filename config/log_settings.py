# -*- coding: utf-8 -*-

import logging
import datetime as dt

LOG_FILE_PATH = './logs/EurekaLabs.log'
LOG_ENABLED = True
UNIT_ID = 'EurekaLabsAPI'


class ASCFilter(logging.Filter):
    """Injects micro seconds info to log. """

    converter = dt.datetime.fromtimestamp

    def __init__(self, unit_id=None):
        super(ASCFilter, self).__init__()
        self.unit_id = unit_id

    def filter(self, record):
        ct = self.converter(record.created)
        record.microsecs = ct.microsecond
        record.unitid = self.unit_id
        return True


def fill_logging_dict(level, log_path, unit_id):
    """
    :param level: 'INFO', 'DEBUG', 'WARNING' or 'CRITICAL'
    :param log_path: path to log file
    :param unit_id: The UnitId
    :return: A dict with the logging configuration.
    """

    dict_cfg = {
        "version": 1,
        "disable_existing_loggers": False,
        'filters': {
            'ascfilter': {
                '()': ASCFilter,
                'unitid': unit_id
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

    return dict_cfg
