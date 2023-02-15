import disnake, typing, googletrans, jokeapi, eng_to_ipa, aiohttp, io, pytesseract
import randfacts, credentials, json, requests, random, jak_python_package.api
import cairo
import src.core.emojis as emojis_list
import src.core.emojis as emojis
import firebase_admin.db
from pyMorseTranslator import translator as morse_translator
from PIL import Image


def get_rules(
    db: firebase_admin.db.Reference, guild: disnake.Guild
) -> typing.List[dict]:
    rules = []
    guild_rules = db.child("guilds").child(str(guild.id)).child("rules").get()

    if not guild_rules:
        embed_blank_value = "\u200b"

        rules.append(
            {
                "name": f"{emojis.numbers['one']}\tNo Negativity",
                "description": embed_blank_value,
            }
        )
        rules.append(
            {
                "name": f"{emojis.numbers['two']}\tNo Spamming",
                "description": embed_blank_value,
            }
        )
        rules.append(
            {
                "name": f"{emojis.numbers['three']}\tNo Swearing",
                "description": embed_blank_value,
            }
        )
        rules.append(
            {
                "name": f"{emojis.numbers['four']}\tNo Discriminatory Or Hate Speech",
                "description": embed_blank_value,
            }
        )
        rules.append(
            {
                "name": f"{emojis.numbers['five']}\tNo NSFW Content",
                "description": embed_blank_value,
            }
        )
        rules.append(
            {
                "name": f"{emojis.numbers['six']}\tNo Potentially Harmful Content",
                "description": embed_blank_value,
            }
        )

        return rules

    for i, rule in enumerate(guild_rules):
        rules.append(
            {
                "name": f"{rule[0]}",
                "description": f"{rule[1]}",
            }
        )

        return rules


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


def morse_code_encode_decode(text: str, action: str):
    if action == "encode":
        encoder = morse_translator.Encoder()
        encoded_text = encoder.encode(text).morse

        return "Text ----> Morse", encoded_text
    elif action == "decode":
        decoder = morse_translator.Decoder()
        decoded_text = decoder.decode(text).plaintext

        return "Morse ----> Text", decoded_text


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


def add_chatbot(
    db: firebase_admin.db.Reference,
    guild: disnake.Guild,
    channel: disnake.TextChannel,
    ai: str,
):
    current_data: list = db.child("guilds").child(str(guild.id)).child("chatbot").get()

    if current_data:
        for data in current_data:
            if data[0] == channel.id:
                return
    else:
        current_data = []

    current_data.append(
        [
            channel.id,
            ai,
        ]
    )

    db.child("guilds").child(str(guild.id)).child("chatbot").set(current_data)


def remove_chatbot(
    db: firebase_admin.db.Reference, guild: disnake.Guild, channel: disnake.TextChannel
):
    current_data: list = db.child("guilds").child(str(guild.id)).child("chatbot").get()

    if current_data:
        for i, data in enumerate(current_data):
            if data[0] == channel.id:
                current_data.pop(i)

        db.child("guilds").child(str(guild.id)).child("chatbot").set(current_data)


def chatbot_response(message: str, ai: str) -> typing.Optional[str]:
    response = ""
    jak_api = jak_python_package.api.API(credentials.RAPID_API_KEY)

    if ai == "alexis":
        response = jak_api.get_alexis_response(message=message)
    elif ai == "chat-gpt":
        response = "Chat GPT is not available right now."

    return response


async def find_pokemon(name) -> dict:
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


async def find_pokemon_card(name) -> dict:
    async with aiohttp.ClientSession(
        headers={"Content-Type": "application/json"},
    ) as client:
        try:
            request = await client.get(
                f"https://api.pokemontcg.io/v1/cards?name={name}",
            )
        except Exception:
            pass

        resp = await request.text()

    cards = json.loads(resp)["cards"]

    rand_int = random.randint(0, len(cards) - 1)

    return cards[rand_int]


def generate_name_fact(
    name: str, heshe: str, hisher: str, guygirl: str, himher: str, girlguy
) -> list:
    lines = [
        f"{heshe} is fun and playful, but has a serious side.",
        f"A smart, talented and humorous {guygirl}, who likes\nto take charge.",
        f"A {guygirl} with a big heart.",
        f"Very rare though, {heshe} is usually a very sweet\nperson and is protective when it comes to {hisher}\nfriends.",
        "A perfect blend of brains and strength.",
        "Someone who has many dreams and desires.",
        f"{str(name)} is a great listener and you can always\ntrust {himher} with anything.",
        f"{str(name)}, a fun energetic {guygirl}, this {guygirl} just\noozes charisma.",
        f"A nice {guygirl}, who respect the feelings of {girlguy}s,\ngood looking personality, charming, smart.",
        f"Many people find {str(name)} rude and arrogant but\n {heshe} is the best and thus has many enemies.",
        f"An attractive, charming {guygirl}, full of joy.",
        f"{heshe} is a great person who will be the best friend\nyou ever had once you crack {hisher} hard outer\nshell.",
        "Romantic and charming.",
        f"One of the sweetest {guygirl}s you will come across\nalthough\nkeep {himher} in your life when {heshe} comes across\nyou. You might regret leaving {himher}.",
        f"{str(name)} is a very unique and interesting person.",
        f"{str(name)} is an amazing friend and {heshe} will always\nbe there for you.",
        f"{str(name)}'s have elegance, charm and good taste,\nare naturally kind, very gentle, and lovers of\nbeauty.",
        f"{heshe} notices when your down and always brings\nyou back up.",
        f"{heshe} is a kind and caring person.",
        f"{str(name)} is overall funny, kind, a savage,\nintelligent and just overall an amazing person.",
        f"{hisher} beauty over powers all the other {guygirl}s and\nnot only is {heshe} smoking hot but {hisher} style is so\ncool.",
        f"Not a fan of romantic commitments but deeply\ncommitted to {hisher} fail out and friends.",
        f"{str(name)} is extremely smart, loving and\nknowledgeable person.",
        "The epitome of cool. Often used to denote\nsomeone whose very understanfing.",
        f"Everyone likes {himher}.",
        f"{heshe} has big dreams, and {heshe} can make them\ncome true.",
        f"You want to be like this {guygirl}, {heshe}'s just too good\nto be true. A true legend.",
        f"Keep {himher} in your life when {heshe} comes across\nyou. You might regret leaving {himher}.",
        f"{str(name)} is a healer of hearts.",
        "The Kind of person who is one in million",
        f"{str(name)} is smart,funny and beautiful.",
        f"{heshe}'s smart beautiful kind and caring.",
        f"Time files with a {str(name)}, as they are simply\nmesmerizing.",
        f"{str(name)} has an amazing personality. Also\nfunny and fun to be around.",
        f"{heshe} is very funny, smart, and good at event the\nnew things {heshe} tries.",
        f"{str(name)} thinks {heshe}'s unattractive but every {girlguy}\n{heshe} walks past just stops and stares.",
        "Strong opinions but has an open mind.",
        "Usually loves hugs and respects people a lot.",
        f"{heshe}'s adorable, {heshe}'s hot, {heshe}'s everything a {girlguy}\ncraves for.",
        f"A good looking {guygirl} with a perfect smile.",
        "Cuddly like a teddy bear but strong like\na soldier.",
        f"{heshe} is loveable, caring, but also tough and\nprotective.",
        f"{girlguy}s really dig a {guygirl} like {himher} cuz {heshe}'s got most\nof the skills..",
        "Will make you laugh a lot.",
        "This person is always well dressed and very\nloved.",
        f"{heshe} is a perfectionist.",
        "The most beautiful eyes in the whole wide\nworld. They Look like stars and if you look too\ndeep you'll get lost in them.",
        "Diplomatic and urbane.",
        "Always genuine and will try and help out if\nyou're in need.",
        f"{str(name)}'s Run the world, and always get what they\ndesire.",
        f"A beautiful {guygirl} who makes people laugh\nall the time.",
        f"{str(name)}'s funny as hell.",
        f"Quite with the ones {heshe} is unfamiliar with, and\necstatic with those {heshe} prizes.",
        f"{str(name)} is an amazing person.",
        f"{str(name)} is a very smart and caring person.",
        "When they need to talk and gives great advice to\nany and everyone.",
        f"{str(name)} is a very smart, sweet, good looking\nand extremely intelligent {guygirl}.",
        "Easygoing and sociable.",
        f"{heshe} can talk to basically anything or anyone for\nhours.",
        "One of the most wonderful person you will ever\nmeet in your life.",
        "Will do anything for friends.",
        f"{heshe} is dutiful and will never put {hisher} own thoughts\nand feelings before {hisher} loved ones.",
        "Wise enough to overcome every situation.",
        f"{heshe} makes you smile with all your heart and you\nlove {himher} and never want to loose {himher}.",
        "Very passionate and romantic and emotional\ntoo!",
        f"If u r {hisher} {girlguy} he'll take care of u like a little\ndiamond of {hisher}.",
        f"{str(name)} has a kind heart, and is family oriented.",
        f"Will insist that {heshe} is a piece of hard candy, but\nif you dig deep enough {heshe}'s got a soft chewy\ncenter.",
        f"{heshe} is likesd by everyone and also has a great\ntaste in fashion.",
        "A very awesome person who is well rounded\nand good at everything.",
        f"{str(name)} can't be wholly defined in few words\nbecause {heshe}'s so close to perfection that any\nwords for {hisher} just won't be good enough.",
        "Helps everyone, great friend, crazy about many\nthings.",
        f"{str(name)} is a {guygirl} you will want to hold close\nforever.",
        "Loves to party and have fun, and can always\nmake you smile.",
        f"{hisher} smile is infectious and {heshe} laughs all the\ntime which everyone loves about {himher}.",
        f"{str(name)} is completely down to earth and sweet\nand kind. {heshe} is the best friend anybody could\never wish for!",
        f"{str(name)} might come off as indifferent and\nimpatient occasionally but it's only because\nthey are working for greater good which takes a\nlot of effort.",
        "Cute and caring. One of the nicest people you'll\nmeet.",
        f"Stunning long legs, hazel eyes, perfect smile,\ndimples, freckles, and every {girlguy} dream.",
        f"Everything {heshe} does is so sexy and appealing,\nwhen you see {himher}..",
        f"{heshe} thinks only about only the lucky {girlguy} {heshe} loves and\nno one else.",
        "Someone you can talk to and trust.",
        f"{str(name)} is funny and {heshe} will make you laugh in\nthe hardest times beacuase {heshe} loves to see\npeople smile.",
        f"The most perfect {guygirl} in the universe.",
        f"{heshe} is a strong hearted charming person.",
        f"{heshe} is good looking, polite, and just all round\nplain awesome.",
        f"{heshe} holds {hisher} emotions and true feelings back\n{heshe}'s very protective of what {heshe} cares for.",
        f"Everyone likes {himher}.",
        "Destined to become a person who does not\nhave an average job.",
        f"One of the most unique {guygirl} you'll every meet.",
        f"{str(name)}'s are extremely caring, affable, and they\nare very sensititve but tend to hide it.",
        f"{heshe}'s the kind of {guygirl}who's so loveable that\neveryone likes her.",
        "Black hair, brown eyes, falls in love hard and\nfast but won't admit it.",
        f"You are really lucky if you have a {str(name)} in your\nlife especially if you are dating her.",
        f"{str(name)} is and achiever and the best person you turn\nto when you need a shoulder to cry on.",
        f"{str(name)} is the definition of compassion.",
        f"The best person ever. {heshe} is one of a kind.",
        f"{heshe}'s beautiful, lovely body and lovely\npersonality.",
        f"A {str(name)} is worthy of being a friend for quite\na long time.",
        f"{heshe} doesn't know how valuable {heshe} really is so\nmake {himher} realise {hisher} worth.",
        f"{heshe} is unique in every way starting from {hisher}\nname to {hisher} looks and personality.",
        f"Always will have your back no matter who you\nare unless you get on {hisher} bad; once you on {hisher}\nbad side there's no coming back.",
        f"{heshe} is loyal to people and won't back stab you.",
        "Really beautiful, has an amazing body.",
        "The ruler of real goon nation and one of a kind.",
        "Never less than awesome.",
        f"{str(name)}'s are the model type, loved by {girlguy}, and\nhated by some {guygirl}s who are jealous.",
        f"{str(name)} can do whatever {heshe} puts {hisher} mind to and\n{heshe} is not quitter, {heshe} does not give up easily\non anything or anyone.",
        f"{heshe} loves music.",
        f"{str(name)} is a very smart and caring person.",
        f"{heshe} has a rocken model body that makes other\n{guygirl} jealous, but {heshe} is very modest.",
        "They are logical, understanding, and see\nthrough any trick or gig you try to pull on them.",
        "The person who radiates happiness.",
        f"{str(name)} is a {guygirl} who is not really insecure and is\nquite protective sometimes.",
        "They have trouble expressing their\nemotions in real life, but it takes the right person\nto see through this barrier and into their true\nhearts.",
        f"{str(name)} has beautiful hairs.",
        f"{heshe} is really funny and sarcastic but really\nsweet and kindhearted at the same time.",
        f"If you ever come across a {str(name)} never let {himher}\ngo because {heshe}'ll be the best thing that you've\never had.",
        f"{str(name)} have a lot of talent in the arts and\nperformance arts and have quite a lot of sports\npotential that they may/may not put to use.",
        "Someone who loves and cares for everyone.",
        f"Modest, but also speak {hisher} mind in a way that\nothers can't.",
        f"Sometimes you need to have patience with {himher}\nbecause {heshe} has anger issues but {heshe}'ll get\nover it very fast.",
        f"{heshe}'s beautiful, talented and intelligent af You\ncan not ignore a {str(name)}, If you do, you have\nforgotten it till you die.",
        "Smart and out to prove the world wrong.",
        f"It's like a drug! Your heart races and you can't\nget enough of {str(name)}'s gorgeousness.",
        f"If you ever find {himher} just hold on tight and never\nlet go cause {heshe} is a gem.",
        f"{str(name)}s are the best!",
        f"{str(name)}'s are absolutely stunning, gorgeous, and\nallurging.",
        f"{heshe} cares about {hisher} family and {hisher} friends and\nis a person who is trustworthy.",
        f"{heshe} is not only unique but one of a kind.",
        f"{str(name)} is too perfect to describe.",
        f"{str(name)} likes to keep {hisher} circle tight and small,{heshe}\n is picky about who {heshe} trusts, and isn't fond of\nlarge circles.",
        f"{girlguy} really wish to have a man who is protective\nenough and secure enough.",
        f"{heshe}'ll leave you coming back for more; wanted\nby many.",
        "Their eyes, eyebrows, and overall facial\nstructure are striking.",
        "Idealistic and peaceable.",
    ]

    return lines


async def get_commands() -> dict:
    async with aiohttp.ClientSession(
        headers={"Content-Type": "application/json"},
    ) as client:
        try:
            request = await client.get(
                "https://raw.githubusercontent.com/Jonak-Adipta-Kalita/JAK-Discord-Bot/main/resources/commands.json",
            )
        except Exception:
            pass

        resp = await request.text()

    json_data = json.loads(resp)

    return json_data


def get_code_output(lang: str, code: str) -> str:
    res = requests.post(
        "https://emkc.org/api/v1/piston/execute",
        json={"language": lang, "source": code},
    )
    jsoned_data = res.json()

    return jsoned_data["output"]


def get_country(code: str) -> dict:
    res = requests.get("https://api.first.org/data/v1/countries")
    jsoned_data = res.json()

    return jsoned_data["data"][code]


async def get_place_details(place: str) -> dict:
    async with aiohttp.ClientSession(
        headers={"Content-Type": "application/json"},
    ) as client:
        try:
            request = await client.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid={credentials.PLACE_API_KEY}"
            )
        except Exception:
            pass

        resp = await request.json()

    return resp


async def get_brawlstars() -> dict:
    jak_api = jak_python_package.api.API(credentials.RAPID_API_KEY)

    return jak_api.get_brawl_stars()


async def get_lyrics(name) -> dict:
    async with aiohttp.ClientSession(
        headers={"Content-Type": "application/json"},
    ) as ses:
        try:
            request = await ses.get(f"https://some-random-api.ml/lyrics?title={name}")
        except Exception:
            pass

        resp = await request.json()

    return resp


def convert_image_to_string(content: str) -> str:
    pytesseract.pytesseract.tesseract_cmd = credentials.TESSERACT_PATH
    img = Image.open(io.BytesIO(content))
    img = img.convert("L")
    text = pytesseract.image_to_string(img)
    print(text)

    return text


async def get_profanity_words() -> list:
    async with aiohttp.ClientSession(
        headers={"Content-Type": "application/json"},
    ) as ses:
        try:
            request = await ses.get(
                f"https://raw.githubusercontent.com/Jonak-Adipta-Kalita/JAK-Discord-Bot/main/resources/profanity.txt"
            )
        except Exception:
            pass

        resp = (await request.text()).split("\n")

    resp[0] = resp[0].split("\ufeff")[1]

    return resp


async def get_hangman_words() -> list:
    async with aiohttp.ClientSession(
        headers={"Content-Type": "application/json"},
    ) as ses:
        try:
            request = await ses.get(
                f"https://raw.githubusercontent.com/Jonak-Adipta-Kalita/JAK-Discord-Bot/main/resources/hangmanWords.txt"
            )
        except Exception:
            pass

        resp = (await request.text()).split("\n")

    return resp


