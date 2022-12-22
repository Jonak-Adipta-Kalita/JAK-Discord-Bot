import disnake


def code_snippet_file(carbon_file: str, author_id: int):
    file = disnake.File(carbon_file, filename=f"snippets/{author_id}.png")

    return file


def name_fact_file(file: str, author_id: int):
    file = disnake.File(file, filename=f"name_fact/{author_id}.png")

    return file


def ambigram_file(file: str, author_id: int):
    file = disnake.File(file, filename=f"ambigrams/{author_id}.png")

    return file
