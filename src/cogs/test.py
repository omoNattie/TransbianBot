import asyncio
from discord.ext import commands


class WaitTest(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command()
        async def test(ctx):
            channel = ctx.channel
            await ctx.send("placeholder")

            def check(m):
                return m.content and m.channel == channel

            try:
                msg = await client.wait_for("message", timeout=30, check=check)
                if msg:
                    await ctx.send("owo")
            except asyncio.TimeoutError:
                await ctx.send("your time has expired")


def setup(client):
    client.add_cog(WaitTest(client))
