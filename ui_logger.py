# logger.py
import datetime
from typing import Any


class Logger:
    def __init__(self):
        pass

    def log(self, text: str, text_widget: Any = None):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{timestamp} : {text}\n"
        if text_widget:
            text_widget.insert('end', log_message)
            text_widget.see('end')  # 滚动到最后一行
        else:
            print(log_message)


def get_logger():
    return Logger()
