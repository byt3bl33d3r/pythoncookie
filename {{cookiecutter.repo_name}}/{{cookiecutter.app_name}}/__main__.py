import asyncio
import logging

handler = logging.StreamHandler()
handler.setFormatter(
    logging.Formatter(
        style="{",
        fmt="[{name}:{filename}] {levelname} - {message}"
    )
)

log = logging.getLogger("{{cookiecutter.app_name}}")
log.setLevel(logging.INFO)
log.addHandler(handler)


def main():
    return
