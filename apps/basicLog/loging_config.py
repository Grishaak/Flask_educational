dict_donfig = {
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
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base"
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "mode": "w",
            "filename": "logfile.log"
        },
    },
    "loggers": {
        "module_logger": {
            "level": "DEBUG",
            "handlers": ["file", "console"]
        }
    }
}
