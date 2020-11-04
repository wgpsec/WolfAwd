import os
import logging
WATCH_DIR = os.getcwd()+'/defense_inotify/www'
# 为None则不监控
WATCH_FLAG_ACCESS = '/flag'


LOG_LEVEL = logging.INFO
LOG_FILE = './monitor.log'
