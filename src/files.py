import discord


def code_snippet_file(carbon_file: str, author_id: int):
    file = discord.File(carbon_file, filename=f"{author_id}.jpg")

    return file