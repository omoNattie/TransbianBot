from discord.ext import commands


class Tubbo(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command()
        async def tubbo(ctx):
            await ctx.message.author.edit(nick="Tubbo, from Dream.")  # changes nickname
            await ctx.send("Hello, Tubbo.")


def setup(client):
    client.add_cog(Tubbo(client))
