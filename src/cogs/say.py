from discord.ext import commands


class Say(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command()
        async def uwu(ctx, *, text=""):
            if text == "":
                await ctx.send("You need a message...")  # if you didn't send anything it will reply
            else:
                funnies = {"r": "w", "l": "w"}
                trans = text.maketrans(funnies)  # change the letters in text
                texts = text.translate(trans)  # translate text using trans
                await ctx.send(texts)
                await ctx.message.delete()


def setup(client):
    client.add_cog(Say(client))
