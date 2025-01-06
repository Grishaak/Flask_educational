import logging
import string


class ASCIIfilter(logging.Filter):

    def filter(self, record: logging.LogRecord) -> int:
        return not any(char not in string.printable for char in record.msg)


logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("filter")
logger.addFilter(ASCIIfilter())


def main():
    logger.info("There are only ascii symbols")
    logger.info("А тут нет асии символов!")


if __name__ == '__main__':
    main()

