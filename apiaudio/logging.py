import logging


class CustomFormatter(logging.Formatter):

    # For debugging: "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    def string_format(color):
        ANSI = {
            "grey": "\x1b[38;20m",
            "yellow": "\x1b[33;20m",
            "red": "\x1b[31;20m",
            "bold_red": "\x1b[31;1m",
            "bold": "\033[1m",
            "reset": "\x1b[0m",
        }
        return f"{ANSI[color]}[%(levelname)s] {ANSI['bold']}%(name)s{ANSI['reset'] + ANSI[color]}: %(message)s{ANSI['reset']}"

    FORMATS = {
        logging.DEBUG: string_format("grey"),
        logging.INFO: string_format("grey"),
        logging.WARNING: string_format("yellow"),
        logging.ERROR: string_format("red"),
        logging.CRITICAL: string_format("bold_red"),
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def SDKLogger(level="WARNING"):
    """
    Add a stream handler for the given name and level to the logging module.
    By default, this logs all apiaudio messages to ``stdout``.

    For debugging, set level=logging.DEBUG

    :type name: string
    :param name: Log name
    :type level: int
    :param level: Logging level, e.g. ``logging.INFO``
    """
    logger = logging.getLogger("apiaudio")
    logger.setLevel(getattr(logging, level))

    # create console handler with a higher log level
    handler = logging.StreamHandler()
    handler.setLevel(level)

    handler.setFormatter(CustomFormatter())

    logger.addHandler(handler)
    return logger
