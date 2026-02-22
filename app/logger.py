import logging
import yaml

def setup_logger():
    # Load config
    with open("config/config.yaml", "r") as file:
        config = yaml.safe_load(file)

    log_file = config["logging"]["file"]

    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers
    if logger.handlers:
        return logger

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger