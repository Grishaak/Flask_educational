import logging
import sys


class CustomHandlerFile(logging.Handler):

    def __init__(self,
                 file_name: str = 'customFile.log',
                 mode='a'):
        super().__init__()
        self.file_name = file_name
        self.mode = mode

    def emit(self, record):
        message = self.format(record)
        with open(self.file_name,
                  mode=self.mode,
                  encoding='utf-8') as fi:
            fi.write(message + '\n')


class CustomStream(logging.StreamHandler):

    def __init__(self):
        super().__init__()

    def emit(self, record):
        msg = self.format(record)
        print(vars(record))
        stream = self.stream
        stream.write(msg)
        self.flush()


custom_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base":
            {
                "format": "%(levelname)s | %(name)s | %(message)s"
            }
    },
    "handlers": {
        "console": {
            "()": CustomStream,
            "level": "DEBUG",
            "formatter": "base"
        },
        "file": {
            "()": CustomHandlerFile,
            "level": 1,
            "formatter": "base",
            "file_name": "custom_file.log",
            "mode": "a"
        },
    },
    "loggers": {
        "module_logger": {
            "level": "DEBUG",
            "handlers": ["file", "console"]
        }
    }
}
