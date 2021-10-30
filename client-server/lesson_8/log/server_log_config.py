import logging
import log
from logging.handlers import TimedRotatingFileHandler


handler = TimedRotatingFileHandler('log/server_log.log', when='D', interval=1, backupCount=0, encoding=None, delay=False, utc=False, atTime=None)
my_format = logging.Formatter('%(asctime)-10s %(levelname)s %(module)s %(message)s')
handler.setFormatter(my_format)
log_loader = logging.FileHandler('log/server_log.log')
handler.setLevel(logging.INFO)

