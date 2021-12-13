import typing, googletrans, jokeapi, eng_to_ipa


def get_prefix() -> typing.Union["str", "list"]:
    return "$"


def translate_text(text: str) -> dict:
    translator = googletrans.Translator()

    return translator.translate(text)


def pronounciation(text: str) -> str:
    return eng_to_ipa.convert(text)


def get_joke() -> str:
    joke_ = jokeapi.Jokes()
    joke = joke_.get_joke(lang="en")

    if joke["type"] == "single":
        return joke["joke"]

    return f"**{joke['setup']}** - {joke['delivery']}"