async def get_8ball_responses() -> list:
    async with aiohttp.ClientSession(
        headers={"Content-Type": "application/json"},
    ) as ses:
        try:
            request = await ses.get(
                f"https://raw.githubusercontent.com/Jonak-Adipta-Kalita/JAK-Discord-Bot/main/resources/8ballResponses.txt"
            )
        except Exception:
            pass

        resp = (await request.text()).split("\n")

    return resp


def get_astrophotography_data(link: str) -> dict:
    res = requests.get(link)
    res = res.json()

    return res


def generate_ambigram(
    word1: str, word2: str, author_id: int, font_size=72, font_color=(0, 0, 0)
) -> str:
    file_name = f"ambigrams/{author_id}.png"
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 500, 500)
    ctx = cairo.Context(surface)

    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()

    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(font_size)
    word1_width, word1_height = ctx.text_extents(word1)[2:4]
    word2_width, word2_height = ctx.text_extents(word2)[2:4]
    canvas_width = max(word1_width, word2_width)
    canvas_height = word1_height + word2_height

    r, g, b = font_color
    ctx.set_source_rgb(r, g, b)

    x1 = (500 - word1_width) / 2
    y1 = (500 - canvas_height) / 2

    ctx.save()
    ctx.scale(-1, 1)
    ctx.translate(-x1 - word1_width, y1)
    ctx.show_text(word1)
    ctx.restore()

    x2 = (500 - word2_width) / 2
    y2 = y1 + word1_height

    ctx.save()
    ctx.scale(1, -1)
    ctx.translate(x2, -y2 - word2_height)
    ctx.show_text(word2)
    ctx.restore()

    surface.write_to_png(file_name)

    return file_name


async def get_google_search_results(query: str) -> dict:
    async with aiohttp.ClientSession(
        headers={"Content-Type": "application/json"},
    ) as ses:
        try:
            request = await ses.get(
                f"https://www.googleapis.com/customsearch/v1/siterestrict?cx={credentials.GOOGLE_SEARCH_ENGINE_ID}&key={credentials.GOOGLE_SEARCH_API_KEY}&q={query}"
            )
        except Exception:
            pass

        resp = await request.json()

    return resp["items"]


def get_music_info(music_name: str):
    pass
