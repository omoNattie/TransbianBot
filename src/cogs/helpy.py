import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command()
        async def helps(ctx):
            helpemb = discord.Embed(color=discord.Color.green())
            helpemb.add_field(name="Commands",
                              value="t!owo\nt!helps\nt!uwu\nt!tubbo)\nt!pfps\nt!banish\nt!eradicate")
            helpemb.add_field(name="About Commands", value="t!owo - About command\nt!helps - This command, talks "
                                                           "about the bots commands\nt!uwu - uwuifies your "
                                                           "text\nt!tubbo - Changes your name to \"Tubbo from "
                                                           "Dream\"\nt!pfps - Gets your or a tagged member's profile "
                                                           "picture\nt!eradicate - bans tagged member, structure is "
                                                           "t!eradicate (member) (reason)\nt!banish - bans tagged "
                                                           "member, structure is t!banish (member) (reason)",
                              inline=False)
            await ctx.send(
                embed=helpemb
            )


def setup(client):
    client.add_cog(Help(client))
