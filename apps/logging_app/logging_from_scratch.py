import getpass
import hashlib
import logging

logger = logging.getLogger("password_checker")


def input_pass_check():
    logger.debug("Начало работы функции input_pass_check.")
    password: str = getpass.getpass()

    if not password:
        logger.warning("Пустой пароль")
        return False

    try:
        hasher = hashlib.md5()
        logger.debug("Создан объект hasher")
        hasher.update(password.encode('utf-8'))
        print(hasher.hexdigest())
        if hasher.hexdigest() == '4242ea74c2f838996b54839471bd10c4':
            return True
    except ValueError as ex:
        logger.exception(f"Вы ввели некорректный символ", exc_info=str(ex))
    else:
        logger.debug("Конец работы функции input_pass_check.")
        return False


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Вы пытаетесь аутентифицироваться.")
    trs = 4
    for i in range(trs):
        if input_pass_check():
            print("Пароль верный.")
            exit(0)
        else:
            print(f"Попыток осталось: {trs - i}")
    logger.error(f"Пользователь ввел {trs} раза  неправильный пароль.")
    exit(1)
