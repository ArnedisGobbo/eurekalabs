#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.config
import os

from config.log_settings import fill_logging_dict, UNIT_ID, LOG_ENABLED, LOG_FILE_PATH
from application.exceptions import InvalidLogPath


logger = logging.getLogger(__name__)


def log_config(log_path, log_enabled, log_level, unit_id):
    log_dir = os.path.dirname(log_path)
    log_dir = '.' if log_dir == '' else log_dir
    if not log_enabled:
        logging.disable(logging.CRITICAL)
    else:
        if not os.path.isdir(log_dir) \
                or not os.access(log_dir, os.W_OK):
            raise InvalidLogPath(os.path.dirname(log_path), msg="invalid log file")
        dict_cfg = fill_logging_dict(log_level, log_path, unit_id)
        logging.config.dictConfig(dict_cfg)


def log_initial(log_file_path,
                log_enabled,
                log_type,
                unit_id):
    def true_to_yes(t):
        return 'yes' if t else 'no'

    logger.info("{} execution started".format(unit_id))
    logger.info("[CONF][GEN] Unit ID: {}".format(unit_id))

    logger.info("[CONF][GEN] Log enabled: {}".format(true_to_yes(log_enabled)))
    logger.info("[CONF][GEN] Log path: {}".format(log_file_path))
    logger.info("[CONF][GEN] Log type: {}".format(log_type))


def setup_log(log_type):
    log_config(LOG_FILE_PATH,
               LOG_ENABLED,
               log_type,
               UNIT_ID)

    log_initial(LOG_FILE_PATH,
                LOG_ENABLED,
                log_type,
                UNIT_ID)
