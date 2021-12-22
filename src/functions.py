import typing, googletrans, jokeapi, eng_to_ipa, aiohttp
import src.emojis as emojis_list


def get_prefix() -> typing.Union["str", "list"]:
    return "$"


def translate_text(text: str) -> dict:
    translator = googletrans.Translator()

    return translator.translate(text)


def pronunciation(text: str) -> str:
    return eng_to_ipa.convert(text)


def get_joke() -> str:
    joke_ = jokeapi.Jokes()
    joke = joke_.get_joke(lang="en")

    if joke["type"] == "single":
        return joke["joke"]

    return f"**{joke['setup']}** - {joke['delivery']}"


async def get_meme():
    async with aiohttp.ClientSession() as client:
        async with client.get("https://some-random-api.ml/meme") as resp:
            return await resp.json()


def emojify_text(text: str):
    emojis = []
    puncs_to_emo = {
        "!": "exclamation",
        "+": "heavy_plus_sign",
        "-": "heavy_minus_sign",
        "*": "heavy_multiplication_x",
        "/": "heavy_division_sign",
        "$": "heavy_dollar_sign",
        "?": "question",
    }

    for word in text.lower():
        if word == " ":
            emojis.append("   ")
        elif word.isdecimal():
            num_to_emo = {
                "0": emojis_list.numbers["zero"],
                "1": emojis_list.numbers["one"],
                "2": emojis_list.numbers["two"],
                "3": emojis_list.numbers["three"],
                "4": emojis_list.numbers["four"],
                "5": emojis_list.numbers["five"],
                "6": emojis_list.numbers["six"],
                "7": emojis_list.numbers["seven"],
                "8": emojis_list.numbers["eight"],
                "9": emojis_list.numbers["nine"],
            }
            emojis.append(f"{num_to_emo.get(word)}")
        elif word.isalpha():
            emojis.append(emojis_list.alphabets[f"regional_indicator_{word}"])
        elif word in puncs_to_emo:
            emojis.append(emojis_list.punctuation[puncs_to_emo.get(word)])

    return emojis
