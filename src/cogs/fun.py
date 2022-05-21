import discord
from discord.ext import commands
from random import randrange


class TransRate(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command()
        async def transrate(ctx):
            transemb = discord.Embed(color=discord.Color.random())
            transemb.add_field(name="Trans Scale", value=f"I think that {ctx.author.name} is {randrange(100)}% trans")

            await ctx.send(
                embed=transemb
            )


def setup(client):
    client.add_cog(TransRate(client))