import logging
import json
import os
import traceback
from datetime import datetime
import pytz


# Create logs folder if not exists
if not os.path.exists('logs'):
    os.makedirs('logs')


class UserContextFilter(logging.Filter):
    log_user_info = {
        'user_name': 'Unknown',
        'email': 'Unknown',
    }

    @classmethod
    def update_user_info(cls, user_name, email):
        cls.log_user_info = {'user_name': user_name, 'email': email}

    def filter(self, record):
        record.user_name = self.log_user_info.get('user_name')
        record.email = self.log_user_info.get('email')
        return True


class DictLogFormatter(logging.Formatter):
    def format(self, record):
        log_dict = {
            'timestamp': datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime('%Y-%m-%d %H:%M:%S %Z'),
            'level': record.levelname,
            'user_name': getattr(record, 'user_name'),
            'email': getattr(record, 'email'),
            'message': record.getMessage(),
            'module': record.module,
            'funcName': record.funcName,
            'lineno': record.lineno,
        }
        # Include traceback if present
        if record.exc_info:
            log_dict['traceback'] = traceback.format_exc()

        return json.dumps(log_dict)

# Configure logging
logger = logging.getLogger("streamlit_app")
logger.setLevel(logging.DEBUG)

# Add user context filter
user_context_filter = UserContextFilter()

# Log file with date
log_filename = datetime.now().strftime('logs/%Y-%m-%d.log')
file_handler = logging.FileHandler(log_filename)
file_handler.setFormatter(DictLogFormatter())

# Stream handler for console
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(DictLogFormatter())

if not logger.handlers:
    logger.addFilter(user_context_filter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
