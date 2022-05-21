import discord
from discord.ext import commands
# imports


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command()
        async def help(ctx):
            helpemb = discord.Embed(color=discord.Color.green())
            helpemb.add_field(name="Commands",
                              value="t!owo\nt!help\nt!uwu\nt!tubbo)\nt!pfps\nt!banish\nt!eradicate\nt!transrate")
            helpemb.add_field(name="About Commands", value="t!owo - About command\nt!help - This command, talks "
                                                           "about the bots commands\nt!uwu - uwuifies your "
                                                           "text\nt!tubbo - Changes your name to \"Tubbo from "
                                                           "Dream\"\nt!pfps - Gets your or a tagged member's profile "
                                                           "picture\nt!eradicate - kick tagged member, structure is "
                                                           "t!eradicate (member) (reason)\nt!banish - Bans tagged "
                                                           "member, structure is t!banish (member) ("
                                                           "reason)\nt!transrate - Tells you on a percent scale how "
                                                           "trans you are",
                              inline=False)
            await ctx.send(
                embed=helpemb
            )


def setup(client):
    client.add_cog(Help(client))
