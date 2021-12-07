import typing, googletrans, jokeapi


def get_prefix() -> typing.Union["str", "list"]:
    return "$"


def translate_text(text: str) -> dict:
    translator = googletrans.Translator(
        service_urls=["translate.google.com", "translate.google.co.uk"],
        raise_exception=True,
    )

    return translator.translate(text)


def get_joke() -> str:
    j = jokeapi.Jokes()
    joke = j.get_joke(lang="en")

    if joke["type"] == "single":
        return joke["joke"]

    return f"**{joke['setup']}** - {joke['delivery']}"
