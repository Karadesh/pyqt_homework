import logging
import log

logging.basicConfig(
    filename='log/client_log.log',
    format='%(asctime)-10s %(levelname)s %(module)s %(message)s',
    level=logging.INFO
)
