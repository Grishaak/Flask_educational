import logging.config

from handler.customHandler import custom_config

logging.config.dictConfig(custom_config)

# root_logger = logging.getLogger()
#
# logging.basicConfig()
# module_log = logging.getLogger("module_log")
# submodule_log = logging.getLogger("module_log.submodule_log")
# submodule_log.setLevel("DEBUG")
#
# module_log.propagate = False
#
# custom_handler = logging.StreamHandler()
# module_log.addHandler(custom_handler)
# formatter = logging.Formatter(fmt="%(levelname)s | %(name)s | %(message)s", style='%')
# custom_handler.setFormatter(formatter)

submoduleLogger = logging.getLogger("module_logger.submodule_logger")
submoduleLogger.setLevel("DEBUG")


def main():
    # print("Root logger")
    # print(root_logger.handlers)
    #
    # print("submodule_log")
    # print(submodule_log.handlers)
    #
    # print("module_log")
    # print(module_log.handlers)
    #
    # submoduleLogger.debug("Привед.")
    # submoduleLogger.debug("Eot hfp ghbdtn.")
    submoduleLogger.debug("msg", extra={'very': 'much'})

if __name__ == '__main__':
     main()
