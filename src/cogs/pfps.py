import discord
from discord.ext import commands


class HelloCog(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command()
        async def pfp(ctx, member: discord.Member = None):
            if member is None:
                selfpfp = ctx.message.author.avatar_url  # if you didn't tag anyone it'll send your own pfp
                await ctx.send(
                    selfpfp
                )
                return
            else:
                atpfp = member.avatar_url  # get tagged member's avatar
                await ctx.send(
                    atpfp  # send said avatar
                )


def setup(client):
    client.add_cog(HelloCog(client))
