import discord
from discord.ext import commands


class Pfps(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command()
        async def pfp(ctx, member: discord.Member = None):
            if member is None:
                selfpfp = ctx.message.author.avatar_url  # if you didn't tag anyone it'll send your own pfp

                nonepfp = discord.Embed(title="Your profile picture", color=discord.Color.random())
                nonepfp.set_image(url=selfpfp)
                await ctx.send(
                    embed=nonepfp
                )
                return
            else:
                atpfp = member.avatar_url  # get tagged member's avatar

                tagpfp = discord.Embed(title=f"{member.name}'s profile picture", color=discord.Color.random())
                tagpfp.set_image(url=atpfp)

                await ctx.send(
                    embed=tagpfp
                )


class Guild(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command()
        async def serverpicture(ctx):
            guildurl = ctx.guild.icon_url

            guildemb = discord.Embed(title=f"{ctx.guild.name}'s picture", color=discord.Color.random())
            guildemb.set_image(url=guildurl)

            await ctx.send(
                embed=guildemb
            )


def setup(client):
    client.add_cog(Pfps(client))
    client.add_cog(Guild(client))
