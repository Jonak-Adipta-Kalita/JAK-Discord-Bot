import typing, googletrans, jokeapi, eng_to_ipa, aiohttp, randfacts, credentials
import src.core.emojis as emojis_list


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


def morse_code_encode_decode(text: str):
    TEXT_TO_MORSE = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        ",": "--..--",
        ".": ".-.-.-",
        "?": "..--..",
        "/": "-..-.",
        "-": "-....-",
        "(": "-.--.",
        ")": "-.--.-",
        ":": "---...",
        "'": ".----.",
        "’": ".----.",
        '"': ".-..-.",
        " ": ".......",
        "!": "-.-.--",
        "@": ".--.-.",
        "$": "...-..-",
        "&": ".-...",
        ";": "-.-.-.",
        "=": "-...-",
        "+": ".-.-.",
        "_": "..--.-",
    }

    MORSE_TO_TEXT = {
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
        "-..": "D",
        ".": "E",
        "..-.": "F",
        "--.": "G",
        "....": "H",
        "..": "I",
        ".---": "J",
        "-.-": "K",
        ".-..": "L",
        "--": "M",
        "-.": "N",
        "---": "O",
        ".--.": "P",
        "--.-": "Q",
        ".-.": "R",
        "...": "S",
        "-": "T",
        "..-": "U",
        "...-": "V",
        ".--": "W",
        "-..-": "X",
        "-.--": "Y",
        "--..": "Z",
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9",
        "-----": "0",
        "--..--": ",",
        ".-.-.-": ".",
        "..--..": "?",
        "-..-.": "/",
        "-....-": "-",
        "-.--.": "(",
        "-.--.-": ")",
        "---...": ":",
        ".----.": "'",
        ".-..-.": '"',
        ".......": " ",
        "-.-.--": "!",
        ".--.-.": "@",
        "...-..-": "$",
        ".-...": "&",
        "-.-.-.": ";",
        "-...-": "=",
        ".-.-.": "+",
        "..--.-": "_",
    }

    _tempset = set(text)
    check = True
    for char in _tempset:
        if char not in [".", "-", " "]:
            check = False

    if check is True:
        _templist = str(text).split(" ")
        converted = "".join(MORSE_TO_TEXT[str(i)] for i in _templist)

        return "Morse ----> Text", converted
    else:
        _templist = []
        for char in str(text):
            _templist.append(char)
        try:
            converted = " ".join(TEXT_TO_MORSE[str(i).upper()] for i in _templist)

            return "Text ----> Morse", converted
        except KeyError:
            return None, None


def fact() -> str:
    return randfacts.get_fact()


async def convert_to_snippet(code) -> bytes:
    async with aiohttp.ClientSession(
        headers={"Content-Type": "application/json"},
    ) as ses:
        try:
            request = await ses.post(
                f"https://carbonara-42.herokuapp.com/api/cook",
                json={
                    "code": code,
                },
            )
        except Exception:
            pass

        resp = await request.read()

    return resp


async def chatbot_response(message: str) -> typing.Optional[str]:
    async with aiohttp.ClientSession(
        headers={"Content-Type": "application/json"},
    ) as client:
        try:
            request = await client.get(
                f"https://some-random-api.ml/chatbot",
                json={"message": message, "key": credentials.CHATBOT_KEY},
            )
        except Exception:
            pass

        resp = await request.json()

    return resp["response"]


async def find_pokemon(name):
    async with aiohttp.ClientSession(
        headers={"Content-Type": "application/json"},
    ) as client:
        try:
            request = await client.get(
                f"https://some-random-api.ml/pokedex",
                json={
                    "pokemon": name,
                },
            )
        except Exception:
            pass

        resp = await request.json()

    return resp
