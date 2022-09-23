import disnake, os, asyncio
import src.core.files as files
import src.core.functions as funcs


class CodeSnippetModal(disnake.ui.Modal):
    def __init__(self, author: disnake.Member):
        self.author = author
        super().__init__(
            title="JAK Discord Bot - Code Snippet",
            components=[
                disnake.ui.TextInput(
                    label="Code",
                    placeholder="Your Code",
                    custom_id="code",
                    style=disnake.TextInputStyle.paragraph,
                )
            ],
            custom_id="code_snippet_modal",
        )

    async def callback(self, interaction: disnake.ModalInteraction):
        await interaction.response.defer()

        author_id = self.author.id
        code = ""

        for key, value in interaction.text_values.items():
            if key == "code":
                code = value

        resp = await funcs.convert_to_snippet(code=code)

        if not os.path.isdir("snippets"):
            os.mkdir("snippets")

        with open(f"snippets/{author_id}.png", "wb") as f:
            f.write(resp)
            carbon_file = f

        await interaction.edit_original_message(
            file=files.code_snippet_file(
                carbon_file=os.path.realpath(carbon_file.name),
                author_id=author_id,
            ),
        )

        await asyncio.sleep(60)

        if os.path.isfile(f"snippets/{author_id}.png"):
            os.remove(f"snippets/{author_id}.png")


class ExecuteCodeModal(disnake.ui.Modal):
    def __init__(self):
        super().__init__(
            title="JAK Discord Bot - Execute Code",
            components=[
                disnake.ui.TextInput(
                    label="Language",
                    placeholder="The Language",
                    custom_id="language",
                ),
                disnake.ui.TextInput(
                    label="Code",
                    placeholder="Your Code",
                    custom_id="code",
                    style=disnake.TextInputStyle.paragraph,
                ),
            ],
            custom_id="execute_code_modal",
        )

    async def callback(self, interaction: disnake.ModalInteraction):
        await interaction.response.defer()

        language = ""
        code = ""

        for key, value in interaction.text_values.items():
            if key == "language":
                language = value
            elif key == "code":
                code = value

        code_response = funcs.get_code_output(language, code)
        await interaction.edit_original_message(content=f"```{code_response}```")
