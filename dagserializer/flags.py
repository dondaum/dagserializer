# initially all flags are set to None, the on-load call of reset() will set
# them for their first time.
LOGGING_LEVEL: str = "INFO"


def reset() -> None:
    global LOGGING_LEVEL

    LOGGING_LEVEL = "INFO"


def set_from_args(args) -> None:
    global LOGGING_LEVEL

    LOGGING_LEVEL = getattr(args, "logging_level", LOGGING_LEVEL)


# initialize everything to the defaults on module load
reset()
