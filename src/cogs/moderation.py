import discord
from discord.ext import commands
from discord.ext.commands import has_permissions


class KickPeople(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command()
        @has_permissions(kick_members=True)  # check if member has permission to kick
        async def eradicate(ctx, m: discord.Member = None, *, reason=None):
            if reason is None:
                reason = "No reason has been provided"  # if no reason provided show

            if m is None:
                await ctx.send("Who am I supposed to kick? You tagged no one!")  # if no one is tagged send
            elif m == ctx.author:
                await ctx.send("That's literally you?")  # if you tagged yourself send
            else:
                await ctx.guild.kick(m)  # kick member
                await ctx.send(f"{m} has been eradicated for {reason}!")

        @eradicate.error  # if permissions are missing send
        async def banish_error(ctx, error):
            if isinstance(error, commands.MissingPermissions):
                await ctx.send("I'm sorry, but this command is made for admins!")
            else:
                raise error


class BanPeople(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command()
        @has_permissions(ban_members=True)  # check if member can ban people
        async def banish(ctx, m: discord.Member = None, *, reason=None):
            if reason is None:
                reason = "No reason has been provided"  # if no reason provided change

            if m is None:
                await ctx.send(f"I can't ban air, {ctx.author.name}!")  # if no one is pinged send this
            elif m == ctx.author:  # if auth pinged themselves send
                await ctx.send(f"Nuu You can't ban yourself, {ctx.author.name}!")
            else:
                await m.ban()  # ban pinged member
                await ctx.send(f"{m} has been sent to the Elysian Plain for {reason}!")  # after ban send this

        @banish.error
        async def eradicate_error(ctx, error):
            if isinstance(error, commands.MissingPermissions):
                await ctx.send("I'm sorry, but this command is made for admins!")
            else:
                raise error


def setup(client):
    client.add_cog(KickPeople(client))
    client.add_cog(BanPeople(client))
