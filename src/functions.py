import typing
import googletrans


def get_prefix() -> typing.Union["str", "list"]:
    return "$"


def translate_text(text: str) -> dict:
    translator = googletrans.Translator(
        service_urls=["translate.google.com", "translate.google.co.uk"],
        raise_exception=True,
    )

    return translator.translate(text)
