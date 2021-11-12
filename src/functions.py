import typing


def get_prefix() -> typing.Union["str", "list"]:
    return "$"


def translate_text(text: str) -> str:
    return text
